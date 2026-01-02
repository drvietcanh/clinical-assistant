"""
Enhanced fields overrides - Neurological
"""
from typing import Any, Dict


NEUROLOGICAL_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
    # ======================== BATCH 4: GI & NEUROLOGICAL DRUGS ========================
        "Omeprazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với omeprazole hoặc PPI",
                ],
                "tương_đối": [
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                    "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                    "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                    "Nhiễm Clostridium difficile - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Pantoprazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với pantoprazole hoặc PPI",
                ],
                "tương_đối": [
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                    "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                    "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                    "Nhiễm Clostridium difficile - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Ranitidine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ranitidine hoặc H2 blocker",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <50) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Famotidine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với famotidine hoặc H2 blocker",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <50) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Paracetamol": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Được xem là an toàn để hạ sốt và giảm đau trong tất cả các giai đoạn của thai kỳ khi dùng ở liều điều trị. "
                    "Tuy nhiên, nên dùng liều thấp nhất có hiệu quả trong thời gian ngắn nhất."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Được Viện Nhi khoa Hoa Kỳ (AAP) xếp vào nhóm thuốc an toàn khi cho con bú.",
                    "recommendation": "Có thể sử dụng. Không cần ngừng cho con bú.",
                },
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với paracetamol",
                    "Suy gan nặng",
                    "Nghiện rượu nặng",
                ],
                "tương_đối": [
                    "Suy gan vừa - giảm liều tối đa",
                    "Suy thận nặng - thận trọng",
                    "Thiếu G6PD - thận trọng",
                    "Suy dinh dưỡng - tăng nguy cơ độc tính",
                ],
            },
        },

        "Ibuprofen": {
            "pregnancy_lactation": {
                "fda_category": "C (D trong 3 tháng cuối)",
                "pregnancy_details": (
                    "FDA Category C trong 6 tháng đầu; Category D trong 3 tháng cuối (nguy cơ đóng ống động mạch sớm, thiểu niệu thai nhi, "
                    "kéo dài thời gian chuyển dạ). KHÔNG DÙNG trong 3 tháng cuối thai kỳ."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết rất ít vào sữa mẹ (liều tương đối cho trẻ < 0.6%). AAP xếp vào nhóm an toàn.",
                    "recommendation": "Có thể sử dụng. Là lựa chọn NSAID ưu tiên cho phụ nữ cho con bú.",
                },
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ibuprofen hoặc NSAID",
                    "Tiền sử hen suyễn do aspirin/NSAID",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                    "Có thai (3 tháng cuối)",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan nặng - thận trọng",
                    "Suy tim vừa - thận trọng",
                    "Tăng huyết áp không kiểm soát",
                    "Đang dùng thuốc chống đông",
                    "Có thai (1-2 tháng đầu) - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Diclofenac": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với diclofenac hoặc NSAID",
                    "Tiền sử hen suyễn do aspirin/NSAID",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                    "Suy gan nặng",
                    "Suy thận nặng (CrCl <30)",
                    "Có thai (3 tháng cuối) - nguy cơ đóng ống động mạch sớm",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Suy thận vừa (CrCl 30-60) - thận trọng",
                    "Suy gan vừa - thận trọng",
                    "Suy tim vừa - thận trọng",
                    "Tăng huyết áp không kiểm soát",
                    "Đang dùng thuốc chống đông",
                    "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Carbamazepine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với carbamazepine",
                    "Block nhĩ thất độ 2-3",
                    "Suy gan nặng",
                    "Tiền sử tủy xương bị ức chế",
                    "Đang dùng MAO inhibitor",
                ],
                "tương_đối": [
                    "Suy gan vừa - thận trọng, theo dõi chức năng gan",
                    "Suy thận nặng - thận trọng",
                    "Bệnh tim mạch - tăng nguy cơ block AV",
                    "Bệnh nhân có tiền sử rối loạn tâm thần",
                    "Glaucoma góc đóng",
                    "Có thai - thận trọng, có thể gây dị tật",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nhạy cảm",
                ],
            },
        },

}
