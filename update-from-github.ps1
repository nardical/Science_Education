# Pull the latest main when this folder has no local edits.
# start-game.bat calls this so a double-click can pick up merged PRs.
$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "git not found. Starting the copy already on this computer."
    exit 0
}
if (-not (Test-Path -LiteralPath ".git")) {
    Write-Host "This folder is not a git repo. Starting the local copy."
    exit 0
}

if (Test-Path -LiteralPath ".streamlit") {
    Remove-Item -LiteralPath ".streamlit" -Recurse -Force -ErrorAction SilentlyContinue
}

$dirty = git status --porcelain
if ($dirty) {
    Write-Host "Local edits found. Skipping the GitHub update so those files stay."
    exit 0
}

git fetch origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "Could not reach GitHub. Starting the copy already on this computer."
    exit 0
}

git checkout main
if ($LASTEXITCODE -ne 0) {
    git checkout -B main origin/main
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "Could not switch to main. Starting the current branch."
    exit 0
}

git pull --ff-only origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "Could not fast-forward main. Starting the copy already on this computer."
    exit 0
}

Write-Host "Now on the latest main."
exit 0
