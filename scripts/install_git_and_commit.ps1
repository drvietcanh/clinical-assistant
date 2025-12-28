# Script to download and install Git, then commit/push
# Requires Administrator rights

$ErrorActionPreference = "Stop"

Write-Host "[INFO] Git Installation and Commit Script"
Write-Host ""

# Check if running as admin
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "[WARNING] This script needs Administrator rights to install Git"
    Write-Host "[INFO] Right-click PowerShell and select 'Run as Administrator'"
    Write-Host ""
    Write-Host "OR use Cursor/VS Code (easier - no admin needed):"
    Write-Host "1. Press Ctrl+Shift+G"
    Write-Host "2. Stage all changes"
    Write-Host "3. Commit and Push"
    exit 1
}

Write-Host "[INFO] Checking if Git is already installed..."

# Check if git exists
$gitPath = Get-Command git -ErrorAction SilentlyContinue
if ($gitPath) {
    Write-Host "[OK] Git is already installed at: $($gitPath.Source)"
    Write-Host "[INFO] Proceeding to commit..."
} else {
    Write-Host "[INFO] Git not found. Downloading installer..."
    
    $gitInstaller = "$env:TEMP\Git-installer.exe"
    $gitUrl = "https://github.com/git-for-windows/git/releases/latest/download/Git-2.43.0-64-bit.exe"
    
    try {
        Invoke-WebRequest -Uri $gitUrl -OutFile $gitInstaller -UseBasicParsing
        Write-Host "[OK] Download complete"
        
        Write-Host "[INFO] Installing Git (this may take a few minutes)..."
        Write-Host "[INFO] Please select 'Add Git to PATH' in the installer!"
        
        # Run installer silently with PATH option
        Start-Process -FilePath $gitInstaller -ArgumentList "/VERYSILENT", "/NORESTART", "/COMPONENTS=icons,ext\shellhere,assoc,assoc_sh" -Wait
        
        Write-Host "[OK] Git installation complete"
        
        # Refresh PATH
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        
        # Wait a bit for PATH to update
        Start-Sleep -Seconds 2
        
        # Verify installation
        $gitPath = Get-Command git -ErrorAction SilentlyContinue
        if (-not $gitPath) {
            Write-Host "[WARNING] Git installed but not in PATH yet"
            Write-Host "[INFO] Please restart terminal and run commit script again"
            exit 1
        }
    } catch {
        Write-Host "[ERROR] Failed to install Git: $_"
        Write-Host "[INFO] Please install manually from: https://git-scm.com/download/win"
        exit 1
    }
}

# Now commit and push
Write-Host ""
Write-Host "[INFO] Committing and pushing changes..."

$repoPath = "d:\1 medical"
Set-Location $repoPath

# Check status
$status = git status --porcelain 2>&1
if (-not $status) {
    Write-Host "[INFO] No changes to commit"
    exit 0
}

Write-Host "[STAGE] Staging all changes..."
git add . 2>&1 | Out-Null

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

git commit -m $commitMessage 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Commit failed"
    exit 1
}

Write-Host "[PUSH] Pushing to remote..."
git push 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARNING] Push may have failed. Check output above."
} else {
    Write-Host "[SUCCESS] All done!"
}

