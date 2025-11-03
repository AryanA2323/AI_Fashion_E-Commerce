# AI-Based Personalized E-Commerce Clothing Website

A full-stack web application that provides personalized clothing recommendations with **REAL products from Amazon and Flipkart** using advanced AI/ML algorithms and user preferences.

## 🚀 Features

- **Real Product Data**: Live products from Amazon and Flipkart via RapidAPI
- **User Authentication**: Firebase Authentication with Email/Password and Google Sign-In
- **AI-Powered Recommendations**: Semantic embeddings (BERT) + TF-IDF for intelligent product matching
- **Multi-Platform Products**: Real-time products from both Amazon and Flipkart
- **Smart Filtering**: Filter by category, price range, and store
- **User Profiles**: Customizable user profiles with interests and preferences
- **Responsive Design**: Modern, mobile-friendly UI with TailwindCSS
- **Intelligent Caching**: 6-hour cache to reduce API calls and stay within free tier limits
- **Advanced ML Engine**: Sentence Transformers with hybrid semantic + TF-IDF scoring

## 🛠️ Tech Stack

### Frontend
- **React.js** - UI Framework
- **TailwindCSS** - Styling
- **React Router** - Navigation
- **Firebase** - Authentication & Database
- **Axios** - HTTP Client

### Backend
- **Flask** - Python Web Framework
- **scikit-learn** - Machine Learning (TF-IDF, Cosine Similarity)
- **Flask-CORS** - Cross-Origin Resource Sharing
- **NumPy & Pandas** - Data Processing

### Database & Auth
- **Firebase Authentication** - User Authentication
- **Cloud Firestore** - User Profiles & Data Storage

## 📁 Project Structure

```
ecommerce-ai-fashion/
├── frontend/                 # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/      # React Components
│   │   │   ├── Navbar.js
│   │   │   ├── ProductCard.js
│   │   │   ├── ProductList.js
│   │   │   └── FilterBar.js
│   │   ├── pages/           # Page Components
│   │   │   ├── Login.js
│   │   │   ├── Signup.js
│   │   │   ├── Dashboard.js
│   │   │   └── Profile.js
│   │   ├── context/         # React Context
│   │   │   └── AuthContext.js
│   │   ├── firebase/        # Firebase Config
│   │   │   ├── config.js
│   │   │   ├── auth.js
│   │   │   └── firestore.js
│   │   ├── utils/           # Utilities
│   │   │   ├── api.js
│   │   │   └── mockData.js
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
│
├── backend/                  # Flask Backend
│   ├── model/
│   │   └── recommendation_engine.py  # ML Recommendation Engine
│   ├── utils/
│   │   └── product_fetcher.py        # API Integration
│   ├── app.py                        # Flask Application
│   ├── requirements.txt
│   └── .env.example
│
└── README.md
```

## 🔧 Setup Instructions

### Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- Firebase Account
- **RapidAPI Account** (Free tier available)
- npm or yarn

### 1. RapidAPI Setup (Required for Real Products)

