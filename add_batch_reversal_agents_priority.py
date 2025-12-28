#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script bổ sung reversal_agents cho các thuốc ưu tiên (ICU/Emergency có antidote)
Batch Priority: 12 thuốc quan trọng nhất
"""

from drugs.drug_database import DRUG_DATABASE

# Chọn 12 thuốc quan trọng từ danh sách thiếu, ưu tiên có antidote
REVERSAL_AGENTS_DATA = {
    "Alteplase": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu cho alteplase. Xử trí: ngừng truyền ngay, hỗ trợ huyết động, truyền máu và các chế phẩm máu nếu chảy máu nặng. Có thể cân nhắc tranexamic acid hoặc aminocaproic acid trong trường hợp chảy máu đe dọa tính mạng (theo guideline chuyên ngành).",
        },
    },
    "Amikacin": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: ngừng thuốc ngay, điều trị hỗ trợ. Trong trường hợp quá liều nặng hoặc suy thận cấp, cân nhắc thẩm tách máu để loại bỏ thuốc. Theo dõi độc tính thận và tai (ototoxicity).",
        },
    },
    "Andexanet alfa": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Andexanet alfa",
                    "dose": "Liều bolus: 400-800mg IV, sau đó truyền liên tục 4-8mg/phút trong 120 phút (theo protocol cụ thể tùy thuốc và thời điểm liều cuối)",
                    "route": "IV",
                    "notes": "Thuốc giải độc chuyên biệt cho factor Xa inhibitors (rivaroxaban, apixaban). Chỉ dùng trong chảy máu nặng đe dọa tính mạng. Tuân thủ nghiêm ngặt protocol và guideline chuyên ngành.",
                }
            ],
            "notes": "Andexanet alfa là thuốc giải độc cho NOAC (rivaroxaban, apixaban). Chỉ sử dụng ở trung tâm có kinh nghiệm và theo protocol cụ thể.",
        },
    },
    "Idarucizumab": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Idarucizumab",
                    "dose": "5g IV (2 lọ x 2.5g), truyền nhanh trong 5-15 phút",
                    "route": "IV",
                    "notes": "Thuốc giải độc đặc hiệu cho dabigatran (direct thrombin inhibitor). Dùng trong chảy máu nặng đe dọa tính mạng hoặc cần phẫu thuật khẩn cấp. Tác dụng nhanh, hiệu quả trong vòng vài phút.",
                }
            ],
            "notes": "Idarucizumab là thuốc giải độc chuyên biệt cho dabigatran. Chỉ sử dụng trong trường hợp chảy máu nặng hoặc cần can thiệp phẫu thuật khẩn cấp.",
        },
    },
    "Propofol": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: ngừng truyền ngay, hỗ trợ hô hấp (thở máy nếu cần), hỗ trợ huyết động. Theo dõi sát dấu hiệu sinh tồn. Propofol có thời gian bán hủy ngắn, thường hồi phục nhanh sau khi ngừng truyền.",
        },
    },
    "Ketamine": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: ngừng truyền, hỗ trợ hô hấp nếu cần, điều trị hỗ trợ. Theo dõi tăng huyết áp, nhịp tim nhanh, và các tác dụng phụ tâm thần. Thời gian tác dụng ngắn, thường hồi phục nhanh.",
        },
    },
    "Dexmedetomidine": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: ngừng truyền, hỗ trợ huyết động nếu hạ huyết áp hoặc nhịp tim chậm. Có thể cân nhắc atropine cho nhịp tim chậm có triệu chứng. Thời gian bán hủy ngắn, thường hồi phục nhanh.",
        },
    },
    "Etomidate": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: ngừng truyền, hỗ trợ hô hấp và huyết động. Theo dõi chức năng thượng thận nếu dùng kéo dài (có thể gây ức chế thượng thận). Thời gian tác dụng ngắn.",
        },
    },
    "Rocuronium": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Sugammadex",
                    "dose": "2-4mg/kg IV (tùy mức độ block), có thể lên đến 16mg/kg trong trường hợp block sâu",
                    "route": "IV",
                    "notes": "Thuốc giải độc đặc hiệu cho aminosteroid neuromuscular blocking agents (rocuronium, vecuronium). Tác dụng nhanh, đảo ngược hoàn toàn block thần kinh cơ. Chống chỉ định ở bệnh nhân dị ứng với sugammadex hoặc cyclodextrin.",
                }
            ],
            "notes": "Sugammadex là thuốc giải độc đặc hiệu cho rocuronium và vecuronium. Hiệu quả cao, đảo ngược nhanh block thần kinh cơ.",
        },
    },
    "Vecuronium": {
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Sugammadex",
                    "dose": "2-4mg/kg IV (tùy mức độ block), có thể lên đến 16mg/kg trong trường hợp block sâu",
                    "route": "IV",
                    "notes": "Thuốc giải độc đặc hiệu cho aminosteroid neuromuscular blocking agents (rocuronium, vecuronium). Tác dụng nhanh, đảo ngược hoàn toàn block thần kinh cơ.",
                }
            ],
            "notes": "Sugammadex là thuốc giải độc đặc hiệu cho vecuronium và rocuronium.",
        },
    },
    "Succinylcholine": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Xử trí: hỗ trợ hô hấp (thở máy) cho đến khi block tự hồi phục. Thời gian tác dụng ngắn (5-10 phút) do bị phân hủy bởi pseudocholinesterase. Trong trường hợp block kéo dài (thiếu hụt pseudocholinesterase), cần thở máy kéo dài và theo dõi sát.",
        },
    },
    "Cisatracurium": {
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Có thể dùng neostigmine + atropine hoặc glycopyrrolate để đảo ngược block, nhưng cần đợi đến khi có dấu hiệu phục hồi tự nhiên (ít nhất 1-2 twitch trên TOF). Cisatracurium tự phân hủy qua cơ chế Hoffman elimination, không phụ thuộc chức năng gan/thận.",
        },
    },
}

def generate_code():
    """Tạo code để thêm vào enhanced_fields_overrides.py"""
    code = "\n# ======================== BATCH PRIORITY: REVERSAL_AGENTS ========================\n"
    code += "# Bổ sung reversal_agents cho 12 thuốc ưu tiên (ICU/Emergency có antidote)\n"
    code += "# Generated automatically by add_batch_reversal_agents_priority.py\n\n"
    code += "EXTRA_ENHANCED_FIELDS.update({\n"
    
    for drug_name, data in REVERSAL_AGENTS_DATA.items():
        code += f'    "{drug_name}": {{\n'
        code += '        "reversal_agents": {\n'
        code += f'            "available": {data["reversal_agents"]["available"]},\n'
        if data["reversal_agents"]["agents"]:
            code += '            "agents": [\n'
            for agent in data["reversal_agents"]["agents"]:
                code += '                {\n'
                code += f'                    "name": "{agent["name"]}",\n'
                code += f'                    "dose": "{agent["dose"]}",\n'
                code += f'                    "route": "{agent["route"]}",\n'
                code += f'                    "notes": "{agent["notes"]}",\n'
                code += '                },\n'
            code += '            ],\n'
        else:
            code += '            "agents": [],\n'
        code += f'            "notes": "{data["reversal_agents"]["notes"]}",\n'
        code += '        },\n'
        code += '    },\n'
    
    code += "})\n"
    code += "# ======================== END BATCH PRIORITY ========================\n"
    return code

if __name__ == '__main__':
    print("="*80)
    print("KIỂM TRA CÁC THUỐC TRONG DATABASE")
    print("="*80)
    for drug_name in REVERSAL_AGENTS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "reversal_agents" in DRUG_DATABASE[drug_name]
            status = "✅ Đã có" if has_field else "❌ THIẾU"
            print(f"  {status}: {drug_name}")
        else:
            print(f"  ⚠️  {drug_name}: Không tìm thấy trong database")
    
    print("\n" + "="*80)
    print("CODE ĐỂ THÊM VÀO enhanced_fields_overrides.py:")
    print("="*80)
    print(generate_code())

