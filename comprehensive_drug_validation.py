#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kiểm tra sâu toàn bộ dữ liệu các thuốc
- Kiểm tra các field có đầy đủ chưa
- Kiểm tra toàn bộ lỗi
- Báo cáo chi tiết
"""

import json
from typing import Dict, List, Any, Tuple
from collections import defaultdict

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    print("❌ Lỗi: Không thể import DRUG_DATABASE")
    exit(1)

# 14 enhanced fields
ENHANCED_FIELDS = [
    "mechanism_of_action",
    "monitoring",
    "precautions",
    "pharmacokinetics",
    "storage",
    "black_box_warnings",
    "drug_interactions",
    "contraindications_detail",
    "pregnancy_lactation",
    "hepatic_adjustment",
    "renal_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions"
]

# Các field cơ bản bắt buộc
REQUIRED_BASIC_FIELDS = [
    "group",
    "vietnamese_name",
    "administration",
    "indications",
    "contraindications",
    "dosage",
    "side_effects",
    "interactions",
    "pregnancy"
]

# Các field tùy chọn nhưng quan trọng
OPTIONAL_IMPORTANT_FIELDS = [
    "risk_flags",
    "guideline_tags",
    "pediatric_dosing",
    "geriatric_dosing",
    "notes"
]


class DrugValidator:
    """Class để kiểm tra và validate dữ liệu thuốc"""
    
    def __init__(self):
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.stats = {
            "total_drugs": 0,
            "complete_drugs": 0,
            "incomplete_drugs": 0,
            "field_stats": defaultdict(int),
            "error_count": 0,
            "warning_count": 0
        }
    
    def is_field_empty(self, value: Any) -> bool:
        """Kiểm tra field có rỗng không - Tối ưu tốc độ"""
        if value is None:
            return True
        # Tối ưu: isinstance check theo thứ tự phổ biến nhất
        if isinstance(value, str):
            return not value.strip()
        # Tối ưu: check length trực tiếp thay vì isinstance riêng
        try:
            return len(value) == 0
        except TypeError:
            # Không phải container type
            return False
    
    def validate_basic_fields(self, drug_name: str, drug_data: Dict) -> List[str]:
        """Kiểm tra các field cơ bản bắt buộc"""
        if drug_data is None or not isinstance(drug_data, dict):
            return REQUIRED_BASIC_FIELDS.copy()
        
        missing = []
        for field in REQUIRED_BASIC_FIELDS:
            if field not in drug_data:
                missing.append(field)
                self.errors[drug_name].append(f"❌ Thiếu field bắt buộc: {field}")
                self.stats["error_count"] += 1
            elif self.is_field_empty(drug_data[field]):
                missing.append(field)
                self.errors[drug_name].append(f"⚠️  Field rỗng: {field}")
                self.stats["error_count"] += 1
        return missing
    
    def validate_enhanced_fields(self, drug_name: str, drug_data: Dict) -> Tuple[List[str], int]:
        """Kiểm tra các enhanced fields - Tối ưu tốc độ"""
        missing = []
        complete_count = 0
        
        if drug_data is None or not isinstance(drug_data, dict):
            return ENHANCED_FIELDS.copy(), 0
        
        # Tối ưu: sử dụng .get() thay vì 'in' check + access
        for field in ENHANCED_FIELDS:
            value = drug_data.get(field)
            if value is None or self.is_field_empty(value):
                missing.append(field)
                if value is None:
                    self.warnings[drug_name].append(f"⚠️  Thiếu enhanced field: {field}")
                else:
                    self.warnings[drug_name].append(f"⚠️  Enhanced field rỗng: {field}")
                self.stats["warning_count"] += 1
            else:
                complete_count += 1
                self.stats["field_stats"][field] += 1
        
        return missing, complete_count
    
    def validate_data_types(self, drug_name: str, drug_data: Dict):
        """Kiểm tra kiểu dữ liệu của các field - Tối ưu tốc độ"""
        if drug_data is None or not isinstance(drug_data, dict):
            return
        
        # Cache type_checks để tránh tạo lại mỗi lần (move to __init__ nếu cần)
        type_checks = {
            "group": str,
            "vietnamese_name": str,
            "administration": list,
            "indications": list,
            "contraindications": (list, dict),
            "dosage": dict,
            "side_effects": list,
            "interactions": list,
            "pregnancy": str,
            "risk_flags": dict,
            "guideline_tags": list,
            "monitoring": list,
            "precautions": list,
            "storage": str,
            "black_box_warnings": (str, type(None)),  # Có thể là None
        }
        
        # Tối ưu: sử dụng .get() và chỉ check khi value không None
        for field, expected_type in type_checks.items():
            value = drug_data.get(field)
            if value is not None:
                if isinstance(expected_type, tuple):
                    if not isinstance(value, expected_type):
                        self.errors[drug_name].append(
                            f"❌ Kiểu dữ liệu sai: {field} (mong đợi {[t.__name__ if hasattr(t, '__name__') else str(t) for t in expected_type]}, nhận được {type(value).__name__})"
                        )
                        self.stats["error_count"] += 1
                elif not isinstance(value, expected_type):
                    self.errors[drug_name].append(
                        f"❌ Kiểu dữ liệu sai: {field} (mong đợi {expected_type.__name__}, nhận được {type(value).__name__})"
                    )
                    self.stats["error_count"] += 1
    
    def validate_dosage_structure(self, drug_name: str, dosage: Any):
        """Kiểm tra cấu trúc của dosage"""
        if not isinstance(dosage, dict):
            self.errors[drug_name].append("❌ Dosage phải là dictionary")
            self.stats["error_count"] += 1
            return
        
        if len(dosage) == 0:
            self.errors[drug_name].append("❌ Dosage rỗng")
            self.stats["error_count"] += 1
    
    def validate_risk_flags(self, drug_name: str, risk_flags: Any):
        """Kiểm tra cấu trúc risk_flags"""
        if not isinstance(risk_flags, dict):
            self.errors[drug_name].append("❌ risk_flags phải là dictionary")
            self.stats["error_count"] += 1
            return
        
        expected_keys = ["high_alert", "narrow_therapeutic_index", "icu_critical_care_only"]
        for key in expected_keys:
            if key not in risk_flags:
                self.warnings[drug_name].append(f"⚠️  risk_flags thiếu key: {key}")
                self.stats["warning_count"] += 1
    
    def validate_drug_interactions(self, drug_name: str, interactions: Any):
        """Kiểm tra cấu trúc drug_interactions"""
        if interactions is None:
            return
        
        if isinstance(interactions, dict):
            expected_keys = ["major", "moderate", "minor"]
            for key in expected_keys:
                if key in interactions:
                    if not isinstance(interactions[key], list):
                        self.errors[drug_name].append(
                            f"❌ drug_interactions['{key}'] phải là list"
                        )
                        self.stats["error_count"] += 1
        elif isinstance(interactions, list):
            # Format cũ - list of strings
            pass
        else:
            self.errors[drug_name].append(
                "❌ drug_interactions phải là dict hoặc list"
            )
            self.stats["error_count"] += 1
    
    def validate_contraindications_detail(self, drug_name: str, contraindications: Any):
        """Kiểm tra cấu trúc contraindications_detail"""
        if contraindications is None:
            return
        
        if isinstance(contraindications, dict):
            expected_keys = ["tuyệt_đối", "tương_đối"]
            for key in expected_keys:
                if key in contraindications:
                    if not isinstance(contraindications[key], list):
                        self.errors[drug_name].append(
                            f"❌ contraindications_detail['{key}'] phải là list"
                        )
                        self.stats["error_count"] += 1
    
    def validate_pregnancy_lactation(self, drug_name: str, pregnancy_data: Any):
        """Kiểm tra cấu trúc pregnancy_lactation"""
        if pregnancy_data is None:
            return
        
        if not isinstance(pregnancy_data, dict):
            self.errors[drug_name].append("❌ pregnancy_lactation phải là dictionary")
            self.stats["error_count"] += 1
            return
        
        if "fda_category" not in pregnancy_data:
            self.warnings[drug_name].append("⚠️  pregnancy_lactation thiếu fda_category")
            self.stats["warning_count"] += 1
    
    def validate_hepatic_adjustment(self, drug_name: str, adjustment: Any):
        """Kiểm tra cấu trúc hepatic_adjustment"""
        if adjustment is None:
            return
        
        if not isinstance(adjustment, dict):
            self.errors[drug_name].append("❌ hepatic_adjustment phải là dictionary")
            self.stats["error_count"] += 1
            return
        
        expected_keys = ["mild", "moderate", "severe"]
        for key in expected_keys:
            if key not in adjustment:
                self.warnings[drug_name].append(
                    f"⚠️  hepatic_adjustment thiếu key: {key}"
                )
                self.stats["warning_count"] += 1
    
    def validate_renal_adjustment(self, drug_name: str, adjustment: Any):
        """Kiểm tra cấu trúc renal_adjustment"""
        if adjustment is None:
            return
        
        if not isinstance(adjustment, dict):
            self.errors[drug_name].append("❌ renal_adjustment phải là dictionary")
            self.stats["error_count"] += 1
            return
        
        expected_keys = ["normal", "30_60", "under_30"]
        for key in expected_keys:
            if key not in adjustment:
                self.warnings[drug_name].append(
                    f"⚠️  renal_adjustment thiếu key: {key}"
                )
                self.stats["warning_count"] += 1
    
    def validate_overdose_management(self, drug_name: str, overdose: Any):
        """Kiểm tra cấu trúc overdose_management"""
        if overdose is None:
            return
        
        if not isinstance(overdose, dict):
            self.errors[drug_name].append("❌ overdose_management phải là dictionary")
            self.stats["error_count"] += 1
            return
    
    def validate_administration_instructions(self, drug_name: str, instructions: Any):
        """Kiểm tra cấu trúc administration_instructions"""
        if instructions is None:
            return
        
        if not isinstance(instructions, dict):
            self.errors[drug_name].append(
                "❌ administration_instructions phải là dictionary"
            )
            self.stats["error_count"] += 1
    
    def validate_pharmacokinetics(self, drug_name: str, pk: Any):
        """Kiểm tra cấu trúc pharmacokinetics"""
        if pk is None:
            return
        
        if not isinstance(pk, dict):
            self.errors[drug_name].append("❌ pharmacokinetics phải là dictionary")
            self.stats["error_count"] += 1
    
    def validate_duplicate_names(self):
        """Kiểm tra tên thuốc trùng lặp"""
        name_counts = defaultdict(list)
        for drug_name in DRUG_DATABASE.keys():
            name_counts[drug_name.lower()].append(drug_name)
        
        duplicates = {k: v for k, v in name_counts.items() if len(v) > 1}
        if duplicates:
            for normalized_name, drug_names in duplicates.items():
                self.warnings["DUPLICATES"].append(
                    f"⚠️  Tên thuốc có thể trùng (case-insensitive): {', '.join(drug_names)}"
                )
                self.stats["warning_count"] += 1
    
    def validate_all(self) -> Dict:
        """Kiểm tra toàn bộ database"""
        print("=" * 100)
        print("KIỂM TRA SÂU TOÀN BỘ DỮ LIỆU THUỐC")
        print("=" * 100)
        print(f"\nTổng số thuốc: {len(DRUG_DATABASE)}")
        print("\nĐang kiểm tra...\n")
        
        self.stats["total_drugs"] = len(DRUG_DATABASE)
        
        # Kiểm tra duplicate names
        self.validate_duplicate_names()
        
        # Tối ưu: single pass với .get() thay vì 'in' checks
        for drug_name, drug_data in DRUG_DATABASE.items():
            if drug_data is None or not isinstance(drug_data, dict):
                continue
            
            # Kiểm tra field cơ bản
            missing_basic = self.validate_basic_fields(drug_name, drug_data)
            
            # Kiểm tra enhanced fields
            missing_enhanced, complete_count = self.validate_enhanced_fields(drug_name, drug_data)
            
            # Kiểm tra kiểu dữ liệu
            self.validate_data_types(drug_name, drug_data)
            
            # Kiểm tra cấu trúc các field phức tạp - tối ưu với .get()
            dosage = drug_data.get("dosage")
            if dosage is not None:
                self.validate_dosage_structure(drug_name, dosage)
            
            risk_flags = drug_data.get("risk_flags")
            if risk_flags is not None:
                self.validate_risk_flags(drug_name, risk_flags)
            
            drug_interactions = drug_data.get("drug_interactions")
            if drug_interactions is not None:
                self.validate_drug_interactions(drug_name, drug_interactions)
            
            contraindications_detail = drug_data.get("contraindications_detail")
            if contraindications_detail is not None:
                self.validate_contraindications_detail(drug_name, contraindications_detail)
            
            pregnancy_lactation = drug_data.get("pregnancy_lactation")
            if pregnancy_lactation is not None:
                self.validate_pregnancy_lactation(drug_name, pregnancy_lactation)
            
            hepatic_adjustment = drug_data.get("hepatic_adjustment")
            if hepatic_adjustment is not None:
                self.validate_hepatic_adjustment(drug_name, hepatic_adjustment)
            
            renal_adjustment = drug_data.get("renal_adjustment")
            if renal_adjustment is not None:
                self.validate_renal_adjustment(drug_name, renal_adjustment)
            
            overdose_management = drug_data.get("overdose_management")
            if overdose_management is not None:
                self.validate_overdose_management(drug_name, overdose_management)
            
            administration_instructions = drug_data.get("administration_instructions")
            if administration_instructions is not None:
                self.validate_administration_instructions(drug_name, administration_instructions)
            
            pharmacokinetics = drug_data.get("pharmacokinetics")
            if pharmacokinetics is not None:
                self.validate_pharmacokinetics(drug_name, pharmacokinetics)
            
            # Đếm thuốc hoàn chỉnh - tối ưu với not operator
            if not missing_basic and not missing_enhanced:
                self.stats["complete_drugs"] += 1
            else:
                self.stats["incomplete_drugs"] += 1
        
        return self.generate_report()
    
    def generate_report(self) -> Dict:
        """Tạo báo cáo chi tiết"""
        report = {
            "summary": self.stats.copy(),
            "errors_by_drug": dict(self.errors),
            "warnings_by_drug": dict(self.warnings),
            "field_completion": {},
            "drugs_with_errors": list(self.errors.keys()),
            "drugs_with_warnings": list(self.warnings.keys()),
        }
        
        # Tính phần trăm hoàn thành cho từng enhanced field
        for field in ENHANCED_FIELDS:
            count = self.stats["field_stats"][field]
            percentage = (count / self.stats["total_drugs"]) * 100 if self.stats["total_drugs"] > 0 else 0
            report["field_completion"][field] = {
                "count": count,
                "percentage": percentage,
                "missing": self.stats["total_drugs"] - count
            }
        
        return report
    
    def print_report(self, report: Dict):
        """In báo cáo ra console"""
        print("\n" + "=" * 100)
        print("BÁO CÁO TỔNG HỢP")
        print("=" * 100)
        
        stats = report["summary"]
        print(f"\n📊 THỐNG KÊ TỔNG QUAN:")
        print(f"   Tổng số thuốc: {stats['total_drugs']}")
        print(f"   ✅ Thuốc hoàn chỉnh: {stats['complete_drugs']} ({stats['complete_drugs']/stats['total_drugs']*100:.1f}%)")
        print(f"   ⚠️  Thuốc chưa hoàn chỉnh: {stats['incomplete_drugs']} ({stats['incomplete_drugs']/stats['total_drugs']*100:.1f}%)")
        print(f"   ❌ Tổng số lỗi: {stats['error_count']}")
        print(f"   ⚠️  Tổng số cảnh báo: {stats['warning_count']}")
        
        print(f"\n📋 HOÀN THÀNH CÁC ENHANCED FIELDS:")
        for field, data in report["field_completion"].items():
            status = "✅" if data["percentage"] == 100 else "⚠️ "
            print(f"   {status} {field:<35} | {data['count']:3d}/{stats['total_drugs']:3d} ({data['percentage']:5.1f}%) | Thiếu: {data['missing']:3d}")
        
        # Thuốc có lỗi
        if report["drugs_with_errors"]:
            print(f"\n❌ THUỐC CÓ LỖI ({len(report['drugs_with_errors'])}):")
            for drug in sorted(report["drugs_with_errors"])[:20]:  # Hiển thị 20 đầu tiên
                print(f"   - {drug}")
                for error in report["errors_by_drug"][drug][:3]:  # Hiển thị 3 lỗi đầu
                    print(f"     {error}")
                if len(report["errors_by_drug"][drug]) > 3:
                    print(f"     ... và {len(report['errors_by_drug'][drug]) - 3} lỗi khác")
            if len(report["drugs_with_errors"]) > 20:
                print(f"   ... và {len(report['drugs_with_errors']) - 20} thuốc khác")
        
        # Thuốc có cảnh báo
        if report["drugs_with_warnings"]:
            print(f"\n⚠️  THUỐC CÓ CẢNH BÁO ({len(report['drugs_with_warnings'])}):")
            warning_summary = defaultdict(int)
            for drug, warnings in report["warnings_by_drug"].items():
                for warning in warnings:
                    # Đếm loại cảnh báo
                    if "Thiếu enhanced field" in warning:
                        warning_summary["Thiếu enhanced field"] += 1
                    elif "Enhanced field rỗng" in warning:
                        warning_summary["Enhanced field rỗng"] += 1
                    elif "thiếu key" in warning:
                        warning_summary["Thiếu key trong dict"] += 1
                    else:
                        warning_summary["Khác"] += 1
            
            for warning_type, count in sorted(warning_summary.items(), key=lambda x: -x[1]):
                print(f"   - {warning_type}: {count}")
        
        # Hiển thị cảnh báo về duplicates nếu có
        if "DUPLICATES" in report["warnings_by_drug"]:
            print(f"\n⚠️  CẢNH BÁO TÊN TRÙNG LẶP:")
            for warning in report["warnings_by_drug"]["DUPLICATES"]:
                print(f"   {warning}")
        
        print("\n" + "=" * 100)
        print("KẾT THÚC BÁO CÁO")
        print("=" * 100)


def main():
    """Hàm chính"""
    try:
        validator = DrugValidator()
        report = validator.validate_all()
        validator.print_report(report)
        
        # Lưu báo cáo vào file JSON
        output_file = "drug_validation_report.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Báo cáo đã được lưu vào: {output_file}")
        
        # Lưu báo cáo text
        output_text_file = "drug_validation_report.txt"
        with open(output_text_file, 'w', encoding='utf-8') as f:
            f.write("BÁO CÁO KIỂM TRA DỮ LIỆU THUỐC\n")
            f.write("=" * 100 + "\n\n")
            
            stats = report["summary"]
            f.write(f"Tổng số thuốc: {stats['total_drugs']}\n")
            f.write(f"Thuốc hoàn chỉnh: {stats['complete_drugs']}\n")
            f.write(f"Thuốc chưa hoàn chỉnh: {stats['incomplete_drugs']}\n")
            f.write(f"Tổng số lỗi: {stats['error_count']}\n")
            f.write(f"Tổng số cảnh báo: {stats['warning_count']}\n\n")
            
            f.write("HOÀN THÀNH CÁC ENHANCED FIELDS:\n")
            for field, data in report["field_completion"].items():
                f.write(f"  {field}: {data['count']}/{stats['total_drugs']} ({data['percentage']:.1f}%)\n")
            
            if report["drugs_with_errors"]:
                f.write(f"\nTHUỐC CÓ LỖI ({len(report['drugs_with_errors'])}):\n")
                for drug in sorted(report["drugs_with_errors"]):
                    f.write(f"\n  {drug}:\n")
                    for error in report["errors_by_drug"][drug]:
                        f.write(f"    {error}\n")
            
            if report["drugs_with_warnings"]:
                f.write(f"\nTHUỐC CÓ CẢNH BÁO ({len(report['drugs_with_warnings'])}):\n")
                for drug in sorted(report["drugs_with_warnings"])[:50]:  # 50 đầu tiên
                    f.write(f"\n  {drug}:\n")
                    for warning in report["warnings_by_drug"][drug][:5]:  # 5 cảnh báo đầu
                        f.write(f"    {warning}\n")
        
        print(f"💾 Báo cáo text đã được lưu vào: {output_text_file}")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

