# Stop on any error
$ErrorActionPreference = "Stop"

function Get-MajorMinorPatch {
    param([string]$version)
    return ($version -split '\.')[0..2] -join '.'
}

# Check for Chocolatey
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "🛠 Chocolatey not found. Installing..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    RefreshEnv
}

Write-Host "✅ Chocolatey is available: $(choco -v)"

# Ensure Google Chrome is installed
if (-not (Get-Command "C:\Program Files\Google\Chrome\Application\chrome.exe" -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Installing Google Chrome..."
    choco install googlechrome -y
}

# Ensure ChromeDriver is installed
if (-not (Get-Command chromedriver -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Installing ChromeDriver..."
    choco install chromedriver -y
}

# Get Chrome version
$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$chromeVersion = (Get-Item $chromePath).VersionInfo.ProductVersion
$chromeCore = Get-MajorMinorPatch $chromeVersion
Write-Host "✅ Google Chrome version: $chromeVersion"

# Get ChromeDriver version
$chromedriverVersion = (& chromedriver --version) -replace '[^\d\.]', ''
$chromedriverCore = Get-MajorMinorPatch $chromedriverVersion
Write-Host "✅ ChromeDriver version: $chromedriverVersion"

# Compare versions
if ($chromeCore -ne $chromedriverCore) {
    Write-Host "⚠️ Version mismatch: Chrome ($chromeCore) vs ChromeDriver ($chromedriverCore)"
    Write-Host "🔄 Updating both..."

    choco upgrade googlechrome -y
    choco upgrade chromedriver -y

    # Re-check versions
    $chromeVersion = (Get-Item $chromePath).VersionInfo.ProductVersion
    $chromedriverVersion = (& chromedriver --version) -replace '[^\d\.]', ''
    $chromeCore = Get-MajorMinorPatch $chromeVersion
    $chromedriverCore = Get-MajorMinorPatch $chromedriverVersion

    Write-Host "🔁 Updated Chrome: $chromeVersion"
    Write-Host "🔁 Updated ChromeDriver: $chromedriverVersion"

    if ($chromeCore -ne $chromedriverCore) {
        Write-Host "❌ Still mismatched after update. Exiting."
        exit 1
    }
}

Write-Host "✅ Chrome and ChromeDriver match: $chromeCore"

# Install Python requirements
Write-Host "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run Python app
Write-Host "🚀 Launching Selenium app..."
python app.py