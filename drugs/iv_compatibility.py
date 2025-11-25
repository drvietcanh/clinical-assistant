"""
IV Compatibility Checker
Check compatibility between multiple IV drugs in the same line
Visual compatibility matrix with color-coded warnings
"""

import streamlit as st
import pandas as pd
from components.iv_compatibility_matrix import (
    render_visual_compatibility_matrix,
    render_compatibility_summary,
    export_matrix_to_html
)


# IV Compatibility Database
IV_COMPATIBILITY_DB = {
    # ========== ANTIBIOTICS ==========
    "Vancomycin": {
        "compatible": ["Gentamicin", "Tobramycin", "Amikacin", "Furosemide"],
        "questionable": ["Piperacillin-Tazobactam", "Heparin", "Morphine"],
        "incompatible": ["Amphotericin B", "Acyclovir", "Phenytoin"],
        "notes": "Y-site: Tốt với aminoglycosides. Tránh pha chung với beta-lactams."
    },
    "Piperacillin-Tazobactam": {
        "compatible": ["Gentamicin", "Tobramycin", "Amikacin", "Metronidazole"],
        "questionable": ["Vancomycin", "Heparin", "Morphine"],
        "incompatible": ["Amphotericin B"],
        "notes": "Y-site: Tương thích với aminoglycosides. Thận trọng với vancomycin."
    },
    "Meropenem": {
        "compatible": ["Gentamicin", "Tobramycin", "Amikacin", "Vancomycin"],
        "questionable": ["Heparin"],
        "incompatible": ["Amphotericin B"],
        "notes": "Y-site: Tương thích tốt với nhiều thuốc."
    },
    "Ceftriaxone": {
        "compatible": ["Metronidazole", "Vancomycin"],
        "questionable": ["Piperacillin-Tazobactam", "Heparin"],
        "incompatible": ["Calcium", "Amphotericin B"],
        "notes": "⚠️ KHÔNG pha chung với calcium (nguy cơ kết tủa tử vong)."
    },
    "Gentamicin": {
        "compatible": ["Vancomycin", "Piperacillin-Tazobactam", "Meropenem", "Clindamycin"],
        "questionable": ["Heparin"],
        "incompatible": ["Amphotericin B", "Phenytoin"],
        "notes": "Y-site: Tương thích tốt với nhiều kháng sinh."
    },
    
    # ========== VASOPRESSORS ==========
    "Norepinephrine": {
        "compatible": ["Dopamine", "Dobutamine", "Epinephrine"],
        "questionable": ["Heparin", "Insulin"],
        "incompatible": ["Alkaline solutions", "Sodium bicarbonate"],
        "notes": "Không pha chung với alkaline. Dùng line riêng nếu có thể."
    },
    "Dopamine": {
        "compatible": ["Norepinephrine", "Dobutamine", "Epinephrine"],
        "questionable": ["Heparin"],
        "incompatible": ["Alkaline solutions", "Sodium bicarbonate"],
        "notes": "Tương thích với vasopressors khác."
    },
    "Epinephrine": {
        "compatible": ["Norepinephrine", "Dopamine"],
        "questionable": ["Heparin"],
        "incompatible": ["Alkaline solutions", "Sodium bicarbonate"],
        "notes": "Dùng line riêng cho vasopressors nếu có thể."
    },
    
    # ========== ANALGESICS/SEDATIVES ==========
    "Morphine": {
        "compatible": ["Fentanyl", "Midazolam", "Propofol"],
        "questionable": ["Vancomycin", "Heparin"],
        "incompatible": [],
        "notes": "Y-site: Tương thích với nhiều thuốc an thần."
    },
    "Fentanyl": {
        "compatible": ["Morphine", "Midazolam", "Propofol"],
        "questionable": ["Heparin"],
        "incompatible": [],
        "notes": "Y-site tương thích."
    },
    
    # ========== ANTICOAGULANTS ==========
    "Heparin": {
        "compatible": ["Most antibiotics"],
        "questionable": ["Vancomycin", "Vasopressors", "Insulin"],
        "incompatible": ["Alteplase", "Warfarin IV"],
        "notes": "Thận trọng với nhiều thuốc. Dùng line riêng nếu có thể."
    },
    
    # ========== ELECTROLYTES ==========
    "Potassium": {
        "compatible": ["Most solutions"],
        "questionable": ["Calcium", "Magnesium"],
        "incompatible": [],
        "notes": "Không vượt quá 40 mEq/L, pha trong NS hoặc D5W."
    },
    "Calcium": {
        "compatible": ["Most solutions"],
        "questionable": ["Ceftriaxone", "Phosphate", "Magnesium"],
        "incompatible": ["Ceftriaxone (nếu pha chung)"],
        "notes": "⚠️ KHÔNG pha chung với ceftriaxone (kết tủa tử vong)."
    },
    "Magnesium": {
        "compatible": ["Most solutions"],
        "questionable": ["Calcium", "Potassium"],
        "incompatible": [],
        "notes": "Tương thích tốt."
    },
    
    # ========== OTHER COMMON DRUGS ==========
    "Insulin": {
        "compatible": ["Most solutions"],
        "questionable": ["Vasopressors", "Heparin"],
        "incompatible": [],
        "notes": "Dùng line riêng nếu có thể để tránh nguy cơ hạ đường huyết."
    },
    "Furosemide": {
        "compatible": ["Vancomycin", "Most antibiotics"],
        "questionable": ["Heparin"],
        "incompatible": [],
        "notes": "Y-site tương thích với nhiều thuốc."
    },
    "Metoclopramide": {
        "compatible": ["Most solutions"],
        "questionable": [],
        "incompatible": [],
        "notes": "Tương thích tốt."
    },
}


