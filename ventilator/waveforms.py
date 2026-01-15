"""
Ventilator Waveform Display
Pressure, Flow, and Volume waveform visualization
"""

import streamlit as st
import numpy as np
import pandas as pd
from typing import Optional, Dict, List
import time


def generate_pressure_waveform(
    duration: float = 5.0,
    sample_rate: float = 100.0,
    peep: float = 10.0,
    peak_pressure: float = 25.0,
    inspiratory_time: float = 1.0,
    expiratory_time: float = 2.0
) -> pd.DataFrame:
    """
    Generate pressure waveform data
    
    Args:
        duration: Duration in seconds
        sample_rate: Samples per second
        peep: PEEP level (cmH2O)
        peak_pressure: Peak inspiratory pressure (cmH2O)
        inspiratory_time: Inspiratory time (seconds)
        expiratory_time: Expiratory time (seconds)
    
    Returns:
        DataFrame with time and pressure columns
    """
    total_time = inspiratory_time + expiratory_time
    num_cycles = int(duration / total_time)
    
    time_points = []
    pressure_values = []
    
    for cycle in range(num_cycles):
        cycle_start = cycle * total_time
        
        # Inspiratory phase
        insp_samples = int(inspiratory_time * sample_rate)
        for i in range(insp_samples):
            t = cycle_start + (i / sample_rate)
            # Simulate pressure rise during inspiration
            progress = i / insp_samples
            pressure = peep + (peak_pressure - peep) * (1 - np.exp(-5 * progress))
            time_points.append(t)
            pressure_values.append(pressure)
        
        # Expiratory phase
        exp_samples = int(expiratory_time * sample_rate)
        for i in range(exp_samples):
            t = cycle_start + inspiratory_time + (i / sample_rate)
            # Simulate pressure decay during expiration
            progress = i / exp_samples
            pressure = peak_pressure - (peak_pressure - peep) * (1 - np.exp(-3 * progress))
            time_points.append(t)
            pressure_values.append(pressure)
    
    df = pd.DataFrame({
        'time': time_points,
        'pressure': pressure_values
    })
    
    return df


def generate_flow_waveform(
    duration: float = 5.0,
    sample_rate: float = 100.0,
    tidal_volume: float = 500.0,
    inspiratory_time: float = 1.0,
    expiratory_time: float = 2.0
) -> pd.DataFrame:
    """
    Generate flow waveform data
    
    Args:
        duration: Duration in seconds
        sample_rate: Samples per second
        tidal_volume: Tidal volume (mL)
        inspiratory_time: Inspiratory time (seconds)
        expiratory_time: Expiratory time (seconds)
    
    Returns:
        DataFrame with time and flow columns
    """
    total_time = inspiratory_time + expiratory_time
    num_cycles = int(duration / total_time)
    
    time_points = []
    flow_values = []
    
    # Calculate peak flow (simplified)
    peak_inspiratory_flow = (tidal_volume / inspiratory_time) * 60 / 1000  # L/min
    peak_expiratory_flow = (tidal_volume / expiratory_time) * 60 / 1000  # L/min
    
    for cycle in range(num_cycles):
        cycle_start = cycle * total_time
        
        # Inspiratory phase (positive flow)
        insp_samples = int(inspiratory_time * sample_rate)
        for i in range(insp_samples):
            t = cycle_start + (i / sample_rate)
            # Simulate flow pattern (sine wave)
            progress = i / insp_samples
            flow = peak_inspiratory_flow * np.sin(np.pi * progress)
            time_points.append(t)
            flow_values.append(flow)
        
        # Expiratory phase (negative flow)
        exp_samples = int(expiratory_time * sample_rate)
        for i in range(exp_samples):
            t = cycle_start + inspiratory_time + (i / sample_rate)
            # Simulate expiratory flow
            progress = i / exp_samples
            flow = -peak_expiratory_flow * (1 - progress) * np.exp(-2 * progress)
            time_points.append(t)
            flow_values.append(flow)
    
    df = pd.DataFrame({
        'time': time_points,
        'flow': flow_values
    })
    
    return df


def generate_volume_waveform(
    duration: float = 5.0,
    sample_rate: float = 100.0,
    tidal_volume: float = 500.0,
    inspiratory_time: float = 1.0,
    expiratory_time: float = 2.0
) -> pd.DataFrame:
    """
    Generate volume waveform data (integrated from flow)
    
    Args:
        duration: Duration in seconds
        sample_rate: Samples per second
        tidal_volume: Tidal volume (mL)
        inspiratory_time: Inspiratory time (seconds)
        expiratory_time: Expiratory time (seconds)
    
    Returns:
        DataFrame with time and volume columns
    """
    flow_df = generate_flow_waveform(duration, sample_rate, tidal_volume, inspiratory_time, expiratory_time)
    
    # Integrate flow to get volume
    volume_values = []
    current_volume = 0.0
    
    for idx, flow in enumerate(flow_df['flow']):
        dt = 1.0 / sample_rate
        # Convert L/min to mL/s
        flow_ml_per_s = (flow / 60.0) * 1000.0
        current_volume += flow_ml_per_s * dt
        # Reset at end of expiration
        if flow < 0 and idx > 0 and flow_df['flow'].iloc[idx-1] > 0:
            current_volume = 0.0
        volume_values.append(current_volume)
    
    df = pd.DataFrame({
        'time': flow_df['time'],
        'volume': volume_values
    })
    
    return df


