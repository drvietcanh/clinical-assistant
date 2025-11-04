"""
eGFR Calculator - Helper Functions
Convert, interpret, recommend functions
"""

def convert_egfr_to_absolute_gfr(egfr_normalized, bsa_actual):
    """
    Convert eGFR normalized (mL/min/1.73m²) to absolute GFR (mL/min)
    
    GFR_absolute = eGFR_normalized × (BSA_actual / 1.73)
    """
    gfr_absolute = egfr_normalized * (bsa_actual / 1.73)
    return gfr_absolute



def interpret_egfr(egfr):
    """Interpret eGFR according to CKD stages"""
    
    if egfr >= 90:
        stage = "G1 - Bình thường hoặc cao"
        description = "Chức năng thận bình thường (nếu không có bằng chứng tổn thương thận khác)"
        color = "#28a745"
        icon = "✅"
        action = "Theo dõi thường quy nếu có yếu tố nguy cơ"
    elif egfr >= 60:
        stage = "G2 - Giảm nhẹ"
        description = "Giảm GFR nhẹ (có thể bình thường ở người cao tuổi)"
        color = "#28a745"
        icon = "✅"
        action = "Theo dõi, kiểm soát yếu tố nguy cơ"
    elif egfr >= 45:
        stage = "G3a - Giảm nhẹ-trung bình"
        description = "Suy thận mạn giai đoạn 3a"
        color = "#ffc107"
        icon = "⚠️"
        action = "Theo dõi 6-12 tháng, điều chỉnh liều thuốc"
    elif egfr >= 30:
        stage = "G3b - Giảm trung bình-nặng"
        description = "Suy thận mạn giai đoạn 3b"
        color = "#fd7e14"
        icon = "⚠️"
        action = "Theo dõi 3-6 tháng, hội chẩn chuyên khoa"
    elif egfr >= 15:
        stage = "G4 - Giảm nặng"
        description = "Suy thận mạn giai đoạn 4"
        color = "#dc3545"
        icon = "🚨"
        action = "Theo dõi 1-3 tháng, chuẩn bị lọc máu"
    else:
        stage = "G5 - Suy thận giai đoạn cuối"
        description = "Suy thận giai đoạn cuối (ESRD)"
        color = "#dc3545"
        icon = "🚨🚨"
        action = "Cần lọc máu hoặc ghép thận NGAY"
    
    return {
        "stage": stage,
        "description": description,
        "color": color,
        "icon": icon,
        "action": action
    }



def get_recommended_formula(bmi, age, nutrition_status):
    """
    Recommend best formula based on patient characteristics
    """
    if bmi >= 30:
        return "Cockcroft-Gault (với ABW)", "Bệnh nhân béo phì, nên dùng Cockcroft-Gault với cân nặng hiệu chỉnh (ABW)"
    elif bmi < 18.5:
        return "CKD-EPI Cystatin C", "Bệnh nhân gầy, nên dùng Cystatin C hoặc kết hợp Creatinin + Cystatin C"
    elif age >= 65:
        return "CKD-EPI 2021", "Người cao tuổi, CKD-EPI 2021 chính xác hơn"
    else:
        return "CKD-EPI 2009", "Bệnh nhân bình thường, CKD-EPI là khuyến cáo"



