"""
Image Library Component
Structure and utilities for medical illustrations and visual aids
"""

import streamlit as st
from pathlib import Path
from typing import Optional, Dict, List
import html


# Image library structure
IMAGE_LIBRARY = {
    "protocols": {
        "sepsis": {
            "path": "static/images/protocols/sepsis/",
            "images": {
                "sepsis_pathophysiology": "sepsis_pathophysiology.png",
                "sepsis_algorithm": "sepsis_algorithm.png",
                "sepsis_timeline": "sepsis_timeline.png"
            }
        },
        "stroke": {
            "path": "static/images/protocols/stroke/",
            "images": {
                "stroke_types": "stroke_types.png",
                "stroke_algorithm": "stroke_algorithm.png",
                "ct_scan_examples": "ct_scan_examples.png"
            }
        },
        "acs": {
            "path": "static/images/protocols/acs/",
            "images": {
                "ecg_stemi": "ecg_stemi.png",
                "ecg_nstemi": "ecg_nstemi.png",
                "acs_algorithm": "acs_algorithm.png"
            }
        }
    },
    "anatomy": {
        "path": "static/images/anatomy/",
        "images": {
            "heart_anatomy": "heart_anatomy.png",
            "brain_anatomy": "brain_anatomy.png",
            "lung_anatomy": "lung_anatomy.png"
        }
    },
    "flowcharts": {
        "path": "static/images/flowcharts/",
        "images": {
            "sepsis_flowchart": "sepsis_flowchart.png",
            "stroke_flowchart": "stroke_flowchart.png",
            "acs_flowchart": "acs_flowchart.png"
        }
    },
    "ecg": {
        "path": "static/images/ecg/",
        "images": {
            "normal_ecg": "normal_ecg.png",
            "stemi_ecg": "stemi_ecg.png",
            "afib_ecg": "afib_ecg.png"
        }
    }
}


def get_image_path(category: str, subcategory: str, image_name: str) -> Optional[str]:
    """
    Get image path from library.
    
    Args:
        category: Image category (protocols, anatomy, flowcharts, ecg)
        subcategory: Subcategory (sepsis, stroke, etc.)
        image_name: Image filename
        
    Returns:
        Full path to image or None if not found
    """
    if category not in IMAGE_LIBRARY:
        return None
    
    if category == "protocols" or category == "flowcharts":
        if subcategory not in IMAGE_LIBRARY[category]:
            return None
        if image_name not in IMAGE_LIBRARY[category][subcategory]["images"]:
            return None
        return f"{IMAGE_LIBRARY[category][subcategory]['path']}{IMAGE_LIBRARY[category][subcategory]['images'][image_name]}"
    else:
        if image_name not in IMAGE_LIBRARY[category]["images"]:
            return None
        return f"{IMAGE_LIBRARY[category]['path']}{IMAGE_LIBRARY[category]['images'][image_name]}"


def render_medical_image(
    image_path: str,
    caption: Optional[str] = None,
    alt_text: Optional[str] = None,
    width: Optional[int] = None,
    show_placeholder: bool = True
):
    """
    Render medical image with proper styling.
    
    Args:
        image_path: Path to image file
        - Can be relative path from static/images/
        - Or full path
        caption: Image caption
        alt_text: Alt text for accessibility
        width: Image width in pixels
        show_placeholder: Show placeholder if image not found
    """
    # Check if image exists
    full_path = Path("static/images") / image_path if not image_path.startswith("/") else image_path
    image_exists = full_path.exists()
    
    if not image_exists and show_placeholder:
        # Show placeholder
        placeholder_html = f"""
        <div style="
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 8px;
            padding: 40px;
            text-align: center;
            margin: 20px 0;
        ">
            <div style="font-size: 3rem; margin-bottom: 10px;">🖼️</div>
            <div style="color: #6c757d; font-size: 0.9rem;">
                {html.escape(caption or 'Medical illustration')}
            </div>
            <div style="color: #adb5bd; font-size: 0.75rem; margin-top: 8px;">
                (Image placeholder - {html.escape(image_path)})
            </div>
        </div>
        """
        st.markdown(placeholder_html, unsafe_allow_html=True)
        return
    
    if image_exists:
        # Render actual image
        width_style = f"width: {width}px;" if width else "width: 100%; max-width: 800px;"
        
        image_html = f"""
        <div style="margin: 20px 0; text-align: center;">
            <img src="/{full_path}" 
                 alt="{html.escape(alt_text or caption or 'Medical illustration')}"
                 style="{width_style} border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />
            {f'<div style="margin-top: 8px; color: #6c757d; font-size: 0.85rem; font-style: italic;">{html.escape(caption)}</div>' if caption else ''}
        </div>
        """
        st.markdown(image_html, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Image not found: {image_path}")


def render_image_gallery(
    images: List[Dict],
    columns: int = 2
):
    """
    Render image gallery.
    
    Args:
        images: List of dicts with 'path', 'caption', 'alt_text'
        columns: Number of columns
    """
    cols = st.columns(columns)
    
    for idx, image in enumerate(images):
        with cols[idx % columns]:
            render_medical_image(
                image_path=image.get("path", ""),
                caption=image.get("caption"),
                alt_text=image.get("alt_text"),
                width=image.get("width")
            )


def create_image_structure():
    """
    Create image library directory structure.
    This should be run once to set up the folder structure.
    """
    base_path = Path("static/images")
    
    directories = [
        base_path / "protocols" / "sepsis",
        base_path / "protocols" / "stroke",
        base_path / "protocols" / "acs",
        base_path / "protocols" / "heart_failure",
        base_path / "anatomy",
        base_path / "flowcharts",
        base_path / "ecg",
        base_path / "xray",
        base_path / "diagrams"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        # Create .gitkeep to preserve empty directories
        (directory / ".gitkeep").touch(exist_ok=True)
    
    return directories

