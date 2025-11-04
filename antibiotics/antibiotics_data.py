"""
Antibiotic Database - Common Injectable Antibiotics in Vietnam
Ưu tiên kháng sinh tiêm truyền (IV/IM) thông dụng tại Việt Nam

NOTE: Data đã được tách ra file antibiotics_data_data.py
File này chỉ re-export để giữ backward compatibility
"""

from .antibiotics_data_data import ANTIBIOTICS_DATABASE

__all__ = ['ANTIBIOTICS_DATABASE']
