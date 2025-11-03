# AI Fashion Store - Quick Start Guide

## Step-by-Step Setup (Windows PowerShell)

### 1. Install Prerequisites

Before starting, ensure you have:
- Node.js installed: https://nodejs.org/
- Python installed: https://www.python.org/
- Git installed (optional): https://git-scm.com/

### 2. Firebase Setup

1. Visit https://console.firebase.google.com/
2. Click "Add project" and create a new Firebase project
3. Enable Authentication:
   - Go to Authentication → Sign-in method
   - Enable "Email/Password"
   - Enable "Google" sign-in
4. Create Firestore Database:
   - Go to Firestore Database
   - Click "Create database"
   - Start in test mode (for development)
5. Get Firebase Config:
   - Go to Project Settings → General
   - Scroll to "Your apps" → Web app
   - Copy the firebaseConfig object

### 3. Frontend Setup

Open PowerShell and run:

```powershell
# Navigate to project
cd c:\Projects\ecommerce-ai-fashion\frontend

# Install dependencies
npm install

# Create .env file
New-Item .env -ItemType File

# Open .env in notepad and paste your Firebase config
notepad .env
```

Add this to `.env`:
```
REACT_APP_FIREBASE_API_KEY=your_api_key_here
REACT_APP_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
REACT_APP_FIREBASE_PROJECT_ID=your_project_id
REACT_APP_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
REACT_APP_FIREBASE_APP_ID=your_app_id
REACT_APP_BACKEND_API_URL=http://localhost:5000
```

### 4. Backend Setup

Open a NEW PowerShell window:

```powershell
# Navigate to backend
cd c:\Projects\ecommerce-ai-fashion\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env
```

### 5. Run the Application

**Terminal 1 (Backend):**
```powershell
cd c:\Projects\ecommerce-ai-fashion\backend
.\venv\Scripts\Activate.ps1
python app.py
```

Wait for: `Running on http://0.0.0.0:5000`

**Terminal 2 (Frontend):**
```powershell
cd c:\Projects\ecommerce-ai-fashion\frontend
npm start
```

Wait for browser to open at: `http://localhost:3000`

### 6. Test the Application

1. Click "Sign up" and create an account
2. Fill in your profile:
   - Name: John Doe
   - Age: 25
   - Gender: Male
   - Select interests: Casual Wear, Streetwear
   - Fashion Style: Minimalist
3. Click "Create Account"
4. View your personalized recommendations!

## Common Issues

### Issue: "Scripts are disabled on this system"
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: "Cannot find module 'react'"
**Solution:**
```powershell
cd frontend
npm install
```

### Issue: "No module named 'flask'"
**Solution:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: Backend not connecting
**Solution:**
- Check if backend is running on port 5000
- Verify `REACT_APP_BACKEND_API_URL=http://localhost:5000` in frontend/.env
- Application works with mock data even if backend is down

## Next Steps

1. **Customize the UI**: Edit files in `frontend/src/components/`
2. **Add more products**: Edit `frontend/src/utils/mockData.js`
3. **Integrate real APIs**: Update `backend/utils/product_fetcher.py`
4. **Deploy**: Follow deployment instructions in main README.md

## Getting Help

- Check the main README.md for detailed documentation
- Verify all environment variables are set correctly
- Ensure both frontend and backend are running
- Check browser console for error messages

Happy coding! 🚀