def render_waveform_display(
    waveform_type: str = "pressure",
    duration: float = 5.0,
    peep: float = 10.0,
    peak_pressure: float = 25.0,
    tidal_volume: float = 500.0,
    rr: float = 20.0,
    ie_ratio: float = 1.0/2.0
):
    """
    Render waveform display
    
    Args:
        waveform_type: Type of waveform (pressure, flow, volume, all)
        duration: Duration to display (seconds)
        peep: PEEP level
        peak_pressure: Peak pressure
        tidal_volume: Tidal volume
        rr: Respiratory rate
        ie_ratio: I:E ratio
    """
    # Calculate times from RR and I:E ratio
    total_cycle_time = 60.0 / rr
    inspiratory_time = total_cycle_time / (1 + 1/ie_ratio)
    expiratory_time = total_cycle_time - inspiratory_time
    
    if waveform_type == "pressure" or waveform_type == "all":
        st.markdown("### 📊 Pressure Waveform")
        pressure_df = generate_pressure_waveform(
            duration=duration,
            peep=peep,
            peak_pressure=peak_pressure,
            inspiratory_time=inspiratory_time,
            expiratory_time=expiratory_time
        )
        
        chart_data = pressure_df.set_index('time')['pressure']
        st.line_chart(chart_data, height=200)
        
        # Display key values
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("PEEP", f"{peep:.1f} cmH2O")
        with col2:
            st.metric("Peak Pressure", f"{peak_pressure:.1f} cmH2O")
        with col3:
            st.metric("Driving Pressure", f"{peak_pressure - peep:.1f} cmH2O")
    
    if waveform_type == "flow" or waveform_type == "all":
        st.markdown("### 💨 Flow Waveform")
        flow_df = generate_flow_waveform(
            duration=duration,
            tidal_volume=tidal_volume,
            inspiratory_time=inspiratory_time,
            expiratory_time=expiratory_time
        )
        
        chart_data = flow_df.set_index('time')['flow']
        st.line_chart(chart_data, height=200)
        
        # Display key values
        peak_insp_flow = (tidal_volume / inspiratory_time) * 60 / 1000
        peak_exp_flow = (tidal_volume / expiratory_time) * 60 / 1000
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Peak Inspiratory Flow", f"{peak_insp_flow:.1f} L/min")
        with col2:
            st.metric("Peak Expiratory Flow", f"{peak_exp_flow:.1f} L/min")
    
    if waveform_type == "volume" or waveform_type == "all":
        st.markdown("### 📈 Volume Waveform")
        volume_df = generate_volume_waveform(
            duration=duration,
            tidal_volume=tidal_volume,
            inspiratory_time=inspiratory_time,
            expiratory_time=expiratory_time
        )
        
        chart_data = volume_df.set_index('time')['volume']
        st.line_chart(chart_data, height=200)
        
        # Display key values
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tidal Volume", f"{tidal_volume:.0f} mL")
        with col2:
            st.metric("Minute Ventilation", f"{(tidal_volume * rr / 1000):.1f} L/min")


def render_waveform_panel():
    """Render complete waveform panel"""
    st.header("📊 Ventilator Waveforms")
    st.caption("Hiển thị sóng máy thở: Pressure, Flow, Volume")
    
    st.markdown("---")
    
    # Parameters
    st.markdown("### ⚙️ Thông số máy thở")
    
    col1, col2 = st.columns(2)
    
    with col1:
        peep = st.number_input("PEEP (cmH2O):", min_value=0.0, value=10.0, key="waveform_peep")
        peak_pressure = st.number_input("Peak Pressure (cmH2O):", min_value=0.0, value=25.0, key="waveform_peak")
        tidal_volume = st.number_input("Tidal Volume (mL):", min_value=0.0, value=500.0, key="waveform_vt")
    
    with col2:
        rr = st.number_input("Respiratory Rate (/min):", min_value=0.0, value=20.0, key="waveform_rr")
        ie_ratio_num = st.number_input("I:E (Inspiratory):", min_value=0.1, value=1.0, key="waveform_ie_num")
        ie_ratio_den = st.number_input("I:E (Expiratory):", min_value=0.1, value=2.0, key="waveform_ie_den")
        duration = st.number_input("Duration (seconds):", min_value=1.0, max_value=30.0, value=5.0, key="waveform_duration")
    
    ie_ratio = ie_ratio_num / ie_ratio_den
    
    st.markdown("---")
    
    # Waveform type selection
    waveform_type = st.radio(
        "Chọn loại sóng:",
        ["pressure", "flow", "volume", "all"],
        format_func=lambda x: {
            "pressure": "📊 Pressure Only",
            "flow": "💨 Flow Only",
            "volume": "📈 Volume Only",
            "all": "📊 All Waveforms"
        }[x],
        key="waveform_type",
        horizontal=True
    )
    
    st.markdown("---")
    
    # Display waveforms
    render_waveform_display(
        waveform_type=waveform_type,
        duration=duration,
        peep=peep,
        peak_pressure=peak_pressure,
        tidal_volume=tidal_volume,
        rr=rr,
        ie_ratio=ie_ratio
    )
    
    st.markdown("---")
    
    # Waveform analysis
    st.markdown("### 🔍 Phân tích sóng")
    
    st.info("""
    **Giải thích:**
    - **Pressure waveform:** Hiển thị áp lực đường thở theo thời gian
    - **Flow waveform:** Hiển thị lưu lượng khí (dương = vào, âm = ra)
    - **Volume waveform:** Hiển thị thể tích khí tích lũy
    
    **Phát hiện bất thường:**
    - Auto-PEEP: Pressure không về baseline
    - Asynchrony: Flow pattern không đều
    - Leak: Volume không về zero
    """)
