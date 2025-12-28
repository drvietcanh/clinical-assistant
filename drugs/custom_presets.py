"""
Custom Drug Presets Manager
Allow users to create and manage custom drug presets
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
import streamlit as st


def _get_presets_file_path() -> Path:
    """Get path to custom presets file."""
    # Use session-based storage for now (can be changed to file-based later)
    return Path(__file__).parent.parent / "data" / "custom_presets.json"


def _load_custom_presets() -> Dict:
    """Load custom presets from file."""
    presets_path = _get_presets_file_path()
    try:
        if presets_path.exists():
            with open(presets_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def _save_custom_presets(presets: Dict):
    """Save custom presets to file."""
    presets_path = _get_presets_file_path()
    presets_path.parent.mkdir(parents=True, exist_ok=True)
    with open(presets_path, "w", encoding="utf-8") as f:
        json.dump(presets, f, ensure_ascii=False, indent=2)


def get_custom_presets() -> Dict:
    """Get all custom presets."""
    return _load_custom_presets()


def add_custom_preset(
    preset_name: str,
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None,
    notes: Optional[str] = None
) -> bool:
    """
    Add a custom preset.
    
    Args:
        preset_name: Name of preset
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: Infusion method
        drop_factor: Optional drop factor
        notes: Optional notes
    
    Returns:
        True if added successfully
    """
    presets = _load_custom_presets()
    
    presets[preset_name] = {
        "drug_name": drug_name,
        "dose_mcg_kg_min": dose_mcg_kg_min,
        "weight_kg": weight_kg,
        "infusion_method": infusion_method,
        "drop_factor": drop_factor,
        "notes": notes
    }
    
    _save_custom_presets(presets)
    return True


def delete_custom_preset(preset_name: str) -> bool:
    """Delete a custom preset."""
    presets = _load_custom_presets()
    if preset_name in presets:
        del presets[preset_name]
        _save_custom_presets(presets)
        return True
    return False


def get_custom_preset(preset_name: str) -> Optional[Dict]:
    """Get a custom preset by name."""
    presets = _load_custom_presets()
    return presets.get(preset_name)


def export_presets() -> str:
    """Export presets as JSON string."""
    presets = _load_custom_presets()
    return json.dumps(presets, ensure_ascii=False, indent=2)


def import_presets(presets_json: str) -> bool:
    """Import presets from JSON string."""
    try:
        presets = json.loads(presets_json)
        _save_custom_presets(presets)
        return True
    except json.JSONDecodeError:
        return False

