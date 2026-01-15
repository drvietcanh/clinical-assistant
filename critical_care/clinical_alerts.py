"""
Clinical Decision Support System - Cross-module alerts and recommendations
Integrates alerts from Ventilator, Sedation, Fluid, Vasopressor, and other modules
"""

import streamlit as st
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert
from typing import List, Dict, Optional
from datetime import datetime


class ClinicalAlert:
    """Represents a clinical alert"""
    
    def __init__(self, priority: str, module: str, message: str, recommendation: str = None, action: str = None):
        """
        Args:
            priority: 'critical', 'warning', or 'info'
            module: Source module (e.g., 'ventilator', 'sedation')
            message: Alert message
            recommendation: Recommended action
            action: Quick action link
        """
        self.priority = priority
        self.module = module
        self.message = message
        self.recommendation = recommendation
        self.action = action
    
    def get_color(self) -> str:
        """Get color based on priority"""
        return {
            'critical': 'error',
            'warning': 'warning',
            'info': 'info'
        }.get(self.priority, 'info')
    
    def get_icon(self) -> str:
        """Get icon based on priority"""
        return {
            'critical': '🚨',
            'warning': '⚠️',
            'info': 'ℹ️'
        }.get(self.priority, 'ℹ️')


def check_ventilator_alerts(vent_data: Dict, abg_data: Dict) -> List[ClinicalAlert]:
    """Check for ventilator-related alerts"""
    alerts = []
    
    # P/F ratio alerts
    if abg_data.get('pf_ratio'):
        pf_ratio = abg_data['pf_ratio']
        if pf_ratio < 100:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='ventilator',
                message=f'P/F ratio rất thấp ({pf_ratio:.0f}) - ARDS nặng',
                recommendation='Xem xét ARDS protocol, tăng PEEP, cân nhắc prone positioning',
                action='🫁 ARDS Protocols'
            ))
        elif pf_ratio < 200:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='ventilator',
                message=f'P/F ratio thấp ({pf_ratio:.0f}) - ARDS trung bình',
                recommendation='Theo dõi sát, cân nhắc điều chỉnh PEEP/FiO2',
                action='🫁 ARDS Protocols'
            ))
    
    # Plateau pressure alerts
    if vent_data.get('plateau'):
        plateau = vent_data['plateau']
        if plateau > 30:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='ventilator',
                message=f'Plateau pressure cao ({plateau:.1f} cmH2O) - Nguy cơ barotrauma',
                recommendation='Giảm tidal volume, kiểm tra compliance, cân nhắc giảm PEEP',
                action='🫁 Ventilator Management'
            ))
        elif plateau > 28:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='ventilator',
                message=f'Plateau pressure tăng ({plateau:.1f} cmH2O)',
                recommendation='Theo dõi sát, cân nhắc giảm Vt',
                action='🫁 Ventilator Management'
            ))
    
    # Driving pressure alerts
    if vent_data.get('plateau') and vent_data.get('peep'):
        driving = vent_data['plateau'] - vent_data['peep']
        if driving > 15:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='ventilator',
                message=f'Driving pressure cao ({driving:.1f} cmH2O)',
                recommendation='Giảm Vt hoặc tăng PEEP để giảm driving pressure',
                action='🫁 Ventilator Management'
            ))
        elif driving > 12:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='ventilator',
                message=f'Driving pressure tăng ({driving:.1f} cmH2O)',
                recommendation='Theo dõi, target ≤15 cmH2O',
                action='🫁 Ventilator Management'
            ))
    
    # ABG alerts
    if abg_data.get('ph'):
        ph = abg_data['ph']
        if ph < 7.20:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='ventilator',
                message=f'pH rất thấp ({ph:.2f}) - Nhiễm toan nặng',
                recommendation='Tăng RR hoặc Vt để giảm PaCO2, kiểm tra nguyên nhân',
                action='🫁 Ventilator Management'
            ))
        elif ph < 7.30:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='ventilator',
                message=f'pH thấp ({ph:.2f}) - Nhiễm toan',
                recommendation='Cân nhắc tăng thông khí',
                action='🫁 Ventilator Management'
            ))
        elif ph > 7.50:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='ventilator',
                message=f'pH cao ({ph:.2f}) - Nhiễm kiềm',
                recommendation='Cân nhắc giảm thông khí',
                action='🫁 Ventilator Management'
            ))
    
    return alerts


