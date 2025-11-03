# Troubleshooting Guide - AI Fashion Store

## 🔧 Common Issues and Solutions

### Frontend Issues

#### Issue: "Scripts are disabled on this system"
**Error Message:** `running scripts is disabled on this system`

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try running the script again.

---

#### Issue: "Cannot find module 'react'"
**Error Message:** `Module not found: Can't resolve 'react'`

**Solution:**
```powershell
cd frontend
rm -rf node_modules package-lock.json
npm install
```

---

#### Issue: "@tailwind directive errors"
**Error Message:** `Unknown at rule @tailwind`

**Solution:** This is a CSS linter warning and can be safely ignored. The app will work fine. These are PostCSS directives that are processed during build.

---

#### Issue: "Firebase auth not working"
**Symptoms:** Login/Signup buttons don't work, Firebase errors in console

**Solution:**
1. Check `frontend/.env` has all Firebase credentials
2. Verify credentials match Firebase Console exactly
3. Check for extra spaces or quotes in `.env` file
4. Ensure Authentication is enabled in Firebase Console
5. Check authorized domains include `localhost` in Firebase Console

Example correct `.env`:
```env
REACT_APP_FIREBASE_API_KEY=AIzaSyAbC123dEf456GhI789jKl012MnO345pQr
REACT_APP_FIREBASE_AUTH_DOMAIN=my-project.firebaseapp.com
REACT_APP_FIREBASE_PROJECT_ID=my-project-id
```

---

#### Issue: "Port 3000 is already in use"
**Error Message:** `Port 3000 is already in use`

**Solution:**
```powershell
# Find and kill the process using port 3000
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F

# Or use a different port
set PORT=3001 && npm start
```

---

### Backend Issues

#### Issue: "No module named 'flask'"
**Error Message:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```powershell
cd backend
# Ensure virtual environment is activated
.\venv\Scripts\Activate.ps1
# You should see (venv) in your prompt

# Reinstall dependencies
pip install -r requirements.txt
```

---

#### Issue: "Virtual environment activation fails"
**Error:** Cannot activate venv

**Solution:**
```powershell
# Delete existing venv and recreate
cd backend
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

#### Issue: "Port 5000 is already in use"
**Error Message:** `Address already in use`

**Solution:**
```powershell
# Find and kill the process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Or change port in backend/.env
PORT=5001
```

Then update `REACT_APP_BACKEND_API_URL=http://localhost:5001` in frontend/.env

---

#### Issue: "sklearn installation fails"
**Error:** scikit-learn won't install

**Solution:**
```powershell
# Update pip first
python -m pip install --upgrade pip

# Install numpy first, then scikit-learn
pip install numpy
pip install scikit-learn

# Or install all dependencies
pip install -r requirements.txt
```

---

### Firebase Issues

#### Issue: "Firebase initialization error"
**Symptoms:** App doesn't load, Firebase errors

**Solution:**
1. Verify all environment variables are set
2. Check Firebase Console for project status
3. Ensure billing is enabled (if using paid features)
4. Check browser console for specific error messages
5. Clear browser cache and cookies

---

#### Issue: "Firestore permission denied"
**Error:** `Missing or insufficient permissions`

**Solution:**
1. Go to Firebase Console → Firestore Database
2. Check Rules tab
3. For development, use:
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}
```

---

### Connection Issues

#### Issue: "Backend not responding"
**Symptoms:** Frontend works but no products load

**Solution:**
1. Check if backend is running: `http://localhost:5000`
2. Verify CORS settings in backend
3. Check `REACT_APP_BACKEND_API_URL` in frontend/.env
4. Look for errors in backend terminal
5. Note: App works with mock data even if backend is down

---

#### Issue: "CORS errors"
**Error Message:** `Access to fetch blocked by CORS policy`

**Solution:**
1. Ensure Flask-CORS is installed: `pip install flask-cors`
2. Check backend/.env has correct CORS_ORIGINS
3. Restart backend server
4. Clear browser cache

---

### Installation Issues

#### Issue: "npm install takes forever"
**Symptoms:** Installation hangs or very slow

**Solution:**
```powershell
# Try with legacy peer deps
npm install --legacy-peer-deps

# Or clean npm cache
npm cache clean --force
npm install
```

