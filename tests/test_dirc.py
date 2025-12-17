from critical_care.dirc.conversions import (
    mcg_kg_min_to_ml_hr,
    ml_hr_to_mcg_kg_min,
)


def test_mcg_kg_min_to_ml_hr_basic():
    assert mcg_kg_min_to_ml_hr(5, 70, 1) == 21.0
    assert mcg_kg_min_to_ml_hr(10, 50, 2) == 15.0


def test_ml_hr_to_mcg_kg_min_basic():
    assert ml_hr_to_mcg_kg_min(21, 70, 1) == 5.0
    assert ml_hr_to_mcg_kg_min(15, 50, 2) == 10.0