def check_sedation_alerts(sed_data: Dict, vent_data: Dict) -> List[ClinicalAlert]:
    """Check for sedation-related alerts"""
    alerts = []
    
    # RASS alerts
    if sed_data.get('rass') is not None:
        rass = sed_data['rass']
        if rass < -4:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='sedation',
                message=f'RASS quá sâu ({rass}) - An thần quá mức',
                recommendation='Giảm liều an thần, đánh giá lại mục tiêu RASS (-1 đến -2)',
                action='💤 Sedation & Analgesia'
            ))
        elif rass > 0:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='sedation',
                message=f'RASS dương tính ({rass}) - Kích động',
                recommendation='Tăng liều an thần, đánh giá nguyên nhân kích động',
                action='💤 Sedation & Analgesia'
            ))
        elif rass > -1:
            alerts.append(ClinicalAlert(
                priority='info',
                module='sedation',
                message=f'RASS gần mức tỉnh ({rass})',
                recommendation='Cân nhắc giảm an thần nếu bệnh nhân ổn định',
                action='💤 Sedation & Analgesia'
            ))
    
    # CAM-ICU alerts
    if sed_data.get('cam_icu') == 'Dương tính':
        alerts.append(ClinicalAlert(
            priority='warning',
            module='sedation',
            message='CAM-ICU dương tính - Mê sảng',
            recommendation='Đánh giá nguyên nhân, cân nhắc giảm an thần, non-pharmacological interventions',
            action='📊 Scoring Systems'
        ))
    
    # Cross-module: Deep sedation + High PEEP
    if sed_data.get('rass', 0) < -3 and vent_data.get('peep', 0) > 15:
        alerts.append(ClinicalAlert(
            priority='info',
            module='sedation',
            message='An thần sâu + PEEP cao - Cân nhắc giảm an thần để đánh giá compliance',
            recommendation='Giảm an thần từ từ để đánh giá đáp ứng với PEEP',
            action='💤 Sedation & Analgesia'
        ))
    
    return alerts


def check_fluid_alerts(fluid_data: Dict, hemo_data: Dict) -> List[ClinicalAlert]:
    """Check for fluid-related alerts"""
    alerts = []
    
    # Fluid balance alerts
    if fluid_data.get('balance') is not None:
        balance = fluid_data['balance']
        if balance > 2000:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='fluid',
                message=f'Dư dịch nhiều ({balance:+.0f} mL/24h)',
                recommendation='Cân nhắc lợi tiểu, hạn chế dịch vào',
                action='💧 Fluid Therapy'
            ))
        elif balance < -1000:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='fluid',
                message=f'Thiếu dịch ({balance:+.0f} mL/24h)',
                recommendation='Đánh giá thể tích tuần hoàn, cân nhắc bù dịch',
                action='💧 Fluid Therapy'
            ))
    
    # Urine output alerts
    if fluid_data.get('urine_output') is not None:
        uo = fluid_data['urine_output']
        if uo < 0.5:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='fluid',
                message=f'Lượng nước tiểu rất thấp ({uo:.1f} mL/kg/h) - Suy thận cấp',
                recommendation='Đánh giá AKI, cân nhắc RRT, kiểm tra thể tích tuần hoàn',
                action='🩺 RRT Calculator'
            ))
        elif uo < 1.0:
            alerts.append(ClinicalAlert(
                priority='warning',
                module='fluid',
                message=f'Lượng nước tiểu thấp ({uo:.1f} mL/kg/h)',
                recommendation='Theo dõi sát, đánh giá thể tích tuần hoàn',
                action='💧 Fluid Therapy'
            ))
    
    # Cross-module: High PEEP + Low CVP
    if hemo_data.get('cvp') is not None and hemo_data.get('cvp', 0) < 5:
        alerts.append(ClinicalAlert(
            priority='info',
            module='fluid',
            message='CVP thấp - Cân nhắc đánh giá thể tích tuần hoàn',
            recommendation='Đánh giá fluid responsiveness nếu có PEEP cao',
            action='💧 Fluid Therapy'
        ))
    
    return alerts


