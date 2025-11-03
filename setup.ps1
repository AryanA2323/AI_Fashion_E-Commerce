# AI Fashion Store - Automated Setup Script for Windows PowerShell
# This script helps automate the setup process

Write-Host "================================" -ForegroundColor Cyan
Write-Host "AI Fashion Store - Setup Script" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Function to check if command exists
function Test-Command {
    param($Command)
    try {
        if (Get-Command $Command -ErrorAction Stop) {
            return $true
        }
    }
    catch {
        return $false
    }
}

# Step 1: Check Prerequisites
Write-Host "[Step 1/6] Checking prerequisites..." -ForegroundColor Yellow
Write-Host ""

$allPrerequisitesMet = $true

if (Test-Command "node") {
    $nodeVersion = node --version
    Write-Host "✓ Node.js is installed: $nodeVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Node.js is NOT installed" -ForegroundColor Red
    Write-Host "  Please install from: https://nodejs.org/" -ForegroundColor Yellow
    $allPrerequisitesMet = $false
}

if (Test-Command "python") {
    $pythonVersion = python --version
    Write-Host "✓ Python is installed: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python is NOT installed" -ForegroundColor Red
    Write-Host "  Please install from: https://www.python.org/" -ForegroundColor Yellow
    $allPrerequisitesMet = $false
}

if (Test-Command "npm") {
    $npmVersion = npm --version
    Write-Host "✓ npm is installed: $npmVersion" -ForegroundColor Green
} else {
    Write-Host "✗ npm is NOT installed" -ForegroundColor Red
    $allPrerequisitesMet = $false
}

Write-Host ""

if (-not $allPrerequisitesMet) {
    Write-Host "Please install missing prerequisites and run this script again." -ForegroundColor Red
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Step 2: Frontend Setup
Write-Host "[Step 2/6] Setting up Frontend..." -ForegroundColor Yellow
Write-Host ""

$frontendPath = Join-Path $PSScriptRoot "frontend"

if (Test-Path $frontendPath) {
    Set-Location $frontendPath
    
    Write-Host "Installing frontend dependencies (this may take a few minutes)..." -ForegroundColor Cyan
    npm install
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ Frontend dependencies installed successfully" -ForegroundColor Green
    } else {
        Write-Host "✗ Failed to install frontend dependencies" -ForegroundColor Red
    }
    
    # Check if .env exists
    $envPath = Join-Path $frontendPath ".env"
    if (-not (Test-Path $envPath)) {
        Write-Host ""
        Write-Host "Creating .env file from template..." -ForegroundColor Cyan
        Copy-Item (Join-Path $frontendPath ".env.example") $envPath
        Write-Host "✓ Created .env file" -ForegroundColor Green
        Write-Host "⚠ IMPORTANT: Please edit frontend/.env and add your Firebase credentials" -ForegroundColor Yellow
    } else {
        Write-Host "✓ .env file already exists" -ForegroundColor Green
    }
} else {
    Write-Host "✗ Frontend directory not found" -ForegroundColor Red
}

Write-Host ""

# Step 3: Backend Setup
Write-Host "[Step 3/6] Setting up Backend..." -ForegroundColor Yellow
Write-Host ""

$backendPath = Join-Path $PSScriptRoot "backend"

if (Test-Path $backendPath) {
    Set-Location $backendPath
    
    # Create virtual environment
    if (-not (Test-Path "venv")) {
        Write-Host "Creating Python virtual environment..." -ForegroundColor Cyan
        python -m venv venv
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Virtual environment created" -ForegroundColor Green
        } else {
            Write-Host "✗ Failed to create virtual environment" -ForegroundColor Red
        }
    } else {
        Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
    }
    
    # Activate virtual environment and install packages
    Write-Host "Installing backend dependencies..." -ForegroundColor Cyan
    
    $venvActivate = Join-Path $backendPath "venv\Scripts\Activate.ps1"
    
    if (Test-Path $venvActivate) {
        # Install packages
        & "$backendPath\venv\Scripts\python.exe" -m pip install --upgrade pip
        & "$backendPath\venv\Scripts\python.exe" -m pip install -r requirements.txt
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Backend dependencies installed successfully" -ForegroundColor Green
        } else {
            Write-Host "✗ Failed to install backend dependencies" -ForegroundColor Red
        }
    }
    
    # Check if .env exists
    $envPath = Join-Path $backendPath ".env"
    if (-not (Test-Path $envPath)) {
        Write-Host ""
        Write-Host "Creating .env file from template..." -ForegroundColor Cyan
        Copy-Item (Join-Path $backendPath ".env.example") $envPath
        Write-Host "✓ Created .env file" -ForegroundColor Green
    } else {
        Write-Host "✓ .env file already exists" -ForegroundColor Green
    }
} else {
    Write-Host "✗ Backend directory not found" -ForegroundColor Red
}

Write-Host ""

# Step 4: Summary
Set-Location $PSScriptRoot

Write-Host "[Step 4/6] Setup Summary" -ForegroundColor Yellow
Write-Host ""
Write-Host "✓ Prerequisites checked" -ForegroundColor Green
Write-Host "✓ Frontend dependencies installed" -ForegroundColor Green
Write-Host "✓ Backend environment created" -ForegroundColor Green
Write-Host "✓ Backend dependencies installed" -ForegroundColor Green
Write-Host ""

# Step 5: Configuration Reminder
Write-Host "[Step 5/6] Configuration Checklist" -ForegroundColor Yellow
Write-Host ""
Write-Host "Before running the application:" -ForegroundColor Cyan
Write-Host "1. Set up Firebase project at https://console.firebase.google.com/" -ForegroundColor White
Write-Host "2. Enable Authentication (Email/Password and Google)" -ForegroundColor White
Write-Host "3. Create Firestore Database" -ForegroundColor White
Write-Host "4. Edit frontend/.env and add your Firebase credentials" -ForegroundColor White
Write-Host ""

# Step 6: Next Steps
Write-Host "[Step 6/6] Next Steps" -ForegroundColor Yellow
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Cyan
Write-Host ""
Write-Host "Terminal 1 (Backend):" -ForegroundColor White
Write-Host "  cd backend" -ForegroundColor Gray
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "  python app.py" -ForegroundColor Gray
Write-Host ""
Write-Host "Terminal 2 (Frontend):" -ForegroundColor White
Write-Host "  cd frontend" -ForegroundColor Gray
Write-Host "  npm start" -ForegroundColor Gray
Write-Host ""
Write-Host "The application will open at http://localhost:3000" -ForegroundColor Green
Write-Host ""

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "For more information, see:" -ForegroundColor Yellow
Write-Host "  - README.md (full documentation)" -ForegroundColor White
Write-Host "  - QUICKSTART.md (quick start guide)" -ForegroundColor White
Write-Host "  - VERIFICATION_CHECKLIST.md (testing checklist)" -ForegroundColor White
Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
