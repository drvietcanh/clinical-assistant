# Script to add Git to PATH and commit/push
$ErrorActionPreference = "Stop"

Write-Host "[INFO] Searching for Git installation..."

# Common Git installation paths
$gitPaths = @(
    "C:\Program Files\Git\bin\git.exe",
    "C:\Program Files (x86)\Git\bin\git.exe",
    "C:\Program Files\Git\cmd\git.exe",
    "C:\Program Files (x86)\Git\cmd\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe"
)

$gitPath = $null
$gitDir = $null

foreach ($path in $gitPaths) {
    if (Test-Path $path) {
        $gitPath = $path
        $gitDir = Split-Path (Split-Path $path) -Parent
        Write-Host "[OK] Found Git at: $gitPath"
        break
    }
}

if (-not $gitPath) {
    Write-Host "[ERROR] Git not found!"
    Write-Host ""
    Write-Host "Please install Git first:"
    Write-Host "1. Download from: https://git-scm.com/download/win"
    Write-Host "2. Install with default settings"
    Write-Host "3. Make sure to select 'Add Git to PATH' during installation"
    Write-Host ""
    Write-Host "Or use Cursor/VS Code to commit (Ctrl+Shift+G)"
    exit 1
}

# Get bin and cmd directories
$binDir = Join-Path $gitDir "bin"
$cmdDir = Join-Path $gitDir "cmd"

# Check current PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($currentPath -notlike "*$binDir*" -and $currentPath -notlike "*$cmdDir*") {
    Write-Host "[INFO] Adding Git to user PATH..."
    
    # Add both bin and cmd to PATH
    $newPath = $currentPath
    if ($newPath -and -not $newPath.EndsWith(";")) {
        $newPath += ";"
    }
    
    if (Test-Path $binDir) {
        $newPath += "$binDir;"
    }
    if (Test-Path $cmdDir) {
        $newPath += "$cmdDir;"
    }
    
    # Remove trailing semicolon
    $newPath = $newPath.TrimEnd(';')
    
    try {
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Host "[OK] Git added to PATH"
        Write-Host "[INFO] Please restart terminal or Cursor for PATH changes to take effect"
    } catch {
        Write-Host "[ERROR] Failed to update PATH: $_"
        Write-Host "[INFO] You may need to run as Administrator"
        exit 1
    }
} else {
    Write-Host "[INFO] Git already in PATH"
}

# Add to current session PATH
$env:Path += ";$binDir;$cmdDir"

# Verify git is accessible
try {
    $gitVersion = & $gitPath --version 2>&1
    Write-Host "[OK] Git is accessible: $gitVersion"
} catch {
    Write-Host "[WARNING] Git found but not accessible in current session"
    Write-Host "[INFO] Restart terminal/Cursor to use git"
}

Write-Host ""
Write-Host "[INFO] Now attempting to commit and push..."

# Change to repo directory
$repoPath = "d:\1 medical"
Set-Location $repoPath

# Check if there are changes
$status = & $gitPath status --porcelain 2>&1
if (-not $status) {
    Write-Host "[INFO] No changes to commit"
    exit 0
}

Write-Host "[STAGE] Staging all changes..."
& $gitPath add . 2>&1 | Out-Null

Write-Host "[COMMIT] Committing..."
$commitMessage = @"
Add auto-link scores system: components, scripts, and auto-generated mapping

- Add score_links.py component for linking to existing scores
- Add score_links_from_content.py for articles/protocols
- Add auto_link_scores_to_content.py script for auto-detection
- Auto-generate article_protocol_score_mapping.py (301 links: 74 articles, 9 protocols)
- Integrate score links into Articles and Protocols pages
- Update protocol_routing.py to support score links
- Add update_score_links.bat for quick updates
- Add documentation for score links system
"@

& $gitPath commit -m $commitMessage 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Commit failed"
    exit 1
}

Write-Host "[PUSH] Pushing to remote..."
& $gitPath push 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARNING] Push may have failed. Check output above."
    Write-Host "[INFO] You may need to configure git credentials"
} else {
    Write-Host "[SUCCESS] All done!"
}

