"""
Phase 1 Image Support Component
Adds image support for protocols (illustrations, flowcharts, diagrams)
"""

import streamlit as st
from pathlib import Path
from typing import Optional, List, Dict
import html


def render_protocol_image(
    image_path: str,
    caption: Optional[str] = None,
    alt_text: Optional[str] = None,
    width: Optional[int] = None
):
    """
    Render image in protocol with proper styling.
    
    Args:
        image_path: Path to image file (relative to static/images/)
        caption: Image caption
        alt_text: Alt text for accessibility
        width: Image width in pixels (optional)
    """
    static_dir = Path(__file__).parent.parent / "static" / "images"
    full_path = static_dir / image_path
    
    if not full_path.exists():
        st.warning(f"⚠️ Hình ảnh không tìm thấy: {image_path}")
        return
    
    # Display image
    st.image(str(full_path), caption=caption, width=width, use_column_width=True)
    
    if alt_text:
        st.caption(f"*{alt_text}*")


def render_flowchart_image(
    flowchart_path: str,
    title: Optional[str] = None,
    description: Optional[str] = None
):
    """
    Render flowchart image with title and description.
    
    Args:
        flowchart_path: Path to flowchart image
        title: Flowchart title
        description: Flowchart description
    """
    if title:
        st.markdown(f"### {title}")
    
    if description:
        st.info(description)
    
    render_protocol_image(flowchart_path, caption=title)
    st.markdown("---")


def render_anatomy_diagram(
    diagram_path: str,
    labels: Optional[List[str]] = None,
    caption: Optional[str] = None
):
    """
    Render anatomy diagram with labels.
    
    Args:
        diagram_path: Path to diagram image
        labels: List of labels to highlight
        caption: Diagram caption
    """
    st.markdown("### 📐 Sơ đồ giải phẫu")
    render_protocol_image(diagram_path, caption=caption)
    
    if labels:
        st.markdown("**Các cấu trúc được đánh dấu:**")
        for label in labels:
            st.markdown(f"- {label}")
    
    st.markdown("---")


def render_ecg_example(
    ecg_path: str,
    diagnosis: str,
    findings: Optional[List[str]] = None
):
    """
    Render ECG example with diagnosis and findings.
    
    Args:
        ecg_path: Path to ECG image
        diagnosis: ECG diagnosis
        findings: List of findings
    """
    st.markdown("### 📊 Ví dụ ECG")
    
    render_protocol_image(ecg_path, caption=f"ECG: {diagnosis}")
    
    st.markdown(f"**Chẩn đoán:** {diagnosis}")
    
    if findings:
        st.markdown("**Các dấu hiệu:**")
        for finding in findings:
            st.markdown(f"- {finding}")
    
    st.markdown("---")


def render_infographic(
    infographic_path: str,
    title: str,
    key_points: Optional[List[str]] = None
):
    """
    Render infographic for patient education.
    
    Args:
        infographic_path: Path to infographic image
        title: Infographic title
        key_points: List of key points
    """
    st.markdown(f"### 📊 {title}")
    
    render_protocol_image(infographic_path, caption=title)
    
    if key_points:
        st.markdown("**Điểm chính:**")
        for point in key_points:
            st.markdown(f"- {point}")
    
    st.markdown("---")


def render_image_gallery(
    images: List[Dict[str, str]],
    columns: int = 2
):
    """
    Render image gallery.
    
    Args:
        images: List of dicts with 'path', 'caption', 'alt'
        columns: Number of columns
    """
    st.markdown("### 🖼️ Hình ảnh minh họa")
    
    cols = st.columns(columns)
    
    for idx, image_info in enumerate(images):
        with cols[idx % columns]:
            render_protocol_image(
                image_info.get("path", ""),
                caption=image_info.get("caption", ""),
                alt_text=image_info.get("alt", "")
            )
    
    st.markdown("---")


# Image path registry for common medical images
IMAGE_REGISTRY = {
    "sepsis_flowchart": "protocols/sepsis_flowchart.png",
    "stroke_pathway": "protocols/stroke_pathway.png",
    "acls_algorithm": "protocols/acls_algorithm.png",
    "heart_anatomy": "anatomy/heart.png",
    "lung_anatomy": "anatomy/lung.png",
    "kidney_anatomy": "anatomy/kidney.png",
    "ecg_normal": "ecg/normal.png",
    "ecg_afib": "ecg/atrial_fibrillation.png",
    "ecg_stemi": "ecg/stemi.png"
}


def get_image_path(image_key: str) -> Optional[str]:
    """
    Get image path from registry.
    
    Args:
        image_key: Image key in registry
        
    Returns:
        Image path or None
    """
    return IMAGE_REGISTRY.get(image_key)

