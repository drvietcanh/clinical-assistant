"""
Phase 1 Calculator Metadata System
Adds educational content, evidence citations, and visual aids to calculators
"""

from typing import Optional, Dict, List, Any
from dataclasses import dataclass
from components.calculator_enhancements import (
    render_calculator_explanation,
    render_evidence_citation,
    render_result_interpretation,
    render_visual_aid_chart,
    render_comparison_tool
)


@dataclass
class CalculatorMetadata:
    """Metadata for calculator educational content"""
    calculator_id: str
    title: str
    explanation: str
    when_to_use: Optional[str] = None
    limitations: Optional[str] = None
    clinical_context: Optional[str] = None
    evidence_citation: Optional[str] = None
    evidence_doi: Optional[str] = None
    evidence_url: Optional[str] = None
    interpretation_guide: Optional[Dict[str, str]] = None
    recommendations: Optional[Dict[str, List[str]]] = None
    visual_aid_type: Optional[str] = None
    visual_aid_data: Optional[Dict] = None


# Calculator metadata database
CALCULATOR_METADATA: Dict[str, CalculatorMetadata] = {
    "qsofa": CalculatorMetadata(
        calculator_id="qsofa",
        title="qSOFA Score",
        explanation="""
        **qSOFA (Quick Sequential Organ Failure Assessment)** là công cụ đánh giá nhanh để xác định bệnh nhân có nguy cơ tử vong cao do nhiễm trùng.
        
        **Công thức:**
        - qSOFA = Số điểm từ 3 tiêu chí (mỗi tiêu chí = 1 điểm)
        - qSOFA ≥ 2: Nguy cơ tử vong cao
        
        **3 Tiêu chí:**
        1. **Huyết áp tâm thu ≤ 100 mmHg**
        2. **Nhịp thở ≥ 22 lần/phút**
        3. **Glasgow Coma Scale < 15**
        """,
        when_to_use="""
        - Sử dụng tại phòng cấp cứu để sàng lọc nhanh bệnh nhân nghi ngờ nhiễm trùng
        - Không cần xét nghiệm, chỉ cần đánh giá lâm sàng
        - Có thể dùng để quyết định có cần đo lactate hay không
        """,
        limitations="""
        - Không thay thế cho SOFA score trong ICU
        - Độ nhạy thấp (có thể bỏ sót một số trường hợp)
        - Không dùng để theo dõi diễn tiến bệnh
        - Không áp dụng cho trẻ em
        """,
        clinical_context="""
        qSOFA được phát triển từ Sepsis-3 definition (2016) để giúp nhận diện nhanh bệnh nhân nhiễm trùng có nguy cơ tử vong cao.
        Điểm ≥ 2 gợi ý cần đánh giá thêm bằng SOFA score và đo lactate.
        """,
        evidence_citation="Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810.",
        evidence_doi="10.1001/jama.2016.0287",
        evidence_url="https://pubmed.ncbi.nlm.nih.gov/26903338/",
        interpretation_guide={
            "0": "Nguy cơ thấp - Tỷ lệ tử vong trong bệnh viện ~3%",
            "1": "Nguy cơ trung bình - Tỷ lệ tử vong trong bệnh viện ~9%",
            "2-3": "Nguy cơ cao - Tỷ lệ tử vong trong bệnh viện ~24-40%"
        },
        recommendations={
            "0-1": [
                "Tiếp tục đánh giá lâm sàng",
                "Xem xét đo lactate nếu có dấu hiệu nhiễm trùng",
                "Theo dõi diễn tiến"
            ],
            "2-3": [
                "Đo lactate ngay lập tức",
                "Tính SOFA score đầy đủ",
                "Xem xét điều trị kháng sinh sớm",
                "Theo dõi sát trong ICU nếu cần"
            ]
        }
    ),
    
    "sofa": CalculatorMetadata(
        calculator_id="sofa",
        title="SOFA Score",
        explanation="""
        **SOFA (Sequential Organ Failure Assessment)** là công cụ đánh giá mức độ suy đa tạng và tiên lượng tử vong trong ICU.
        
        **6 Hệ thống cơ quan được đánh giá:**
        1. Hô hấp (PaO2/FiO2)
        2. Đông máu (Tiểu cầu)
        3. Gan (Bilirubin)
        4. Tim mạch (MAP, vasopressors)
        5. Thần kinh (GCS)
        6. Thận (Creatinine, lượng nước tiểu)
        
        **Điểm số:** 0-4 cho mỗi hệ thống, tổng 0-24 điểm
        """,
        when_to_use="""
        - Đánh giá mức độ suy đa tạng trong ICU
        - Theo dõi diễn tiến bệnh (tính hàng ngày)
        - Tiên lượng tử vong
        - Nghiên cứu và báo cáo
        """,
        limitations="""
        - Cần xét nghiệm và monitoring liên tục
        - Không áp dụng cho trẻ em (dùng PELOD-2)
        - Một số thông số có thể không có sẵn
        - Không phản ánh nguyên nhân suy đa tạng
        """,
        clinical_context="""
        SOFA score được phát triển từ 1996 và được cập nhật trong Sepsis-3 (2016).
        Điểm SOFA tăng ≥ 2 điểm từ baseline gợi ý sepsis.
        Điểm cao hơn tương quan với tỷ lệ tử vong cao hơn.
        """,
        evidence_citation="Vincent JL, Moreno R, Takala J, et al. The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure. Intensive Care Med. 1996;22(7):707-710.",
        evidence_doi="10.1007/BF01709751",
        interpretation_guide={
            "0-6": "Suy đa tạng nhẹ - Tỷ lệ tử vong ~10-20%",
            "7-12": "Suy đa tạng trung bình - Tỷ lệ tử vong ~30-50%",
            "13-24": "Suy đa tạng nặng - Tỷ lệ tử vong ~50-95%"
        }
    ),
    
    "cha2ds2vasc": CalculatorMetadata(
        calculator_id="cha2ds2vasc",
        title="CHA₂DS₂-VASc Score",
        explanation="""
        **CHA₂DS₂-VASc** là công cụ đánh giá nguy cơ đột quỵ ở bệnh nhân rung nhĩ không do bệnh van tim.
        
        **Các yếu tố nguy cơ:**
        - **C**ongestive heart failure (1 điểm)
        - **H**ypertension (1 điểm)
        - **A**ge ≥75 (2 điểm) hoặc 65-74 (1 điểm)
        - **D**iabetes (1 điểm)
        - **S**troke/TIA/thromboembolism (2 điểm)
        - **V**ascular disease (1 điểm)
        - **S**ex (Female) (1 điểm)
        
        **Tổng điểm:** 0-9 điểm
        """,
        when_to_use="""
        - Bệnh nhân rung nhĩ không do bệnh van tim
        - Quyết định có cần chống đông hay không
        - Theo dõi nguy cơ đột quỵ theo thời gian
        """,
        limitations="""
        - Chỉ áp dụng cho rung nhĩ không do bệnh van tim
        - Không tính đến nguy cơ chảy máu (dùng HAS-BLED)
        - Một số yếu tố có thể thay đổi theo thời gian
        """,
        clinical_context="""
        CHA₂DS₂-VASc được phát triển từ CHADS₂ để cải thiện độ nhạy trong nhận diện bệnh nhân nguy cơ thấp.
        Điểm ≥ 2 ở nam và ≥ 3 ở nữ: Khuyến nghị chống đông (AHA/ACC 2019).
        """,
        evidence_citation="Lip GY, Nieuwlaat R, Pisters R, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation. Chest. 2010;137(2):263-272.",
        evidence_doi="10.1378/chest.09-1584",
        interpretation_guide={
            "0 (Nam)": "Nguy cơ rất thấp - Không cần chống đông",
            "1 (Nam)": "Nguy cơ thấp - Có thể không cần chống đông",
            "≥2 (Nam)": "Nguy cơ cao - Khuyến nghị chống đông",
            "0-1 (Nữ)": "Nguy cơ thấp - Có thể không cần chống đông",
            "≥2 (Nữ)": "Nguy cơ cao - Khuyến nghị chống đông"
        },
        recommendations={
            "0-1": [
                "Không cần chống đông (trừ khi có chỉ định khác)",
                "Theo dõi định kỳ"
            ],
            "≥2": [
                "Khuyến nghị chống đông (DOAC hoặc warfarin)",
                "Đánh giá nguy cơ chảy máu bằng HAS-BLED",
                "Theo dõi định kỳ và điều chỉnh liều"
            ]
        }
    ),
    
    "curb65": CalculatorMetadata(
        calculator_id="curb65",
        title="CURB-65 Score",
        explanation="""
        **CURB-65** là công cụ đánh giá mức độ nặng của viêm phổi cộng đồng (CAP).
        
        **5 Tiêu chí (mỗi tiêu chí = 1 điểm):**
        1. **C**onfusion (Lú lẫn)
        2. **U**rea >7 mmol/L
        3. **R**espiratory rate ≥30 lần/phút
        4. **B**lood pressure <90/60 mmHg
        5. **Age** ≥65 tuổi
        
        **Tổng điểm:** 0-5 điểm
        """,
        when_to_use="""
        - Đánh giá mức độ nặng viêm phổi cộng đồng
        - Quyết định nhập viện hay điều trị ngoại trú
        - Tiên lượng tử vong
        """,
        limitations="""
        - Chỉ áp dụng cho viêm phổi cộng đồng
        - Không áp dụng cho viêm phổi bệnh viện
        - Một số thông số có thể không có sẵn ngay
        """,
        clinical_context="""
        CURB-65 được phát triển từ CURB score bằng cách thêm tuổi.
        Điểm cao hơn tương quan với tỷ lệ tử vong cao hơn và nhu cầu nhập viện.
        """,
        evidence_citation="Lim WS, van der Eerden MM, Laing R, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-382.",
        evidence_doi="10.1136/thorax.58.5.377",
        interpretation_guide={
            "0-1": "Nguy cơ thấp - Tỷ lệ tử vong ~1-3% - Có thể điều trị ngoại trú",
            "2": "Nguy cơ trung bình - Tỷ lệ tử vong ~9% - Nên nhập viện",
            "3-5": "Nguy cơ cao - Tỷ lệ tử vong ~15-40% - Cần nhập viện/ICU"
        },
        recommendations={
            "0-1": [
                "Điều trị ngoại trú với kháng sinh uống",
                "Theo dõi tại nhà",
                "Tái khám sau 48-72 giờ"
            ],
            "2": [
                "Nhập viện điều trị",
                "Kháng sinh IV",
                "Theo dõi sát"
            ],
            "3-5": [
                "Nhập viện/ICU ngay",
                "Kháng sinh IV phổ rộng",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi sát"
            ]
        }
    ),
    
    "news2": CalculatorMetadata(
        calculator_id="news2",
        title="NEWS2 Score",
        explanation="""
        **NEWS2 (National Early Warning Score 2)** là hệ thống cảnh báo sớm để phát hiện tình trạng xấu đi của bệnh nhân.
        
        **7 thông số được đánh giá:**
        1. Nhịp thở (Respiratory rate)
        2. Độ bão hòa oxy (SpO2)
        3. Huyết áp tâm thu (Systolic BP)
        4. Nhịp tim (Pulse rate)
        5. Mức độ ý thức (Level of consciousness)
        6. Nhiệt độ (Temperature)
        7. Oxy bổ sung (Supplemental oxygen)
        
        **Điểm số:** 0-20 điểm (tổng)
        """,
        when_to_use="""
        - Đánh giá bệnh nhân hàng ngày trong ward
        - Phát hiện sớm tình trạng xấu đi
        - Quyết định mức độ phản ứng lâm sàng
        - Theo dõi diễn tiến bệnh
        """,
        limitations="""
        - Cần đo đầy đủ 7 thông số
        - Một số thông số có thể không có sẵn
        - Cần đánh giá lại thường xuyên
        - Không thay thế đánh giá lâm sàng
        """,
        clinical_context="""
        NEWS2 được phát triển bởi Royal College of Physicians (RCP) 2017.
        Điểm cao hơn tương quan với nguy cơ xấu đi cao hơn và cần phản ứng lâm sàng nhanh hơn.
        NEWS2 ≥7: Cần đánh giá ngay bởi bác sĩ có kinh nghiệm.
        """,
        evidence_citation="Royal College of Physicians. National Early Warning Score (NEWS) 2: Standardising the assessment of acute-illness severity in the NHS. London: RCP, 2017.",
        evidence_url="https://www.rcplondon.ac.uk/projects/outputs/national-early-warning-score-news-2",
        interpretation_guide={
            "0-4": "Nguy cơ thấp - Theo dõi thường quy",
            "5-6": "Nguy cơ trung bình - Đánh giá bởi nhân viên có kinh nghiệm",
            "7-8": "Nguy cơ cao - Đánh giá ngay bởi bác sĩ có kinh nghiệm",
            "≥9": "Nguy cơ rất cao - Đánh giá ngay bởi bác sĩ có kinh nghiệm, cân nhắc chuyển ICU"
        },
        recommendations={
            "0-4": [
                "Theo dõi thường quy",
                "Đánh giá lại sau 12 giờ"
            ],
            "5-6": [
                "Đánh giá bởi nhân viên có kinh nghiệm",
                "Tăng tần suất theo dõi",
                "Đánh giá lại sau 4-6 giờ"
            ],
            "7-8": [
                "Đánh giá ngay bởi bác sĩ có kinh nghiệm",
                "Theo dõi sát (mỗi 1-2 giờ)",
                "Cân nhắc chuyển HDU/ICU",
                "Đánh giá lại sau 1 giờ"
            ],
            "≥9": [
                "Đánh giá ngay bởi bác sĩ có kinh nghiệm",
                "Theo dõi liên tục",
                "Cân nhắc chuyển ICU ngay",
                "Đánh giá lại sau 30 phút"
            ]
        }
    ),
    
    "gcs": CalculatorMetadata(
        calculator_id="gcs",
        title="Glasgow Coma Scale (GCS)",
        explanation="""
        **Glasgow Coma Scale (GCS)** là thang điểm đánh giá mức độ ý thức và chức năng thần kinh.
        
        **3 thành phần:**
        1. **Eye Opening (E)** - Mở mắt: 1-4 điểm
        2. **Verbal Response (V)** - Phản ứng lời nói: 1-5 điểm
        3. **Motor Response (M)** - Phản ứng vận động: 1-6 điểm
        
        **Tổng điểm:** 3-15 điểm
        - **3-8:** Hôn mê sâu (Coma)
        - **9-12:** Hôn mê trung bình (Moderate coma)
        - **13-15:** Tỉnh táo (Mild impairment/Normal)
        """,
        when_to_use="""
        - Đánh giá mức độ ý thức ở bệnh nhân chấn thương sọ não
        - Theo dõi diễn tiến sau chấn thương
        - Đánh giá bệnh nhân hôn mê
        - Quyết định mức độ chăm sóc (ICU, ward)
        """,
        limitations="""
        - Không áp dụng cho trẻ em <4 tuổi (dùng Pediatric GCS)
        - Có thể không chính xác nếu bệnh nhân đang dùng thuốc an thần
        - Cần đánh giá lại thường xuyên
        - Không thay thế đánh giá thần kinh đầy đủ
        """,
        clinical_context="""
        GCS được phát triển năm 1974 bởi Teasdale và Jennett.
        Điểm GCS thấp (<9) thường cần đặt nội khí quản và chăm sóc ICU.
        GCS giảm ≥2 điểm là dấu hiệu xấu đi cần can thiệp ngay.
        """,
        evidence_citation="Teasdale G, Jennett B. Assessment of coma and impaired consciousness. A practical scale. Lancet. 1974;2(7872):81-4.",
        evidence_doi="10.1016/s0140-6736(74)91639-0",
        interpretation_guide={
            "3-8": "Hôn mê sâu - Cần đặt nội khí quản, chăm sóc ICU",
            "9-12": "Hôn mê trung bình - Cần theo dõi sát, cân nhắc ICU",
            "13-15": "Tỉnh táo - Có thể theo dõi ở ward, đánh giá lại thường xuyên"
        },
        recommendations={
            "3-8": [
                "Đặt nội khí quản để bảo vệ đường thở",
                "Chăm sóc ICU",
                "CT Head ngay",
                "Thần kinh consult",
                "Theo dõi GCS mỗi 1-2 giờ"
            ],
            "9-12": [
                "Theo dõi sát",
                "Cân nhắc chuyển ICU",
                "CT Head",
                "Thần kinh consult",
                "Theo dõi GCS mỗi 2-4 giờ"
            ],
            "13-15": [
                "Theo dõi ở ward",
                "Đánh giá lại thường xuyên",
                "Xem xét CT Head nếu có chỉ định",
                "Theo dõi GCS mỗi 4-6 giờ"
            ]
        }
    ),
    
    "nihss": CalculatorMetadata(
        calculator_id="nihss",
        title="NIHSS (National Institutes of Health Stroke Scale)",
        explanation="""
        **NIHSS** là thang điểm đánh giá mức độ nặng của đột quỵ và tiên lượng.
        
        **15 items được đánh giá:**
        1. Level of consciousness
        2. Best gaze
        3. Visual fields
        4. Facial palsy
        5. Motor arm (right)
        6. Motor arm (left)
        7. Motor leg (right)
        8. Motor leg (left)
        9. Limb ataxia
        10. Sensory
        11. Best language
        12. Dysarthria
        13. Extinction/inattention
        
        **Tổng điểm:** 0-42 điểm
        - **0:** Không có triệu chứng
        - **1-4:** Đột quỵ nhẹ
        - **5-15:** Đột quỵ trung bình
        - **16-20:** Đột quỵ nặng
        - **21-42:** Đột quỵ rất nặng
        """,
        when_to_use="""
        - Đánh giá mức độ nặng đột quỵ cấp
        - Quyết định điều trị (tPA, thrombectomy)
        - Tiên lượng kết quả
        - Theo dõi diễn tiến sau điều trị
        """,
        limitations="""
        - Cần đánh giá bởi người được đào tạo
        - Mất thời gian (10-15 phút)
        - Một số items có thể không đánh giá được (aphasia, sedation)
        - Không thay thế đánh giá lâm sàng đầy đủ
        """,
        clinical_context="""
        NIHSS được phát triển bởi NIH để đánh giá đột quỵ.
        NIHSS ≥6: Có thể hưởng lợi từ tPA (nếu trong cửa sổ thời gian).
        NIHSS ≥10: Cân nhắc thrombectomy.
        NIHSS cao hơn tương quan với tiên lượng xấu hơn.
        """,
        evidence_citation="Brott T, Adams HP Jr, Olinger CP, et al. Measurements of acute cerebral infarction: a clinical examination scale. Stroke. 1989;20(7):864-70.",
        evidence_doi="10.1161/01.str.20.7.864",
        interpretation_guide={
            "0": "Không có triệu chứng - Tiên lượng tốt",
            "1-4": "Đột quỵ nhẹ - Tiên lượng tốt, có thể hồi phục hoàn toàn",
            "5-15": "Đột quỵ trung bình - Tiên lượng trung bình, cần điều trị tích cực",
            "16-20": "Đột quỵ nặng - Tiên lượng xấu, cần điều trị tích cực",
            "21-42": "Đột quỵ rất nặng - Tiên lượng rất xấu, tỷ lệ tử vong cao"
        },
        recommendations={
            "0-4": [
                "Đánh giá điều trị tPA nếu trong cửa sổ",
                "Theo dõi sát",
                "Tái đánh giá sau 24h"
            ],
            "5-15": [
                "Đánh giá điều trị tPA/thrombectomy",
                "Nhập viện điều trị",
                "Theo dõi sát",
                "Tái đánh giá sau 24h"
            ],
            "16-20": [
                "Điều trị tích cực",
                "Cân nhắc ICU",
                "Đánh giá thrombectomy",
                "Theo dõi sát"
            ],
            "21-42": [
                "Điều trị tích cực ngay",
                "ICU",
                "Thảo luận với gia đình về tiên lượng",
                "Theo dõi liên tục"
            ]
        }
    ),
    
    "meld": CalculatorMetadata(
        calculator_id="meld",
        title="MELD Score",
        explanation="""
        **MELD (Model for End-stage Liver Disease)** là thang điểm đánh giá mức độ nặng bệnh gan và tiên lượng tử vong.
        
        **Công thức:**
        MELD = 3.78 × ln(Total Bilirubin) + 11.2 × ln(INR) + 9.57 × ln(Creatinine) + 6.43
        
        **Thông số:**
        - Total Bilirubin (mg/dL)
        - INR (International Normalized Ratio)
        - Creatinine (mg/dL)
        
        **Tổng điểm:** 6-40 điểm
        - **<10:** Nguy cơ thấp
        - **10-19:** Nguy cơ trung bình
        - **20-29:** Nguy cơ cao
        - **≥30:** Nguy cơ rất cao
        """,
        when_to_use="""
        - Đánh giá mức độ nặng bệnh gan
        - Ưu tiên ghép gan (transplant listing)
        - Tiên lượng tử vong 3 tháng
        - Quyết định điều trị (TIPS, RRT)
        """,
        limitations="""
        - Không áp dụng cho bệnh nhân <12 tuổi
        - Cần có đầy đủ xét nghiệm
        - Không chính xác cho một số bệnh gan đặc biệt
        - Cần tính lại thường xuyên
        """,
        clinical_context="""
        MELD được phát triển để ưu tiên ghép gan.
        MELD ≥15: Cân nhắc ghép gan.
        MELD ≥25: Ưu tiên cao cho ghép gan.
        MELD cao hơn tương quan với tỷ lệ tử vong cao hơn.
        """,
        evidence_citation="Kamath PS, Wiesner RH, Malinchoc M, et al. A model to predict survival in patients with end-stage liver disease. Hepatology. 2001;33(2):464-70.",
        evidence_doi="10.1053/jhep.2001.22172",
        interpretation_guide={
            "<10": "Nguy cơ thấp - Tỷ lệ tử vong 3 tháng ~1.9%",
            "10-19": "Nguy cơ trung bình - Tỷ lệ tử vong 3 tháng ~6.0-19.6%",
            "20-29": "Nguy cơ cao - Tỷ lệ tử vong 3 tháng ~52.6%",
            "≥30": "Nguy cơ rất cao - Tỷ lệ tử vong 3 tháng ~71.3%"
        },
        recommendations={
            "<10": [
                "Theo dõi định kỳ",
                "Điều trị bệnh gan nền"
            ],
            "10-19": [
                "Theo dõi sát",
                "Cân nhắc ghép gan",
                "Điều trị biến chứng"
            ],
            "20-29": [
                "Ưu tiên cao cho ghép gan",
                "Điều trị tích cực",
                "Theo dõi sát"
            ],
            "≥30": [
                "Ưu tiên rất cao cho ghép gan",
                "Điều trị tích cực",
                "ICU nếu cần",
                "Thảo luận với gia đình"
            ]
        }
    ),
    
    "child_pugh": CalculatorMetadata(
        calculator_id="child_pugh",
        title="Child-Pugh Score",
        explanation="""
        **Child-Pugh Score** đánh giá mức độ nặng xơ gan và tiên lượng.
        
        **5 thông số:**
        1. **Total Bilirubin** (mg/dL)
        2. **Albumin** (g/dL)
        3. **INR** hoặc PT
        4. **Ascites** (Cổ trướng)
        5. **Hepatic Encephalopathy** (Bệnh não gan)
        
        **Mỗi thông số:** 1-3 điểm
        **Tổng điểm:** 5-15 điểm
        
        **Phân loại:**
        - **Class A (5-6 điểm):** Xơ gan nhẹ
        - **Class B (7-9 điểm):** Xơ gan trung bình
        - **Class C (10-15 điểm):** Xơ gan nặng
        """,
        when_to_use="""
        - Đánh giá mức độ nặng xơ gan
        - Tiên lượng phẫu thuật
        - Quyết định điều trị
        - Theo dõi diễn tiến
        """,
        limitations="""
        - Không chính xác cho một số bệnh gan đặc biệt
        - Một số thông số có thể chủ quan (ascites, encephalopathy)
        - Không thay thế đánh giá lâm sàng
        """,
        clinical_context="""
        Child-Pugh được phát triển từ 1964 và cập nhật 1973.
        Class A: Tiên lượng tốt, có thể phẫu thuật.
        Class B: Tiên lượng trung bình, cân nhắc cẩn thận.
        Class C: Tiên lượng xấu, tránh phẫu thuật nếu có thể.
        """,
        evidence_citation="Pugh RN, Murray-Lyon IM, Dawson JL, et al. Transection of the oesophagus for bleeding oesophageal varices. Br J Surg. 1973;60(8):646-9.",
        evidence_doi="10.1002/bjs.1800600817",
        interpretation_guide={
            "A (5-6)": "Xơ gan nhẹ - Tiên lượng tốt, tỷ lệ tử vong 1 năm ~10%",
            "B (7-9)": "Xơ gan trung bình - Tiên lượng trung bình, tỷ lệ tử vong 1 năm ~30%",
            "C (10-15)": "Xơ gan nặng - Tiên lượng xấu, tỷ lệ tử vong 1 năm ~50-80%"
        },
        recommendations={
            "A (5-6)": [
                "Có thể phẫu thuật",
                "Theo dõi định kỳ",
                "Điều trị bệnh gan nền"
            ],
            "B (7-9)": [
                "Cân nhắc cẩn thận trước phẫu thuật",
                "Theo dõi sát",
                "Điều trị biến chứng",
                "Cân nhắc ghép gan"
            ],
            "C (10-15)": [
                "Tránh phẫu thuật nếu có thể",
                "Điều trị tích cực",
                "Ưu tiên ghép gan",
                "Thảo luận với gia đình"
            ]
        }
    ),
    
    "ascvd": CalculatorMetadata(
        calculator_id="ascvd",
        title="ASCVD Risk Calculator",
        explanation="""
        **ASCVD (Atherosclerotic Cardiovascular Disease) Risk Calculator** đánh giá nguy cơ biến cố tim mạch trong 10 năm.
        
        **Các yếu tố:**
        - Tuổi
        - Giới tính
        - Chủng tộc (African American vs. Other)
        - Total Cholesterol (mg/dL)
        - HDL Cholesterol (mg/dL)
        - Huyết áp tâm thu (mmHg)
        - Đang điều trị tăng huyết áp (Yes/No)
        - Đái tháo đường (Yes/No)
        - Hút thuốc (Yes/No)
        
        **Kết quả:** Nguy cơ % trong 10 năm
        - **<5%:** Nguy cơ thấp
        - **5-7.4%:** Nguy cơ biên
        - **7.5-19.9%:** Nguy cơ trung bình
        - **≥20%:** Nguy cơ cao
        """,
        when_to_use="""
        - Đánh giá nguy cơ tim mạch ở người 40-75 tuổi
        - Quyết định điều trị statin
        - Tư vấn bệnh nhân về nguy cơ
        - Theo dõi nguy cơ theo thời gian
        """,
        limitations="""
        - Chỉ áp dụng cho người 40-75 tuổi
        - Không áp dụng cho người đã có ASCVD
        - Cần có đầy đủ thông tin
        - Không thay thế đánh giá lâm sàng
        """,
        clinical_context="""
        ASCVD Risk Calculator được phát triển từ Pooled Cohort Equations (AHA/ACC 2013, cập nhật 2018).
        Nguy cơ ≥7.5%: Khuyến cáo statin (AHA/ACC 2018).
        Nguy cơ ≥20%: Khuyến cáo statin mạnh.
        """,
        evidence_citation="Goff DC Jr, Lloyd-Jones DM, Bennett G, et al. 2013 ACC/AHA guideline on the assessment of cardiovascular risk: a report of the American College of Cardiology/American Heart Association Task Force on Practice Guidelines. Circulation. 2014;129(25 Suppl 2):S49-73.",
        evidence_doi="10.1161/01.cir.0000437741.48606.98",
        interpretation_guide={
            "<5%": "Nguy cơ thấp - Không cần statin (trừ khi có chỉ định khác)",
            "5-7.4%": "Nguy cơ biên - Cân nhắc statin",
            "7.5-19.9%": "Nguy cơ trung bình - Khuyến cáo statin",
            "≥20%": "Nguy cơ cao - Khuyến cáo statin mạnh"
        },
        recommendations={
            "<5%": [
                "Lối sống lành mạnh",
                "Theo dõi định kỳ",
                "Không cần statin (trừ khi có chỉ định khác)"
            ],
            "5-7.4%": [
                "Lối sống lành mạnh",
                "Cân nhắc statin",
                "Thảo luận với bệnh nhân"
            ],
            "7.5-19.9%": [
                "Khuyến cáo statin",
                "Lối sống lành mạnh",
                "Theo dõi định kỳ"
            ],
            "≥20%": [
                "Khuyến cáo statin mạnh",
                "Lối sống lành mạnh",
                "Theo dõi sát",
                "Điều trị các yếu tố nguy cơ khác"
            ]
        }
    ),
    
    "wells_pe": CalculatorMetadata(
        calculator_id="wells_pe",
        title="Wells PE Score",
        explanation="""
        **Wells PE Score** đánh giá xác suất tiền test của tắc mạch phổi (PE).
        
        **7 tiêu chí lâm sàng:**
        1. Dấu hiệu DVT (+3 điểm)
        2. PE có khả năng cao nhất (+3 điểm)
        3. Nhịp tim >100 (+1.5 điểm)
        4. Phẫu thuật/immobilization trong 4 tuần (+1.5 điểm)
        5. Tiền sử DVT/PE (+1.5 điểm)
        6. Ho ra máu (+1 điểm)
        7. Ung thư đang điều trị (+1 điểm)
        
        **Tổng điểm:** -3 đến +12.5
        """,
        when_to_use="""
        - Bệnh nhân có triệu chứng nghi ngờ PE (khó thở, đau ngực, ho ra máu)
        - Cần quyết định chiến lược xét nghiệm
        - Giảm thiểu chụp CTPA không cần thiết
        - Kết hợp với D-dimer để tối ưu hóa chẩn đoán
        """,
        limitations="""
        - Cần đánh giá lâm sàng chính xác
        - Không thay thế xét nghiệm chẩn đoán
        - Cần kết hợp với D-dimer hoặc CTPA
        - Độ nhạy và độ đặc hiệu phụ thuộc vào kinh nghiệm người đánh giá
        """,
        clinical_context="""
        Wells Score được phát triển bởi Wells et al. (2000).
        Wells Score >4: PE likely → CTPA ngay (hoặc D-dimer nếu không có CTPA).
        Wells Score ≤4: PE unlikely → D-dimer trước, nếu dương tính mới CTPA.
        Kết hợp Wells Score + D-dimer giúp giảm 20-30% số lượng CTPA không cần thiết.
        """,
        evidence_citation="Wells PS, Anderson DR, Rodger M, et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism: increasing the models utility with the SimpliRED D-dimer. Thromb Haemost. 2000;83(3):416-20.",
        evidence_doi="10.1055/s-0037-1613830",
        interpretation_guide={
            "≤4": "PE unlikely - Xác suất thấp, nên làm D-dimer trước",
            ">4": "PE likely - Xác suất cao, nên chụp CTPA ngay"
        },
        recommendations={
            "≤4": [
                "Làm D-dimer",
                "Nếu D-dimer âm tính: Loại trừ PE",
                "Nếu D-dimer dương tính: Chụp CTPA"
            ],
            ">4": [
                "Chụp CTPA ngay",
                "Nếu không có CTPA: Làm D-dimer",
                "Điều trị chống đông nếu có PE"
            ]
        }
    ),
    
    "timi": CalculatorMetadata(
        calculator_id="timi",
        title="TIMI Risk Score",
        explanation="""
        **TIMI Risk Score** dự đoán tử vong, nhồi máu cơ tim mới hoặc cần tái can thiệp trong 14 ngày.
        
        **7 tiêu chí:**
        1. Tuổi ≥65 (+1 điểm)
        2. ≥3 yếu tố nguy cơ mạch vành (+1 điểm)
        3. Bệnh mạch vành đã biết (hẹp ≥50%) (+1 điểm)
        4. ST chênh xuống ≥0.5mm (+1 điểm)
        5. ≥2 cơn đau ngực trong 24h (+1 điểm)
        6. Aspirin trong 7 ngày qua (+1 điểm)
        7. Tăng troponin/CK-MB (+1 điểm)
        
        **Tổng điểm:** 0-7
        """,
        when_to_use="""
        - Bệnh nhân có UA/NSTEMI
        - Cần quyết định chiến lược điều trị (invasive vs conservative)
        - Đánh giá tiên lượng và kết quả lâm sàng
        - Hướng dẫn thời điểm can thiệp mạch vành
        """,
        limitations="""
        - Chỉ áp dụng cho UA/NSTEMI, không áp dụng cho STEMI
        - Cần có đầy đủ thông tin lâm sàng và xét nghiệm
        - Không thay thế đánh giá lâm sàng cá thể hóa
        - Một số yếu tố có thể không có sẵn ngay
        """,
        clinical_context="""
        TIMI Risk Score được phát triển từ TIMI 11B và ESSENCE trials (Antman et al., 2000).
        TIMI 0-2: Nguy cơ thấp → Cân nhắc điều trị bảo tồn.
        TIMI 3-4: Nguy cơ trung bình → Cân nhắc can thiệp sớm.
        TIMI 5-7: Nguy cơ cao → Khuyến cáo can thiệp sớm (<48h).
        """,
        evidence_citation="Antman EM, Cohen M, Bernink PJ, et al. The TIMI risk score for unstable angina/non-ST elevation MI: A method for prognostication and therapeutic decision making. JAMA. 2000;284(7):835-42.",
        evidence_doi="10.1001/jama.284.7.835",
        interpretation_guide={
            "0-2": "Nguy cơ thấp - Tỷ lệ tử vong/biến cố ~4.7%",
            "3-4": "Nguy cơ trung bình - Tỷ lệ tử vong/biến cố ~8.3%",
            "5-7": "Nguy cơ cao - Tỷ lệ tử vong/biến cố ~13.2-40.9%"
        },
        recommendations={
            "0-2": [
                "Cân nhắc điều trị bảo tồn",
                "Theo dõi sát",
                "Đánh giá lại nếu diễn tiến xấu"
            ],
            "3-4": [
                "Cân nhắc can thiệp sớm",
                "Điều trị chống đông",
                "Theo dõi sát"
            ],
            "5-7": [
                "Khuyến cáo can thiệp sớm (<48h)",
                "Điều trị chống đông tích cực",
                "ICU nếu cần",
                "Theo dõi sát"
            ]
        }
    ),
    
    "grace": CalculatorMetadata(
        calculator_id="grace",
        title="GRACE Score",
        explanation="""
        **GRACE (Global Registry of Acute Coronary Events) Score** dự đoán tử vong trong bệnh viện và 6 tháng sau ACS.
        
        **8 thông số lâm sàng:**
        1. Tuổi (năm)
        2. Nhịp tim (bpm)
        3. Huyết áp tâm thu (mmHg)
        4. Creatinine (mg/dL)
        5. Killip class
        6. ST chênh lên
        7. Cardiac arrest tại nhập viện
        8. Tăng men tim (CK-MB/Troponin)
        
        **Tổng điểm:** 0-258
        """,
        when_to_use="""
        - Bệnh nhân có ACS (STEMI/NSTEMI/UA)
        - Cần đánh giá tiên lượng tử vong
        - Quyết định chiến lược điều trị (invasive vs conservative)
        - Hướng dẫn thời điểm can thiệp mạch vành
        """,
        limitations="""
        - Cần có đầy đủ thông tin lâm sàng và xét nghiệm
        - Không áp dụng cho bệnh nhân không có ACS
        - Một số thông số có thể không có sẵn ngay
        - Không thay thế đánh giá lâm sàng cá thể hóa
        """,
        clinical_context="""
        GRACE Score được phát triển từ Global Registry of Acute Coronary Events (Granger et al., 2003).
        GRACE <109: Nguy cơ tử vong thấp → Cân nhắc điều trị bảo tồn.
        GRACE 109-140: Nguy cơ tử vong trung bình → Cân nhắc can thiệp sớm.
        GRACE >140: Nguy cơ tử vong cao → Khuyến cáo can thiệp sớm.
        """,
        evidence_citation="Granger CB, Goldberg RJ, Dabbous O, et al. Predictors of hospital mortality in the global registry of acute coronary events. Arch Intern Med. 2003;163(19):2345-53.",
        evidence_doi="10.1001/archinte.163.19.2345",
        interpretation_guide={
            "<109": "Nguy cơ tử vong thấp - Tỷ lệ tử vong trong bệnh viện ~1-3%",
            "109-140": "Nguy cơ tử vong trung bình - Tỷ lệ tử vong trong bệnh viện ~3-8%",
            ">140": "Nguy cơ tử vong cao - Tỷ lệ tử vong trong bệnh viện ~>8%"
        },
        recommendations={
            "<109": [
                "Cân nhắc điều trị bảo tồn",
                "Theo dõi sát",
                "Đánh giá lại nếu diễn tiến xấu"
            ],
            "109-140": [
                "Cân nhắc can thiệp sớm",
                "Điều trị chống đông",
                "Theo dõi sát"
            ],
            ">140": [
                "Khuyến cáo can thiệp sớm",
                "Điều trị chống đông tích cực",
                "ICU nếu cần",
                "Theo dõi sát"
            ]
        }
    ),
    
    "wells_dvt": CalculatorMetadata(
        calculator_id="wells_dvt",
        title="Wells DVT Score",
        explanation="""
        **Wells DVT Score** đánh giá xác suất tiền test của huyết khối tĩnh mạch sâu (DVT).
        
        **9 tiêu chí lâm sàng:**
        1. Active cancer (+1 điểm)
        2. Paralysis/immobilization (+1 điểm)
        3. Bedridden >3 days or major surgery (+1 điểm)
        4. Localized tenderness (+1 điểm)
        5. Entire leg swollen (+1 điểm)
        6. Calf swelling >3 cm (+1 điểm)
        7. Pitting edema (+1 điểm)
        8. Collateral superficial veins (+1 điểm)
        9. Alternative diagnosis likely (-2 điểm)
        
        **Tổng điểm:** -2 đến +8
        """,
        when_to_use="""
        - Bệnh nhân có triệu chứng nghi ngờ DVT (sưng chân, đau, đỏ)
        - Cần quyết định chiến lược xét nghiệm
        - Giảm thiểu siêu âm Doppler không cần thiết
        - Kết hợp với D-dimer để tối ưu hóa chẩn đoán
        """,
        limitations="""
        - Cần đánh giá lâm sàng chính xác
        - Không thay thế xét nghiệm chẩn đoán
        - Cần kết hợp với D-dimer hoặc siêu âm Doppler
        - Độ nhạy và độ đặc hiệu phụ thuộc vào kinh nghiệm người đánh giá
        """,
        clinical_context="""
        Wells DVT Score được phát triển bởi Wells et al. (1997).
        Wells Score ≥2: DVT likely → Siêu âm Doppler ngay (hoặc D-dimer nếu không có siêu âm).
        Wells Score <2: DVT unlikely → D-dimer trước, nếu dương tính mới siêu âm Doppler.
        Kết hợp Wells Score + D-dimer giúp giảm 20-30% số lượng siêu âm không cần thiết.
        """,
        evidence_citation="Wells PS, Anderson DR, Bormanis J, et al. Value of assessment of pretest probability of deep-vein thrombosis in clinical management. Lancet. 1997;350(9094):1795-8.",
        evidence_doi="10.1016/S0140-6736(97)08140-3",
        interpretation_guide={
            "<2": "DVT unlikely - Xác suất thấp, nên làm D-dimer trước",
            "≥2": "DVT likely - Xác suất cao, nên siêu âm Doppler ngay"
        },
        recommendations={
            "<2": [
                "Làm D-dimer",
                "Nếu D-dimer âm tính: Loại trừ DVT",
                "Nếu D-dimer dương tính: Siêu âm Doppler"
            ],
            "≥2": [
                "Siêu âm Doppler ngay",
                "Nếu không có siêu âm: Làm D-dimer",
                "Điều trị chống đông nếu có DVT"
            ]
        }
    ),
    
    "bisap": CalculatorMetadata(
        calculator_id="bisap",
        title="BISAP Score",
        explanation="""
        **BISAP (Bedside Index for Severity in Acute Pancreatitis) Score** đánh giá mức độ nặng và tiên lượng tử vong trong viêm tụy cấp.
        
        **5 tiêu chí (mỗi tiêu chí = 1 điểm):**
        1. **B**UN > 25 mg/dL (>8.93 mmol/L)
        2. **I**mpaired mental status (Lú lẫn, GCS < 15)
        3. **S**IRS (≥2 tiêu chí SIRS)
        4. **A**ge > 60 tuổi
        5. **P**leural effusion (Tràn dịch màng phổi trên X-quang)
        
        **Tổng điểm:** 0-5
        """,
        when_to_use="""
        - Tất cả bệnh nhân viêm tụy cấp
        - Đặc biệt hữu ích trong 24h đầu nhập viện
        - Hướng dẫn quyết định chuyển ICU
        - Đánh giá tiên lượng tử vong
        """,
        limitations="""
        - Cần đánh giá trong 24h đầu
        - Một số tiêu chí có thể chủ quan (mental status)
        - Không thay thế đánh giá lâm sàng toàn diện
        - Cần kết hợp với các dấu hiệu lâm sàng khác
        """,
        clinical_context="""
        BISAP Score được phát triển bởi Wu et al. (2008).
        BISAP 0-2: Viêm tụy nhẹ → Tử vong <2%.
        BISAP 3-4: Viêm tụy trung bình → Tử vong 5-15%.
        BISAP 5: Viêm tụy nặng → Tử vong >20%.
        BISAP đơn giản hơn Ranson (5 vs 11 tiêu chí) nhưng độ chính xác tương đương.
        """,
        evidence_citation="Wu BU, Johannes RS, Sun X, et al. The early prediction of mortality in acute pancreatitis: a large population-based study. Gut. 2008;57(12):1698-703.",
        evidence_doi="10.1136/gut.2008.152702",
        interpretation_guide={
            "0-2": "Viêm tụy nhẹ - Tử vong <2%, thường không cần ICU",
            "3-4": "Viêm tụy trung bình - Tử vong 5-15%, cân nhắc ICU",
            "5": "Viêm tụy nặng - Tử vong >20%, cần ICU"
        },
        recommendations={
            "0-2": [
                "Điều trị nội khoa thường quy",
                "Theo dõi sát",
                "Không cần ICU (thường)"
            ],
            "3-4": [
                "Theo dõi chặt",
                "Cân nhắc ICU/HDU",
                "Điều trị tích cực",
                "Xem xét can thiệp nếu cần"
            ],
            "5": [
                "CẦN ICU",
                "Điều trị tích cực",
                "Xem xét can thiệp",
                "Thảo luận với gia đình"
            ]
        }
    ),
    
    "ranson": CalculatorMetadata(
        calculator_id="ranson",
        title="Ranson Criteria",
        explanation="""
        **Ranson Criteria** đánh giá mức độ nặng và tiên lượng tử vong trong viêm tụy cấp.
        
        **11 tiêu chí (2 bộ):**
        **Lúc nhập viện (0h):** 5 tiêu chí
        1. Tuổi >55
        2. WBC >16,000/mm³
        3. Glucose >200 mg/dL
        4. LDH >350 U/L
        5. AST >250 U/L
        
        **Sau 48 giờ:** 6 tiêu chí
        6. Hct giảm >10%
        7. BUN tăng >5 mg/dL
        8. Ca <8 mg/dL
        9. PaO₂ <60 mmHg
        10. Base deficit >4 mEq/L
        11. Fluid sequestration >6 L
        
        **Tổng điểm:** 0-11
        """,
        when_to_use="""
        - Tất cả bệnh nhân viêm tụy cấp
        - Đánh giá tiên lượng tử vong
        - Hướng dẫn quyết định chuyển ICU
        - Đánh giá sau 48h nhập viện
        """,
        limitations="""
        - Cần CHỜ 48H để tính đủ điểm
        - Phức tạp hơn BISAP (11 vs 5 tiêu chí)
        - Một số tiêu chí có thể không có sẵn ngay
        - Không thay thế đánh giá lâm sàng toàn diện
        """,
        clinical_context="""
        Ranson Criteria được phát triển bởi Ranson et al. (1974).
        Ranson <3: Viêm tụy nhẹ → Tử vong <1%.
        Ranson 3-5: Viêm tụy trung bình → Tử vong 10-20%.
        Ranson ≥6: Viêm tụy nặng → Tử vong >50%.
        Ranson là tiêu chuẩn vàng nhưng phức tạp, BISAP đơn giản hơn và tương đương.
        """,
        evidence_citation="Ranson JH, Rifkind KM, Roses DF, et al. Prognostic signs and the role of operative management in acute pancreatitis. Surg Gynecol Obstet. 1974;139(1):69-81.",
        evidence_doi="",
        interpretation_guide={
            "<3": "Viêm tụy nhẹ - Tử vong <1%, thường không cần ICU",
            "3-5": "Viêm tụy trung bình - Tử vong 10-20%, cân nhắc ICU",
            "≥6": "Viêm tụy nặng - Tử vong >50%, cần ICU"
        },
        recommendations={
            "<3": [
                "Điều trị nội khoa thường quy",
                "Theo dõi sát",
                "Không cần ICU (thường)"
            ],
            "3-5": [
                "Theo dõi chặt",
                "Cân nhắc ICU/HDU",
                "Điều trị tích cực",
                "Xem xét can thiệp nếu cần"
            ],
            "≥6": [
                "CẦN ICU",
                "Điều trị tích cực",
                "Xem xét can thiệp",
                "Thảo luận với gia đình"
            ]
        }
    )
}