def get_compatibility(drug1, drug2):
    """
    Get compatibility status between two drugs
    
    Returns:
        tuple: (status, notes)
        status: "compatible", "questionable", "incompatible", or "unknown"
    """
    if drug1 not in IV_COMPATIBILITY_DB or drug2 not in IV_COMPATIBILITY_DB:
        return "unknown", "Không có dữ liệu về tương thích giữa hai thuốc này."
    
    db1 = IV_COMPATIBILITY_DB[drug1]
    db2 = IV_COMPATIBILITY_DB[drug2]
    
    # Check if drug2 is in drug1's compatible list
    if drug2 in db1.get("compatible", []):
        return "compatible", db1.get("notes", "")
    
    # Check if drug2 is in drug1's incompatible list
    if drug2 in db1.get("incompatible", []):
        return "incompatible", db1.get("notes", "")
    
    # Check if drug2 is in drug1's questionable list
    if drug2 in db1.get("questionable", []):
        return "questionable", db1.get("notes", "")
    
    # Check reverse (drug1 in drug2's lists)
    if drug1 in db2.get("compatible", []):
        return "compatible", db2.get("notes", "")
    
    if drug1 in db2.get("incompatible", []):
        return "incompatible", db2.get("notes", "")
    
    if drug1 in db2.get("questionable", []):
        return "questionable", db2.get("notes", "")
    
    # If not in any list, assume compatible but with caution
    return "unknown", "Không có dữ liệu cụ thể. Thận trọng khi dùng chung, nên dùng line riêng hoặc flush giữa các thuốc."


def check_multiple_compatibility(drug_list):
    """
    Check compatibility between all pairs in a drug list
    
    Returns:
        list of dicts with compatibility info
    """
    results = []
    checked_pairs = set()
    
    for i, drug1 in enumerate(drug_list):
        for j, drug2 in enumerate(drug_list[i+1:], start=i+1):
            # Skip same drug
            if drug1 == drug2:
                continue
            
            # Avoid duplicate checks
            pair = tuple(sorted([drug1, drug2]))
            if pair in checked_pairs:
                continue
            
            checked_pairs.add(pair)
            
            status, notes = get_compatibility(drug1, drug2)
            results.append({
                "drug1": drug1,
                "drug2": drug2,
                "status": status,
                "notes": notes
            })
    
    # Sort by severity (incompatible > questionable > compatible > unknown)
    severity_order = {"incompatible": 0, "questionable": 1, "compatible": 2, "unknown": 3}
    results.sort(key=lambda x: severity_order.get(x["status"], 4))
    
    return results


