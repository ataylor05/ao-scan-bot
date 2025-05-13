#!/bin/bash

set -e

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "🛠 Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || {
        echo "❌ Failed to install Homebrew."
        exit 1
    }
    echo "✅ Homebrew installed successfully."
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi
echo "✅ Found $(brew --version)"


# Function to extract major.minor.patch from a full version like 123.0.6312.59
get_major_minor_patch() {
    echo "$1" | cut -d. -f1-3
}

# Check if Google Chrome is installed
if [ ! -f "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
    echo "❌ Google Chrome not found in the expected path."
    echo "📦 Installing Google Chrome with Homebrew..."
    brew install --cask google-chrome || { echo "❌ Failed to install Chrome."; exit 1; }
fi

# Get Google Chrome version
chrome_version_raw=$("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --version)
chrome_version=$(echo "$chrome_version_raw" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
chrome_core_version=$(get_major_minor_patch "$chrome_version")

echo "✅ Google Chrome version: $chrome_version"

# Check if chromedriver is installed
if ! command -v chromedriver &> /dev/null; then
    echo "❌ ChromeDriver is not installed."
    echo "📦 Installing ChromeDriver with Homebrew..."
    brew install chromedriver || { echo "❌ Failed to install ChromeDriver."; exit 1; }
fi

# Get ChromeDriver version
chromedriver_version_raw=$(chromedriver --version)
chromedriver_version=$(echo "$chromedriver_version_raw" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
chromedriver_core_version=$(get_major_minor_patch "$chromedriver_version")

echo "✅ ChromeDriver version: $chromedriver_version"

# Compare core versions (major.minor.patch)
if [ "$chrome_core_version" != "$chromedriver_core_version" ]; then
    echo "⚠️ Version mismatch: Chrome ($chrome_core_version) vs ChromeDriver ($chromedriver_core_version)"
    echo "🔄 Updating both Google Chrome and ChromeDriver..."

    brew upgrade --cask google-chrome || echo "⚠️ Could not upgrade Google Chrome."
    brew upgrade chromedriver || echo "⚠️ Could not upgrade ChromeDriver."

    # Refresh versions
    chrome_version=$("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
    chromedriver_version=$(chromedriver --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')

    chrome_core_version=$(get_major_minor_patch "$chrome_version")
    chromedriver_core_version=$(get_major_minor_patch "$chromedriver_version")

    echo "🔁 Updated Chrome version: $chrome_version"
    echo "🔁 Updated ChromeDriver version: $chromedriver_version"

    if [ "$chrome_core_version" != "$chromedriver_core_version" ]; then
        echo "❌ Versions still mismatched after update."
        exit 1
    fi
fi

echo "✅ Chrome and ChromeDriver are compatible: $chrome_core_version"


# Launch your Selenium project
echo "🚀 Launching Python Selenium script..."

pip3 install -r requirements.txt --break-system-packages

python3 app.py
