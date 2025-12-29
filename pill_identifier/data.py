"""
Pill Identifier Database
Drug identification by physical characteristics (color, shape, imprint, size)
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Pill:
    """Pill/drug physical characteristics"""
    drug_name: str
    generic_name: str
    color: str  # e.g., "White", "Yellow", "Blue"
    shape: str  # e.g., "Round", "Oval", "Capsule"
    imprint: str = ""  # Text or numbers on pill
    size: str = ""  # e.g., "Small", "Medium", "Large"
    strength: str = ""  # e.g., "500mg", "10mg"
    form: str = "Tablet"  # Tablet, Capsule, etc.
    notes: str = ""


# Pill Database
# Common drugs with physical characteristics
PILL_DATABASE: List[Pill] = [
    # === ANTIBIOTICS ===
    Pill(
        drug_name="Amoxicillin",
        generic_name="Amoxicillin",
        color="White",
        shape="Capsule",
        imprint="AMOX 500",
        size="Medium",
        strength="500mg",
        form="Capsule"
    ),
    Pill(
        drug_name="Amoxicillin",
        generic_name="Amoxicillin",
        color="Pink",
        shape="Oval",
        imprint="AMOX 250",
        size="Small",
        strength="250mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Azithromycin",
        generic_name="Azithromycin",
        color="White",
        shape="Oval",
        imprint="AZ 500",
        size="Large",
        strength="500mg",
        form="Tablet"
    ),
    
    # === CARDIOVASCULAR ===
    Pill(
        drug_name="Amlodipine",
        generic_name="Amlodipine",
        color="White",
        shape="Round",
        imprint="AML 5",
        size="Small",
        strength="5mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Amlodipine",
        generic_name="Amlodipine",
        color="White",
        shape="Round",
        imprint="AML 10",
        size="Small",
        strength="10mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Atenolol",
        generic_name="Atenolol",
        color="White",
        shape="Round",
        imprint="ATN 50",
        size="Small",
        strength="50mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Enalapril",
        generic_name="Enalapril",
        color="White",
        shape="Round",
        imprint="ENL 5",
        size="Small",
        strength="5mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Losartan",
        generic_name="Losartan",
        color="White",
        shape="Oval",
        imprint="LOS 50",
        size="Medium",
        strength="50mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Atorvastatin",
        generic_name="Atorvastatin",
        color="White",
        shape="Oval",
        imprint="ATV 20",
        size="Medium",
        strength="20mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Atorvastatin",
        generic_name="Atorvastatin",
        color="White",
        shape="Oval",
        imprint="ATV 40",
        size="Medium",
        strength="40mg",
        form="Tablet"
    ),
    
    # === DIABETES ===
    Pill(
        drug_name="Metformin",
        generic_name="Metformin",
        color="White",
        shape="Round",
        imprint="MET 500",
        size="Medium",
        strength="500mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Metformin",
        generic_name="Metformin",
        color="White",
        shape="Round",
        imprint="MET 850",
        size="Large",
        strength="850mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Gliclazide",
        generic_name="Gliclazide",
        color="White",
        shape="Round",
        imprint="GLZ 80",
        size="Small",
        strength="80mg",
        form="Tablet"
    ),
    
    # === GI ===
    Pill(
        drug_name="Omeprazole",
        generic_name="Omeprazole",
        color="Pink",
        shape="Capsule",
        imprint="OME 20",
        size="Medium",
        strength="20mg",
        form="Capsule"
    ),
    Pill(
        drug_name="Omeprazole",
        generic_name="Omeprazole",
        color="Pink",
        shape="Capsule",
        imprint="OME 40",
        size="Medium",
        strength="40mg",
        form="Capsule"
    ),
    
    # === ANALGESICS ===
    Pill(
        drug_name="Paracetamol",
        generic_name="Paracetamol",
        color="White",
        shape="Round",
        imprint="PAR 500",
        size="Medium",
        strength="500mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Ibuprofen",
        generic_name="Ibuprofen",
        color="White",
        shape="Round",
        imprint="IBU 400",
        size="Medium",
        strength="400mg",
        form="Tablet"
    ),
    
    # === ANTICOAGULANTS ===
    Pill(
        drug_name="Warfarin",
        generic_name="Warfarin",
        color="Blue",
        shape="Round",
        imprint="WAR 5",
        size="Small",
        strength="5mg",
        form="Tablet"
    ),
    Pill(
        drug_name="Warfarin",
        generic_name="Warfarin",
        color="Pink",
        shape="Round",
        imprint="WAR 2",
        size="Small",
        strength="2mg",
        form="Tablet"
    ),
    
    # === ANTIHISTAMINES ===
    Pill(
        drug_name="Loratadine",
        generic_name="Loratadine",
        color="White",
        shape="Round",
        imprint="LOR 10",
        size="Small",
        strength="10mg",
        form="Tablet"
    ),
    
    # === ANTACIDS ===
    Pill(
        drug_name="Calcium Carbonate",
        generic_name="Calcium Carbonate",
        color="White",
        shape="Round",
        imprint="",
        size="Large",
        strength="500mg",
        form="Tablet",
        notes="Antacid, thường không có ký hiệu"
    ),
]


def get_all_pills() -> List[Pill]:
    """Get all pills"""
    return PILL_DATABASE


def get_pills_by_color(color: str) -> List[Pill]:
    """Get pills filtered by color"""
    if not color or color == "All":
        return PILL_DATABASE
    return [p for p in PILL_DATABASE if p.color.lower() == color.lower()]


def get_pills_by_shape(shape: str) -> List[Pill]:
    """Get pills filtered by shape"""
    if not shape or shape == "All":
        return PILL_DATABASE
    return [p for p in PILL_DATABASE if p.shape.lower() == shape.lower()]


def get_color_list() -> List[str]:
    """Get list of all colors"""
    colors = set(p.color for p in PILL_DATABASE)
    return sorted(list(colors))


def get_shape_list() -> List[str]:
    """Get list of all shapes"""
    shapes = set(p.shape for p in PILL_DATABASE)
    return sorted(list(shapes))

