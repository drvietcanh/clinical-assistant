"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# NOTE: Data đã được tách ra thư mục gastrointestinal/
# File này import và merge tất cả để giữ backward compatibility

from .gastrointestinal import GASTROINTESTINAL_DRUGS

__all__ = ['GASTROINTESTINAL_DRUGS']
