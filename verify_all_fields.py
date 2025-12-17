"""Script kiểm tra lại tất cả thuốc có đủ 14 fields Phase 1"""

from drugs.drug_database import DRUG_DATABASE
from check_all_14_fields import BASIC_FIELDS, OPTIONAL_FIELDS

def main():
    total = len(DRUG_DATABASE)
    
    # Kiểm tra fields cơ bản
    has_basic = []
    for name, data in DRUG_DATABASE.items():
        if all(f in data for f in BASIC_FIELDS):
            has_basic.append(name)
    
    # Kiểm tra đủ 14 fields
    has_all_14 = []
    missing_details = {}
    
    for name in has_basic:
        data = DRUG_DATABASE[name]
        missing = []
        
        # Kiểm tra các fields tùy chọn
        for field in OPTIONAL_FIELDS:
            if field not in data:
                missing.append(field)
            elif field == 'contraindications' and not isinstance(data.get(field), dict):
                missing.append(field)
        
        if not missing:
            has_all_14.append(name)
        else:
            missing_details[name] = missing
    
    # Thống kê từng field
    all_fields = BASIC_FIELDS + OPTIONAL_FIELDS
    field_stats = {}
    
    for field in all_fields:
        count = 0
        for name, data in DRUG_DATABASE.items():
            if field in data:
                if field == 'contraindications':
                    if isinstance(data[field], dict):
                        count += 1
                else:
                    count += 1
        field_stats[field] = count
    
    # In kết quả
    print("=" * 80)
    print("KIỂM TRA TOÀN BỘ - 14 FIELDS PHASE 1")
    print("=" * 80)
    print()
    
    print(f"📊 TỔNG QUAN:")
    print(f"   - Tổng số thuốc: {total}")
    print(f"   - Thuốc có đủ 6 fields cơ bản: {len(has_basic)}/{total} ({len(has_basic)*100//total}%)")
    print(f"   - Thuốc có đủ 14 fields: {len(has_all_14)}/{total} ({len(has_all_14)*100//total}%)")
    print()
    
    if missing_details:
        print(f"⚠️  Thuốc thiếu fields ({len(missing_details)}):")
        for name in sorted(list(missing_details.keys()))[:20]:
            print(f"   - {name}: {', '.join(missing_details[name])}")
        if len(missing_details) > 20:
            print(f"   ... và {len(missing_details) - 20} thuốc khác")
    else:
        print("✅ Tất cả thuốc đều có đủ 14 fields!")
    print()
    
    print("📋 CHI TIẾT TỪNG FIELD:")
    print()
    print("6 Fields cơ bản:")
    for field in BASIC_FIELDS:
        count = field_stats.get(field, 0)
        pct = count * 100 // total
        status = "✅" if count == total else "⚠️"
        print(f"   {status} {field}: {count}/{total} ({pct}%)")
    print()
    
    print("8 Fields tùy chọn:")
    for field in OPTIONAL_FIELDS:
        count = field_stats.get(field, 0)
        pct = count * 100 // total
        status = "✅" if count == total else "⚠️"
        print(f"   {status} {field}: {count}/{total} ({pct}%)")
    print()
    
    print("=" * 80)
    if len(has_all_14) == total:
        print("🎉 HOÀN HẢO: 100% thuốc có đủ 14 fields Phase 1!")
    else:
        print(f"⚠️  Còn {total - len(has_all_14)} thuốc chưa đủ 14 fields")
    print("=" * 80)

if __name__ == "__main__":
    main()

