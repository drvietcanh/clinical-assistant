"""
Basic unit tests for BMI/IBW/BSA calculator.

Các test này dùng các ví dụ chuẩn, giúp phát hiện sai lệch lớn trong công thức.
Chạy:
    pytest tests/scores/test_bmi_ibw_bsa.py
"""

from scores.metabolism.bmi_ibw_bsa import (
    calculate_bmi,
    calculate_ibw,
    calculate_abw,
    calculate_bsa_mosteller,
    calculate_bsa_dubois,
)


def test_calculate_bmi_normal_case():
    """BMI cho 70kg, 170cm ~ 24.2"""
    bmi = calculate_bmi(weight=70, height_cm=170)
    assert 24.1 < bmi < 24.3


def test_calculate_ibw_male_reference():
    """IBW nam 170cm (Devine): 50 + 0.91*(170-152.4) ≈ 65.9kg"""
    ibw = calculate_ibw(height_cm=170, gender="male")
    assert 65.0 < ibw < 67.0


def test_calculate_ibw_female_reference():
    """IBW nữ 160cm (Devine): 45.5 + 0.91*(160-152.4) ≈ 52.4kg"""
    ibw = calculate_ibw(height_cm=160, gender="female")
    assert 51.5 < ibw < 53.5


def test_calculate_abw_obese_case():
    """ABW cho bệnh nhân béo phì: IBW=60, actual=100 → ABW = 60 + 0.4*(40) = 76kg"""
    ibw = 60.0
    actual_weight = 100.0
    abw = calculate_abw(actual_weight=actual_weight, ibw=ibw)
    assert 75.0 < abw < 77.0


def test_bsa_mosteller_reference():
    """BSA Mosteller 70kg, 170cm ~ 1.84 m2"""
    bsa = calculate_bsa_mosteller(weight=70, height_cm=170)
    assert 1.8 < bsa < 1.9


def test_bsa_dubois_reference():
    """BSA DuBois 70kg, 170cm ~ 1.84 m2 (gần với Mosteller)"""
    bsa = calculate_bsa_dubois(weight=70, height_cm=170)
    assert 1.7 < bsa < 1.9

