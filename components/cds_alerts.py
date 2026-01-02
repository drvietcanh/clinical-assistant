"""
Clinical Decision Support (CDS) Alerts Component
Alert system for drug interactions, contraindications, and clinical warnings
"""

import streamlit as st
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass


class AlertSeverity(Enum):
    """Alert severity levels"""
    CRITICAL = "critical"  # Red - Immediate action required
    WARNING = "warning"   # Orange - Caution advised
    INFO = "info"         # Blue - Informational
    SUCCESS = "success"   # Green - Positive confirmation


@dataclass
class CDSAlert:
    """CDS Alert data structure"""
    severity: AlertSeverity
    title: str
    message: str
    category: str  # 'interaction', 'contraindication', 'dosing', 'monitoring', etc.
    actionable: bool = False
    action_text: Optional[str] = None
    references: Optional[List[str]] = None


def render_cds_alert(alert: CDSAlert) -> None:
    """
    Render a CDS alert
    
    Args:
        alert: CDSAlert object
    """
    severity_colors = {
        AlertSeverity.CRITICAL: ("#f44336", "🔴"),
        AlertSeverity.WARNING: ("#ff9800", "⚠️"),
        AlertSeverity.INFO: ("#2196f3", "ℹ️"),
        AlertSeverity.SUCCESS: ("#4caf50", "✅"),
    }
    
    color, icon = severity_colors.get(alert.severity, ("#757575", "ℹ️"))
    
    alert_html = f"""
    <div style="
        background: {color}15;
        border-left: 4px solid {color};
        padding: 12px;
        border-radius: 4px;
        margin: 8px 0;
    ">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 1.2em;">{icon}</span>
            <strong style="color: {color}; font-size: 1.1em;">{alert.title}</strong>
        </div>
        <div style="color: var(--text-primary, #212121); margin-bottom: 8px;">
            {alert.message}
        </div>
    """
    
    if alert.actionable and alert.action_text:
        alert_html += f"""
        <div style="margin-top: 8px;">
            <strong>Hành động đề xuất:</strong> {alert.action_text}
        </div>
        """
    
    if alert.references:
        alert_html += f"""
        <div style="margin-top: 8px; font-size: 0.85em; color: var(--text-secondary, #666);">
            <strong>Tham khảo:</strong> {', '.join(alert.references)}
        </div>
        """
    
    alert_html += "</div>"
    
    st.markdown(alert_html, unsafe_allow_html=True)


def check_drug_interactions(drugs: List[str]) -> List[CDSAlert]:
    """
    Check for drug interactions
    
    Args:
        drugs: List of drug names
    
    Returns:
        List of CDSAlert objects
    """
    alerts = []
    
    # Example interaction checks (to be expanded with actual data)
    known_interactions = {
        ("Warfarin", "Aspirin"): {
            "severity": AlertSeverity.CRITICAL,
            "message": "Tăng nguy cơ chảy máu khi dùng chung Warfarin và Aspirin"
        },
        ("Digoxin", "Amiodarone"): {
            "severity": AlertSeverity.WARNING,
            "message": "Amiodarone có thể làm tăng nồng độ Digoxin, cần theo dõi nồng độ"
        }
    }
    
    # Check for known interactions
    for i, drug1 in enumerate(drugs):
        for drug2 in drugs[i+1:]:
            key1 = (drug1, drug2)
            key2 = (drug2, drug1)
            
            interaction = known_interactions.get(key1) or known_interactions.get(key2)
            if interaction:
                alerts.append(CDSAlert(
                    severity=interaction["severity"],
                    title="Tương tác thuốc",
                    message=interaction["message"],
                    category="interaction",
                    actionable=True,
                    action_text="Xem xét điều chỉnh liều hoặc thay thế thuốc",
                    references=["Drug Interaction Database"]
                ))
    
    return alerts


def check_contraindications(drug: str, conditions: List[str]) -> List[CDSAlert]:
    """
    Check for contraindications
    
    Args:
        drug: Drug name
        conditions: List of patient conditions
    
    Returns:
        List of CDSAlert objects
    """
    alerts = []
    
    # Example contraindications (to be expanded with actual data)
    known_contraindications = {
        "Warfarin": ["Pregnancy", "Active bleeding"],
        "ACE Inhibitors": ["Pregnancy", "Bilateral renal artery stenosis"],
        "Metformin": ["Severe renal impairment", "Lactic acidosis"],
    }
    
    contraindications = known_contraindications.get(drug, [])
    
    for condition in conditions:
        if condition in contraindications:
            alerts.append(CDSAlert(
                severity=AlertSeverity.CRITICAL,
                title="Chống chỉ định",
                message=f"{drug} chống chỉ định ở bệnh nhân có {condition}",
                category="contraindication",
                actionable=True,
                action_text="Không sử dụng thuốc này, tìm thuốc thay thế",
                references=["Drug Database"]
            ))
    
    return alerts


def render_cds_alerts_panel(alerts: List[CDSAlert]) -> None:
    """
    Render panel with all CDS alerts
    
    Args:
        alerts: List of CDSAlert objects
    """
    if not alerts:
        return
    
    # Group by severity
    critical = [a for a in alerts if a.severity == AlertSeverity.CRITICAL]
    warnings = [a for a in alerts if a.severity == AlertSeverity.WARNING]
    info = [a for a in alerts if a.severity == AlertSeverity.INFO]
    
    st.markdown("### 🚨 Cảnh báo Lâm sàng (CDS)")
    
    if critical:
        st.markdown("#### 🔴 Cảnh báo nghiêm trọng")
        for alert in critical:
            render_cds_alert(alert)
    
    if warnings:
        st.markdown("#### ⚠️ Cảnh báo")
        for alert in warnings:
            render_cds_alert(alert)
    
    if info:
        st.markdown("#### ℹ️ Thông tin")
        for alert in info:
            render_cds_alert(alert)


__all__ = [
    'AlertSeverity',
    'CDSAlert',
    'render_cds_alert',
    'check_drug_interactions',
    'check_contraindications',
    'render_cds_alerts_panel',
]

