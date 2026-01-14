#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual Supplementation Helper
Script hỗ trợ bổ sung thủ công dữ liệu thuốc với CLI interactive
"""

import json
import sys
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import re

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import FieldValidator, STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import FieldValidator, STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS


class ManualSupplementationHelper:
    """Helper class cho bổ sung thủ công"""
    
    def __init__(self):
        self.workbook_file = Path(__file__).parent / "manual_supplementation_workbook.json"
        self.progress_file = Path(__file__).parent / "manual_supplementation_progress.json"
        self.workbook = self.load_workbook()
        self.progress = self.load_progress()
        self.validator = FieldValidator()
    
    def load_workbook(self) -> Dict[str, Any]:
        """Load workbook"""
        if not self.workbook_file.exists():
            print("⚠️  Chưa có workbook. Chạy create_manual_supplementation_template.py trước.")
            return {}
        
        with open(self.workbook_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_progress(self) -> Dict[str, Any]:
        """Load progress tracking"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_progress(self):
        """Lưu progress"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=2)
    
    def get_pending_drugs(self, priority: Optional[str] = None) -> List[str]:
        """Lấy danh sách thuốc chưa hoàn thành"""
        pending = []
        
        templates = self.workbook.get("templates", {})
        for drug_name, template in templates.items():
            status = template.get("status", "pending")
            template_priority = template.get("priority", "P3")
            
            if status in ["pending", "in_progress"]:
                if priority is None or template_priority == priority:
                    pending.append(drug_name)
        
        return sorted(pending)
    
    def get_drug_template(self, drug_name: str) -> Optional[Dict[str, Any]]:
        """Lấy template của một thuốc"""
        templates = self.workbook.get("templates", {})
        return templates.get(drug_name)
    
    def update_drug_status(self, drug_name: str, status: str):
        """Cập nhật trạng thái thuốc"""
        template = self.get_drug_template(drug_name)
        if template:
            template["status"] = status
            template["last_updated"] = datetime.now().isoformat()
            
            # Update progress
            if drug_name not in self.progress:
                self.progress[drug_name] = {}
            
            self.progress[drug_name]["status"] = status
            self.progress[drug_name]["last_updated"] = datetime.now().isoformat()
            
            self.save_workbook()
            self.save_progress()
    
    def mark_field_completed(self, drug_name: str, field: str, data: Any, sources: List[str]):
        """Đánh dấu field đã hoàn thành"""
        template = self.get_drug_template(drug_name)
        if not template:
            return False
        
        # Update template
        if "supplementation_data" not in template:
            template["supplementation_data"] = {}
        
        template["supplementation_data"][field] = data
        
        if field not in template["fields_completed"]:
            template["fields_completed"].append(field)
        
        if field in template["fields_to_supplement"]:
            template["fields_to_supplement"].remove(field)
        
        # Update sources
        for source in sources:
            if source not in template["sources_checked"]:
                template["sources_checked"].append(source)
        
        template["last_updated"] = datetime.now().isoformat()
        
        # Update progress
        if drug_name not in self.progress:
            self.progress[drug_name] = {
                "fields_to_supplement": [],
                "fields_completed": [],
                "fields_skipped": [],
                "sources_checked": []
            }
        
        if field not in self.progress[drug_name]["fields_completed"]:
            self.progress[drug_name]["fields_completed"].append(field)
        
        for source in sources:
            if source not in self.progress[drug_name]["sources_checked"]:
                self.progress[drug_name]["sources_checked"].append(source)
        
        self.save_workbook()
        self.save_progress()
        return True
    
    def mark_field_skipped(self, drug_name: str, field: str, reason: str):
        """Đánh dấu field đã bỏ qua"""
        template = self.get_drug_template(drug_name)
        if not template:
            return False
        
        if field not in template["fields_skipped"]:
            template["fields_skipped"].append(field)
        
        if field in template["fields_to_supplement"]:
            template["fields_to_supplement"].remove(field)
        
        template["notes"] = f"{template.get('notes', '')}\nBỏ qua {field}: {reason}".strip()
        template["last_updated"] = datetime.now().isoformat()
        
        # Update progress
        if drug_name not in self.progress:
            self.progress[drug_name] = {
                "fields_to_supplement": [],
                "fields_completed": [],
                "fields_skipped": [],
                "sources_checked": []
            }
        
        if field not in self.progress[drug_name]["fields_skipped"]:
            self.progress[drug_name]["fields_skipped"].append(field)
        
        self.save_workbook()
        self.save_progress()
        return True
    
    def save_workbook(self):
        """Lưu workbook"""
        with open(self.workbook_file, 'w', encoding='utf-8') as f:
            json.dump(self.workbook, f, ensure_ascii=False, indent=2)
    
    def validate_field_data(self, field: str, data: Any) -> Tuple[bool, Optional[str]]:
        """Validate dữ liệu field"""
        return self.validator.validate_field_type({"temp": data}, "temp")
    
    def find_drug_module_file(self, drug_name: str) -> Optional[Path]:
        """Tìm file module chứa thuốc"""
        drug_data = DRUG_DATABASE.get(drug_name, {})
        if not isinstance(drug_data, dict):
            return None
        
        group = drug_data.get("group", "")
        
        # Map group to module file
        module_mapping = {
            "Cardiovascular": "cardiovascular",
            "Diabetes": "diabetes",
            "Gastrointestinal": "gastrointestinal",
            "Analgesics": "analgesics",
            "Respiratory": "respiratory",
            "Neurological": "neurological",
            "Hematology": "hematology",
            "Supportive": "supportive",
            "Antimicrobial": "antimicrobial",
            "Metabolic": "metabolic",
            "Endocrinology": "endocrinology",
            "Oncology": "oncology",
            "Emergency": "emergency",
            "Urology": "urology",
            "Dermatology": "dermatology",
            "Ophthalmology": "ophthalmology",
            "Obstetrics": "obstetrics_gynecology",
            "ENT": "ent_oral_nasal_combinations",
            "Miscellaneous": "miscellaneous",
            "Anesthesia": "anesthesia",
            "Vaccines": "vaccines",
            "Toxicology": "toxicology",
            "Allergy": "allergy",
            "Nutrition": "nutrition",
            "Rheumatology": "rheumatology",
            "Immunology": "immunology"
        }
        
        # Try to find module
        modules_dir = Path(__file__).parent / "drug_modules"
        
        for key, module_name in module_mapping.items():
            if key.lower() in group.lower():
                module_file = modules_dir / f"{module_name}.py"
                if module_file.exists():
                    return module_file
        
        # Try to find in subdirectories
        for subdir in modules_dir.iterdir():
            if subdir.is_dir():
                module_file = subdir / f"{subdir.name}.py"
                if module_file.exists():
                    # Check if drug is in this file
                    try:
                        with open(module_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                                return module_file
                    except:
                        pass
        
        return None
    
    def backup_module_file(self, module_file: Path) -> Path:
        """Tạo backup file module"""
        backup_dir = module_file.parent / ".backups"
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = backup_dir / f"{module_file.stem}_{timestamp}{module_file.suffix}"
        
        shutil.copy2(module_file, backup_file)
        return backup_file
    
    def show_drug_info(self, drug_name: str):
        """Hiển thị thông tin thuốc"""
        template = self.get_drug_template(drug_name)
        if not template:
            print(f"⚠️  Không tìm thấy template cho {drug_name}")
            return
        
        drug_data = DRUG_DATABASE.get(drug_name, {})
        
        print("\n" + "="*70)
        print(f"THÔNG TIN THUỐC: {drug_name}")
        print("="*70)
        print(f"Nhóm: {template.get('group', 'Unknown')}")
        print(f"Tên tiếng Việt: {template.get('vietnamese_name', 'N/A')}")
        print(f"Mức độ ưu tiên: {template.get('priority', 'P3')}")
        print(f"Trạng thái: {template.get('status', 'pending')}")
        print(f"\nField cần bổ sung: {', '.join(template.get('fields_to_supplement', []))}")
        print(f"Field đã hoàn thành: {', '.join(template.get('fields_completed', []))}")
        print(f"Field đã bỏ qua: {', '.join(template.get('fields_skipped', []))}")
        
        if template.get('sources_checked'):
            print(f"\nNguồn đã kiểm tra: {', '.join(template['sources_checked'])}")
        
        if template.get('notes'):
            print(f"\nGhi chú: {template['notes']}")
        
        print("="*70)
    
    def interactive_supplement(self, drug_name: str):
        """Interactive bổ sung cho một thuốc"""
        template = self.get_drug_template(drug_name)
        if not template:
            print(f"⚠️  Không tìm thấy template cho {drug_name}")
            return
        
        self.update_drug_status(drug_name, "in_progress")
        
        fields_to_supplement = template.get("fields_to_supplement", [])
        
        if not fields_to_supplement:
            print(f"✅ {drug_name} không còn field nào cần bổ sung")
            self.update_drug_status(drug_name, "completed")
            return
        
        print(f"\n{'='*70}")
        print(f"BỔ SUNG THỦ CÔNG: {drug_name}")
        print(f"{'='*70}")
        
        for field in fields_to_supplement:
            print(f"\n📋 Field: {field}")
            
            # Show guidelines
            guidelines = template.get("field_guidelines", {}).get(field, {})
            if guidelines:
                print(f"   Format: {guidelines.get('format', 'N/A')}")
                print(f"   Nguồn tham khảo: {', '.join(guidelines.get('sources', []))}")
                if guidelines.get('notes'):
                    print(f"   Ghi chú: {guidelines['notes']}")
            
            print("\nLựa chọn:")
            print("  1. Bổ sung dữ liệu")
            print("  2. Bỏ qua field này")
            print("  3. Xem thông tin hiện tại")
            print("  4. Bỏ qua thuốc này")
            
            choice = input("\nChọn (1-4): ").strip()
            
            if choice == "1":
                self.supplement_field_interactive(drug_name, field, template)
            elif choice == "2":
                reason = input("Lý do bỏ qua: ").strip()
                self.mark_field_skipped(drug_name, field, reason)
                print(f"✅ Đã đánh dấu bỏ qua {field}")
            elif choice == "3":
                current_data = template.get("current_data", {}).get(field)
                print(f"\nDữ liệu hiện tại: {current_data}")
                continue
            elif choice == "4":
                print(f"⚠️  Bỏ qua thuốc {drug_name}")
                break
            else:
                print("⚠️  Lựa chọn không hợp lệ")
        
        # Check if all fields are done
        remaining_fields = template.get("fields_to_supplement", [])
        if not remaining_fields:
            self.update_drug_status(drug_name, "completed")
            print(f"\n✅ Đã hoàn thành bổ sung cho {drug_name}")
        else:
            print(f"\n⚠️  Còn {len(remaining_fields)} field chưa bổ sung")
    
    def supplement_field_interactive(self, drug_name: str, field: str, template: Dict[str, Any]):
        """Interactive bổ sung một field"""
        print(f"\n{'='*50}")
        print(f"Bổ sung field: {field}")
        print(f"{'='*50}")
        
        # Get sources
        sources = []
        print("\nNhập nguồn tham khảo (Enter để kết thúc):")
        while True:
            source = input("  Nguồn: ").strip()
            if not source:
                break
            sources.append(source)
        
        if not sources:
            print("⚠️  Cần ít nhất một nguồn tham khảo")
            return
        
        # Get data based on field type
        guidelines = template.get("field_guidelines", {}).get(field, {})
        field_format = guidelines.get("format", "string")
        
        print(f"\nNhập dữ liệu (Format: {field_format}):")
        
        if field_format == "string":
            data = input("  Giá trị: ").strip()
            if not data:
                print("⚠️  Dữ liệu không được rỗng")
                return
        
        elif field_format == "list of strings":
            print("  Nhập từng dòng (Enter trống để kết thúc):")
            data = []
            while True:
                item = input("    - ").strip()
                if not item:
                    break
                data.append(item)
            
            if not data:
                print("⚠️  Cần ít nhất một phần tử")
                return
        
        elif field_format == "dict":
            print("  Nhập JSON (hoặc Enter để nhập từng key):")
            json_input = input("  JSON: ").strip()
            
            if json_input:
                try:
                    data = json.loads(json_input)
                except json.JSONDecodeError:
                    print("⚠️  JSON không hợp lệ")
                    return
            else:
                # Interactive dict input
                data = {}
                print("  Nhập từng key-value (Enter trống để kết thúc):")
                while True:
                    key = input("    Key: ").strip()
                    if not key:
                        break
                    value = input(f"    Value cho '{key}': ").strip()
                    data[key] = value
        
        else:
            print(f"⚠️  Format {field_format} chưa được hỗ trợ tự động")
            print("  Vui lòng nhập JSON:")
            json_input = input("  JSON: ").strip()
            try:
                data = json.loads(json_input)
            except json.JSONDecodeError:
                print("⚠️  JSON không hợp lệ")
                return
        
        # Validate
        is_valid, error = self.validate_field_data(field, data)
        if not is_valid:
            print(f"⚠️  Dữ liệu không hợp lệ: {error}")
            confirm = input("  Vẫn tiếp tục? (y/n): ").strip().lower()
            if confirm != 'y':
                return
        
        # Confirm
        print(f"\nDữ liệu sẽ được lưu:")
        print(f"  Field: {field}")
        print(f"  Data: {data}")
        print(f"  Sources: {', '.join(sources)}")
        
        confirm = input("\nXác nhận lưu? (y/n): ").strip().lower()
        if confirm != 'y':
            print("⚠️  Đã hủy")
            return
        
        # Save
        success = self.mark_field_completed(drug_name, field, data, sources)
        if success:
            print(f"✅ Đã lưu dữ liệu cho {field}")
        else:
            print(f"⚠️  Lỗi khi lưu dữ liệu")
    
    def show_progress_summary(self):
        """Hiển thị tổng kết tiến độ"""
        templates = self.workbook.get("templates", {})
        
        stats = {
            "total": len(templates),
            "pending": 0,
            "in_progress": 0,
            "completed": 0,
            "skipped": 0,
            "by_priority": {"P0": 0, "P1": 0, "P2": 0, "P3": 0}
        }
        
        for template in templates.values():
            status = template.get("status", "pending")
            priority = template.get("priority", "P3")
            
            stats[status] = stats.get(status, 0) + 1
            stats["by_priority"][priority] = stats["by_priority"].get(priority, 0) + 1
        
        print("\n" + "="*70)
        print("TỔNG KẾT TIẾN ĐỘ")
        print("="*70)
        print(f"Tổng số thuốc: {stats['total']}")
        print(f"  - Chưa làm: {stats['pending']}")
        print(f"  - Đang làm: {stats['in_progress']}")
        print(f"  - Hoàn thành: {stats['completed']}")
        print(f"  - Bỏ qua: {stats['skipped']}")
        print("\nTheo mức độ ưu tiên:")
        for priority in ["P0", "P1", "P2", "P3"]:
            count = stats["by_priority"].get(priority, 0)
            print(f"  {priority}: {count} thuốc")
        print("="*70)


def main():
    """Main CLI"""
    helper = ManualSupplementationHelper()
    
    if not helper.workbook:
        print("⚠️  Chưa có workbook. Chạy create_manual_supplementation_template.py trước.")
        return
    
    while True:
        print("\n" + "="*70)
        print("BỔ SUNG THỦ CÔNG DỮ LIỆU THUỐC")
        print("="*70)
        print("1. Xem danh sách thuốc cần bổ sung")
        print("2. Bổ sung một thuốc")
        print("3. Xem thông tin thuốc")
        print("4. Xem tổng kết tiến độ")
        print("5. Thoát")
        
        choice = input("\nChọn (1-5): ").strip()
        
        if choice == "1":
            priority = input("Lọc theo mức độ ưu tiên (P0/P1/P2/P3/Enter để xem tất cả): ").strip()
            priority = priority if priority else None
            
            pending = helper.get_pending_drugs(priority)
            
            if not pending:
                print("✅ Không còn thuốc nào cần bổ sung")
            else:
                print(f"\nDanh sách ({len(pending)} thuốc):")
                for i, drug_name in enumerate(pending, 1):
                    template = helper.get_drug_template(drug_name)
                    priority_level = template.get("priority", "P3") if template else "P3"
                    fields_count = len(template.get("fields_to_supplement", [])) if template else 0
                    print(f"  {i}. {drug_name} [{priority_level}] - {fields_count} field")
        
        elif choice == "2":
            drug_name = input("Tên thuốc: ").strip()
            if not drug_name:
                print("⚠️  Tên thuốc không được rỗng")
                continue
            
            if drug_name not in helper.workbook.get("templates", {}):
                print(f"⚠️  Không tìm thấy {drug_name}")
                continue
            
            helper.interactive_supplement(drug_name)
        
        elif choice == "3":
            drug_name = input("Tên thuốc: ").strip()
            if not drug_name:
                print("⚠️  Tên thuốc không được rỗng")
                continue
            
            helper.show_drug_info(drug_name)
        
        elif choice == "4":
            helper.show_progress_summary()
        
        elif choice == "5":
            print("👋 Tạm biệt!")
            break
        
        else:
            print("⚠️  Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
