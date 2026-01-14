"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Short-acting Beta-2 Agonist (SABA)s

SHORT_ACTING_BETA_2_AGONIST_SABA_DRUGS = {
    "Salbutamol": {'group': 'Respiratory - Short-acting Beta-2 Agonist (SABA)',vietnamese_name': 'Salbutamol, Ventolin', 'administration': [
        'Inhalation', 'IV', 'PO'],
        'indications': [
        'COPD (cắt cơn)', 'Co thắt phế quản cấp',
        'Dự phòng co thắt do vận động'],
        'contraindications': [
        'Nhịp tim nhanh nặng'],
        'dosage': {'adult_inhalation':
        '1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần', 'adult_nebulizer':
        '2.5-5mg mỗi 4-6 giờ', 'adult_iv':
        '0.5mg IV, sau đó 5-20mcg/phút truyền liên tục', 'notes':
        'Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên'},
        'side_effects': ['Tim đập nhanh', 'Run cơ', 'Đau đầu',
        'Hạ kali máu (liều cao)', 'Loạn nhịp tim (hiếm)'],
        'interactions': [
        'Beta-blocker: đối kháng tác dụng (tránh dùng)'],mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.'
        , 'monitoring': [
        'Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao)',
        'Kali máu nếu dùng liều cao hoặc kéo dài',
        'Đáp ứng phế quản (peak flow, FEV1)',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)'],precautions': [
        'Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên',
        'Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'],pharmacokinetics': {'half_life': '2-7 giờ (hít), 2-4 giờ (IV)',
        'onset': '5-15 phút (hít), 2-5 phút (IV)', 'duration': '4-6 giờ',
        'protein_binding': '10%', 'clearance':
        'Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.',
        'black_box_warnings':
        'Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.'
    },
    "Terbutaline":     {
        "group": "Respiratory - Short-acting Beta-2 Agonist (SABA)",
        "vietnamese_name": "Terbutaline, Bricanyl",
        "administration": [
            "Inhalation",
            "SC",
            "PO"
    ],
        "indications": [
            "Hen phế quản (cắt cơn)",
            "COPD (cắt cơn)",
            "Co thắt phế quản cấp",
            "Dự phòng co thắt do vận động"
    ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng"
    ],
        "dosage": {
            "adult_inhalation": "250-500mcg (1-2 puffs) mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "5mg mỗi 4-6 giờ",
            "adult_sc": "0.25-0.5mg SC (đợt cấp nặng, không có khí dung)",
            "adult_po": "2.5-5mg x 3 lần/ngày",
            "notes": "Dùng khi cần (PRN) cho cắt cơn. Dạng SC dùng trong cấp cứu khi không có khí dung.",
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Hạ kali máu (liều cao)",
            "Loạn nhịp tim (hiếm)"
    ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng (tránh dùng)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Tương tự salbutamol nhưng có thể dùng dạng SC trong cấp cứu. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.""",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng SC hoặc liều cao)",
            "Kali máu nếu dùng liều cao hoặc kéo dài",
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)"
    ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên",
            "Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dạng SC: dùng trong cấp cứu khi không có khí dung, theo dõi chặt chẽ nhịp tim",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (hít), 2-3 giờ (SC)",
            "onset": "5-15 phút (hít), 5-10 phút (SC)",
            "duration": "4-6 giờ",
            "protein_binding": "25%",
            "clearance": "Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ)",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.""",
        "black_box_warnings": """Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát.""",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "",
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": [],
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    }

__all__ = ['SHORT_ACTING_BETA_2_AGONIST_SABA_DRUGS']
