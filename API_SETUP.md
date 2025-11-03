# RapidAPI Integration Setup Guide

## Overview
This project now uses **real product data** from Amazon and Flipkart via RapidAPI instead of mock data.

## Getting Started

### 1. Create RapidAPI Account
1. Go to [https://rapidapi.com/](https://rapidapi.com/)
2. Click "Sign Up" (it's free!)
3. Verify your email address

### 2. Subscribe to APIs

#### Amazon Products API
**Recommended: Real-Time Amazon Data**
- URL: https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data
- Free Tier: 100 requests/month
- Features: Product search, details, reviews
- Subscribe: Click "Subscribe to Test" → Select "Basic (Free)" plan

**Alternative: Amazon Product Data**
- URL: https://rapidapi.com/DataCrawler/api/amazon-data-scraper127
- Free Tier: 100 requests/month

#### Flipkart Products API
**Recommended: Flipkart Scraper API**
- URL: https://rapidapi.com/datascraper/api/flipkart-scraper-api
- Free Tier: 100 requests/month
- Features: Product search, trending, categories

**Alternative: Flipkart Product Search**
- URL: https://rapidapi.com/quetommy/api/flipkart-product-search
- Free Tier: 50 requests/month

### 3. Get Your API Key
1. Go to your RapidAPI Dashboard
2. Click on any API you subscribed to
3. Navigate to "Endpoints" tab
4. Your API key is shown in the "Headers" section: `X-RapidAPI-Key: YOUR_KEY_HERE`
5. Copy this key

### 4. Configure Backend
1. Open `backend/.env` file
2. Add your RapidAPI key:
```env
RAPIDAPI_KEY=your_actual_key_here_without_quotes
```

Example:
```env
RAPIDAPI_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### 5. Restart Backend Server
Stop the backend server (Ctrl+C) and restart:
```bash
cd backend
python app.py
```

## API Endpoints

### Frontend Can Use These:

#### Get Personalized Recommendations
```
POST /api/recommendations
Body: {
  "interests": ["casual", "streetwear"],
  "fashionStyle": "minimalist",
  "filters": {
    "category": "all",
    "priceRange": "all",
    "source": "both"  // amazon | flipkart | both
  }
}
```

#### Get All Products
```
GET /api/products/all?source=both&limit=60&category=all
```

#### Search Products
```
GET /api/products/search?q=tshirt&source=both&limit=20
```

#### Get Products by Category
```
GET /api/products/category/Casual%20Wear?source=both&limit=30
```

#### Get Trending Products
```
GET /api/trending?limit=20
```

#### Get Similar Products
```
POST /api/similar-products
Body: {
  "product": { ...product object... },
  "limit": 5
}
```

## Rate Limits & Caching

### Free Tier Limits
- **Amazon API**: 100 requests/month
- **Flipkart API**: 100 requests/month
- **Total**: ~200 requests/month

### Built-in Caching
The backend automatically caches API responses for **6 hours** to minimize API calls:
- Search results cached by query
- Category products cached
- Trending products cached
- Cache stored in-memory

### Best Practices
1. **Use cache effectively**: Same searches within 6 hours won't hit the API
2. **Limit results**: Default limits are optimized (20-60 products)
3. **Combine sources**: Use `source=both` to get diverse results
4. **Development**: Use fewer products during testing

### Rate Limit Protection
- Backend tracks requests per hour
- Maximum 50 requests/hour enforced
- Returns error if limit exceeded
- Resets every hour

## Testing the Integration

### 1. Check API Key Setup
```bash
curl http://localhost:5000/
```
Should return: `{"status": "success", "message": "API is running"}`

### 2. Test Product Fetch
```bash
curl "http://localhost:5000/api/products/search?q=shirt&source=amazon&limit=5"
```

### 3. Monitor Console
Backend logs show:
- ✓ API requests made
- ✓ Cache hits (no API call needed)
- ⚠ Errors or rate limits

## Troubleshooting

### "RAPIDAPI_KEY not set" Error
**Problem**: API key not configured
**Solution**: Add key to `backend/.env` file

### "Rate limit exceeded" Error
**Problem**: Too many API requests
**Solution**: 
- Wait 1 hour for reset
- Use cached data
- Reduce limit parameters

### "API request error" or 429 Status
**Problem**: Monthly quota exceeded
**Solution**:
- Check RapidAPI Dashboard for usage
- Subscribe to paid tier if needed
- Use alternative APIs

### No Products Returned
**Problem**: API response format changed or network issue
**Solution**:
- Check backend console for error messages
- Verify API subscriptions are active
- Try alternative APIs

### Import Error for `requests`
**Problem**: Missing Python package
**Solution**:
```bash
cd backend
pip install requests
```

## Cost Analysis

### Free Tier (Recommended for Development)
- **Cost**: $0/month
- **Requests**: ~200/month (2 APIs)
- **Best For**: Development, testing, small demos

### Basic Paid Tier
- **Cost**: ~$10-20/month per API
- **Requests**: 10,000-50,000/month
- **Best For**: Small production apps

### Pro Tier
- **Cost**: ~$50-100/month per API
- **Requests**: Unlimited or 500,000/month
- **Best For**: Production apps with many users

## Alternative APIs

If you need more requests or different data:

### 1. SerpAPI (Google Shopping)
- URL: https://serpapi.com/
- Free: 100 searches/month
- Features: Google Shopping results

### 2. Rainforest API (Amazon)
- URL: https://www.rainforestapi.com/
- Free: 1,000 requests trial
- Features: Real-time Amazon data

### 3. Keepa (Amazon Price History)
- URL: https://keepa.com/
- Features: Historical prices, tracking

### 4. ScraperAPI (Custom Scraping)
- URL: https://www.scraperapi.com/
- Free: 5,000 requests trial
- Features: Custom scraping solution

## Production Deployment

### Environment Variables
Set in your hosting platform (Heroku, Render, Railway):
```
RAPIDAPI_KEY=your_production_key
FLASK_ENV=production
FLASK_DEBUG=False
```

### Scaling Tips
1. Use Redis for distributed caching
2. Implement database cache (MongoDB, PostgreSQL)
3. Queue API requests for batch processing
4. Monitor usage with Sentry or LogRocket

## Support

### RapidAPI Support
- Dashboard: https://rapidapi.com/dashboard
- Docs: https://docs.rapidapi.com/
- Support: support@rapidapi.com

### Project Issues
- Check backend console for error logs
- Verify `.env` configuration
- Test API subscriptions in RapidAPI dashboard

---

**Note**: This integration uses real APIs with rate limits. Always monitor your usage in the RapidAPI dashboard to avoid unexpected charges or service interruptions.
