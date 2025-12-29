"""
Data Backup Manager - Quản lý backup và restore dữ liệu
Đảm bảo an toàn dữ liệu, có thể khôi phục khi cần
"""

from typing import Dict, List, Optional
from pathlib import Path
import json
import shutil
from datetime import datetime
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# ============================================================================
# BACKUP FUNCTIONS - Chức năng backup
# ============================================================================

def create_backup(backup_dir: str = "drug_data_backups", include_overrides: bool = True) -> str:
    """
    Tạo backup dữ liệu thuốc
    
    Args:
        backup_dir: Thư mục lưu backup
        include_overrides: Có bao gồm enhanced_fields_overrides không
    
    Returns:
        Path to backup file
    """
    backup_path = Path(backup_dir)
    backup_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_path / f"drug_database_backup_{timestamp}.json"
    
    backup_data = {
        "timestamp": timestamp,
        "date": datetime.now().isoformat(),
        "total_drugs": len(DRUG_DATABASE),
        "drug_database": DRUG_DATABASE,
    }
    
    if include_overrides:
        backup_data["enhanced_fields_overrides"] = EXTRA_ENHANCED_FIELDS
    
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    
    return str(backup_file)

def list_backups(backup_dir: str = "drug_data_backups") -> List[Dict]:
    """Liệt kê các backup có sẵn"""
    backup_path = Path(backup_dir)
    
    if not backup_path.exists():
        return []
    
    backups = []
    for backup_file in backup_path.glob("drug_database_backup_*.json"):
        try:
            with open(backup_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                backups.append({
                    "file": str(backup_file),
                    "timestamp": data.get("timestamp", ""),
                    "date": data.get("date", ""),
                    "total_drugs": data.get("total_drugs", 0),
                })
        except:
            continue
    
    # Sort by timestamp (newest first)
    backups.sort(key=lambda x: x["timestamp"], reverse=True)
    return backups

def restore_backup(backup_file: str, dry_run: bool = True) -> Dict:
    """
    Khôi phục từ backup
    
    Args:
        backup_file: Path to backup file
        dry_run: True nếu chỉ xem preview, False nếu thực sự restore
    
    Returns:
        Dict với thông tin restore
    """
    with open(backup_file, 'r', encoding='utf-8') as f:
        backup_data = json.load(f)
    
    current_count = len(DRUG_DATABASE)
    backup_count = backup_data.get("total_drugs", 0)
    
    info = {
        "backup_file": backup_file,
        "backup_timestamp": backup_data.get("timestamp", ""),
        "backup_date": backup_data.get("date", ""),
        "current_drugs": current_count,
        "backup_drugs": backup_count,
        "difference": backup_count - current_count,
        "dry_run": dry_run,
    }
    
    if not dry_run:
        # Actually restore (this would need to write to files)
        info["note"] = "Restore thực sự cần được thực hiện thủ công bằng cách copy file"
    
    return info

# ============================================================================
# CHANGE TRACKING - Theo dõi thay đổi
# ============================================================================

def track_changes(drug_name: str, old_data: Dict, new_data: Dict) -> Dict:
    """
    Theo dõi thay đổi của một thuốc
    
    Returns:
        Dict với các thay đổi
    """
    changes = {
        "drug_name": drug_name,
        "timestamp": datetime.now().isoformat(),
        "added_fields": [],
        "removed_fields": [],
        "modified_fields": [],
    }
    
    old_keys = set(old_data.keys())
    new_keys = set(new_data.keys())
    
    # Added fields
    changes["added_fields"] = list(new_keys - old_keys)
    
    # Removed fields
    changes["removed_fields"] = list(old_keys - new_keys)
    
    # Modified fields
    common_keys = old_keys & new_keys
    for key in common_keys:
        if old_data[key] != new_data[key]:
            changes["modified_fields"].append({
                "field": key,
                "old_value": str(old_data[key])[:100],  # Truncate
                "new_value": str(new_data[key])[:100],
            })
    
    return changes

def save_change_log(changes: Dict, log_file: str = "drug_changes_log.json"):
    """Lưu log thay đổi"""
    log_path = Path(log_file)
    
    # Load existing log
    if log_path.exists():
        with open(log_path, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
    else:
        log_data = {"changes": []}
    
    # Add new change
    log_data["changes"].append(changes)
    
    # Keep only last 1000 changes
    if len(log_data["changes"]) > 1000:
        log_data["changes"] = log_data["changes"][-1000:]
    
    # Save
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

