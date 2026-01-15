"""
Real-time Ventilator Data Simulator
Simulates realistic ventilator data for demo and testing
"""

import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, Optional
import time


class VentilatorDataSimulator:
    """Simulates ventilator data in real-time"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.base_params = {
            'peep': 10.0,
            'peak_pressure': 25.0,
            'plateau_pressure': 22.0,
            'tidal_volume': 500.0,
            'respiratory_rate': 20.0,
            'fio2': 0.6,
            'compliance': 30.0
        }
        self.variation_range = {
            'peep': 1.0,
            'peak_pressure': 2.0,
            'plateau_pressure': 1.5,
            'tidal_volume': 20.0,
            'respiratory_rate': 1.0,
            'fio2': 0.05,
            'compliance': 2.0
        }
    
    def generate_realistic_data(self, elapsed_time: float) -> Dict:
        """
        Generate realistic ventilator data with natural variations
        
        Args:
            elapsed_time: Time elapsed since start (seconds)
        
        Returns:
            Dictionary with current ventilator parameters
        """
        data = {}
        
        # Add natural variations (simulate patient breathing)
        for param, base_value in self.base_params.items():
            variation = self.variation_range.get(param, 0)
            
            # Add slow drift (simulate patient condition changes)
            drift = np.sin(elapsed_time / 60.0) * (variation * 0.3)
            
            # Add fast variations (simulate breath-to-breath changes)
            noise = np.random.normal(0, variation * 0.2)
            
            data[param] = base_value + drift + noise
        
        # Ensure realistic relationships
        data['plateau_pressure'] = min(data['plateau_pressure'], data['peak_pressure'] - 2)
        data['driving_pressure'] = data['plateau_pressure'] - data['peep']
        
        # Calculate derived parameters
        if data['compliance'] > 0:
            data['calculated_vt'] = data['compliance'] * data['driving_pressure']
        else:
            data['calculated_vt'] = data['tidal_volume']
        
        data['minute_ventilation'] = (data['tidal_volume'] * data['respiratory_rate']) / 1000.0
        
        # Add timestamp
        data['timestamp'] = self.start_time + timedelta(seconds=elapsed_time)
        
        return data
    
    def simulate_abg_data(self, elapsed_time: float, pf_ratio_target: float = 200.0) -> Dict:
        """
        Simulate ABG data based on ventilator settings
        
        Args:
            elapsed_time: Time elapsed
            pf_ratio_target: Target P/F ratio
        
        Returns:
            Dictionary with ABG parameters
        """
        # Simulate PaO2 based on FiO2 and PEEP
        fio2 = self.base_params.get('fio2', 0.6)
        peep = self.base_params.get('peep', 10.0)
        
        # Simplified model: PaO2 increases with FiO2 and PEEP
        base_pao2 = fio2 * 100 + peep * 2
        pao2 = base_pao2 + np.random.normal(0, 5)
        
        # Calculate P/F ratio
        pf_ratio = pao2 / fio2 if fio2 > 0 else 0
        
        # Simulate PaCO2 (inversely related to minute ventilation)
        mv = (self.base_params['tidal_volume'] * self.base_params['respiratory_rate']) / 1000.0
        paco2 = 40 + (8 - mv) * 5 + np.random.normal(0, 2)
        paco2 = max(25, min(60, paco2))
        
        # Simulate pH (related to PaCO2)
        ph = 7.40 - (paco2 - 40) * 0.008 + np.random.normal(0, 0.02)
        ph = max(7.20, min(7.50, ph))
        
        # Simulate HCO3
        hco3 = 24 + (ph - 7.40) * 10 + np.random.normal(0, 1)
        hco3 = max(18, min(30, hco3))
        
        return {
            'pao2': pao2,
            'paco2': paco2,
            'ph': ph,
            'hco3': hco3,
            'pf_ratio': pf_ratio,
            'timestamp': self.start_time + timedelta(seconds=elapsed_time)
        }


def init_simulator_state():
    """Initialize simulator state"""
    if 'ventilator_simulator' not in st.session_state:
        st.session_state['ventilator_simulator'] = VentilatorDataSimulator()
    
    if 'simulator_running' not in st.session_state:
        st.session_state['simulator_running'] = False
    
    if 'simulator_data_history' not in st.session_state:
        st.session_state['simulator_data_history'] = []


def render_data_simulator():
    """Render real-time data simulator interface"""
    st.header("🔄 Real-time Data Simulator")
    st.caption("Mô phỏng dữ liệu máy thở real-time cho demo và testing")
    
    init_simulator_state()
    
    simulator = st.session_state['ventilator_simulator']
    
    st.markdown("---")
    
    # Control panel
    st.markdown("### 🎛️ Điều khiển")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        is_running = st.checkbox(
            "Bật simulator",
            value=st.session_state.get('simulator_running', False),
            key="simulator_running"
        )
        st.session_state['simulator_running'] = is_running
    
    with col2:
        update_rate = st.selectbox(
            "Tần suất cập nhật:",
            ["Mỗi giây", "Mỗi 2 giây", "Mỗi 5 giây"],
            key="simulator_rate"
        )
        rate_seconds = {"Mỗi giây": 1, "Mỗi 2 giây": 2, "Mỗi 5 giây": 5}[update_rate]
    
    with col3:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state['simulator_data_history'] = []
            st.session_state['ventilator_simulator'] = VentilatorDataSimulator()
            st.rerun()
    
    st.markdown("---")
    
    # Base parameters
    st.markdown("### ⚙️ Thông số cơ bản")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        simulator.base_params['peep'] = st.number_input(
            "PEEP (cmH2O):",
            min_value=0.0,
            value=simulator.base_params['peep'],
            key="sim_peep"
        )
        simulator.base_params['peak_pressure'] = st.number_input(
            "Peak Pressure (cmH2O):",
            min_value=0.0,
            value=simulator.base_params['peak_pressure'],
            key="sim_peak"
        )
    
    with col2:
        simulator.base_params['tidal_volume'] = st.number_input(
            "Tidal Volume (mL):",
            min_value=0.0,
            value=simulator.base_params['tidal_volume'],
            key="sim_vt"
        )
        simulator.base_params['respiratory_rate'] = st.number_input(
            "RR (/min):",
            min_value=0.0,
            value=simulator.base_params['respiratory_rate'],
            key="sim_rr"
        )
    
    with col3:
        simulator.base_params['fio2'] = st.slider(
            "FiO2:",
            0.21,
            1.0,
            simulator.base_params['fio2'],
            0.01,
            key="sim_fio2"
        )
        simulator.base_params['compliance'] = st.number_input(
            "Compliance (mL/cmH2O):",
            min_value=0.0,
            value=simulator.base_params['compliance'],
            key="sim_compliance"
        )
    
    st.markdown("---")
    
    # Current data display
    if is_running:
        elapsed_time = (datetime.now() - simulator.start_time).total_seconds()
        current_data = simulator.generate_realistic_data(elapsed_time)
        abg_data = simulator.simulate_abg_data(elapsed_time)
        
        # Add to history
        combined_data = {**current_data, **abg_data}
        st.session_state['simulator_data_history'].append(combined_data)
        
        # Keep only last 100 points
        if len(st.session_state['simulator_data_history']) > 100:
            st.session_state['simulator_data_history'] = st.session_state['simulator_data_history'][-100:]
        
        # Display current values
        st.markdown("### 📊 Dữ liệu hiện tại")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("PEEP", f"{current_data['peep']:.1f} cmH2O")
            st.metric("Plateau", f"{current_data['plateau_pressure']:.1f} cmH2O")
        
        with col2:
            st.metric("Tidal Volume", f"{current_data['tidal_volume']:.0f} mL")
            st.metric("RR", f"{current_data['respiratory_rate']:.1f} /min")
        
        with col3:
            st.metric("P/F Ratio", f"{abg_data['pf_ratio']:.0f}")
            st.metric("PaCO2", f"{abg_data['paco2']:.1f} mmHg")
        
        with col4:
            st.metric("pH", f"{abg_data['ph']:.2f}")
            st.metric("Compliance", f"{current_data['compliance']:.1f} mL/cmH2O")
        
        # Trends
        if len(st.session_state['simulator_data_history']) > 1:
            st.markdown("---")
            st.markdown("### 📈 Xu hướng")
            
            df = pd.DataFrame(st.session_state['simulator_data_history'])
            
            # Select parameters to plot
            plot_params = st.multiselect(
                "Chọn thông số:",
                ['peep', 'plateau_pressure', 'tidal_volume', 'pf_ratio', 'ph', 'paco2'],
                default=['plateau_pressure', 'pf_ratio'],
                key="sim_plot_params"
            )
            
            if plot_params:
                plot_df = df[['timestamp'] + plot_params].copy()
                plot_df = plot_df.set_index('timestamp')
                st.line_chart(plot_df, height=300)
        
        # Auto-refresh
        time.sleep(rate_seconds)
        st.rerun()
    else:
        st.info("Bật simulator để xem dữ liệu real-time")
        
        # Show sample data
        sample_data = simulator.generate_realistic_data(0)
        sample_abg = simulator.simulate_abg_data(0)
        
        st.markdown("### 📊 Dữ liệu mẫu")
        col1, col2 = st.columns(2)
        
        with col1:
            st.json({
                "PEEP": f"{sample_data['peep']:.1f} cmH2O",
                "Peak Pressure": f"{sample_data['peak_pressure']:.1f} cmH2O",
                "Plateau": f"{sample_data['plateau_pressure']:.1f} cmH2O",
                "Tidal Volume": f"{sample_data['tidal_volume']:.0f} mL",
                "RR": f"{sample_data['respiratory_rate']:.1f} /min"
            })
        
        with col2:
            st.json({
                "PaO2": f"{sample_abg['pao2']:.1f} mmHg",
                "PaCO2": f"{sample_abg['paco2']:.1f} mmHg",
                "pH": f"{sample_abg['ph']:.2f}",
                "P/F Ratio": f"{sample_abg['pf_ratio']:.0f}"
            })