def check_sepsis_alerts(abg_data: Dict, hemo_data: Dict) -> List[ClinicalAlert]:
    """Check for sepsis-related alerts"""
    alerts = []
    
    # Low P/F + Hypotension suggests sepsis-related ARDS
    if abg_data.get('pf_ratio') and abg_data['pf_ratio'] < 200:
        if hemo_data.get('map') and hemo_data['map'] < 65:
            alerts.append(ClinicalAlert(
                priority='critical',
                module='sepsis',
                message='ARDS + Hạ huyết áp - Nghi ngờ sepsis',
                recommendation='Xem xét sepsis protocol, kháng sinh, bù dịch',
                action='🦠 Sepsis Protocols'
            ))
    
    return alerts


def check_all_alerts(patient_data: Dict) -> List[ClinicalAlert]:
    """Check all alerts across all modules"""
    all_alerts = []
    
    vent_data = patient_data.get('ventilator', {})
    abg_data = patient_data.get('abg', {})
    sed_data = patient_data.get('sedation', {})
    fluid_data = patient_data.get('fluid', {})
    hemo_data = patient_data.get('vasopressor', {})
    
    # Ventilator alerts
    all_alerts.extend(check_ventilator_alerts(vent_data, abg_data))
    
    # Sedation alerts
    all_alerts.extend(check_sedation_alerts(sed_data, vent_data))
    
    # Fluid alerts
    all_alerts.extend(check_fluid_alerts(fluid_data, hemo_data))
    
    # Sepsis alerts
    all_alerts.extend(check_sepsis_alerts(abg_data, hemo_data))
    
    # Sort by priority
    priority_order = {'critical': 0, 'warning': 1, 'info': 2}
    all_alerts.sort(key=lambda x: priority_order.get(x.priority, 3))
    
    return all_alerts


def render_clinical_alerts(patient_data: Dict = None):
    """Render clinical alerts panel"""
    if patient_data is None:
        # Try to get from session state
        if 'patient_data' in st.session_state:
            patient_data = st.session_state['patient_data']
        else:
            st.info("Chưa có dữ liệu bệnh nhân. Vui lòng nhập thông tin ở Patient Dashboard.")
            return
    
    alerts = check_all_alerts(patient_data)
    
    if not alerts:
        st.success("✅ Không có cảnh báo. Tất cả thông số trong giới hạn an toàn.")
        return
    
    st.markdown("### 🚨 Cảnh báo lâm sàng")
    st.caption(f"Tổng cộng {len(alerts)} cảnh báo")
    
    # Group by priority
    critical_alerts = [a for a in alerts if a.priority == 'critical']
    warning_alerts = [a for a in alerts if a.priority == 'warning']
    info_alerts = [a for a in alerts if a.priority == 'info']
    
    # Display critical alerts
    if critical_alerts:
        st.markdown("#### 🚨 Cảnh báo nghiêm trọng")
        for alert in critical_alerts:
            render_error_alert(
                f"**{alert.module.upper()}:** {alert.message}",
                alert.recommendation
            )
            if alert.action:
                if st.button(f"→ {alert.action}", key=f"alert_action_{id(alert)}"):
                    st.session_state['critical_care_tool_selection'] = alert.action
                    st.rerun()
            st.markdown("---")
    
    # Display warning alerts
    if warning_alerts:
        st.markdown("#### ⚠️ Cảnh báo")
        for alert in warning_alerts:
            render_warning_alert(
                f"**{alert.module.upper()}:** {alert.message}",
                alert.recommendation
            )
            if alert.action:
                if st.button(f"→ {alert.action}", key=f"alert_action_{id(alert)}"):
                    st.session_state['critical_care_tool_selection'] = alert.action
                    st.rerun()
            st.markdown("---")
    
    # Display info alerts
    if info_alerts:
        st.markdown("#### ℹ️ Thông tin")
        for alert in info_alerts:
            render_info_alert(
                f"**{alert.module.upper()}:** {alert.message}",
                alert.recommendation
            )
            if alert.action:
                if st.button(f"→ {alert.action}", key=f"alert_action_{id(alert)}"):
                    st.session_state['critical_care_tool_selection'] = alert.action
                    st.rerun()
            st.markdown("---")