---

#### Issue: "Python version mismatch"
**Error:** Requires Python 3.8+

**Solution:**
```powershell
# Check Python version
python --version

# If too old, install latest from python.org
# Then recreate virtual environment
cd backend
Remove-Item -Recurse -Force venv
python -m venv venv
```

---

### Runtime Issues

#### Issue: "Products not displaying"
**Symptoms:** Dashboard shows no products

**Solution:**
1. Check browser console for errors
2. Open Network tab in DevTools
3. Verify API calls are successful
4. Check if mock data is loading
5. Verify filters aren't hiding all products

---

#### Issue: "Images not loading"
**Symptoms:** Product cards show broken images

**Solution:**
- Images use Unsplash CDN, requires internet connection
- Check internet connectivity
- Some firewalls block image CDNs
- Images may be rate-limited if making many requests

---

#### Issue: "User not persisting after refresh"
**Symptoms:** Logged out after page reload

**Solution:**
1. Check browser allows cookies
2. Check Firebase session configuration
3. Clear browser data and login again
4. Check browser console for storage errors

---

### Development Issues

#### Issue: "Hot reload not working"
**Symptoms:** Changes don't appear without manual refresh

**Solution:**
```powershell
# Frontend
cd frontend
# Stop server (Ctrl+C)
rm -rf node_modules/.cache
npm start

# Backend - Flask auto-reloads in debug mode
# Check FLASK_DEBUG=True in .env
```

---

#### Issue: "Linter/ESLint errors"
**Symptoms:** Red underlines in code editor

**Solution:**
These are often warnings, not errors. App will still run.
To fix:
```powershell
cd frontend
npm install --save-dev eslint
npx eslint --fix src/**/*.js
```

---

## 🔍 Debugging Tips

### Check Browser Console
```
1. Open Developer Tools (F12)
2. Go to Console tab
3. Look for red error messages
4. Check Network tab for failed requests
```

### Check Backend Logs
```
Look at the terminal running Flask
Errors will appear in red
Check for Python tracebacks
```

### Verify Environment Variables
```powershell
# Frontend - check .env is loaded
# In browser console:
console.log(process.env.REACT_APP_FIREBASE_API_KEY)

# Backend - check Python can read .env
# In Python:
import os
print(os.getenv('FLASK_DEBUG'))
```

### Test API Independently
```powershell
# Test if backend is responding
curl http://localhost:5000

# Should return JSON with status: success
```

---

## 🆘 Still Having Issues?

### Systematic Debugging Approach:

1. **Identify the Layer**
   - Frontend issue? (UI, React, routing)
   - Backend issue? (API, Flask, Python)
   - Firebase issue? (Auth, Database)
   - Connection issue? (CORS, network)

2. **Check Logs**
   - Browser console
   - Frontend terminal
   - Backend terminal
   - Firebase Console

3. **Isolate the Problem**
   - Does signup work? → Test auth
   - Do products show? → Test API
   - Can you filter? → Test frontend logic

4. **Start Fresh** (if all else fails)
   ```powershell
   # Frontend
   cd frontend
   rm -rf node_modules package-lock.json
   npm install
   
   # Backend
   cd backend
   Remove-Item -Recurse -Force venv
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

---

## 📞 Getting Help

### Before Asking for Help, Gather:
1. Exact error message (copy entire message)
2. Steps to reproduce the issue
3. Your OS and versions (Node, Python, npm)
4. Which terminal commands you ran
5. Screenshots of error (if UI issue)

### Check These Resources:
- README.md - Full documentation
- QUICKSTART.md - Setup guide
- VERIFICATION_CHECKLIST.md - Test your setup
- PROJECT_SUMMARY.md - Project overview

---

## ✅ Prevention Tips

### To Avoid Issues:

1. **Always activate venv** before running backend
2. **Run npm install** after pulling new changes
3. **Keep environment files updated**
4. **Don't commit .env files** to version control
5. **Test in incognito mode** to rule out cache issues
6. **Check both terminals** for errors
7. **Restart servers** after configuration changes

---

**Remember: The frontend works with mock data even if backend is down!**
