# Git Commit and Push Script
$ErrorActionPreference = "Stop"

$repoPath = "d:\1 medical"
Set-Location $repoPath

# Try to find git
$gitPath = $null
$possiblePaths = @(
    "C:\Program Files\Git\bin\git.exe",
    "C:\Program Files (x86)\Git\bin\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\git.exe",
    "$env:ProgramFiles\Git\cmd\git.exe",
    "$env:ProgramFiles(x86)\Git\cmd\git.exe"
)

foreach ($path in $possiblePaths) {
    if (Test-Path $path) {
        $gitPath = $path
        break
    }
}

# Also try from PATH
if (-not $gitPath) {
    try {
        $gitCmd = Get-Command git -ErrorAction SilentlyContinue
        if ($gitCmd) {
            $gitPath = $gitCmd.Source
        }
    } catch {}
}

if (-not $gitPath) {
    Write-Host "Git not found. Please install Git or add it to PATH."
    Write-Host "You can commit manually using:"
    Write-Host "  git add ."
    Write-Host "  git commit -m 'Add auto-link scores system'"
    Write-Host "  git push"
    exit 1
}

Write-Host "Using git at: $gitPath"
Write-Host ""

# Check if there are changes
$status = & $gitPath status --porcelain
if (-not $status) {
    Write-Host "No changes to commit."
    exit 0
}

Write-Host "Staging all changes..."
& $gitPath add .

Write-Host "Committing..."
$commitMessage = "Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script
- Auto-generate article_protocol_score_mapping.py
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links"

& $gitPath commit -m $commitMessage

Write-Host "Pushing to remote..."
& $gitPath push

Write-Host ""
Write-Host "Done!"

