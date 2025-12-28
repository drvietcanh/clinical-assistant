"""
Shock Index Calculator
Calculate shock index for early shock detection
"""

from typing import Dict, List, Optional
from datetime import datetime


class ShockIndexScore:
    """Represents a shock index assessment."""
    
    def __init__(
        self,
        heart_rate: float,
        systolic_bp: float,
        shock_index: float,
        notes: Optional[str] = None
    ):
        self.heart_rate = heart_rate
        self.systolic_bp = systolic_bp
        self.shock_index = shock_index
        self.notes = notes
        self.timestamp = datetime.now()
    
    def get_classification(self) -> str:
        """Get shock index classification."""
        if self.shock_index < 0.7:
            return "Bình thường (Normal)"
        elif self.shock_index <= 1.0:
            return "Tăng (Elevated)"
        else:
            return "Cao (High) - Sốc"
    
    def get_severity(self) -> str:
        """Get severity level."""
        if self.shock_index < 0.7:
            return "Không sốc"
        elif self.shock_index <= 1.0:
            return "Nguy cơ sốc"
        else:
            return "Sốc"
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "heart_rate": self.heart_rate,
            "systolic_bp": self.systolic_bp,
            "shock_index": self.shock_index,
            "classification": self.get_classification(),
            "severity": self.get_severity(),
            "notes": self.notes,
            "timestamp": self.timestamp.isoformat()
        }


def calculate_shock_index(heart_rate: float, systolic_bp: float) -> Dict:
    """
    Calculate shock index.
    
    Args:
        heart_rate: Heart rate (bpm)
        systolic_bp: Systolic blood pressure (mmHg)
    
    Returns:
        Dictionary with shock index details
    """
    # Validate inputs
    if heart_rate <= 0:
        raise ValueError("Heart rate must be positive")
    if systolic_bp <= 0:
        raise ValueError("Systolic BP must be positive")
    
    # Calculate shock index
    shock_index = heart_rate / systolic_bp
    
    # Classify
    if shock_index < 0.7:
        classification = "Bình thường (Normal)"
        severity = "Không sốc"
        risk_level = "Thấp"
    elif shock_index <= 1.0:
        classification = "Tăng (Elevated)"
        severity = "Nguy cơ sốc"
        risk_level = "Trung bình"
    else:
        classification = "Cao (High) - Sốc"
        severity = "Sốc"
        risk_level = "Cao"
    
    # Generate interpretation
    interpretation = []
    if shock_index < 0.7:
        interpretation.append("Shock index bình thường - Không có dấu hiệu sốc")
    elif shock_index <= 1.0:
        interpretation.append("⚠️ Shock index tăng - Cần theo dõi sát")
        interpretation.append("⚠️ Có nguy cơ sốc - Cần đánh giá thêm")
    else:
        interpretation.append("❌ Shock index cao - Nghi ngờ sốc")
        interpretation.append("❌ Cần can thiệp ngay - Truyền dịch, vasopressor")
    
    # Generate recommendations
    recommendations = []
    if shock_index >= 1.0:
        recommendations.append("🔴 Can thiệp ngay:")
        recommendations.append("  • Truyền dịch tĩnh mạch (NS, LR)")
        recommendations.append("  • Đánh giá đáp ứng dịch")
        recommendations.append("  • Xem xét vasopressor nếu không đáp ứng")
        recommendations.append("  • Theo dõi sát huyết áp, nhịp tim")
        recommendations.append("  • Đánh giá nguyên nhân sốc")
    elif shock_index >= 0.7:
        recommendations.append("⚠️ Theo dõi sát:")
        recommendations.append("  • Đánh giá lại sau 15-30 phút")
        recommendations.append("  • Xem xét truyền dịch nếu có chỉ định")
        recommendations.append("  • Theo dõi các dấu hiệu sốc khác")
    
    # Additional clinical context
    clinical_context = []
    if systolic_bp < 90:
        clinical_context.append("⚠️ Huyết áp tâm thu < 90 mmHg - Hạ huyết áp")
    if heart_rate > 100:
        clinical_context.append("⚠️ Nhịp tim > 100 bpm - Nhịp nhanh")
    if heart_rate > 120:
        clinical_context.append("⚠️ Nhịp tim > 120 bpm - Nhịp nhanh rõ")
    
    return {
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "shock_index": round(shock_index, 2),
        "classification": classification,
        "severity": severity,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "recommendations": recommendations,
        "clinical_context": clinical_context
    }


def add_shock_index_to_history(
    history: List[Dict],
    heart_rate: float,
    systolic_bp: float,
    notes: Optional[str] = None
) -> Dict:
    """
    Add shock index to history.
    
    Args:
        history: List of previous shock index assessments
        heart_rate: Heart rate (bpm)
        systolic_bp: Systolic BP (mmHg)
        notes: Optional notes
    
    Returns:
        Shock index dictionary
    """
    result = calculate_shock_index(heart_rate, systolic_bp)
    shock_index = result["shock_index"]
    
    score = ShockIndexScore(heart_rate, systolic_bp, shock_index, notes)
    score_dict = score.to_dict()
    history.append(score_dict)
    
    return score_dict


def get_shock_index_trend(history: List[Dict]) -> Dict:
    """
    Analyze shock index trend.
    
    Args:
        history: List of shock index assessments
    
    Returns:
        Trend analysis dictionary
    """
    if len(history) < 2:
        return {
            "trend": "Không đủ dữ liệu",
            "change": 0,
            "first_index": history[0].get("shock_index", 0) if history else 0,
            "last_index": history[-1].get("shock_index", 0) if history else 0,
            "total_assessments": len(history)
        }
    
    first_index = history[0].get("shock_index", 0)
    last_index = history[-1].get("shock_index", 0)
    change = last_index - first_index
    
    if change > 0.1:
        trend = "Xấu đi (Tăng)"
        worsening = True
    elif change < -0.1:
        trend = "Cải thiện (Giảm)"
        worsening = False
    else:
        trend = "Ổn định"
        worsening = None
    
    return {
        "trend": trend,
        "change": round(change, 2),
        "first_index": round(first_index, 2),
        "last_index": round(last_index, 2),
        "worsening": worsening,
        "total_assessments": len(history)
    }


def get_shock_index_reference() -> Dict:
    """Get shock index reference values."""
    return {
        "normal": "< 0.7",
        "elevated": "0.7 - 1.0",
        "high": "> 1.0",
        "formula": "Shock Index = Heart Rate / Systolic BP",
        "clinical_significance": {
            "normal": "Không có dấu hiệu sốc",
            "elevated": "Nguy cơ sốc - Cần theo dõi",
            "high": "Nghi ngờ sốc - Cần can thiệp"
        },
        "notes": [
            "Shock index là chỉ số đơn giản để phát hiện sốc sớm",
            "Nhạy cảm hơn huyết áp hoặc nhịp tim đơn lẻ",
            "Có giá trị trong cấp cứu và ICU",
            "Shock index > 1.0 gợi ý sốc rõ ràng",
            "Cần đánh giá toàn diện kèm các dấu hiệu khác"
        ]
    }

