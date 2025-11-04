"""
Drug Database - Common Medications in Vietnam
Database 100-200 thuốc phổ biến tại Việt Nam
Ưu tiên thuốc thường dùng trong lâm sàng

NOTE: Data đã được tách ra file drug_database_data.py
File này chỉ re-export để giữ backward compatibility
"""

from .drug_database_data import (
    DRUG_DATABASE,
    DRUG_GROUPS,
    TOTAL_DRUGS
)

__all__ = ['DRUG_DATABASE', 'DRUG_GROUPS', 'TOTAL_DRUGS']
