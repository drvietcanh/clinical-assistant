"""Oncology Medications
Active module - contains all oncology drug data"""

# NOTE: Data đã được tách ra thư mục oncology/
# File này import và merge tất cả để giữ backward compatibility

from .oncology import ONCOLOGY_DRUGS

__all__ = ['ONCOLOGY_DRUGS']
