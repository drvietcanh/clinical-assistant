"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# NOTE: Data đã được tách ra thư mục infectious_other/
# File này import và merge tất cả để giữ backward compatibility

from .infectious_other import INFECTIOUS_OTHER_DRUGS

__all__ = ['INFECTIOUS_OTHER_DRUGS']
