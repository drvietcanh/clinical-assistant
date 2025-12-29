"""
ICD-10 Data - International Classification of Diseases, 10th Revision
Common ICD-10 codes organized by category
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ICD10Code:
    """ICD-10 code information"""
    code: str  # e.g., "A00.0"
    name_en: str  # English name
    name_vn: str  # Vietnamese name
    category: str  # Category/specialty
    chapter: str  # ICD-10 chapter
    block: str = ""  # ICD-10 block
    notes: str = ""  # Additional notes


# ICD-10 Database - Common codes organized by category
# This is a subset of the most commonly used codes
# Full ICD-10 has 70,000+ codes

ICD10_DATABASE: List[ICD10Code] = [
    # === INFECTIOUS DISEASES ===
    ICD10Code("A00.0", "Cholera due to Vibrio cholerae 01, biovar cholerae", 
              "Dịch tả do Vibrio cholerae 01, biovar cholerae", "Infectious", "Chapter I"),
    ICD10Code("A00.1", "Cholera due to Vibrio cholerae 01, biovar eltor", 
              "Dịch tả do Vibrio cholerae 01, biovar eltor", "Infectious", "Chapter I"),
    ICD10Code("A15.0", "Tuberculosis of lung, confirmed by sputum microscopy with or without culture", 
              "Lao phổi, xác nhận bằng soi đờm có hoặc không có cấy", "Infectious", "Chapter I"),
    ICD10Code("A15.1", "Tuberculosis of lung, confirmed by culture only", 
              "Lao phổi, xác nhận chỉ bằng cấy", "Infectious", "Chapter I"),
    ICD10Code("A15.2", "Tuberculosis of lung, confirmed histologically", 
              "Lao phổi, xác nhận bằng mô học", "Infectious", "Chapter I"),
    ICD10Code("A15.9", "Respiratory tuberculosis unspecified, bacteriological and histological examination not done", 
              "Lao hô hấp không xác định, chưa làm xét nghiệm vi khuẩn và mô học", "Infectious", "Chapter I"),
    ICD10Code("A16.0", "Tuberculosis of lung, bacteriologically and histologically negative", 
              "Lao phổi, âm tính vi khuẩn và mô học", "Infectious", "Chapter I"),
    ICD10Code("A16.2", "Tuberculosis of lung, without mention of bacteriological or histological confirmation", 
              "Lao phổi, không đề cập xác nhận vi khuẩn hoặc mô học", "Infectious", "Chapter I"),
    ICD10Code("A41.9", "Sepsis, unspecified organism", 
              "Nhiễm khuẩn huyết, không xác định tác nhân", "Infectious", "Chapter I"),
    ICD10Code("A41.51", "Sepsis due to Escherichia coli", 
              "Nhiễm khuẩn huyết do Escherichia coli", "Infectious", "Chapter I"),
    ICD10Code("A41.52", "Sepsis due to Pseudomonas", 
              "Nhiễm khuẩn huyết do Pseudomonas", "Infectious", "Chapter I"),
    ICD10Code("A41.9", "Sepsis, unspecified organism", 
              "Nhiễm khuẩn huyết, không xác định tác nhân", "Infectious", "Chapter I"),
    ICD10Code("B20", "Human immunodeficiency virus [HIV] disease", 
              "Bệnh do virus suy giảm miễn dịch ở người [HIV]", "Infectious", "Chapter I"),
    ICD10Code("B34.2", "Coronavirus infection, unspecified", 
              "Nhiễm coronavirus, không xác định", "Infectious", "Chapter I"),
    ICD10Code("B34.9", "Viral infection, unspecified", 
              "Nhiễm virus, không xác định", "Infectious", "Chapter I"),
    
    # === NEOPLASMS ===
    ICD10Code("C50.9", "Malignant neoplasm of breast, unspecified", 
              "U ác tính vú, không xác định", "Oncology", "Chapter II"),
    ICD10Code("C34.10", "Malignant neoplasm of unspecified main bronchus", 
              "U ác tính phế quản chính không xác định", "Oncology", "Chapter II"),
    ICD10Code("C34.90", "Malignant neoplasm of unspecified part of bronchus or lung", 
              "U ác tính phần không xác định của phế quản hoặc phổi", "Oncology", "Chapter II"),
    ICD10Code("C25.9", "Malignant neoplasm of pancreas, unspecified", 
              "U ác tính tụy, không xác định", "Oncology", "Chapter II"),
    ICD10Code("C18.9", "Malignant neoplasm of colon, unspecified", 
              "U ác tính đại tràng, không xác định", "Oncology", "Chapter II"),
    ICD10Code("C22.0", "Liver cell carcinoma", 
              "Ung thư tế bào gan", "Oncology", "Chapter II"),
    ICD10Code("C61", "Malignant neoplasm of prostate", 
              "U ác tính tuyến tiền liệt", "Oncology", "Chapter II"),
    ICD10Code("C25.0", "Malignant neoplasm of head of pancreas", 
              "U ác tính đầu tụy", "Oncology", "Chapter II"),
    
    # === BLOOD DISORDERS ===
    ICD10Code("D50.9", "Iron deficiency anemia, unspecified", 
              "Thiếu máu thiếu sắt, không xác định", "Hematology", "Chapter III"),
    ICD10Code("D64.9", "Anemia, unspecified", 
              "Thiếu máu, không xác định", "Hematology", "Chapter III"),
    ICD10Code("D69.6", "Thrombocytopenia, unspecified", 
              "Giảm tiểu cầu, không xác định", "Hematology", "Chapter III"),
    ICD10Code("D65", "Disseminated intravascular coagulation [defibrination syndrome]", 
              "Đông máu nội mạch lan tỏa [hội chứng mất fibrin]", "Hematology", "Chapter III"),
    
    # === ENDOCRINE DISORDERS ===
    ICD10Code("E10.9", "Type 1 diabetes mellitus without complications", 
              "Đái tháo đường type 1 không biến chứng", "Endocrinology", "Chapter IV"),
    ICD10Code("E11.9", "Type 2 diabetes mellitus without complications", 
              "Đái tháo đường type 2 không biến chứng", "Endocrinology", "Chapter IV"),
    ICD10Code("E11.65", "Type 2 diabetes mellitus with hyperglycemia", 
              "Đái tháo đường type 2 với tăng đường huyết", "Endocrinology", "Chapter IV"),
    ICD10Code("E11.21", "Type 2 diabetes mellitus with diabetic nephropathy", 
              "Đái tháo đường type 2 với bệnh thận đái tháo đường", "Endocrinology", "Chapter IV"),
    ICD10Code("E11.40", "Type 2 diabetes mellitus with diabetic neuropathy, unspecified", 
              "Đái tháo đường type 2 với bệnh thần kinh đái tháo đường, không xác định", "Endocrinology", "Chapter IV"),
    ICD10Code("E11.9", "Type 2 diabetes mellitus without complications", 
              "Đái tháo đường type 2 không biến chứng", "Endocrinology", "Chapter IV"),
    ICD10Code("E03.9", "Hypothyroidism, unspecified", 
              "Suy giáp, không xác định", "Endocrinology", "Chapter IV"),
    ICD10Code("E05.90", "Thyrotoxicosis, unspecified without thyrotoxic crisis or storm", 
              "Cường giáp, không xác định không có cơn bão giáp", "Endocrinology", "Chapter IV"),
    ICD10Code("E87.6", "Hypokalemia", 
              "Hạ kali máu", "Endocrinology", "Chapter IV"),
    ICD10Code("E87.5", "Hyperkalemia", 
              "Tăng kali máu", "Endocrinology", "Chapter IV"),
    ICD10Code("E87.3", "Alkalosis", 
              "Kiềm máu", "Endocrinology", "Chapter IV"),
    ICD10Code("E87.2", "Acidosis", 
              "Toan máu", "Endocrinology", "Chapter IV"),
    
    # === MENTAL DISORDERS ===
    ICD10Code("F32.9", "Major depressive disorder, single episode, unspecified", 
              "Rối loạn trầm cảm nặng, đơn độc, không xác định", "Psychiatry", "Chapter V"),
    ICD10Code("F41.9", "Anxiety disorder, unspecified", 
              "Rối loạn lo âu, không xác định", "Psychiatry", "Chapter V"),
    ICD10Code("F10.10", "Alcohol abuse, uncomplicated", 
              "Lạm dụng rượu, không biến chứng", "Psychiatry", "Chapter V"),
    ICD10Code("F20.9", "Schizophrenia, unspecified", 
              "Tâm thần phân liệt, không xác định", "Psychiatry", "Chapter V"),
    
    # === NERVOUS SYSTEM ===
    ICD10Code("G93.1", "Anoxic brain damage, not elsewhere classified", 
              "Tổn thương não do thiếu oxy, không phân loại nơi khác", "Neurology", "Chapter VI"),
    ICD10Code("G40.909", "Epilepsy, unspecified, not intractable, without status epilepticus", 
              "Động kinh, không xác định, không kháng trị, không có trạng thái động kinh", "Neurology", "Chapter VI"),
    ICD10Code("G93.1", "Anoxic brain damage, not elsewhere classified", 
              "Tổn thương não do thiếu oxy, không phân loại nơi khác", "Neurology", "Chapter VI"),
    ICD10Code("I63.9", "Cerebral infarction, unspecified", 
              "Nhồi máu não, không xác định", "Neurology", "Chapter IX"),
    ICD10Code("I64", "Stroke, not specified as hemorrhage or infarction", 
              "Đột quỵ, không xác định xuất huyết hay nhồi máu", "Neurology", "Chapter IX"),
    ICD10Code("G91.9", "Hydrocephalus, unspecified", 
              "Não úng thủy, không xác định", "Neurology", "Chapter VI"),
    
    # === EYE DISORDERS ===
    ICD10Code("H54.0", "Blindness, both eyes", 
              "Mù, cả hai mắt", "Ophthalmology", "Chapter VII"),
    ICD10Code("H25.9", "Unspecified age-related cataract", 
              "Đục thủy tinh thể liên quan tuổi, không xác định", "Ophthalmology", "Chapter VII"),
    ICD10Code("H40.9", "Unspecified glaucoma", 
              "Glaucoma, không xác định", "Ophthalmology", "Chapter VII"),
    
    # === EAR DISORDERS ===
    ICD10Code("H90.3", "Sensorineural hearing loss, bilateral", 
              "Điếc tiếp nhận, hai bên", "ENT", "Chapter VIII"),
    ICD10Code("H91.9", "Hearing loss, unspecified", 
              "Điếc, không xác định", "ENT", "Chapter VIII"),
    
    # === CIRCULATORY SYSTEM ===
    ICD10Code("I10", "Essential (primary) hypertension", 
              "Tăng huyết áp nguyên phát", "Cardiology", "Chapter IX"),
    ICD10Code("I11.9", "Hypertensive heart disease without heart failure", 
              "Bệnh tim tăng huyết áp không suy tim", "Cardiology", "Chapter IX"),
    ICD10Code("I12.9", "Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease", 
              "Bệnh thận mạn tính tăng huyết áp với CKD giai đoạn 1-4 hoặc CKD không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I13.2", "Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease", 
              "Bệnh tim và thận mạn tính tăng huyết áp với suy tim và CKD giai đoạn 5 hoặc bệnh thận giai đoạn cuối", "Cardiology", "Chapter IX"),
    ICD10Code("I20.9", "Angina pectoris, unspecified", 
              "Đau thắt ngực, không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I21.9", "Acute myocardial infarction, unspecified", 
              "Nhồi máu cơ tim cấp, không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I21.11", "ST elevation (STEMI) myocardial infarction involving left anterior descending coronary artery", 
              "Nhồi máu cơ tim ST chênh lên (STEMI) liên quan động mạch vành trước xuống trái", "Cardiology", "Chapter IX"),
    ICD10Code("I21.19", "ST elevation (STEMI) myocardial infarction involving other coronary artery", 
              "Nhồi máu cơ tim ST chênh lên (STEMI) liên quan động mạch vành khác", "Cardiology", "Chapter IX"),
    ICD10Code("I21.29", "Non-ST elevation (NSTEMI) myocardial infarction", 
              "Nhồi máu cơ tim không ST chênh lên (NSTEMI)", "Cardiology", "Chapter IX"),
    ICD10Code("I25.10", "Atherosclerotic heart disease of native coronary artery without angina pectoris", 
              "Bệnh tim xơ vữa động mạch mạch vành tự nhiên không đau thắt ngực", "Cardiology", "Chapter IX"),
    ICD10Code("I50.9", "Heart failure, unspecified", 
              "Suy tim, không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I50.1", "Left ventricular failure", 
              "Suy thất trái", "Cardiology", "Chapter IX"),
    ICD10Code("I50.2", "Systolic heart failure", 
              "Suy tim tâm thu", "Cardiology", "Chapter IX"),
    ICD10Code("I50.3", "Diastolic heart failure", 
              "Suy tim tâm trương", "Cardiology", "Chapter IX"),
    ICD10Code("I50.4", "Combined systolic and diastolic heart failure", 
              "Suy tim tâm thu và tâm trương kết hợp", "Cardiology", "Chapter IX"),
    ICD10Code("I48.91", "Unspecified atrial fibrillation", 
              "Rung nhĩ, không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I49.9", "Cardiac arrhythmia, unspecified", 
              "Rối loạn nhịp tim, không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I26.99", "Other pulmonary embolism without acute cor pulmonale", 
              "Thuyên tắc phổi khác không có tâm phế cấp", "Cardiology", "Chapter IX"),
    ICD10Code("I80.9", "Phlebitis and thrombophlebitis of unspecified site", 
              "Viêm tĩnh mạch và huyết khối tĩnh mạch, vị trí không xác định", "Cardiology", "Chapter IX"),
    ICD10Code("I82.90", "Acute embolism and thrombosis of unspecified vein", 
              "Thuyên tắc và huyết khối tĩnh mạch cấp, không xác định", "Cardiology", "Chapter IX"),
    
    # === RESPIRATORY SYSTEM ===
    ICD10Code("J18.9", "Pneumonia, unspecified organism", 
              "Viêm phổi, không xác định tác nhân", "Respiratory", "Chapter X"),
    ICD10Code("J15.9", "Unspecified bacterial pneumonia", 
              "Viêm phổi do vi khuẩn, không xác định", "Respiratory", "Chapter X"),
    ICD10Code("J12.9", "Viral pneumonia, unspecified", 
              "Viêm phổi do virus, không xác định", "Respiratory", "Chapter X"),
    ICD10Code("J44.0", "Chronic obstructive pulmonary disease with acute lower respiratory infection", 
              "Bệnh phổi tắc nghẽn mạn tính với nhiễm trùng hô hấp dưới cấp", "Respiratory", "Chapter X"),
    ICD10Code("J44.1", "Chronic obstructive pulmonary disease with (acute) exacerbation", 
              "Bệnh phổi tắc nghẽn mạn tính với đợt cấp", "Respiratory", "Chapter X"),
    ICD10Code("J44.9", "Chronic obstructive pulmonary disease, unspecified", 
              "Bệnh phổi tắc nghẽn mạn tính, không xác định", "Respiratory", "Chapter X"),
    ICD10Code("J45.909", "Unspecified asthma, uncomplicated", 
              "Hen phế quản, không xác định, không biến chứng", "Respiratory", "Chapter X"),
    ICD10Code("J96.00", "Acute respiratory failure, unspecified whether with hypoxia or hypercapnia", 
              "Suy hô hấp cấp, không xác định có thiếu oxy hay tăng CO2", "Respiratory", "Chapter X"),
    ICD10Code("J96.90", "Respiratory failure, unspecified, unspecified whether with hypoxia or hypercapnia", 
              "Suy hô hấp, không xác định, không xác định có thiếu oxy hay tăng CO2", "Respiratory", "Chapter X"),
    
    # === DIGESTIVE SYSTEM ===
    ICD10Code("K25.9", "Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation", 
              "Loét dạ dày, không xác định cấp hay mạn, không xuất huyết hay thủng", "GI", "Chapter XI"),
    ICD10Code("K26.9", "Duodenal ulcer, unspecified as acute or chronic, without hemorrhage or perforation", 
              "Loét tá tràng, không xác định cấp hay mạn, không xuất huyết hay thủng", "GI", "Chapter XI"),
    ICD10Code("K29.30", "Chronic gastritis, unspecified, without bleeding", 
              "Viêm dạ dày mạn tính, không xác định, không chảy máu", "GI", "Chapter XI"),
    ICD10Code("K29.90", "Gastritis, unspecified, without bleeding", 
              "Viêm dạ dày, không xác định, không chảy máu", "GI", "Chapter XI"),
    ICD10Code("K59.00", "Constipation, unspecified", 
              "Táo bón, không xác định", "GI", "Chapter XI"),
    ICD10Code("K59.09", "Other constipation", 
              "Táo bón khác", "GI", "Chapter XI"),
    ICD10Code("K59.01", "Slow transit constipation", 
              "Táo bón chậm vận chuyển", "GI", "Chapter XI"),
    ICD10Code("K92.2", "Gastrointestinal hemorrhage, unspecified", 
              "Xuất huyết tiêu hóa, không xác định", "GI", "Chapter XI"),
    ICD10Code("K74.60", "Unspecified cirrhosis of liver", 
              "Xơ gan, không xác định", "GI", "Chapter XI"),
    ICD10Code("K70.30", "Alcoholic cirrhosis of liver without ascites", 
              "Xơ gan do rượu không cổ trướng", "GI", "Chapter XI"),
    ICD10Code("K76.9", "Liver disease, unspecified", 
              "Bệnh gan, không xác định", "GI", "Chapter XI"),
    ICD10Code("K85.90", "Acute pancreatitis, unspecified", 
              "Viêm tụy cấp, không xác định", "GI", "Chapter XI"),
    ICD10Code("K86.9", "Disease of pancreas, unspecified", 
              "Bệnh tụy, không xác định", "GI", "Chapter XI"),
    
    # === SKIN DISORDERS ===
    ICD10Code("L50.9", "Urticaria, unspecified", 
              "Mề đay, không xác định", "Dermatology", "Chapter XII"),
    ICD10Code("L70.9", "Acne, unspecified", 
              "Mụn trứng cá, không xác định", "Dermatology", "Chapter XII"),
    
    # === MUSCULOSKELETAL ===
    ICD10Code("M79.3", "Panniculitis, unspecified", 
              "Viêm mô mỡ dưới da, không xác định", "Rheumatology", "Chapter XIII"),
    ICD10Code("M25.561", "Pain in right knee", 
              "Đau gối phải", "Rheumatology", "Chapter XIII"),
    ICD10Code("M25.562", "Pain in left knee", 
              "Đau gối trái", "Rheumatology", "Chapter XIII"),
    ICD10Code("M54.5", "Low back pain", 
              "Đau thắt lưng", "Rheumatology", "Chapter XIII"),
    ICD10Code("M54.9", "Dorsalgia, unspecified", 
              "Đau lưng, không xác định", "Rheumatology", "Chapter XIII"),
    
    # === GENITOURINARY ===
    ICD10Code("N18.6", "End stage renal disease", 
              "Bệnh thận giai đoạn cuối", "Nephrology", "Chapter XIV"),
    ICD10Code("N18.9", "Chronic kidney disease, unspecified", 
              "Bệnh thận mạn tính, không xác định", "Nephrology", "Chapter XIV"),
    ICD10Code("N19", "Unspecified kidney failure", 
              "Suy thận, không xác định", "Nephrology", "Chapter XIV"),
    ICD10Code("N17.9", "Acute kidney failure, unspecified", 
              "Suy thận cấp, không xác định", "Nephrology", "Chapter XIV"),
    ICD10Code("N39.0", "Urinary tract infection, site not specified", 
              "Nhiễm trùng đường tiết niệu, vị trí không xác định", "Nephrology", "Chapter XIV"),
    ICD10Code("N40.1", "Benign prostatic hyperplasia with lower urinary tract symptoms", 
              "Tăng sản tuyến tiền liệt lành tính với triệu chứng đường tiết niệu dưới", "Urology", "Chapter XIV"),
    
    # === PREGNANCY ===
    ICD10Code("O80", "Encounter for full-term uncomplicated delivery", 
              "Gặp gỡ để sinh đủ tháng không biến chứng", "Obstetrics", "Chapter XV"),
    ICD10Code("O36.4", "Maternal care for intrauterine death", 
              "Chăm sóc mẹ cho thai chết lưu", "Obstetrics", "Chapter XV"),
    
    # === PERINATAL ===
    ICD10Code("P07.10", "Low birth weight, unspecified, 1000-2499 grams", 
              "Cân nặng sơ sinh thấp, không xác định, 1000-2499 gram", "Pediatrics", "Chapter XVI"),
    ICD10Code("P07.14", "Extremely low birth weight, less than 1000 grams", 
              "Cân nặng sơ sinh cực thấp, dưới 1000 gram", "Pediatrics", "Chapter XVI"),
    
    # === CONGENITAL MALFORMATIONS ===
    ICD10Code("Q21.1", "Atrial septal defect", 
              "Thông liên nhĩ", "Cardiology", "Chapter XVII"),
    ICD10Code("Q21.0", "Ventricular septal defect", 
              "Thông liên thất", "Cardiology", "Chapter XVII"),
    
    # === SYMPTOMS ===
    ICD10Code("R05.9", "Cough, unspecified", 
              "Ho, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R06.02", "Shortness of breath", 
              "Khó thở", "General", "Chapter XVIII"),
    ICD10Code("R50.9", "Fever, unspecified", 
              "Sốt, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R51.9", "Headache, unspecified", 
              "Đau đầu, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R10.9", "Unspecified abdominal pain", 
              "Đau bụng, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R11.0", "Nausea", 
              "Buồn nôn", "General", "Chapter XVIII"),
    ICD10Code("R11.2", "Nausea with vomiting, unspecified", 
              "Buồn nôn với nôn, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R53.83", "Other fatigue", 
              "Mệt mỏi khác", "General", "Chapter XVIII"),
    ICD10Code("R06.00", "Dyspnea, unspecified", 
              "Khó thở, không xác định", "General", "Chapter XVIII"),
    ICD10Code("R06.02", "Shortness of breath", 
              "Khó thở", "General", "Chapter XVIII"),
    ICD10Code("R06.09", "Other forms of dyspnea", 
              "Các dạng khó thở khác", "General", "Chapter XVIII"),
    ICD10Code("R55", "Syncope and collapse", 
              "Ngất và sụp đổ", "General", "Chapter XVIII"),
    ICD10Code("R94.31", "Abnormal electrocardiogram [ECG] [EKG]", 
              "Điện tâm đồ bất thường", "General", "Chapter XVIII"),
    
    # === INJURY ===
    ICD10Code("S72.9", "Unspecified fracture of femur", 
              "Gãy xương đùi, không xác định", "Trauma", "Chapter XIX"),
    ICD10Code("S42.9", "Unspecified fracture of shoulder and upper arm", 
              "Gãy xương vai và cánh tay trên, không xác định", "Trauma", "Chapter XIX"),
    ICD10Code("S06.9", "Unspecified intracranial injury", 
              "Chấn thương nội sọ, không xác định", "Trauma", "Chapter XIX"),
    
    # === EXTERNAL CAUSES ===
    ICD10Code("V89.9", "Person injured in unspecified motor-vehicle accident, traffic", 
              "Người bị thương trong tai nạn xe cơ giới không xác định, giao thông", "Trauma", "Chapter XX"),
    ICD10Code("W19.XXXA", "Unspecified fall, initial encounter", 
              "Ngã không xác định, lần gặp đầu tiên", "Trauma", "Chapter XX"),
    
    # === FACTORS INFLUENCING HEALTH ===
    ICD10Code("Z51.11", "Encounter for antineoplastic chemotherapy", 
              "Gặp gỡ để hóa trị liệu chống ung thư", "General", "Chapter XXI"),
    ICD10Code("Z95.1", "Presence of aortocoronary bypass graft", 
              "Có cầu nối động mạch vành chủ", "General", "Chapter XXI"),
    ICD10Code("Z87.891", "Personal history of nicotine dependence", 
              "Tiền sử cá nhân phụ thuộc nicotine", "General", "Chapter XXI"),
    ICD10Code("Z79.84", "Long term (current) use of insulin", 
              "Sử dụng insulin dài hạn (hiện tại)", "General", "Chapter XXI"),
    ICD10Code("Z79.4", "Long term (current) use of insulin", 
              "Sử dụng insulin dài hạn (hiện tại)", "General", "Chapter XXI"),
    ICD10Code("Z79.84", "Long term (current) use of insulin", 
              "Sử dụng insulin dài hạn (hiện tại)", "General", "Chapter XXI"),
    ICD10Code("Z98.85", "Transplanted organ removal status", 
              "Tình trạng loại bỏ cơ quan cấy ghép", "General", "Chapter XXI"),
]

# Category mapping for easier filtering
CATEGORY_MAPPING = {
    "Infectious": ["A00", "A15", "A16", "A41", "B20", "B34"],
    "Oncology": ["C50", "C34", "C25", "C18", "C22", "C61"],
    "Hematology": ["D50", "D64", "D69", "D65"],
    "Endocrinology": ["E10", "E11", "E03", "E05", "E87"],
    "Psychiatry": ["F32", "F41", "F10", "F20"],
    "Neurology": ["G93", "G40", "I63", "I64", "G91"],
    "Ophthalmology": ["H54", "H25", "H40"],
    "ENT": ["H90", "H91"],
    "Cardiology": ["I10", "I11", "I12", "I13", "I20", "I21", "I25", "I50", "I48", "I49", "I26", "I80", "I82", "Q21"],
    "Respiratory": ["J18", "J15", "J12", "J44", "J45", "J96"],
    "GI": ["K25", "K26", "K29", "K59", "K92", "K74", "K70", "K76", "K85", "K86"],
    "Dermatology": ["L50", "L70"],
    "Rheumatology": ["M79", "M25", "M54"],
    "Nephrology": ["N18", "N19", "N17", "N39"],
    "Urology": ["N40"],
    "Obstetrics": ["O80", "O36"],
    "Pediatrics": ["P07"],
    "General": ["R05", "R06", "R50", "R51", "R10", "R11", "R53", "R55", "R94", "Z51", "Z95", "Z87", "Z79", "Z98"],
    "Trauma": ["S72", "S42", "S06", "V89", "W19"],
}


def get_all_codes() -> List[ICD10Code]:
    """Get all ICD-10 codes"""
    return ICD10_DATABASE


def get_codes_by_category(category: str) -> List[ICD10Code]:
    """Get ICD-10 codes by category"""
    if category not in CATEGORY_MAPPING:
        return []
    
    prefixes = CATEGORY_MAPPING[category]
    return [code for code in ICD10_DATABASE if any(code.code.startswith(prefix) for prefix in prefixes)]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    return sorted(list(CATEGORY_MAPPING.keys()))

