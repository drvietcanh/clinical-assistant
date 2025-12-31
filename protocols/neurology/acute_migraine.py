import streamlit as st

def render_acute_migraine():
    st.header("🧠 Cắt Cơn Đau Nửa Đầu (Acute Migraine)")
    st.caption("Dựa trên hướng dẫn AHS 2021 & IHS")

    st.subheader("1. Đánh giá nhanh (SNOOP4)")
    st.warning("Loại trừ đau đầu thứ phát nguy hiểm (Red Flags):")
    st.markdown("- **S**ystemic: Sốt, sụt cân, ung thư, HIV.")
    st.markdown("- **N**eurologic: Dấu thần kinh khu trú, lơ mơ.")
    st.markdown("- **O**nset: Khởi phát sét đánh (Thunderclap) -> Nghi xuất huyết dưới nhện.")
    st.markdown("- **O**lder: Khởi phát mới > 50 tuổi -> Nghi viêm động mạch thái dương.")
    st.markdown("- **P**attern: Thay đổi tính chất, đau tăng khi ho/gắng sức.")

    st.markdown("---")
    st.subheader("2. Điều trị Cắt cơn (Stratified Care)")
    
    severity = st.radio("Mức độ đau / Ảnh hưởng chức năng:", ["Nhẹ - Trung bình", "Trung bình - Nặng"])

    if severity == "Nhẹ - Trung bình":
        st.success("**Bước 1: NSAIDs / Non-opioid**")
        st.markdown("- **Ibuprofen:** 400-800 mg.")
        st.markdown("- **Naproxen sodium:** 500-825 mg.")
        st.markdown("- **Excedrin (Aspirin + Paracetamol + Caffeine):** Hiệu quả tốt.")
        st.info("Tránh dùng > 10 ngày/tháng để ngừa đau đầu do lạm dụng thuốc (MOH).")

    else:
        st.warning("**Bước 2: Triptans (Đặc hiệu)**")
        st.markdown("- **Sumatriptan:** 50-100 mg uống (hoặc 6mg dưới da nếu nôn).")
        st.markdown("- **Rizatriptan:** 10 mg (tan trong miệng).")
        st.markdown("- *Kết hợp:* Triptan + Naproxen (hiệu quả hơn đơn trị).")
        st.error("**Chống chỉ định Triptan:** Bệnh mạch vành, Đột quỵ, Tăng huyết áp không kiểm soát.")
        
        with st.expander("Nếu Triptan thất bại hoặc chống chỉ định?"):
            st.markdown("- **Gepants (Ubrogepant, Rimegepant):** Đối kháng CGRP đường uống. An toàn cho tim mạch.")
            st.markdown("- **Lasmiditan:** Agonist 5-HT1F. (Gây chóng mặt, không lái xe).")
            st.markdown("- **Dihydroergotamine (DHE):** IV/IM/Xịt mũi. (Chống nôn kỹ).")

    st.markdown("---")
    st.subheader("3. Điều trị tại Cấp cứu (Migraine Cocktail)")
    st.info("Cho bệnh nhân đau nặng, kéo dài (>72h - Status Migrainosus).")
    st.markdown("1.  **Dịch truyền:** NaCl 0.9% 500-1000ml.")
    st.markdown("2.  **Chống nôn (Dopamine antagonists):** Metoclopramide 10mg IV hoặc Prochlorperazine 10mg IV.")
    st.markdown("3.  **NSAID:** Ketorolac 15-30mg IV.")
    st.markdown("4.  **Corticosteroid:** Dexamethasone 4-10mg IV (ngừa tái phát).")
    st.markdown("5.  *Tránh Opioids (Morphine) vì kém hiệu quả và gây nghiện.*")
