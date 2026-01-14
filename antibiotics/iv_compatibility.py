"""
IV Compatibility Checker - Phase 5
Kiểm tra tính tương thích khi pha chế IV
"""

import streamlit as st
from typing import Dict, List, Tuple, Optional

# IV Compatibility Database
# Format: {("Drug1", "Drug2"): {
#     "y_site": "compatible"/"incompatible"/"questionable",
#     "same_line": "compatible"/"incompatible"/"questionable",
#     "notes": "...",
#     "dilution": "...",
#     "stability": "...",
#     "severity": "major"/"minor"/"info",
#     "sources": [...]
# }}
# Note: If y_site or same_line not specified, fallback to old "compatible" field
IV_COMPATIBILITY_DB = {
    # Vancomycin
    ("Vancomycin", "Piperacillin-Tazobactam"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,  # Backward compatibility
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng hoặc rửa line giữa các liều.",
        "dilution": "Vancomycin: Pha trong NS hoặc D5W (250-500mg trong 100-250mL). Piperacillin-Tazobactam: Pha trong NS (3.375g trong 50-100mL).",
        "stability": "Vancomycin: Ổn định 24h ở nhiệt độ phòng. Piperacillin-Tazobactam: Ổn định 24h ở nhiệt độ phòng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Vancomycin", "Ceftriaxone"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "dilution": "Vancomycin: Pha trong NS hoặc D5W. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Vancomycin: Ổn định 24h. Ceftriaxone: Ổn định 24h ở nhiệt độ phòng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "Aminoglycosides"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "dilution": "Vancomycin: Pha trong NS hoặc D5W. Aminoglycosides: Pha trong NS hoặc D5W.",
        "stability": "Vancomycin: Ổn định 24h. Aminoglycosides: Ổn định 24h.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Vancomycin", "Amphotericin B"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline (0.9% NaCl).",
        "dilution": "Pha trong NS: 250-500mg trong 100-250mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Vancomycin", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Dextrose 5% in Water.",
        "dilution": "Pha trong D5W: 250-500mg trong 100-250mL D5W.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Piperacillin-Tazobactam
    ("Piperacillin-Tazobactam", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng hoặc rửa line giữa các liều.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Piperacillin-Tazobactam", "Aminoglycosides"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Piperacillin-Tazobactam", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Ceftriaxone
    ("Ceftriaxone", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ceftriaxone", "Calcium"): {
        "compatible": False,
        "notes": "Không tương thích với calcium - Tạo kết tủa. Tránh pha chung hoặc truyền cùng lúc.",
        "severity": "major",
        "sources": ["FDA Warning", "Trissel's IV Compatibility"]
    },
    ("Ceftriaxone", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Meropenem
    ("Meropenem", "NS"): {
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Meropenem", "D5W"): {
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Aminoglycosides
    ("Aminoglycosides", "Vancomycin"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Aminoglycosides", "Beta-lactams"): {
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Common IV fluids
    ("NS", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích.",
        "severity": "info",
        "sources": ["Standard"]
    },
    
    # Meropenem
    ("Meropenem", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Meropenem: Pha trong NS hoặc D5W (1g trong 50-100mL). Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Meropenem: Ổn định 4h ở nhiệt độ phòng. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Meropenem", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Meropenem: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Meropenem: Ổn định 4h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Ceftriaxone - More entries
    ("Ceftriaxone", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ceftriaxone: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Ceftriaxone: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ceftriaxone", "Meropenem"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ceftriaxone: Pha trong NS hoặc D5W. Meropenem: Pha trong NS hoặc D5W.",
        "stability": "Ceftriaxone: Ổn định 24h. Meropenem: Ổn định 4h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Fluoroquinolones
    ("Ciprofloxacin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 200-400mg trong 100-250mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ciprofloxacin", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "dilution": "Pha trong D5W: 200-400mg trong 100-250mL D5W.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ciprofloxacin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ciprofloxacin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Ciprofloxacin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Levofloxacin
    ("Levofloxacin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 250-750mg trong 100-250mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Levofloxacin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Levofloxacin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Levofloxacin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Azithromycin
    ("Azithromycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 500mg trong 250-500mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Linezolid
    ("Linezolid", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 600mg trong 100-300mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Linezolid", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Linezolid: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Linezolid: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Daptomycin
    ("Daptomycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 4-6mg/kg trong 50-100mL NS.",
        "stability": "Ổn định 12h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Fluconazole
    ("Fluconazole", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 200-400mg trong 100-200mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Fluconazole", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Fluconazole: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Fluconazole: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Piperacillin-Tazobactam - More entries
    ("Piperacillin-Tazobactam", "Ceftriaxone"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Piperacillin-Tazobactam: Pha trong NS. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Piperacillin-Tazobactam: Ổn định 24h. Ceftriaxone: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Piperacillin-Tazobactam", "Meropenem"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Piperacillin-Tazobactam: Pha trong NS. Meropenem: Pha trong NS hoặc D5W.",
        "stability": "Piperacillin-Tazobactam: Ổn định 24h. Meropenem: Ổn định 4h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Piperacillin-Tazobactam", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "dilution": "Pha trong D5W: 3.375g trong 50-100mL D5W.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Cefepime
    ("Cefepime", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 1-2g trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Cefepime", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Cefepime: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Cefepime: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Cefepime", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Cefepime: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Cefepime: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Ceftazidime
    ("Ceftazidime", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 1-2g trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ceftazidime", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ceftazidime: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Ceftazidime: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Cefotaxime
    ("Cefotaxime", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 1-2g trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Cefotaxime", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Cefotaxime: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Cefotaxime: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Imipenem-Cilastatin
    ("Imipenem-Cilastatin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 500mg-1g trong 100mL NS.",
        "stability": "Ổn định 4h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Imipenem-Cilastatin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Imipenem-Cilastatin: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Imipenem-Cilastatin: Ổn định 4h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Ertapenem
    ("Ertapenem", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 1g trong 50mL NS.",
        "stability": "Ổn định 6h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ertapenem", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "dilution": "Pha trong D5W: 1g trong 50mL D5W.",
        "stability": "Ổn định 6h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Gentamicin (specific)
    ("Gentamicin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 80-160mg trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Gentamicin", "Vancomycin"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "dilution": "Gentamicin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Gentamicin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    ("Gentamicin", "Piperacillin-Tazobactam"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng.",
        "dilution": "Gentamicin: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Gentamicin: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Tobramycin (specific)
    ("Tobramycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 80-160mg trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Tobramycin", "Vancomycin"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "dilution": "Tobramycin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Tobramycin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    
    # Amikacin (specific)
    ("Amikacin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 500mg-1g trong 100-200mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Amikacin", "Vancomycin"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích - Tạo kết tủa. Pha riêng, truyền riêng. Ngoài ra, tăng nguy cơ độc thận khi phối hợp.",
        "dilution": "Amikacin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Amikacin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "major",
        "sources": ["Trissel's IV Compatibility", "ASHP Handbook"]
    },
    
    # Clarithromycin
    ("Clarithromycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 500mg trong 250mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Colistin
    ("Colistin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 2.5-5mg/kg trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Colistin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Colistin: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Colistin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Voriconazole
    ("Voriconazole", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 200mg trong 100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Voriconazole", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Voriconazole: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Voriconazole: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Caspofungin
    ("Caspofungin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 50-70mg trong 250mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Caspofungin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Caspofungin: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Caspofungin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Metronidazole
    ("Metronidazole", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 500mg trong 100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Metronidazole", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích - Có thể pha chung hoặc truyền qua Y-site.",
        "dilution": "Metronidazole: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Metronidazole: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Metronidazole", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích - Có thể pha chung hoặc truyền qua Y-site.",
        "dilution": "Metronidazole: Pha trong NS. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Metronidazole: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Clindamycin
    ("Clindamycin", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 300-900mg trong 50-100mL NS.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Clindamycin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Clindamycin: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Clindamycin: Ổn định 24h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Tigecycline
    ("Tigecycline", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 50-100mg trong 100mL NS.",
        "stability": "Ổn định 6h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Tigecycline", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Tigecycline: Pha trong NS hoặc D5W. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Tigecycline: Ổn định 6h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Electrolytes and common IV solutions
    ("Potassium", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Standard"]
    },
    ("Magnesium", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Standard"]
    },
    ("Calcium", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "severity": "info",
        "sources": ["Standard"]
    },
    ("Calcium", "Ceftriaxone"): {
        "y_site": "incompatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Không tương thích với calcium - Tạo kết tủa. Tránh pha chung hoặc truyền cùng lúc.",
        "severity": "major",
        "sources": ["FDA Warning", "Trissel's IV Compatibility"]
    },
    
    # LR (Lactated Ringer's)
    ("LR", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích.",
        "severity": "info",
        "sources": ["Standard"]
    },
    ("Vancomycin", "LR"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Lactated Ringer's.",
        "dilution": "Pha trong LR: 250-500mg trong 100-250mL LR.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More common combinations
    ("Ceftriaxone", "Metronidazole"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích - Có thể pha chung hoặc truyền qua Y-site.",
        "dilution": "Ceftriaxone: Pha trong NS hoặc D5W. Metronidazole: Pha trong NS.",
        "stability": "Ceftriaxone: Ổn định 24h. Metronidazole: Ổn định 24h.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Meropenem", "Metronidazole"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích - Có thể pha chung hoặc truyền qua Y-site.",
        "dilution": "Meropenem: Pha trong NS hoặc D5W. Metronidazole: Pha trong NS.",
        "stability": "Meropenem: Ổn định 4h. Metronidazole: Ổn định 24h.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Piperacillin-Tazobactam", "Metronidazole"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích - Có thể pha chung hoặc truyền qua Y-site.",
        "dilution": "Piperacillin-Tazobactam: Pha trong NS. Metronidazole: Pha trong NS.",
        "stability": "Piperacillin-Tazobactam: Ổn định 24h. Metronidazole: Ổn định 24h.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # Amphotericin B (more entries)
    ("Amphotericin B", "NS"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Normal Saline.",
        "dilution": "Pha trong NS: 0.1-0.5mg/mL trong D5W (không pha trong NS cho lipid formulation).",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Amphotericin B", "D5W"): {
        "y_site": "compatible",
        "same_line": "compatible",
        "compatible": True,
        "notes": "Tương thích với Dextrose 5%.",
        "dilution": "Pha trong D5W: 0.1-0.5mg/mL trong D5W.",
        "stability": "Ổn định 24h ở nhiệt độ phòng.",
        "severity": "info",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More Levofloxacin combinations
    ("Levofloxacin", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Levofloxacin: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Levofloxacin: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Levofloxacin", "Ceftriaxone"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Levofloxacin: Pha trong NS hoặc D5W. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Levofloxacin: Ổn định 24h. Ceftriaxone: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More Ciprofloxacin combinations
    ("Ciprofloxacin", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ciprofloxacin: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Ciprofloxacin: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Ciprofloxacin", "Ceftriaxone"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Ciprofloxacin: Pha trong NS hoặc D5W. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Ciprofloxacin: Ổn định 24h. Ceftriaxone: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More Linezolid combinations
    ("Linezolid", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Linezolid: Pha trong NS hoặc D5W. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Linezolid: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Linezolid", "Ceftriaxone"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Linezolid: Pha trong NS hoặc D5W. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Linezolid: Ổn định 24h. Ceftriaxone: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More Daptomycin combinations
    ("Daptomycin", "Vancomycin"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Daptomycin: Pha trong NS. Vancomycin: Pha trong NS hoặc D5W.",
        "stability": "Daptomycin: Ổn định 12h. Vancomycin: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    
    # More Fluconazole combinations
    ("Fluconazole", "Piperacillin-Tazobactam"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Fluconazole: Pha trong NS. Piperacillin-Tazobactam: Pha trong NS.",
        "stability": "Fluconazole: Ổn định 24h. Piperacillin-Tazobactam: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    },
    ("Fluconazole", "Ceftriaxone"): {
        "y_site": "compatible",
        "same_line": "incompatible",
        "compatible": False,
        "notes": "Y-site: Tương thích (có thể rửa line). Same line: Không tương thích - Pha riêng.",
        "dilution": "Fluconazole: Pha trong NS. Ceftriaxone: Pha trong NS hoặc D5W.",
        "stability": "Fluconazole: Ổn định 24h. Ceftriaxone: Ổn định 24h.",
        "severity": "minor",
        "sources": ["Trissel's IV Compatibility"]
    }
}


def normalize_drug_name(drug_name: str) -> str:
    """
    Normalize drug name for matching
    """
    # Remove common variations
    normalized = drug_name.strip()
    
    # Handle common aliases
    aliases = {
        "gentamicin": "Gentamicin",
        "tobramycin": "Tobramycin",
        "amikacin": "Amikacin",
        "piperacillin/tazobactam": "Piperacillin-Tazobactam",
        "pip/taz": "Piperacillin-Tazobactam",
        "zosyn": "Piperacillin-Tazobactam",
        "tazocin": "Piperacillin-Tazobactam",
        "primaxin": "Imipenem-Cilastatin",
        "invanz": "Ertapenem",
        "zithromax": "Azithromycin",
        "zyvox": "Linezolid",
        "cubicin": "Daptomycin",
        "diflucan": "Fluconazole",
        "vfen": "Voriconazole",
        "cancidas": "Caspofungin",
        "flagyl": "Metronidazole",
        "cleocin": "Clindamycin",
        "tygacil": "Tigecycline",
        "colistimethate": "Colistin",
        "polymyxin": "Colistin",
        "rocephin": "Ceftriaxone",
        "maxipime": "Cefepime",
        "fortaz": "Ceftazidime",
        "claforan": "Cefotaxime",
        "merrem": "Meropenem",
        "cipro": "Ciprofloxacin",
        "levaquin": "Levofloxacin",
        "bactrim": "Trimethoprim-Sulfamethoxazole",
        "co-trimoxazole": "Trimethoprim-Sulfamethoxazole"
    }
    
    normalized_lower = normalized.lower()
    for alias, standard in aliases.items():
        if alias in normalized_lower:
            return standard
    
    return normalized


def check_iv_compatibility(drug1: str, drug2: str) -> Optional[Dict]:
    """
    Check IV compatibility between two drugs
    
    Args:
        drug1: Tên thuốc 1
        drug2: Tên thuốc 2
    
    Returns:
        Dict với compatibility info hoặc None nếu không tìm thấy
        Includes: y_site, same_line, notes, dilution, stability, severity, sources
    """
    drug1_norm = normalize_drug_name(drug1)
    drug2_norm = normalize_drug_name(drug2)
    
    # Check both orders
    key1 = (drug1_norm, drug2_norm)
    key2 = (drug2_norm, drug1_norm)
    
    result = None
    if key1 in IV_COMPATIBILITY_DB:
        result = IV_COMPATIBILITY_DB[key1].copy()
    elif key2 in IV_COMPATIBILITY_DB:
        result = IV_COMPATIBILITY_DB[key2].copy()
    
    if result:
        # Backward compatibility: if y_site/same_line not specified, use "compatible" field
        if "y_site" not in result and "same_line" not in result:
            if "compatible" in result:
                compat_status = "compatible" if result["compatible"] else "incompatible"
                result["y_site"] = compat_status
                result["same_line"] = compat_status
        
        # Ensure both fields exist
        if "y_site" not in result:
            result["y_site"] = "unknown"
        if "same_line" not in result:
            result["same_line"] = "unknown"
    
    return result


def check_multiple_drugs(drugs: List[str]) -> List[Dict]:
    """
    Check compatibility for multiple drugs
    
    Args:
        drugs: List tên thuốc
    
    Returns:
        List of compatibility results
    """
    results = []
    
    # Check all pairs
    for i in range(len(drugs)):
        for j in range(i + 1, len(drugs)):
            compat = check_iv_compatibility(drugs[i], drugs[j])
            if compat:
                results.append({
                    "drug1": drugs[i],
                    "drug2": drugs[j],
                    **compat
                })
            else:
                # Unknown compatibility - warn
                results.append({
                    "drug1": drugs[i],
                    "drug2": drugs[j],
                    "compatible": None,
                    "notes": "Không có dữ liệu tương thích. Khuyến cáo pha riêng và truyền riêng để an toàn.",
                    "severity": "warning",
                    "sources": []
                })
    
    return results


def render_iv_compatibility_checker(antibiotic_name: str):
    """
    Render IV compatibility checker UI
    
    Args:
        antibiotic_name: Tên kháng sinh chính
    """
    st.markdown("---")
    st.markdown("### 💉 Kiểm tra tương thích IV")
    
    st.info("""
    **Kiểm tra tính tương thích khi pha chế IV:**
    - **Y-site:** Truyền qua Y-connector (có thể rửa line giữa các liều)
    - **Same line:** Pha chung trong cùng một bag/syringe
    - Tránh tạo kết tủa hoặc mất tác dụng
    - Đảm bảo an toàn khi truyền cùng lúc
    - Dựa trên Trissel's IV Compatibility và ASHP Handbook
    """)
    
    # Input: Other drugs
    st.markdown("#### 📋 Thuốc khác đang truyền")
    
    # Sanitize antibiotic name for keys
    from .database_display import _make_safe_session_key
    safe_ab_name = _make_safe_session_key("iv_compat", antibiotic_name)
    
    other_drugs_text = st.text_input(
        "Nhập tên thuốc (phân cách bằng dấu phẩy):",
        placeholder="Ví dụ: Piperacillin-Tazobactam, Ceftriaxone, NS",
        key=_make_safe_session_key(safe_ab_name, "drugs"),
        help="Nhập các thuốc hoặc dịch truyền khác đang dùng cùng lúc"
    )
    
    # Common IV fluids
    st.markdown("#### 💧 Dịch truyền")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        use_ns = st.checkbox("Normal Saline (NS)", key=_make_safe_session_key(safe_ab_name, "ns"))
    with col2:
        use_d5w = st.checkbox("D5W", key=_make_safe_session_key(safe_ab_name, "d5w"))
    with col3:
        use_calcium = st.checkbox("Calcium", key=_make_safe_session_key(safe_ab_name, "calcium"))
    
    # Build drug list
    drugs_to_check = [antibiotic_name]
    
    if other_drugs_text:
        other_drugs = [d.strip() for d in other_drugs_text.split(",") if d.strip()]
        drugs_to_check.extend(other_drugs)
    
    if use_ns:
        drugs_to_check.append("NS")
    if use_d5w:
        drugs_to_check.append("D5W")
    if use_calcium:
        drugs_to_check.append("Calcium")
    
    if len(drugs_to_check) < 2:
        st.warning("⚠️ Vui lòng chọn ít nhất 1 thuốc/dịch truyền khác để kiểm tra")
        return
    
    # Check button
    if st.button("🔍 Kiểm tra tương thích", type="primary", key=_make_safe_session_key(safe_ab_name, "check")):
        results = check_multiple_drugs(drugs_to_check)
        
        if not results:
            st.info("✅ Không có thông tin tương thích trong database. Khuyến cáo pha riêng và truyền riêng.")
            return
        
        st.markdown("---")
        st.markdown("### 📊 Kết quả Kiểm tra")
        
        # Group by compatibility
        compatible = []
        incompatible = []
        unknown = []
        
        for result in results:
            if result['compatible'] is True:
                compatible.append(result)
            elif result['compatible'] is False:
                incompatible.append(result)
            else:
                unknown.append(result)
        
        # Show incompatible first (most important)
        if incompatible:
            st.error("### 🚨 Không Tương Thích")
            for result in incompatible:
                y_site = result.get('y_site', 'unknown')
                same_line = result.get('same_line', 'unknown')
                
                # Enhanced visual display with color-coded badges
                st.markdown(f"""
                <div style="background: #ffebee; border-left: 4px solid #f44336; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
                    <h4 style="color: #c62828; margin-top: 0;">⚠️ {result['drug1']} + {result['drug2']}</h4>
                """, unsafe_allow_html=True)
                
                # Y-site vs Same line comparison table
                compat_table = """
                <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
                    <thead>
                        <tr style="background: #f5f5f5;">
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Loại</th>
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Trạng thái</th>
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Mô tả</th>
                        </tr>
                    </thead>
                    <tbody>
                """
                
                if y_site != 'unknown':
                    y_site_color = "#f44336" if y_site == "incompatible" else "#ff9800" if y_site == "questionable" else "#4caf50"
                    y_site_icon = "❌" if y_site == "incompatible" else "⚠️" if y_site == "questionable" else "✅"
                    y_site_desc = "Không tương thích" if y_site == "incompatible" else "Cần thận trọng" if y_site == "questionable" else "Tương thích"
                    compat_table += f"""
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Y-site</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {y_site_color}; font-weight: bold;">{y_site_icon} {y_site.title()}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{y_site_desc} - Có thể rửa line giữa các liều</td>
                        </tr>
                    """
                
                if same_line != 'unknown':
                    same_line_color = "#f44336" if same_line == "incompatible" else "#ff9800" if same_line == "questionable" else "#4caf50"
                    same_line_icon = "❌" if same_line == "incompatible" else "⚠️" if same_line == "questionable" else "✅"
                    same_line_desc = "Không tương thích" if same_line == "incompatible" else "Cần thận trọng" if same_line == "questionable" else "Tương thích"
                    compat_table += f"""
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Same line</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {same_line_color}; font-weight: bold;">{same_line_icon} {same_line.title()}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{same_line_desc} - Pha chung trong cùng bag/syringe</td>
                        </tr>
                    """
                
                compat_table += """
                    </tbody>
                </table>
                """
                
                st.markdown(compat_table, unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 10px;'><strong>Ghi chú:</strong> {result['notes']}</p>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Show dilution and stability if available
                if result.get('dilution'):
                    with st.expander("💧 Hướng dẫn pha chế"):
                        st.info(result['dilution'])
                
                if result.get('stability'):
                    with st.expander("⏱️ Thông tin ổn định"):
                        st.info(result['stability'])
                
                st.error("**Khuyến cáo:** Pha riêng, truyền riêng hoặc rửa line giữa các liều.")
        
        # Show unknown
        if unknown:
            st.warning("### ⚠️ Chưa Có Dữ Liệu")
            for result in unknown:
                st.warning(f"""
                **{result['drug1']} + {result['drug2']}**
                
                {result['notes']}
                """)
        
        # Show compatible
        if compatible:
            st.success("### ✅ Tương Thích")
            for result in compatible:
                y_site = result.get('y_site', 'unknown')
                same_line = result.get('same_line', 'unknown')
                
                st.markdown(f"""
                <div style="background: #e8f5e9; border-left: 4px solid #4caf50; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
                    <h4 style="color: #2e7d32; margin-top: 0;">✅ {result['drug1']} + {result['drug2']}</h4>
                """, unsafe_allow_html=True)
                
                # Y-site vs Same line comparison table
                compat_table = """
                <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
                    <thead>
                        <tr style="background: #f5f5f5;">
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Loại</th>
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Trạng thái</th>
                            <th style="padding: 8px; border: 1px solid #ddd; text-align: left;">Mô tả</th>
                        </tr>
                    </thead>
                    <tbody>
                """
                
                if y_site != 'unknown':
                    y_site_color = "#f44336" if y_site == "incompatible" else "#ff9800" if y_site == "questionable" else "#4caf50"
                    y_site_icon = "❌" if y_site == "incompatible" else "⚠️" if y_site == "questionable" else "✅"
                    y_site_desc = "Không tương thích" if y_site == "incompatible" else "Cần thận trọng" if y_site == "questionable" else "Tương thích"
                    compat_table += f"""
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Y-site</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {y_site_color}; font-weight: bold;">{y_site_icon} {y_site.title()}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{y_site_desc} - Có thể rửa line giữa các liều</td>
                        </tr>
                    """
                
                if same_line != 'unknown':
                    same_line_color = "#f44336" if same_line == "incompatible" else "#ff9800" if same_line == "questionable" else "#4caf50"
                    same_line_icon = "❌" if same_line == "incompatible" else "⚠️" if same_line == "questionable" else "✅"
                    same_line_desc = "Không tương thích" if same_line == "incompatible" else "Cần thận trọng" if same_line == "questionable" else "Tương thích"
                    compat_table += f"""
                        <tr>
                            <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Same line</td>
                            <td style="padding: 8px; border: 1px solid #ddd; color: {same_line_color}; font-weight: bold;">{same_line_icon} {same_line.title()}</td>
                            <td style="padding: 8px; border: 1px solid #ddd;">{same_line_desc} - Pha chung trong cùng bag/syringe</td>
                        </tr>
                    """
                
                compat_table += """
                    </tbody>
                </table>
                """
                
                st.markdown(compat_table, unsafe_allow_html=True)
                st.markdown(f"<p style='margin-top: 10px;'><strong>Ghi chú:</strong> {result['notes']}</p>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Show dilution and stability if available
                if result.get('dilution'):
                    with st.expander("💧 Hướng dẫn pha chế"):
                        st.info(result['dilution'])
                
                if result.get('stability'):
                    with st.expander("⏱️ Thông tin ổn định"):
                        st.info(result['stability'])
        
        # Summary
        st.markdown("---")
        if incompatible:
            st.error(f"⚠️ **Cảnh báo:** Có {len(incompatible)} cặp thuốc không tương thích. Cần pha riêng và truyền riêng!")
        elif unknown:
            st.warning(f"ℹ️ **Lưu ý:** Có {len(unknown)} cặp thuốc chưa có dữ liệu. Khuyến cáo pha riêng để an toàn.")
        else:
            st.success(f"✅ **Tất cả {len(compatible)} cặp thuốc đều tương thích!**")


def get_compatibility_summary(drug1: str, drug2: str) -> str:
    """
    Get quick compatibility summary for display
    
    Returns:
        Short summary string
    """
    compat = check_iv_compatibility(drug1, drug2)
    
    if compat is None:
        return "❓ Chưa có dữ liệu"
    elif compat['compatible']:
        return "✅ Tương thích"
    else:
        return "❌ Không tương thích"