def get_calculator_metadata(calculator_id: str) -> Optional[CalculatorMetadata]:
    """
    Get metadata for a calculator.
    
    Args:
        calculator_id: Calculator ID
        
    Returns:
        CalculatorMetadata or None
    """
    return CALCULATOR_METADATA.get(calculator_id)


def render_calculator_education(calculator_id: str):
    """
    Render educational content for a calculator.
    
    Args:
        calculator_id: Calculator ID
    """
    metadata = get_calculator_metadata(calculator_id)
    if not metadata:
        return
    
    render_calculator_explanation(
        title=metadata.title,
        content=metadata.explanation,
        when_to_use=metadata.when_to_use,
        limitations=metadata.limitations,
        clinical_context=metadata.clinical_context
    )
    
    if metadata.evidence_citation:
        render_evidence_citation(
            citation_text=metadata.evidence_citation,
            doi=metadata.evidence_doi,
            url=metadata.evidence_url
        )


def render_calculator_result_with_interpretation(
    calculator_id: str,
    result: str,
    result_value: Optional[float] = None
):
    """
    Render calculator result with interpretation.
    
    Args:
        calculator_id: Calculator ID
        result: Result text
        result_value: Numeric result value (if applicable)
    """
    metadata = get_calculator_metadata(calculator_id)
    if not metadata or not metadata.interpretation_guide:
        st.markdown(f"**Kết quả:** {result}")
        return
    
    # Find matching interpretation
    interpretation = None
    recommendations = None
    
    if result_value is not None:
        # Try to match numeric ranges
        for key, value in metadata.interpretation_guide.items():
            if "-" in key:
                parts = key.split("-")
                if len(parts) == 2:
                    try:
                        low, high = float(parts[0]), float(parts[1])
                        if low <= result_value <= high:
                            interpretation = value
                            if metadata.recommendations:
                                recommendations = metadata.recommendations.get(key)
                            break
                    except:
                        pass
            elif key.replace(".", "").isdigit():
                try:
                    if float(key) == result_value:
                        interpretation = value
                        if metadata.recommendations:
                            recommendations = metadata.recommendations.get(key)
                        break
                except:
                    pass
    
    # Fallback to string matching
    if not interpretation:
        interpretation = metadata.interpretation_guide.get(result, "Vui lòng tham khảo tài liệu chuyên môn.")
        if metadata.recommendations:
            recommendations = metadata.recommendations.get(result)
    
    render_result_interpretation(
        result=result,
        interpretation=interpretation or "Vui lòng tham khảo tài liệu chuyên môn.",
        recommendations=recommendations
    )

