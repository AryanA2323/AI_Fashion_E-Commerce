# ⚡ Quick Start Guide - Real Product Integration

## 🎯 What You Need

1. **RapidAPI Account** (Free) - https://rapidapi.com/
2. **2 API Subscriptions** (Both Free):
   - Real-Time Amazon Data API
   - Flipkart Scraper API

## 📝 Setup Steps (5 minutes)

### Step 1: Get RapidAPI Key

1. Visit https://rapidapi.com/ → Click "Sign Up"
2. Verify your email
3. Search for "Real-Time Amazon Data" → Subscribe to **Basic (Free)** plan
4. Search for "Flipkart Scraper" → Subscribe to **Basic (Free)** plan
5. Go to either API → "Endpoints" tab → Copy your key from Headers:
   ```
   X-RapidAPI-Key: a1b2c3d4e5f6...
   ```

### Step 2: Configure Backend

1. Open `backend/.env` file
2. Find the line: `RAPIDAPI_KEY=`
3. Paste your key after the `=`:
   ```
   RAPIDAPI_KEY=a1b2c3d4e5f6g7h8i9j0
   ```
4. Save the file

### Step 3: Run the Project

**Terminal 1 - Backend:**
```powershell
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm start
```

### Step 4: Test It!

1. Open http://localhost:3000
2. Login or Signup
3. Go to "All Products" page
4. **You should see real Amazon & Flipkart products!** 🎉

## ✅ Success Indicators

- Backend shows: `✓ Fetched X Amazon products`
- Frontend shows: "From Amazon & Flipkart" message
- Products have real titles, prices, and images
- Clicking products opens real Amazon/Flipkart pages

## ❌ Common Issues

### "RAPIDAPI_KEY not set"
- **Fix**: Add your key to `backend/.env`

### "No products loading"
- **Fix**: 
  1. Check backend is running (http://localhost:5000)
  2. Check browser console (F12)
  3. Verify RapidAPI subscriptions are active

### "Rate limit exceeded"
- **Fix**: Wait 1 hour or check your RapidAPI dashboard
- Free tier: 100 requests/month per API

## 📊 Free Tier Limits

- **100 Amazon API calls/month**
- **100 Flipkart API calls/month**
- **Built-in 6-hour caching** (same searches don't count!)

### How Long Will It Last?

With caching enabled:
- **Browsing**: Unlimited (uses cache)
- **New searches**: ~200/month
- **Category changes**: ~6/month (cached for 6 hours)

**Bottom line**: Free tier is perfect for development and demos!

## 🚀 Next Steps

1. **Customize interests** in your profile
2. Check **Personalized** page for AI recommendations
3. Try **searching** for products
4. Filter by **category** and **price range**

## 📖 Detailed Documentation

- **Complete Setup**: [API_SETUP.md](./API_SETUP.md)
- **Technical Details**: [REAL_DATA_INTEGRATION.md](./REAL_DATA_INTEGRATION.md)
- **Main README**: [README.md](./README.md)

## 💡 Pro Tips

1. **Cache is your friend**: Same queries are free (cached 6 hours)
2. **Monitor usage**: https://rapidapi.com/dashboard
3. **Test locally first**: Use up to 200 requests/month for development
4. **Upgrade for production**: $10-20/month for 10,000+ requests

---

**Need Help?** Check the troubleshooting section in [API_SETUP.md](./API_SETUP.md#troubleshooting)

**Ready to go?** Follow the 4 steps above and start shopping with real products! 🛍️
