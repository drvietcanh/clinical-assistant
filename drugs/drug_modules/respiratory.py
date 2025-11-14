"""Respiratory Medications
Active module - contains all respiratory drug data"""

# NOTE: Data đã được tách ra thư mục respiratory/
# File này import và merge tất cả để giữ backward compatibility

from .respiratory import RESPIRATORY_DRUGS

__all__ = ['RESPIRATORY_DRUGS']
