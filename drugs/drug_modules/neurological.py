"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# NOTE: Data đã được tách ra thư mục neurological/
# File này import và merge tất cả để giữ backward compatibility

from .neurological import NEUROLOGICAL_DRUGS

__all__ = ['NEUROLOGICAL_DRUGS']
