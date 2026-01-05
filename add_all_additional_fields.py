"""
Script bổ sung tất cả field bổ sung cho các thuốc đã có đủ field chuẩn
"""
import sys
import json
from pathlib import Path
import io

# Setup path
sys.path.insert(0, str(Path.cwd()))

from add_fields_helper import add_additional_fields
from drugs.drug_database import DRUG_DATABASE
from drugs.drug_manager_tool import get_drug_manager
from drugs.field_validator import get_field_validator

# Setup encoding
if sys.platform == 'win32' and not isinstance(sys.stdout, io.TextIOWrapper):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass

def find_drugs_needing_additional_fields():
    """Tìm các thuốc cần bổ sung field bổ sung"""
    manager = get_drug_manager()
    validator = get_field_validator()
    
    drugs_to_update = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        result = validator.validate_all_fields(drug_data)
        
        # Chỉ xử lý thuốc đã có đủ 14 field chuẩn
        if len(result.get('missing_standard_fields', [])) == 0:
            missing_additional = result.get('missing_additional_fields', [])
            if missing_additional:
                files = manager.find_drug_file(drug_name)
                if files:
                    drugs_to_update.append({
                        'name': drug_name,
                        'file': files[0],
                        'missing': missing_additional
                    })
    
    return drugs_to_update

def main():
    drugs = find_drugs_needing_additional_fields()
    
    print("="*60)
    print(f"TIM THAY {len(drugs)} THUOC CAN BO SUNG FIELD BO SUNG")
    print("="*60)
    
    if len(drugs) == 0:
        print("Khong co thuoc nao can bo sung!")
        return
    
    # Bổ sung field bổ sung
    success_count = 0
    failed_count = 0
    
    for i, drug_info in enumerate(drugs, 1):
        drug_name = drug_info['name']
        file_path = drug_info['file']
        missing = drug_info['missing']
        
        print(f"\n[{i}/{len(drugs)}] {drug_name}")
        print(f"  File: {file_path}")
        print(f"  Thieu {len(missing)} field: {', '.join(missing[:3])}")
        if len(missing) > 3:
            print(f"  ... va {len(missing) - 3} field khac")
        
        try:
            result = add_additional_fields(drug_name, file_path, dry_run=False)
            if result['success'] and result.get('added_fields'):
                success_count += 1
                print(f"  ✓ Da bo sung {len(result['added_fields'])} field")
            else:
                failed_count += 1
                print(f"  - Khong bo sung duoc")
        except Exception as e:
            failed_count += 1
            print(f"  ✗ Loi: {e}")
    
    print("\n" + "="*60)
    print("KET QUA")
    print("="*60)
    print(f"Thanh cong: {success_count}")
    print(f"Loi/Bo qua: {failed_count}")
    print(f"Tong: {len(drugs)}")

if __name__ == "__main__":
    main()

