"""
Auto commit and push script
Tìm git và thực hiện commit/push tự động
"""

import os
import subprocess
import sys
from pathlib import Path

# Tìm git executable
def find_git():
    """Tìm git executable trong các vị trí thông thường."""
    possible_paths = [
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe",
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files (x86)\Git\cmd\git.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\Git\bin\git.exe"),
        os.path.expanduser(r"~\AppData\Local\Programs\Git\cmd\git.exe"),
    ]
    
    # Thêm từ PATH
    for path_dir in os.environ.get("PATH", "").split(os.pathsep):
        git_path = os.path.join(path_dir, "git.exe")
        if os.path.exists(git_path):
            possible_paths.append(git_path)
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Thử tìm trong PATH bằng where
    try:
        result = subprocess.run(["where.exe", "git"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().split('\n')[0]
    except:
        pass
    
    return None


def run_git_command(git_path, *args, cwd=None):
    """Chạy git command."""
    try:
        cmd = [git_path] + list(args)
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def main():
    """Main function."""
    repo_path = Path(__file__).parent.parent
    os.chdir(repo_path)
    
    print(f"[INFO] Working directory: {repo_path}")
    
    # Tìm git
    git_path = find_git()
    if not git_path:
        print("[ERROR] Git not found!")
        print("\nPlease install Git or add it to PATH.")
        print("\nAlternatively, you can commit using Cursor/VS Code:")
        print("1. Press Ctrl+Shift+G (Source Control)")
        print("2. Stage all changes")
        print("3. Enter commit message")
        print("4. Click Commit and Push")
        return 1
    
    print(f"[OK] Found git at: {git_path}")
    
    # Check status
    print("\n[CHECK] Checking git status...")
    success, stdout, stderr = run_git_command(git_path, "status", "--porcelain", cwd=str(repo_path))
    if not success:
        print(f"[ERROR] Git status failed: {stderr}")
        return 1
    
    if not stdout.strip():
        print("[INFO] No changes to commit.")
        return 0
    
    print(f"[INFO] Changes detected:\n{stdout}")
    
    # Stage all
    print("\n[STAGE] Staging all changes...")
    success, stdout, stderr = run_git_command(git_path, "add", ".", cwd=str(repo_path))
    if not success:
        print(f"[ERROR] Git add failed: {stderr}")
        return 1
    print("[OK] All changes staged")
    
    # Commit
    print("\n[COMMIT] Committing...")
    commit_message = """Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system"""
    
    success, stdout, stderr = run_git_command(
        git_path, "commit", "-m", commit_message, cwd=str(repo_path)
    )
    if not success:
        print(f"[ERROR] Git commit failed: {stderr}")
        return 1
    print(f"[OK] Committed: {stdout.strip()}")
    
    # Push
    print("\n[PUSH] Pushing to remote...")
    success, stdout, stderr = run_git_command(git_path, "push", cwd=str(repo_path))
    if not success:
        print(f"[WARNING] Git push failed: {stderr}")
        print("\nYou may need to:")
        print("1. Check your git credentials")
        print("2. Set up remote if not configured")
        print("3. Push manually using: git push")
        return 1
    
    print(f"[OK] Pushed successfully: {stdout.strip()}")
    print("\n[SUCCESS] All done!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

