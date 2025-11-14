"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# NOTE: Data đã được tách ra thư mục supportive/
# File này import và merge tất cả để giữ backward compatibility

from .supportive import SUPPORTIVE_DRUGS

__all__ = ['SUPPORTIVE_DRUGS']
