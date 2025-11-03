# Setup Verification Checklist

## ✅ Pre-Setup Checklist

Before running the application, verify:

- [ ] Node.js is installed (run `node --version`)
- [ ] Python is installed (run `python --version`)
- [ ] npm is installed (run `npm --version`)
- [ ] You have a Firebase account
- [ ] You have a text editor (VS Code recommended)

## ✅ Firebase Setup Checklist

- [ ] Created Firebase project
- [ ] Enabled Email/Password authentication
- [ ] Enabled Google authentication
- [ ] Created Firestore database
- [ ] Copied Firebase configuration
- [ ] Saved config to frontend/.env

## ✅ Frontend Setup Checklist

- [ ] Navigated to `c:\Projects\ecommerce-ai-fashion\frontend`
- [ ] Ran `npm install` successfully
- [ ] Created `.env` file
- [ ] Added all Firebase credentials to `.env`
- [ ] Added `REACT_APP_BACKEND_API_URL=http://localhost:5000`
- [ ] No errors in terminal after `npm install`

## ✅ Backend Setup Checklist

- [ ] Navigated to `c:\Projects\ecommerce-ai-fashion\backend`
- [ ] Created virtual environment with `python -m venv venv`
- [ ] Activated virtual environment
- [ ] Ran `pip install -r requirements.txt` successfully
- [ ] Created `.env` file (copy from .env.example)
- [ ] No errors during package installation

## ✅ Running Application Checklist

### Backend Terminal
- [ ] Virtual environment is activated (you see `(venv)` in prompt)
- [ ] Ran `python app.py`
- [ ] See "Running on http://0.0.0.0:5000"
- [ ] No error messages in terminal

### Frontend Terminal
- [ ] Navigated to frontend directory
- [ ] Ran `npm start`
- [ ] Browser opens automatically to http://localhost:3000
- [ ] No compilation errors

## ✅ Application Testing Checklist

### Initial Load
- [ ] Application loads without errors
- [ ] Login page is displayed
- [ ] UI looks correct (proper styling)
- [ ] No console errors in browser DevTools

### Sign Up Flow
- [ ] Can click "Sign up" link
- [ ] Sign up form displays correctly
- [ ] All fields are present (Name, Age, Email, Password, etc.)
- [ ] Interest buttons are clickable
- [ ] Can select multiple interests
- [ ] Can submit form
- [ ] Redirects to dashboard after signup

### Login Flow
- [ ] Can navigate back to login
- [ ] Can enter email and password
- [ ] Login button works
- [ ] Redirects to dashboard after login
- [ ] Google sign-in button is present

### Dashboard
- [ ] Dashboard loads with welcome message
- [ ] User name is displayed correctly
- [ ] Products are displayed in grid
- [ ] Product cards show images, titles, prices
- [ ] Filter bar is visible and functional
- [ ] Can apply filters
- [ ] Products update based on filters

### Profile Page
- [ ] Can navigate to profile page
- [ ] Profile information is displayed
- [ ] Can click "Edit Profile"
- [ ] Can modify profile fields
- [ ] Can save changes
- [ ] Changes persist after refresh

### Logout
- [ ] Can click logout button in navbar
- [ ] Redirects to login page
- [ ] Protected routes redirect to login when not authenticated

## ✅ Common Issues Resolution

### Issue: npm install fails
**Check:**
- [ ] Internet connection is active
- [ ] You're in the frontend directory
- [ ] No package-lock.json conflicts
- [ ] Try: `npm install --legacy-peer-deps`

### Issue: Python packages won't install
**Check:**
- [ ] Virtual environment is activated
- [ ] Python version is 3.8+
- [ ] pip is updated: `python -m pip install --upgrade pip`
- [ ] Try installing packages individually

### Issue: Firebase authentication not working
**Check:**
- [ ] Firebase credentials in .env are correct
- [ ] No extra spaces in .env file
- [ ] Authentication methods enabled in Firebase Console
- [ ] Authorized domains include localhost

### Issue: Backend connection fails
**Check:**
- [ ] Backend is running on port 5000
- [ ] REACT_APP_BACKEND_API_URL in frontend .env is correct
- [ ] No firewall blocking port 5000
- [ ] Application works with mock data even if backend is down

### Issue: Pages show blank
**Check:**
- [ ] Check browser console for errors
- [ ] Verify React DevTools shows components
- [ ] Check Network tab for failed requests
- [ ] Clear browser cache and reload

## ✅ Environment Variables Verification

### Frontend .env should have:
```
REACT_APP_FIREBASE_API_KEY=AIza...
REACT_APP_FIREBASE_AUTH_DOMAIN=project.firebaseapp.com
REACT_APP_FIREBASE_PROJECT_ID=project-id
REACT_APP_FIREBASE_STORAGE_BUCKET=project.appspot.com
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=123456
REACT_APP_FIREBASE_APP_ID=1:123:web:abc
REACT_APP_BACKEND_API_URL=http://localhost:5000
```

### Backend .env should have (optional for development):
```
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
```

## ✅ Success Indicators

You know everything is working when:
- [ ] ✅ No red errors in any terminal
- [ ] ✅ Frontend loads at http://localhost:3000
- [ ] ✅ Backend API responds at http://localhost:5000
- [ ] ✅ Can create an account
- [ ] ✅ Can log in
- [ ] ✅ Dashboard shows products
- [ ] ✅ Filters work correctly
- [ ] ✅ Profile can be edited
- [ ] ✅ Can log out successfully

## 📸 Screenshots Checklist

Take screenshots to verify:
- [ ] Login page
- [ ] Signup page with all fields
- [ ] Dashboard with products
- [ ] Filter bar with options
- [ ] Product cards with details
- [ ] Profile page
- [ ] Edited profile after changes

## 🎉 Final Verification

If you can do all of these, you're ready:
- [ ] Create a new account with your preferences
- [ ] See personalized recommendations on dashboard
- [ ] Apply filters and see products update
- [ ] Edit your profile and see changes
- [ ] Log out and log back in
- [ ] Everything persists after page refresh

---

**If all checkboxes are checked, congratulations! Your AI Fashion Store is fully functional! 🎊**

For help, refer to:
- README.md (full documentation)
- QUICKSTART.md (setup guide)
- PROJECT_SUMMARY.md (overview)
