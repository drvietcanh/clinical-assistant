"""
Antibiotic Database - Common Injectable Antibiotics in Vietnam
NOTE: This module imports from antibiotics_data_data.py which has been split.
This file maintains backward compatibility.
"""

from .antibiotics_data_data import ANTIBIOTICS_DATABASE

__all__ = ['ANTIBIOTICS_DATABASE']