def render_iv_compatibility_checker():
    """Render IV Compatibility Checker UI"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #FF6B6B 0%, #EE5A6F 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>💉 Kiểm Tra Tương Thích IV</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Kiểm tra tương thích giữa nhiều thuốc trong cùng một line IV • An toàn cho bệnh nhân
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Info
    with st.expander("ℹ️ Thông tin về IV Compatibility", expanded=False):
        st.info("""
        **Các mức độ tương thích:**
        - ✅ **Compatible**: Có thể dùng chung an toàn (Y-site hoặc cùng line)
        - ⚠️ **Questionable**: Thận trọng, nên dùng line riêng hoặc flush giữa các thuốc
        - ❌ **Incompatible**: KHÔNG được dùng chung, có thể kết tủa hoặc tương tác nguy hiểm
        - ❓ **Unknown**: Không có dữ liệu, nên thận trọng
        
        **Lưu ý:**
        - Dữ liệu dựa trên Y-site compatibility
        - Một số thuốc cần line riêng (vasopressors, insulin)
        - Luôn flush line giữa các thuốc khác nhau
        - Kiểm tra với dược sĩ trước khi pha chung
        """)
    
    st.markdown("---")
    
    # Drug input section
    st.markdown("### 📋 Chọn thuốc cần kiểm tra")
    
    available_drugs = sorted(IV_COMPATIBILITY_DB.keys())
    
    col1, col2 = st.columns(2)
    
    selected_drugs = []
    
    with col1:
        st.markdown("**Thuốc trong line IV:**")
        num_drugs = st.number_input(
            "Số lượng thuốc cần kiểm tra:",
            min_value=2,
            max_value=10,
            value=2,
            step=1,
            key="iv_num_drugs"
        )
        
        for i in range(num_drugs):
            drug = st.selectbox(
                f"Thuốc {i+1}:",
                ["-- Chọn thuốc --"] + available_drugs,
                key=f"iv_drug_{i}"
            )
            if drug != "-- Chọn thuốc --":
                selected_drugs.append(drug)
    
    with col2:
        st.markdown("**Danh sách thuốc có sẵn:**")
        st.caption(f"{len(available_drugs)} thuốc trong database")
        st.write(", ".join(available_drugs[:20]))
        if len(available_drugs) > 20:
            st.caption(f"... và {len(available_drugs) - 20} thuốc khác")
    
    st.markdown("---")
    
    # Check compatibility
    if len(selected_drugs) >= 2:
        if st.button("🔍 Kiểm Tra Tương Thích", use_container_width=True, type="primary"):
            results = check_multiple_compatibility(selected_drugs)
            
            if results:
                st.markdown("### 📊 Kết Quả Kiểm Tra")
                
                # Summary
                incompatible_count = sum(1 for r in results if r["status"] == "incompatible")
                questionable_count = sum(1 for r in results if r["status"] == "questionable")
                compatible_count = sum(1 for r in results if r["status"] == "compatible")
                
                # Render compatibility summary with visual metrics
                render_compatibility_summary(results)
                
                st.markdown("---")
                
                # Detailed results
                for result in results:
                    status = result["status"]
                    drug1 = result["drug1"]
                    drug2 = result["drug2"]
                    notes = result["notes"]
                    
                    if status == "incompatible":
                        st.error(f"""
                        ❌ **{drug1} + {drug2} - KHÔNG TƯƯNG THÍCH**
                        
                        {notes}
                        
                        **⚠️ HÀNH ĐỘNG:** KHÔNG được dùng chung. Dùng line riêng hoặc flush kỹ giữa các thuốc.
                        """)
                    
                    elif status == "questionable":
                        st.warning(f"""
                        ⚠️ **{drug1} + {drug2} - THẬN TRỌNG**
                        
                        {notes}
                        
                        **💡 KHUYẾN NGHỊ:** Nên dùng line riêng hoặc flush kỹ giữa các thuốc.
                        """)
                    
                    elif status == "compatible":
                        st.success(f"""
                        ✅ **{drug1} + {drug2} - TƯƠNG THÍCH**
                        
                        {notes}
                        
                        **💡 LƯU Ý:** Vẫn nên flush giữa các thuốc để đảm bảo an toàn.
                        """)
                    
                    else:  # unknown
                        st.info(f"""
                        ❓ **{drug1} + {drug2} - CHƯA RÕ**
                        
                        {notes}
                        """)
                    
                    st.markdown("---")
                
                # Visual Compatibility Matrix
                st.markdown("### 📊 Ma Trận Tương Thích Trực Quan")
                
                # Render visual matrix
                render_visual_compatibility_matrix(
                    drugs=selected_drugs,
                    compatibility_data=results,
                    show_tooltips=True,
                    compact=False
                )
                
                # Export options
                st.markdown("---")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    # Export HTML
                    html_content = export_matrix_to_html(
                        drugs=selected_drugs,
                        compatibility_data=results,
                        title="IV Compatibility Matrix"
                    )
                    st.download_button(
                        label="📄 Tải HTML",
                        data=html_content,
                        file_name="iv_compatibility_matrix.html",
                        mime="text/html",
                        use_container_width=True
                    )
                
                with col2:
                    # Copy to clipboard (as text summary)
                    summary_text = f"IV Compatibility Matrix\n"
                    summary_text += f"Drugs: {', '.join(selected_drugs)}\n\n"
                    for result in results:
                        summary_text += f"{result['drug1']} + {result['drug2']}: {result['status']}\n"
                        summary_text += f"  {result['notes']}\n\n"
                    
                    st.download_button(
                        label="📋 Tải TXT",
                        data=summary_text,
                        file_name="iv_compatibility_summary.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col3:
                    # Print view
                    if st.button("🖨️ Xem In", use_container_width=True):
                        st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang này")
            
            else:
                st.warning("Không có kết quả kiểm tra.")
    
    else:
        st.info("Vui lòng chọn ít nhất 2 thuốc để kiểm tra tương thích.")