def render_alerts_summary(patient_data: Dict = None) -> Dict:
    """Render alerts summary (for dashboard)"""
    if patient_data is None:
        if 'patient_data' in st.session_state:
            patient_data = st.session_state['patient_data']
        else:
            return {'critical': 0, 'warning': 0, 'info': 0, 'total': 0}
    
    alerts = check_all_alerts(patient_data)
    
    summary = {
        'critical': len([a for a in alerts if a.priority == 'critical']),
        'warning': len([a for a in alerts if a.priority == 'warning']),
        'info': len([a for a in alerts if a.priority == 'info']),
        'total': len(alerts)
    }
    
    return summary


def check_predictive_alerts(patient_data: Dict, history_data: List[Dict] = None) -> List[ClinicalAlert]:
    """
    Check for predictive alerts based on trends
    
    Args:
        patient_data: Current patient data
        history_data: Historical data for trend analysis
    
    Returns:
        List of predictive alerts
    """
    alerts = []
    
    if not history_data or len(history_data) < 3:
        return alerts
    
    # Analyze trends
    import pandas as pd
    import numpy as np
    
    # Convert history to DataFrame
    df_data = []
    for entry in history_data:
        if 'ventilator' in entry:
            df_data.append({
                'timestamp': entry.get('timestamp', datetime.now()),
                'plateau': entry.get('ventilator', {}).get('plateau', None),
                'pf_ratio': entry.get('abg', {}).get('pf_ratio', None),
                'compliance': entry.get('ventilator', {}).get('compliance', None)
            })
    
    if len(df_data) < 3:
        return alerts
    
    df = pd.DataFrame(df_data)
    df = df.sort_values('timestamp')
    
    # Check plateau pressure trend
    if 'plateau' in df.columns and df['plateau'].notna().sum() >= 3:
        plateau_values = df['plateau'].dropna().values
        if len(plateau_values) >= 3:
            # Calculate trend
            x = np.arange(len(plateau_values))
            slope = np.polyfit(x, plateau_values, 1)[0]
            
            if slope > 0.5:  # Increasing trend
                current_plateau = plateau_values[-1]
                if current_plateau > 28:
                    alerts.append(ClinicalAlert(
                        priority='warning',
                        module='ventilator',
                        message=f'Plateau pressure đang tăng ({current_plateau:.1f} cmH2O) - Có thể vượt ngưỡng an toàn',
                        recommendation='Theo dõi sát, cân nhắc giảm Vt hoặc PEEP',
                        action='🫁 Ventilator Management'
                    ))
    
    # Check P/F ratio trend
    if 'pf_ratio' in df.columns and df['pf_ratio'].notna().sum() >= 3:
        pf_values = df['pf_ratio'].dropna().values
        if len(pf_values) >= 3:
            slope = np.polyfit(np.arange(len(pf_values)), pf_values, 1)[0]
            
            if slope < -5:  # Decreasing trend
                current_pf = pf_values[-1]
                if current_pf < 250:
                    alerts.append(ClinicalAlert(
                        priority='warning',
                        module='ventilator',
                        message=f'P/F ratio đang giảm ({current_pf:.0f}) - Có thể tiến triển ARDS',
                        recommendation='Cân nhắc tăng PEEP, đánh giá ARDS protocol',
                        action='🫁 ARDS Protocols'
                    ))
    
    return alerts


def get_alert_history(patient_data: Dict = None) -> List[Dict]:
    """
    Get alert history for a patient
    
    Args:
        patient_data: Patient data
    
    Returns:
        List of alert history entries
    """
    if 'alert_history' not in st.session_state:
        st.session_state['alert_history'] = []
    
    # Add current alerts to history
    current_alerts = check_all_alerts(patient_data or {})
    
    for alert in current_alerts:
        alert_entry = {
            'timestamp': datetime.now(),
            'priority': alert.priority,
            'module': alert.module,
            'message': alert.message,
            'resolved': False
        }
        
        # Check if already in history
        if not any(
            a['message'] == alert.message and not a['resolved']
            for a in st.session_state['alert_history']
        ):
            st.session_state['alert_history'].append(alert_entry)
    
    return st.session_state['alert_history']
