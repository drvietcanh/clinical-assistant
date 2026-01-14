"""
Unit tests cho CHA₂DS₂-VASc score.

Các case dựa trên logic chuẩn:
- Mỗi yếu tố nguy cơ 1 hoặc 2 điểm
- Nữ giới +1 điểm nếu có thêm yếu tố.
"""

from scores.cardiology.cha2ds2vasc import calculate_cha2ds2vasc_score


def test_male_low_risk_zero_points():
    """Nam, <65 tuổi, không yếu tố nguy cơ → 0 điểm."""
    score = calculate_cha2ds2vasc_score(
        chf=False,
        htn=False,
        age_group="< 65 tuổi",
        dm=False,
        stroke=False,
        vasc=False,
        sex="Nam",
    )
    assert score == 0


def test_male_moderate_risk_two_points():
    """Nam, 68 tuổi + THA → 2 điểm (age 65-74 =1, HTN=1)."""
    score = calculate_cha2ds2vasc_score(
        chf=False,
        htn=True,
        age_group="65-74 tuổi",
        dm=False,
        stroke=False,
        vasc=False,
        sex="Nam",
    )
    assert score == 2


def test_female_sex_point_only():
    """Nữ, <65 tuổi, không yếu tố khác → 1 điểm (giới tính)."""
    score = calculate_cha2ds2vasc_score(
        chf=False,
        htn=False,
        age_group="< 65 tuổi",
        dm=False,
        stroke=False,
        vasc=False,
        sex="Nữ",
    )
    assert score == 1


def test_high_risk_multiple_factors():
    """Bệnh nhân rất nguy cơ cao với nhiều yếu tố."""
    score = calculate_cha2ds2vasc_score(
        chf=True,
        htn=True,
        age_group="≥ 75 tuổi",  # 2 điểm
        dm=True,
        stroke=True,  # 2 điểm
        vasc=True,
        sex="Nữ",  # 1 điểm
    )
    # CHF(1) + HTN(1) + Age≥75(2) + DM(1) + Stroke(2) + Vasc(1) + Sex(1) = 9
    assert score == 9