1. Go to [RapidAPI](https://rapidapi.com/) and create a free account
2. Subscribe to these free APIs:
   - [Real-Time Amazon Data API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data) - 100 requests/month free
   - [Flipkart Scraper API](https://rapidapi.com/datascraper/api/flipkart-scraper-api) - 100 requests/month free
3. Copy your API key from the dashboard (shown in Headers section)

**📖 Detailed Setup Guide**: See [API_SETUP.md](./API_SETUP.md) for complete instructions

### 2. Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project
3. Enable Authentication (Email/Password and Google)
4. Create a Firestore Database
5. Get your Firebase configuration credentials

### 2. Frontend Setup

```powershell
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create .env file from example
cp .env.example .env

# Add your Firebase credentials to .env
# REACT_APP_FIREBASE_API_KEY=your_api_key
# REACT_APP_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
# REACT_APP_FIREBASE_PROJECT_ID=your_project_id
# REACT_APP_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
# REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
# REACT_APP_FIREBASE_APP_ID=your_app_id
# REACT_APP_BACKEND_API_URL=http://localhost:5000

# Start development server
npm start
```

The frontend will run on `http://localhost:3000`

### 3. Backend Setup

```powershell
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On Windows CMD:
.\venv\Scripts\activate.bat
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Edit .env file and add your RapidAPI key
# IMPORTANT: Add your RapidAPI key here for real products!
# RAPIDAPI_KEY=your_rapidapi_key_here

# Run Flask server
python app.py
```

The backend will run on `http://localhost:5000`

**⚠️ Important**: Without RapidAPI key, the app will show errors when fetching products. Get your free key from [RapidAPI](https://rapidapi.com/).

## 🚀 Running the Application

1. **Start Backend** (Terminal 1):
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python app.py
```

2. **Start Frontend** (Terminal 2):
```powershell
cd frontend
npm start
```

3. **Open Browser**:
   - Navigate to `http://localhost:3000`
   - Sign up or log in
   - Complete your profile with interests
   - Get personalized recommendations!

## 📊 How It Works

### Recommendation Algorithm

1. **User Profile Creation**: Users provide interests and fashion preferences
2. **Text Vectorization**: User preferences and product descriptions are converted to TF-IDF vectors
3. **Similarity Matching**: Cosine similarity calculates relevance scores
4. **Ranking**: Products are ranked by relevance and filtered by user preferences
5. **Personalization**: Recommendations improve over time with user interactions

### Data Flow

```
User Profile → Flask API → ML Engine → Product Matching → Ranked Results → Frontend Display
```

## 🔑 API Endpoints

### Backend API

- `GET /` - Health check
- `POST /api/recommendations` - Get personalized recommendations
- `POST /api/track-interaction` - Track user interactions
- `GET /api/products/search` - Search products by keyword

### Request Example

```javascript
POST /api/recommendations
{
  "interests": ["casual", "streetwear"],
  "fashionStyle": "minimalist",
  "filters": {
    "category": "all",
    "priceRange": "1000-2500",
    "source": "all"
  }
}
```

## 🔐 Environment Variables

### Frontend (.env)

```env
REACT_APP_FIREBASE_API_KEY=your_api_key
REACT_APP_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
REACT_APP_FIREBASE_PROJECT_ID=your_project_id
REACT_APP_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
REACT_APP_FIREBASE_APP_ID=your_app_id
REACT_APP_BACKEND_API_URL=http://localhost:5000
```

### Backend (.env)

```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000

# RapidAPI Configuration (REQUIRED for real products)
RAPIDAPI_KEY=your_rapidapi_key_here

# CORS Settings
CORS_ORIGINS=http://localhost:3000
```

**Get your RapidAPI key**: https://rapidapi.com/dashboard

## 🌐 Real Product Data Integration

### ✅ Currently Integrated

This app now uses **real product data** from Amazon and Flipkart via RapidAPI:

**APIs Used**:
- **Real-Time Amazon Data API** - Live Amazon product search, details, and prices
- **Flipkart Scraper API** - Real Flipkart product catalog

**Features**:
- ✅ Real product titles, prices, and images
- ✅ Actual ratings and reviews
- ✅ Clickable URLs to product pages
- ✅ Live inventory and availability
- ✅ 6-hour intelligent caching
- ✅ Rate limit protection
- ✅ Free tier: ~200 requests/month

**Setup Guide**: See [API_SETUP.md](./API_SETUP.md) for detailed instructions

**Integration Details**: See [REAL_DATA_INTEGRATION.md](./REAL_DATA_INTEGRATION.md) for technical implementation

### Alternative Options

If you prefer direct API access:
- **Amazon Product Advertising API** - Requires Amazon Associates approval
- **Flipkart Affiliate API** - Requires Flipkart Affiliate approval

RapidAPI is recommended for faster development and easier integration.

## 🚀 Deployment

### Environment Variables for Production

**Frontend (Vercel/Netlify)**:
- Add all `REACT_APP_*` variables from `.env`

**Backend (Render/Heroku/Railway)**:
- Add `RAPIDAPI_KEY` - **REQUIRED** for real products
- Add `FLASK_ENV=production`
- Add `CORS_ORIGINS` with your frontend URL

### Frontend (Vercel/Netlify)

```powershell
cd frontend
npm run build

# Deploy build folder to Vercel or Netlify
```

### Backend (Render/Heroku/Railway)

```powershell
# Create Procfile (already exists)
# Procfile: web: gunicorn app:app

# Push to Git and deploy
git init
git add .
git commit -m "Initial commit"
# Follow platform-specific deployment instructions

# Don't forget to set RAPIDAPI_KEY environment variable!
```

**⚠️ Production Note**: Monitor your RapidAPI usage dashboard. Consider upgrading to paid tier for production apps with many users.

## 📱 Features Breakdown

### User Authentication
- Email/Password registration and login
- Google OAuth integration
- Password validation and error handling
- Protected routes

### User Profile Management
- Customizable profile with personal information
- Interest selection (8+ categories)
- Fashion style preferences
- Profile editing and updates

### Product Recommendations
- AI-powered personalized suggestions
- Real-time filtering
- Relevance scoring
- Multi-source product aggregation

### Filtering & Search
- Category filters (Casual, Formal, Streetwear, etc.)
- Price range filters
- Source filters (Amazon, Flipkart)
- Active filter display and clearing

## 🧪 Testing

Currently using mock data for development. The application will automatically fallback to mock products if the backend is unavailable.

## 🛣️ Roadmap

- [x] Integrate real Amazon & Flipkart APIs ✅
- [x] Advanced ML with Sentence Transformers ✅
- [ ] Add collaborative filtering
- [ ] Implement wishlist functionality
- [ ] Add product comparison feature
- [ ] Visual search with image recognition
- [ ] Mobile app (React Native)
- [ ] Real-time price tracking
- [ ] Email notifications for deals
- [ ] Chatbot for fashion advice

## 🐛 Troubleshooting

### Product Data Issues

**Problem**: "RAPIDAPI_KEY not set" error
- **Solution**: Add your RapidAPI key to `backend/.env` file
- Get free key at: https://rapidapi.com/

**Problem**: "Rate limit exceeded" error
- **Solution**: You've hit the monthly/hourly API limit
- Wait for reset or upgrade your RapidAPI plan
- Check usage: https://rapidapi.com/dashboard

**Problem**: No products loading
- **Solution**: 
  1. Check backend is running on port 5000
  2. Verify RapidAPI key is valid
  3. Check browser console for errors
  4. Ensure you've subscribed to both APIs on RapidAPI

### Frontend Issues

**Problem**: `@tailwind` errors in CSS
- **Solution**: These are CSS linter warnings and won't affect functionality

**Problem**: Firebase errors
- **Solution**: Verify Firebase configuration in `.env` file

### Backend Issues

**Problem**: Module import errors
- **Solution**: Ensure virtual environment is activated and dependencies are installed

**Problem**: CORS errors
- **Solution**: Check `CORS_ORIGINS` in backend `.env` matches frontend URL

**Problem**: Sentence Transformers import slow
- **Solution**: First run downloads models (~100MB), subsequent runs are fast

**📖 Full Troubleshooting Guide**: See [API_SETUP.md](./API_SETUP.md#troubleshooting)

## 📝 License

This project is open source and available under the MIT License.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using React, Flask, Firebase, and Machine Learning**
#   A I _ F a s h i o n _ E - C o m m e r c e  
 