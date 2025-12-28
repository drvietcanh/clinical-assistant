# Git Commit Instructions

## Files Changed:
- `config/article_protocol_score_mapping.py` (auto-generated)
- `components/score_links.py`
- `components/score_links_from_content.py`
- `config/protocol_routing.py`
- `pages/04_📋_Protocols.py`
- `pages/09_🫁_Critical_Care.py`
- `pages/12_📚_In_Depth_Articles.py`
- `scripts/auto_link_scores_to_content.py`
- `scripts/update_score_links.bat`
- `scripts/git_commit_push.ps1`
- `docs/SCORE_LINKS_COMPONENT.md`
- `docs/SCORE_LINKS_FROM_CONTENT.md`
- `docs/AUTO_LINK_SCORES_SCRIPT.md`

## Commit Message:
```
Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system
```

## How to Commit:

### Option 1: Using Cursor/VS Code
1. Open Source Control panel (Ctrl+Shift+G)
2. Stage all changes
3. Enter commit message above
4. Click Commit
5. Click Push

### Option 2: Using Git Bash
```bash
cd "d:/1 medical"
git add .
git commit -m "Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system"
git push
```

