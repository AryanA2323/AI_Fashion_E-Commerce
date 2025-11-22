"""
Product API Service - Integration with Platzi Fake Store API for fashion products
"""
import requests
import os
from datetime import datetime, timedelta
import json
from services.platzi_api import PlatziAPI

class ProductAPIService:
    """
    Service to fetch real product data from RapidAPI endpoints
    
    Supported APIs:
    1. Real-Time Amazon Data API - Product search, details, reviews
    2. Amazon Product Search API - Search products by keywords
    3. Flipkart Product API - Indian market products
    
    Features:
    - Caching to reduce API calls
    - Rate limiting
    - Error handling with fallbacks
    - Unified product format
    """
    
    def __init__(self):
        # Initialize Platzi Fake Store API (free, no credentials required)
        self.platzi_api = PlatziAPI()
        
        # Cache configuration
        self.cache = {}
        self.cache_ttl = timedelta(hours=6)  # Cache for 6 hours
        
        print("✓ Using Platzi Fake Store API (200+ products, free, unlimited, no credentials required)")
    
    def _get_cache_key(self, api_type, query, **kwargs):
        """Generate cache key from parameters"""
        params_str = json.dumps(kwargs, sort_keys=True)
        return f"{api_type}:{query}:{params_str}"
    
    def _get_from_cache(self, cache_key):
        """Get data from cache if not expired"""
        if cache_key in self.cache:
            data, timestamp = self.cache[cache_key]
            if datetime.now() - timestamp < self.cache_ttl:
                return data
        return None
    
    def _set_cache(self, cache_key, data):
        """Store data in cache"""
        self.cache[cache_key] = (data, datetime.now())
    
    def _get_mock_response_DEPRECATED(self):
        """Return comprehensive mock Amazon API response with 40+ products"""
        return {
            "status": "OK",
            "data": {
                "products": [
                    # Casual Wear
                    {"asin": "B0MOCK001", "product_title": "Men's Classic Cotton T-Shirt - Comfortable Casual Fit", "product_price": "$24.99", "product_original_price": "$29.99", "product_star_rating": "4.5", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK001", "product_photo": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400", "is_prime": True},
                    {"asin": "B0MOCK003", "product_title": "Men's Slim Fit Jeans - Dark Wash Denim Casual", "product_price": "$45.99", "product_original_price": "$59.99", "product_star_rating": "4.3", "product_num_ratings": 567, "product_url": "https://www.amazon.com/dp/B0MOCK003", "product_photo": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400", "is_prime": False},
                    {"asin": "B0MOCK011", "product_title": "Men's Casual Hoodie - Fleece Pullover", "product_price": "$35.99", "product_original_price": "$45.99", "product_star_rating": "4.6", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK011", "product_photo": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400", "is_prime": True},
                    {"asin": "B0MOCK012", "product_title": "Women's Casual Summer Dress - Floral Print", "product_price": "$39.99", "product_original_price": "$49.99", "product_star_rating": "4.7", "product_num_ratings": 1567, "product_url": "https://www.amazon.com/dp/B0MOCK012", "product_photo": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400", "is_prime": True},
                    {"asin": "B0MOCK013", "product_title": "Women's Casual Denim Jacket - Light Wash", "product_price": "$52.99", "product_original_price": "$68.99", "product_star_rating": "4.6", "product_num_ratings": 678, "product_url": "https://www.amazon.com/dp/B0MOCK013", "product_photo": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400", "is_prime": False},
                    {"asin": "B0MOCK014", "product_title": "Men's Casual Cargo Shorts - Cotton Blend", "product_price": "$28.99", "product_original_price": "$36.99", "product_star_rating": "4.4", "product_num_ratings": 445, "product_url": "https://www.amazon.com/dp/B0MOCK014", "product_photo": "https://images.unsplash.com/photo-1591195120140-d531256e280e?w=400", "is_prime": True},
                    
                    # Formal Wear
                    {"asin": "B0MOCK005", "product_title": "Men's Formal Blazer - Business Professional Suit Jacket", "product_price": "$89.99", "product_original_price": "$120.00", "product_star_rating": "4.4", "product_num_ratings": 445, "product_url": "https://www.amazon.com/dp/B0MOCK005", "product_photo": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400", "is_prime": True},
                    {"asin": "B0MOCK015", "product_title": "Men's Formal Dress Shirt - White Cotton", "product_price": "$32.99", "product_original_price": "$42.99", "product_star_rating": "4.5", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK015", "product_photo": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400", "is_prime": True},
                    {"asin": "B0MOCK016", "product_title": "Men's Formal Dress Pants - Slim Fit Trousers", "product_price": "$45.99", "product_original_price": "$59.99", "product_star_rating": "4.3", "product_num_ratings": 789, "product_url": "https://www.amazon.com/dp/B0MOCK016", "product_photo": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400", "is_prime": True},
                    {"asin": "B0MOCK017", "product_title": "Women's Formal Blazer - Office Professional", "product_price": "$75.99", "product_original_price": "$95.99", "product_star_rating": "4.7", "product_num_ratings": 567, "product_url": "https://www.amazon.com/dp/B0MOCK017", "product_photo": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400", "is_prime": True},
                    {"asin": "B0MOCK018", "product_title": "Men's Formal Silk Tie - Classic Pattern", "product_price": "$19.99", "product_original_price": "$29.99", "product_star_rating": "4.6", "product_num_ratings": 342, "product_url": "https://www.amazon.com/dp/B0MOCK018", "product_photo": "https://images.unsplash.com/photo-1589756823695-278bc8d1c4d7?w=400", "is_prime": False},
                    
                    # Streetwear
                    {"asin": "B0MOCK019", "product_title": "Streetwear Graphic Hoodie - Urban Style", "product_price": "$48.99", "product_original_price": "$62.99", "product_star_rating": "4.8", "product_num_ratings": 1891, "product_url": "https://www.amazon.com/dp/B0MOCK019", "product_photo": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400", "is_prime": True},
                    {"asin": "B0MOCK020", "product_title": "Streetwear Bomber Jacket - Hip Hop Fashion", "product_price": "$79.99", "product_original_price": "$99.99", "product_star_rating": "4.7", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK020", "product_photo": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400", "is_prime": True},
                    {"asin": "B0MOCK021", "product_title": "Streetwear Cargo Pants - Tactical Urban", "product_price": "$55.99", "product_original_price": "$72.99", "product_star_rating": "4.5", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK021", "product_photo": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400", "is_prime": True},
                    {"asin": "B0MOCK022", "product_title": "Streetwear Oversized T-Shirt - Bold Print", "product_price": "$32.99", "product_original_price": "$42.99", "product_star_rating": "4.6", "product_num_ratings": 678, "product_url": "https://www.amazon.com/dp/B0MOCK022", "product_photo": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400", "is_prime": False},
                    
                    # Athletic Wear
                    {"asin": "B0MOCK004", "product_title": "Women's Athletic Leggings - High Waisted Yoga Pants", "product_price": "$28.99", "product_original_price": "$34.99", "product_star_rating": "4.6", "product_num_ratings": 2341, "product_url": "https://www.amazon.com/dp/B0MOCK004", "product_photo": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400", "is_prime": True},
                    {"asin": "B0MOCK007", "product_title": "Men's Running Shoes - Lightweight Athletic Sneakers", "product_price": "$65.99", "product_original_price": "$85.00", "product_star_rating": "4.5", "product_num_ratings": 3421, "product_url": "https://www.amazon.com/dp/B0MOCK007", "product_photo": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "is_prime": True},
                    {"asin": "B0MOCK023", "product_title": "Men's Athletic Compression Shirt - Gym Training", "product_price": "$24.99", "product_original_price": "$32.99", "product_star_rating": "4.7", "product_num_ratings": 1567, "product_url": "https://www.amazon.com/dp/B0MOCK023", "product_photo": "https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400", "is_prime": True},
                    {"asin": "B0MOCK024", "product_title": "Women's Athletic Sports Bra - High Support", "product_price": "$29.99", "product_original_price": "$39.99", "product_star_rating": "4.8", "product_num_ratings": 2145, "product_url": "https://www.amazon.com/dp/B0MOCK024", "product_photo": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400", "is_prime": True},
                    {"asin": "B0MOCK025", "product_title": "Men's Athletic Training Shorts - Performance Fabric", "product_price": "$26.99", "product_original_price": "$35.99", "product_star_rating": "4.5", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK025", "product_photo": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400", "is_prime": False},
                    
                    # Party Wear
                    {"asin": "B0MOCK026", "product_title": "Women's Party Evening Dress - Cocktail Sequin", "product_price": "$68.99", "product_original_price": "$89.99", "product_star_rating": "4.8", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK026", "product_photo": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400", "is_prime": True},
                    {"asin": "B0MOCK027", "product_title": "Men's Party Suit - Slim Fit Tuxedo", "product_price": "$149.99", "product_original_price": "$199.99", "product_star_rating": "4.7", "product_num_ratings": 678, "product_url": "https://www.amazon.com/dp/B0MOCK027", "product_photo": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400", "is_prime": True},
                    {"asin": "B0MOCK028", "product_title": "Women's Party Heels - Elegant Evening Shoes", "product_price": "$54.99", "product_original_price": "$72.99", "product_star_rating": "4.6", "product_num_ratings": 445, "product_url": "https://www.amazon.com/dp/B0MOCK028", "product_photo": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400", "is_prime": False},
                    
                    # Traditional Wear
                    {"asin": "B0MOCK029", "product_title": "Traditional Kurta - Ethnic Indian Wear", "product_price": "$42.99", "product_original_price": "$55.99", "product_star_rating": "4.7", "product_num_ratings": 1567, "product_url": "https://www.amazon.com/dp/B0MOCK029", "product_photo": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400", "is_prime": True},
                    {"asin": "B0MOCK030", "product_title": "Traditional Saree - Silk Ethnic Wear", "product_price": "$78.99", "product_original_price": "$102.99", "product_star_rating": "4.9", "product_num_ratings": 2341, "product_url": "https://www.amazon.com/dp/B0MOCK030", "product_photo": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400", "is_prime": True},
                    {"asin": "B0MOCK031", "product_title": "Traditional Sherwani - Wedding Ethnic Dress", "product_price": "$125.99", "product_original_price": "$165.99", "product_star_rating": "4.8", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK031", "product_photo": "https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400", "is_prime": True},
                    {"asin": "B0MOCK032", "product_title": "Traditional Lehenga - Ethnic Bridal Wear", "product_price": "$158.99", "product_original_price": "$208.99", "product_star_rating": "4.9", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK032", "product_photo": "https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400", "is_prime": True},
                    {"asin": "B0MOCK033", "product_title": "Traditional Nehru Jacket - Ethnic Formal", "product_price": "$68.99", "product_original_price": "$89.99", "product_star_rating": "4.6", "product_num_ratings": 567, "product_url": "https://www.amazon.com/dp/B0MOCK033", "product_photo": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400", "is_prime": False},
                    
                    # Additional Mix
                    {"asin": "B0MOCK006", "product_title": "Women's Knit Sweater - Cozy Winter Pullover Casual", "product_price": "$42.99", "product_original_price": "$54.99", "product_star_rating": "4.8", "product_num_ratings": 1789, "product_url": "https://www.amazon.com/dp/B0MOCK006", "product_photo": "https://images.unsplash.com/photo-1584370848010-d7fe6bc767ec?w=400", "is_prime": True},
                    {"asin": "B0MOCK009", "product_title": "Men's Polo Shirt - Classic Fit Casual Cotton", "product_price": "$29.99", "product_original_price": "$39.99", "product_star_rating": "4.4", "product_num_ratings": 912, "product_url": "https://www.amazon.com/dp/B0MOCK009", "product_photo": "https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=400", "is_prime": True},
                    {"asin": "B0MOCK010", "product_title": "Women's Yoga Pants - Stretchy Comfortable Athletic Fit", "product_price": "$32.99", "product_original_price": "$44.99", "product_star_rating": "4.7", "product_num_ratings": 2156, "product_url": "https://www.amazon.com/dp/B0MOCK010", "product_photo": "https://images.unsplash.com/photo-1518310952931-b1de897abd40?w=400", "is_prime": True},
                    {"asin": "B0MOCK034", "product_title": "Men's Leather Jacket - Casual Motorcycle Style", "product_price": "$118.99", "product_original_price": "$155.99", "product_star_rating": "4.7", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK034", "product_photo": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400", "is_prime": True},
                    {"asin": "B0MOCK035", "product_title": "Women's Cardigan - Casual Knit Sweater", "product_price": "$38.99", "product_original_price": "$50.99", "product_star_rating": "4.5", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK035", "product_photo": "https://images.unsplash.com/photo-1584370848010-d7fe6bc767ec?w=400", "is_prime": True},
                    {"asin": "B0MOCK036", "product_title": "Men's Formal Oxford Shoes - Dress Leather", "product_price": "$72.99", "product_original_price": "$95.99", "product_star_rating": "4.6", "product_num_ratings": 678, "product_url": "https://www.amazon.com/dp/B0MOCK036", "product_photo": "https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400", "is_prime": True},
                    {"asin": "B0MOCK037", "product_title": "Women's Sneakers - Casual Walking Shoes", "product_price": "$48.99", "product_original_price": "$64.99", "product_star_rating": "4.7", "product_num_ratings": 1567, "product_url": "https://www.amazon.com/dp/B0MOCK037", "product_photo": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400", "is_prime": False},
                    {"asin": "B0MOCK038", "product_title": "Men's Chino Pants - Business Casual Trousers", "product_price": "$42.99", "product_original_price": "$56.99", "product_star_rating": "4.5", "product_num_ratings": 892, "product_url": "https://www.amazon.com/dp/B0MOCK038", "product_photo": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400", "is_prime": True},
                    {"asin": "B0MOCK039", "product_title": "Women's Maxi Dress - Bohemian Summer Casual", "product_price": "$52.99", "product_original_price": "$68.99", "product_star_rating": "4.8", "product_num_ratings": 1789, "product_url": "https://www.amazon.com/dp/B0MOCK039", "product_photo": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400", "is_prime": True},
                    {"asin": "B0MOCK040", "product_title": "Men's Windbreaker - Athletic Outdoor Jacket", "product_price": "$45.99", "product_original_price": "$59.99", "product_star_rating": "4.6", "product_num_ratings": 1234, "product_url": "https://www.amazon.com/dp/B0MOCK040", "product_photo": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400", "is_prime": True}
                ]
            }
        }
    
    def _make_request_DEPRECATED(self, url, params=None, headers=None):
        """DEPRECATED - No longer using RapidAPI"""
        # This method is no longer used
        # We now use Fake Store API directly
        pass
        
        # Original API code (disabled)
        # if not self.rapidapi_key:
        #     print("⚠️  Using mock data - RapidAPI key not configured")
        #     return self._get_mock_response()
        # 
        # # Check rate limit
        # if self.request_count >= self.max_requests_per_hour:
        #     print("⚠️  Rate limit exceeded. Using mock data.")
        #     return self._get_mock_response()
        # 
        # default_headers = {
        #     "X-RapidAPI-Key": self.rapidapi_key,
        #     "X-RapidAPI-Host": ""
        # }
        # 
        # if headers:
        #     default_headers.update(headers)
        # 
        # try:
        #     self.request_count += 1
        #     response = requests.get(url, params=params, headers=default_headers, timeout=10)
        #     response.raise_for_status()
        #     return response.json()
        # except requests.exceptions.HTTPError as e:
        #     if '429' in str(e):
        #         print(f"⚠️  RapidAPI rate limit hit (429). Using mock data as fallback.")
        #         return self._get_mock_response()
        #     print(f"API request error: {str(e)}")
        #     raise
        # except requests.exceptions.RequestException as e:
        #     print(f"API request error: {str(e)}")
        #     raise
    
    def search_amazon_products(self, query, category=None, max_results=20, gender='unisex'):
        """
        Search fashion products using Fake Store API
        
        Args:
            query (str): Search query
            category (str): Product category
            max_results (int): Maximum number of results
            gender (str): User gender (male, female, unisex)
            
        Returns:
            list: Formatted product list
        """
        # Check cache first
        cache_key = self._get_cache_key('fakestore', query, category=category, gender=gender)
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            print(f"✓ Returning cached FakeStore data for: {query}")
            return cached_data
        
        try:
            print(f"🔍 Searching Platzi API for: {query} (gender: {gender})")
            
            # Search using Platzi API
            products = self.platzi_api.search_fashion(query, gender=gender, limit=max_results)
            
            # Filter by category if specified
            if category and category != 'all':
                category_lower = category.lower()
                products = [p for p in products if p.get('category', '').lower() == category_lower]
            
            # Limit results
            products = products[:max_results]
            
            # Cache results
            self._set_cache(cache_key, products)
            
            print(f"✓ Fetched {len(products)} fashion products from Platzi API")
            return products
            
        except Exception as e:
            print(f"❌ Error fetching products from Platzi API: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
    
    def search_flipkart_products(self, query, category=None, max_results=20):
        """
        Search Flipkart products using RapidAPI
        
        Args:
            query (str): Search query
            category (str): Product category
            max_results (int): Maximum number of results
            
        Returns:
            list: Formatted product list
        """
        # Check cache first
        cache_key = self._get_cache_key('flipkart', query, category=category)
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            print(f"✓ Returning cached Flipkart data for: {query}")
            return cached_data
        
        try:
            url = f"{self.flipkart_api_base}/search"
            params = {
                "query": query,
                "page": "1"
            }
            
            headers = {
                "X-RapidAPI-Host": "flipkart-scraper-api.p.rapidapi.com"
            }
            
            response_data = self._make_request(url, params=params, headers=headers)
            
            # Format products
            products = self._format_flipkart_products(response_data.get('products', []))
            
            # Limit results
            products = products[:max_results]
            
            # Cache results
            self._set_cache(cache_key, products)
            
            print(f"✓ Fetched {len(products)} Flipkart products for: {query}")
            return products
            
        except Exception as e:
            print(f"Error fetching Flipkart products: {str(e)}")
            return []
    
    def get_products_by_category(self, category, source='fakestore', max_results=30, gender='unisex'):
        """
        Get products for a specific category from Fake Store API
        
        Args:
            category (str): Category name (Casual Wear, Formal Wear, etc.)
            source (str): Data source (always 'fakestore' now)
            max_results (int): Maximum products to return
            gender (str): User gender for filtering
            
        Returns:
            list: Product list from Fake Store API
        """
        print(f"🔍 Fetching {max_results} products for category: {category} (gender: {gender})")
        
        try:
            # Get all fashion products from Platzi API
            products = self.platzi_api.get_all_fashion_products(limit=max_results * 2)
            
            print(f"✓ Fetched {len(products)} total fashion products from Platzi API")
            
            # Filter by gender if specified
            if gender and gender != 'unisex':
                products = [p for p in products if p.get('gender', 'unisex').lower() == gender.lower()]
                print(f"✓ After gender filter ({gender}): {len(products)} products")
            
            # Filter by category if specified (category matching is loose)
            if category and category != 'all':
                # Normalize category name (remove "Wear" suffix and make lowercase)
                category_key = category.lower().replace(' wear', '').replace(' ', '')
                
                # Filter products that match the category
                filtered = []
                for p in products:
                    product_category = p.get('category', '').lower()
                    # Match if category keyword is in product category or vice versa
                    if category_key in product_category or product_category in category_key:
                        filtered.append(p)
                
                products = filtered
                print(f"✓ After category filter ({category}): {len(products)} products")
            
            result = products[:max_results]
            print(f"✓ Returning {len(result)} products for {category}")
            return result
            
        except Exception as e:
            print(f"❌ Error in get_products_by_category: {str(e)}")
            import traceback
            traceback.print_exc()
            return []
    
    def get_trending_products(self, limit=20, gender='unisex'):
        """
        Get trending products from Fake Store API
        
        Args:
            limit (int): Number of trending products
            gender (str): User gender for filtering
            
        Returns:
            list: Trending products (all clothing products)
        """
        print(f"Fetching trending products (limit: {limit}, gender: {gender})")
        
        # Get all fashion products from Platzi API
        products = self.platzi_api.get_all_fashion_products(limit=limit * 2)
        
        # Filter by gender if specified
        if gender and gender != 'unisex':
            products = [p for p in products if p.get('gender', 'unisex').lower() == gender.lower()]
        
        # Sort by rating to get "trending" items
        products.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        print(f"✓ Fetched {len(products)} trending products")
        return products[:limit]
    
    def _format_amazon_products(self, raw_products, gender='unisex'):
        """
        Format Amazon API response to unified product structure
        
        Args:
            raw_products (list): Raw Amazon products
            gender (str): User gender for filtering
            
        Returns:
            list: Formatted products (clothing items only)
        """
        formatted = []
        
        for item in raw_products:
            try:
                product_title = item.get('product_title', 'Unknown Product')
                
                # Filter: Only include clothing products
                if not self._is_clothing_product(product_title):
                    continue
                
                # Filter by gender
                if not self._matches_gender(product_title, gender):
                    continue
                
                # Extract price (handle different formats)
                price_str = item.get('product_price', '0')
                price_usd = self._extract_price(price_str)
                
                # Convert USD to INR (approximate rate: 1 USD = 83 INR)
                price_inr = round(price_usd * 83, 2)
                
                # Extract rating
                rating = float(item.get('product_star_rating', '0').split()[0]) if item.get('product_star_rating') else 4.0
                
                product = {
                    'id': item.get('asin', ''),
                    'title': product_title,
                    'price': price_inr,
                    'originalPrice': round(price_inr * 1.2, 2),  # Estimate original price
                    'image': item.get('product_photo', ''),
                    'rating': min(rating, 5.0),
                    'reviews': int(item.get('product_num_ratings', 0)),
                    'source': 'Amazon',
                    'category': self._detect_category(product_title),
                    'url': item.get('product_url', ''),
                    'tags': self._extract_tags(product_title),
                    'description': item.get('product_description', product_title)
                }
                
                formatted.append(product)
            except Exception as e:
                print(f"Error formatting Amazon product: {str(e)}")
                continue
        
        return formatted
    
    def _format_flipkart_products(self, raw_products):
        """
        Format Flipkart API response to unified product structure
        
        Args:
            raw_products (list): Raw Flipkart products
            
        Returns:
            list: Formatted products
        """
        formatted = []
        
        for item in raw_products:
            try:
                # Extract price
                price_str = item.get('price', '0')
                price = self._extract_price(price_str)
                
                # Extract rating
                rating = float(item.get('rating', 4.0))
                
                product = {
                    'id': item.get('id', item.get('product_id', '')),
                    'title': item.get('name', item.get('title', 'Unknown Product')),
                    'price': price,
                    'originalPrice': price * 1.15,  # Estimate original price
                    'image': item.get('image', item.get('thumbnail', '')),
                    'rating': min(rating, 5.0),
                    'reviews': int(item.get('reviews_count', 0)),
                    'source': 'Flipkart',
                    'category': self._detect_category(item.get('name', item.get('title', ''))),
                    'url': item.get('url', item.get('product_url', '')),
                    'tags': self._extract_tags(item.get('name', item.get('title', ''))),
                    'description': item.get('description', item.get('name', ''))
                }
                
                formatted.append(product)
            except Exception as e:
                print(f"Error formatting Flipkart product: {str(e)}")
                continue
        
        return formatted
    
    def _extract_price(self, price_str):
        """
        Extract numeric price from string
        Note: Returns price in USD. Convert to INR in format functions.
        """
        try:
            # Remove currency symbols and commas
            price_clean = ''.join(c for c in str(price_str) if c.isdigit() or c == '.')
            if price_clean:
                return float(price_clean)
            return 0.0
        except:
            return 0.0
    
    def _is_clothing_product(self, title):
        """Check if product is clothing/apparel"""
        title_lower = title.lower()
        
        # Clothing keywords
        clothing_keywords = [
            'shirt', 't-shirt', 'tshirt', 'tee', 'polo', 'tank', 'top',
            'jeans', 'pants', 'trouser', 'shorts', 'skirt', 'dress',
            'jacket', 'coat', 'blazer', 'hoodie', 'sweater', 'cardigan',
            'suit', 'tracksuit', 'jumpsuit', 'romper',
            'leggings', 'joggers', 'sweatpants', 'sweatshirt',
            'kurta', 'saree', 'ethnic wear', 'traditional wear',
            'formal wear', 'casual wear', 'streetwear', 'activewear',
            'athletic wear', 'sportswear', 'gym wear', 'workout',
            'denim', 'cotton', 'polyester', 'fabric',
            'men clothing', 'women clothing', 'apparel', 'garment',
            'outfit', 'wear', 'sleeve', 'collar', 'button',
            'pullover', 'henley', 'flannel', 'chambray', 'oxford'
        ]
        
        # Non-clothing keywords to exclude
        exclude_keywords = [
            'phone', 'case', 'charger', 'cable', 'adapter', 'screen protector',
            'bag', 'backpack', 'wallet', 'purse', 'luggage',
            'shoe', 'sneaker', 'boot', 'sandal', 'slipper', 'footwear',
            'watch', 'jewelry', 'ring', 'necklace', 'bracelet', 'earring',
            'hat', 'cap', 'beanie', 'scarf', 'glove', 'sock',
            'sunglasses', 'glasses', 'belt', 'tie',
            'toy', 'game', 'book', 'electronics', 'home', 'kitchen',
            'beauty', 'makeup', 'skin', 'hair', 'perfume'
        ]
        
        # Check for exclusions first
        for keyword in exclude_keywords:
            if keyword in title_lower:
                return False
        
        # Check for clothing keywords
        for keyword in clothing_keywords:
            if keyword in title_lower:
                return True
        
        return False
    
    def _add_gender_to_query(self, query, gender):
        """Add gender prefix to search query"""
        if gender and gender.lower() != 'unisex':
            if gender.lower() == 'male':
                return f"mens {query}"
            elif gender.lower() == 'female':
                return f"womens {query}"
        return query
    
    def _matches_gender(self, title, gender):
        """Check if product matches user's gender preference"""
        if not gender or gender.lower() == 'unisex':
            return True
        
        title_lower = title.lower()
        
        # Gender-specific keywords
        male_keywords = [
            "men's", "mens", "men", "male", "boy", "boys", "guy", "guys",
            "man's", "mans", "masculine", "him", "his"
        ]
        
        female_keywords = [
            "women's", "womens", "women", "female", "girl", "girls", "lady", "ladies",
            "woman's", "womans", "feminine", "her", "hers"
        ]
        
        # Unisex keywords that suggest the product is for anyone
        unisex_keywords = [
            "unisex", "neutral", "everyone", "all gender", "anyone"
        ]
        
        # Check for unisex indicators first
        for keyword in unisex_keywords:
            if keyword in title_lower:
                return True
        
        # Check gender match
        if gender.lower() == 'male':
            # Check if it's explicitly for women
            for keyword in female_keywords:
                if keyword in title_lower:
                    # Exclude if it's explicitly female unless it's also marked as unisex
                    return False
            # Include if it's for men or gender-neutral
            return True
        
        elif gender.lower() == 'female':
            # Check if it's explicitly for men
            for keyword in male_keywords:
                if keyword in title_lower:
                    # Exclude if it's explicitly male unless it's also marked as unisex
                    return False
            # Include if it's for women or gender-neutral
            return True
        
        return True
    
    def _detect_category(self, title):
        """Detect product category from title"""
        title_lower = title.lower()
        
        category_keywords = {
            'Casual Wear': ['casual', 't-shirt', 'tshirt', 'jeans', 'polo'],
            'Formal Wear': ['formal', 'blazer', 'suit', 'trouser', 'shirt'],
            'Streetwear': ['streetwear', 'hoodie', 'sneaker', 'street style'],
            'Athletic Wear': ['athletic', 'sports', 'gym', 'workout', 'track'],
            'Party Wear': ['party', 'cocktail', 'evening', 'dress'],
            'Traditional Wear': ['traditional', 'ethnic', 'kurta', 'saree'],
            'Winter Wear': ['winter', 'jacket', 'coat', 'sweater', 'warm'],
            'Summer Wear': ['summer', 'shorts', 'tank', 'light']
        }
        
        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in title_lower:
                    return category
        
        return 'Casual Wear'  # Default
    
    def _extract_tags(self, title):
        """Extract relevant tags from product title"""
        title_lower = title.lower()
        
        all_tags = [
            'trendy', 'comfortable', 'stylish', 'premium', 'cotton',
            'slim fit', 'regular fit', 'casual', 'formal', 'party',
            'summer', 'winter', 'lightweight', 'breathable'
        ]
        
        tags = [tag for tag in all_tags if tag in title_lower]
        
        # Add at least 2 tags
        if len(tags) < 2:
            tags.extend(['trendy', 'comfortable'][:2 - len(tags)])
        
        return tags[:5]  # Max 5 tags
    
    def _get_amazon_category_id(self, category):
        """Map category to Amazon category ID"""
        category_map = {
            'Casual Wear': '7141123011',
            'Formal Wear': '1045024',
            'Streetwear': '7141123011',
            'Athletic Wear': '3375251',
            'Party Wear': '1040658',
            'Traditional Wear': '1968062011'
        }
        return category_map.get(category, '7141123011')  # Default to men's fashion
