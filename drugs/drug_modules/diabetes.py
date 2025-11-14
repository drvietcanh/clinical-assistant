"""Diabetes Medications
Active module - contains all diabetes drug data"""

# NOTE: Data đã được tách ra thư mục diabetes/
# File này import và merge tất cả để giữ backward compatibility

from .diabetes import DIABETES_DRUGS

__all__ = ['DIABETES_DRUGS']
