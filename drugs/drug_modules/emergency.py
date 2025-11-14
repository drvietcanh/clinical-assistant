"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# NOTE: Data đã được tách ra thư mục emergency/
# File này import và merge tất cả để giữ backward compatibility

from .emergency import EMERGENCY_DRUGS

__all__ = ['EMERGENCY_DRUGS']
