"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# NOTE: Data đã được tách ra thư mục analgesics/
# File này import và merge tất cả để giữ backward compatibility

from .analgesics import ANALGESICS_DRUGS

__all__ = ['ANALGESICS_DRUGS']
