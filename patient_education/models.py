"""
Patient Education Models
Data models for patient education topics
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class PatientEducationTopic:
    """Patient education topic information"""
    id: str
    title: str
    title_vn: str
    category: str  # Disease, Medication, Lifestyle, Procedure
    content: str  # Main content in simple language
    related_disease: Optional[str] = None  # Link to disease
    related_drugs: List[str] = field(default_factory=list)  # Link to drugs
    printable: bool = True
    language: str = "vi"  # Vietnamese

