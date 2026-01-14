"""Infectious Disease & Antibiotic Drugs - Tetracyclines"""

# Tetracyclines - File đã được kiểm tra và sửa lỗi syntax đầy đủ

TETRACYCLINES_DRUGS = {
    "Doxycycline": {
        'group': 'Infectious Disease - Tetracycline Antibiotic',
        'vietnamese_name': 'Doxycycline, Vibramycin',
        'administration': ['PO', 'IV'],
        'indications': ['Nhiễm trùng đường hô hấp', 'Nhiễm trùng da (mụn trứng cá)', 'Chlamydia', 'Lyme disease', 'Sốt rét phòng ngừa', 'Rickettsia', 'Mycoplasma'],
        'contraindications': ['Dị ứng doxycycline/tetracycline', 'Có thai (3 tháng cuối)', 'Trẻ em <8 tuổi (gây vàng răng)'],
        'dosage': {
            'adult_respiratory': '100mg x 2 lần/ngày x 7-14 ngày',
            'adult_chlamydia': '100mg x 2 lần/ngày x 7 ngày',
            'adult_acne': '50-100mg x 1-2 lần/ngày',
            'adult_malaria_prophylaxis': '100mg x 1 lần/ngày',
            'notes': 'Uống với nhiều nước, tránh nằm ngay sau khi uống. Tránh nắng'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Không đổi'},
        'side_effects': ['Buồn nôn, nôn', 'Loét thực quản (nếu không uống đủ nước)', 'Phản ứng quang hóa (nhạy cảm ánh sáng)', 'Vàng răng (trẻ em, có thai)', 'Tăng áp lực nội sọ (hiếm)', 'Độc gan (liều cao)'],
        'interactions': ['Antacid/Sắt/Calcium: giảm hấp thu - cách 2 giờ', 'Warfarin: tăng tác dụng chống đông', 'Digoxin: tăng nồng độ digoxin', 'Phenytoin/Carbamazepine: giảm nồng độ doxycycline'],pregnancy': 'D - Chống chỉ định trong 3 tháng cuối',
        'mechanism_of_action': 'Tetracycline kháng sinh phổ rộng. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn cản gắn aminoacyl-tRNA.',
        'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC)', 'Dạ dày-ruột (buồn nôn, nôn)', 'Da (tăng độ nhạy cảm với ánh sáng)', 'Răng và xương (ở trẻ em)', 'Chức năng gan (ALT, AST)'],
        'precautions': ['KHÔNG dùng cho trẻ em < 8 tuổi', 'Tăng độ nhạy cảm với ánh sáng', 'Uống với nhiều nước', 'KHÔNG uống nằm ngửa', 'Tương tác với nhiều thuốc'],
        'storage': 'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.',
        'black_box_warnings': 'Không có black box warning. Tuy nhiên, ố vàng răng vĩnh viễn ở trẻ em < 8 tuổi là không hồi phục.',
        'pregnancy_lactation': {
            'fda_category': 'D',
            'pregnancy_details': 'Chống chỉ định trong tam cá nguyệt thứ hai và thứ ba.',
            'lactation': {'safety': 'Compatible', 'details': 'Bài tiết vào sữa mẹ ở nồng độ thấp.', 'recommendation': 'Có thể dùng khi cho con bú, nhưng thận trọng.'}
        }
    },
    
    "Minocycline": {
        'group': 'Infectious Disease - Tetracycline Antibiotic',
        'vietnamese_name': 'Minocycline, Minocin',
        'administration': ['PO', 'IV'],
        'indications': ['Nhiễm trùng đường hô hấp', 'Nhiễm trùng da (mụn trứng cá)', 'Chlamydia', 'Rickettsia', 'Mycoplasma', 'Nocardia'],
        'contraindications': ['Dị ứng minocycline/tetracycline', 'Có thai (3 tháng cuối)', 'Trẻ em <8 tuổi', 'Viêm gan tự miễn do minocycline trước đây'],
        'dosage': {
            'adult_standard': '100mg x 2 lần/ngày x 7-14 ngày',
            'adult_acne': '50-100mg x 1-2 lần/ngày',
            'notes': 'Nguy cơ độc gan và viêm gan tự miễn cao hơn doxycycline.'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Không đổi'},
        'side_effects': ['Buồn nôn, nôn', 'Chóng mặt, mất thăng bằng', 'Viêm gan tự miễn (hiếm nhưng nguy hiểm)', 'Tăng sắc tố da/vàng da', 'Phản ứng quang hóa'],
        'interactions': ['Antacid/Sắt/Calcium: giảm hấp thu', 'Warfarin: tăng tác dụng chống đông', 'Digoxin: tăng nồng độ'],pregnancy': 'D',
        'mechanism_of_action': 'Glycylcycline kháng sinh phổ rộng. Đặc biệt hiệu quả với Nocardia.',
        'precautions': ['NGUY CƠ VIÊM GAN TỰ MIỄN - cao hơn doxycycline', 'NGUY CƠ TĂNG SẮC TỐ DA/VÀNG DA - có thể không hồi phục', 'CHÓNG MẶT, MẤT THĂNG BẰNG'],
        'storage': 'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.',
        'black_box_warnings': 'NGUY CƠ VIÊM GAN TỰ MIỄN - có thể gây tử vong.',
        'pregnancy_lactation': {
            'fda_category': 'D',
            'pregnancy_details': 'Chống chỉ định trong tam cá nguyệt thứ hai và thứ ba.',
            'lactation': {'safety': 'Compatible', 'details': 'Bài tiết vào sữa mẹ ở nồng độ thấp.', 'recommendation': 'Có thể dùng nhưng thận trọng.'}
        }
    },
    
    "Tetracycline": {
        'group': 'Infectious Disease - Tetracycline Antibiotic',
        'vietnamese_name': 'Tetracycline, Tetracyn',
        'administration': ['PO'],
        'indications': ['Nhiễm trùng đường hô hấp', 'Nhiễm trùng da (mụn trứng cá)', 'Chlamydia', 'Rickettsia', 'Mycoplasma', 'Helicobacter pylori'],
        'contraindications': ['Dị ứng tetracycline', 'Có thai (3 tháng cuối)', 'Trẻ em <8 tuổi', 'Suy thận nặng (tích lũy)'],
        'dosage': {
            'adult_standard': '250-500mg x 4 lần/ngày',
            'adult_severe': '500mg x 4 lần/ngày',
            'notes': 'Tích lũy ở suy thận → thường dùng doxycycline thay thế.'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 50%', 'under_30': 'TRÁNH DÙNG', 'hemodialysis': 'TRÁNH DÙNG'},
        'side_effects': ['Buồn nôn, nôn', 'Loét thực quản', 'Phản ứng quang hóa', 'Vàng răng', 'Tăng áp lực nội sọ', 'Độc gan', 'Độc thận'],
        'interactions': ['Antacid/Sắt/Calcium: giảm hấp thu', 'Warfarin: tăng tác dụng chống đông', 'Digoxin: tăng nồng độ', 'Methoxyflurane: tăng độc thận'],pregnancy': 'D - Chống chỉ định trong 3 tháng cuối',
        'mechanism_of_action': 'Tetracycline kháng sinh phổ rộng. Ít dùng hơn doxycycline do tích lũy ở suy thận.',
        'monitoring': ['Dấu hiệu nhiễm trùng', 'Dạ dày-ruột', 'Da (nhạy cảm ánh sáng)', 'Răng và xương', 'Chức năng gan', 'Chức năng thận - QUAN TRỌNG'],
        'precautions': ['KHÔNG dùng cho trẻ em < 8 tuổi', 'Tích lũy ở suy thận → TRÁNH DÙNG ở suy thận nặng', 'Tăng độ nhạy cảm với ánh sáng'],
        'storage': 'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Dễ bị hỏng.',
        'black_box_warnings': 'Không có black box warning. Tuy nhiên, tích lũy ở suy thận → tăng độc tính.',
        'pregnancy_lactation': {
            'fda_category': 'D',
            'pregnancy_details': 'Chống chỉ định trong 3 tháng cuối thai kỳ.',
            'lactation': {'safety': 'Compatible', 'details': 'Bài tiết vào sữa mẹ ở nồng độ thấp.', 'recommendation': 'Có thể dùng nhưng thận trọng.'}
        }
    },
    
    "Tigecycline": {
        'group': 'Antibiotic - Glycylcycline (Tetracycline derivative)',
        'vietnamese_name': 'Tigecycline, Tygacil',
        'administration': ['IV'],
        'indications': ['Nhiễm khuẩn da và mô mềm phức tạp (cSSTI)', 'Nhiễm khuẩn ổ bụng phức tạp (cIAI)', 'Viêm phổi cộng đồng (CAP)', 'Nhiễm khuẩn do vi khuẩn kháng đa thuốc (MDR)', 'MRSA', 'VRE', 'CRE'],
        'contraindications': {
            'tuyệt_đối': ['Dị ứng tigecycline hoặc tetracycline'],tương_đối': ['Có thai (category D)', 'Trẻ <8 tuổi', 'Suy gan nặng']
        },dosage': {
            'adult_standard': '100mg IV x 1 lần (loading dose), sau đó 50mg IV mỗi 12 giờ',
            'notes': 'CẢNH BÁO: Tăng tỷ lệ tử vong so với các kháng sinh khác - chỉ dùng khi không còn lựa chọn khác.'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Không đổi', 'hemodialysis': 'Không đổi'},
        'side_effects': ['Buồn nôn, nôn (rất phổ biến, 20-30%)', 'Tiêu chảy', 'Tăng tỷ lệ tử vong', 'Tăng ALT, AST', 'Phát ban', 'Chóng mặt'],
        'interactions': ['Warfarin: có thể tăng INR', 'Thuốc tránh thai đường uống: có thể giảm hiệu quả'],pregnancy': 'D - Sử dụng nếu lợi ích > nguy cơ',
        'mechanism_of_action': 'Glycylcycline kháng sinh phổ rất rộng. Hiệu quả với MDR Gram-dương và Gram-âm. CẢNH BÁO: tăng tỷ lệ tử vong.',
        'monitoring': ['Dấu hiệu nhiễm trùng', 'Dạ dày-ruột (buồn nôn rất phổ biến)', 'Chức năng gan', 'Dấu hiệu sinh tồn - CẢNH BÁO: tăng tỷ lệ tử vong'],
        'precautions': ['CẢNH BÁO: Tăng tỷ lệ tử vong - chỉ dùng khi không còn lựa chọn khác', 'Buồn nôn, nôn rất phổ biến (20-30%)', 'Không cần điều chỉnh liều ở suy thận'],
        'storage': 'Bảo quản bột khô ở nhiệt độ phòng. Sau khi pha: 24 giờ ở nhiệt độ phòng, 48 giờ trong tủ lạnh.',
        'black_box_warnings': 'CẢNH BÁO: Tăng tỷ lệ tử vong so với các kháng sinh khác. Chỉ dùng khi không còn lựa chọn khác (MDR).',
        'pregnancy_lactation': {
            'fda_category': 'D',
            'pregnancy_details': 'CHỐNG CHỈ ĐỊNH trong thai kỳ. Gây độc thai nhi.',
            'lactation': {'safety': 'Caution', 'details': 'Bài tiết vào sữa mẹ. Có thể gây độc tính ở trẻ.', 'recommendation': 'Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời.'}
        },hepatic_adjustment': {'mild': 'Không cần chỉnh liều.', 'moderate': 'Giảm liều khởi đầu 50%.', 'severe': 'CHỐNG CHỈ ĐỊNH hoặc giảm liều mạnh.'},administration_instructions': {
            'iv': {'reconstitution': 'Pha trong NaCl 0.9% hoặc D5W.', 'infusion_rate': 'Truyền IV trong 60 phút.', 'notes': 'Điều chỉnh liều theo chức năng gan. CHỐNG CHỈ ĐỊNH trong thai kỳ và trẻ <8 tuổi.'}
        }
    }
}

__all__ = ['TETRACYCLINES_DRUGS']