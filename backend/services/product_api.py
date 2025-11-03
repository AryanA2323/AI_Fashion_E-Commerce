"""
Product API Service - Integration with RapidAPI for real Amazon and Flipkart products
"""
import requests
import os
from datetime import datetime, timedelta
import json

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
        self.rapidapi_key = os.getenv('RAPIDAPI_KEY', '')
        
        # API endpoints
        self.amazon_api_base = "https://real-time-amazon-data.p.rapidapi.com"
        self.flipkart_api_base = "https://flipkart-scraper-api.p.rapidapi.com"
        
        # Cache configuration
        self.cache = {}
        self.cache_ttl = timedelta(hours=6)  # Cache for 6 hours
        
        # Rate limiting
        self.request_count = 0
        self.max_requests_per_hour = 50  # Free tier limit
        
        if not self.rapidapi_key:
            print("⚠️  RAPIDAPI_KEY not set. Please add it to .env file")
            print("Get your free API key at: https://rapidapi.com/")
        else:
            print(f"✓ RapidAPI key loaded: {self.rapidapi_key[:10]}...")
    
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
    
    def _make_request(self, url, params=None, headers=None):
        """Make API request with error handling"""
        if not self.rapidapi_key:
            raise Exception("RapidAPI key not configured")
        
        # Check rate limit
        if self.request_count >= self.max_requests_per_hour:
            raise Exception("Rate limit exceeded. Please try again later.")
        
        default_headers = {
            "X-RapidAPI-Key": self.rapidapi_key,
            "X-RapidAPI-Host": ""
        }
        
        if headers:
            default_headers.update(headers)
        
        try:
            self.request_count += 1
            response = requests.get(url, params=params, headers=default_headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request error: {str(e)}")
            raise
    
    def search_amazon_products(self, query, category=None, max_results=20, gender='unisex'):
        """
        Search Amazon products using RapidAPI
        
        Args:
            query (str): Search query
            category (str): Product category
            max_results (int): Maximum number of results
            gender (str): User gender (male, female, unisex)
            
        Returns:
            list: Formatted product list
        """
        # Check cache first
        cache_key = self._get_cache_key('amazon', query, category=category)
        cached_data = self._get_from_cache(cache_key)
        if cached_data:
            print(f"✓ Returning cached Amazon data for: {query}")
            return cached_data
        
        try:
            # Add gender to query for better filtering
            gender_query = self._add_gender_to_query(query, gender)
            
            url = f"{self.amazon_api_base}/search"
            params = {
                "query": gender_query,
                "country": "US",
                "page": "1"
            }
            
            if category:
                params["category_id"] = self._get_amazon_category_id(category)
            
            headers = {
                "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
            }
            
            print(f"🔍 Searching Amazon for: {query}")
            print(f"URL: {url}")
            print(f"Params: {params}")
            
            response_data = self._make_request(url, params=params, headers=headers)
            print(f"✓ Amazon API response received")
            print(f"Response data keys: {response_data.keys() if response_data else 'None'}")
            
            # Format and filter products by gender
            products = self._format_amazon_products(response_data.get('data', {}).get('products', []), gender)
            
            # Limit results
            products = products[:max_results]
            
            # Cache results
            self._set_cache(cache_key, products)
            
            print(f"✓ Fetched {len(products)} Amazon products for: {query}")
            return products
            
        except Exception as e:
            print(f"❌ Error fetching Amazon products: {str(e)}")
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
    
    def get_products_by_category(self, category, source='amazon', max_results=30, gender='unisex'):
        """
        Get products for a specific category from Amazon
        
        Args:
            category (str): Category name (Casual, Formal, Streetwear, etc.)
            source (str): 'amazon' (Flipkart temporarily disabled)
            max_results (int): Maximum products to return
            gender (str): User gender for filtering
            
        Returns:
            list: Product list from Amazon
        """
        # Map category to search queries (clothing focused)
        category_queries = {
            'Casual Wear': 'casual shirt tshirt jeans clothing',
            'Formal Wear': 'formal blazer pants shirt clothing',
            'Streetwear': 'streetwear hoodie jacket clothing',
            'Athletic Wear': 'athletic sports gym clothing',
            'Party Wear': 'party dress formal clothing',
            'Traditional Wear': 'ethnic traditional wear clothing',
            'Winter Wear': 'winter jacket coat sweater clothing',
            'Summer Wear': 'summer tshirt shorts clothing'
        }
        
        query = category_queries.get(category, category.lower())
        products = []
        
        # Only use Amazon for now
        amazon_products = self.search_amazon_products(query, category, max_results, gender)
        products.extend(amazon_products)
        
        return products[:max_results]
    
    def get_trending_products(self, limit=20, gender='unisex'):
        """
        Get trending products from Amazon
        
        Args:
            limit (int): Number of trending products
            gender (str): User gender for filtering
            
        Returns:
            list: Trending products
        """
        trending_queries = [
            'clothing bestseller',
            'trending fashion apparel',
            'popular clothing wear'
        ]
        
        all_products = []
        per_query_limit = limit // len(trending_queries)
        
        for query in trending_queries:
            # Fetch from Amazon only
            amazon = self.search_amazon_products(query, max_results=per_query_limit, gender=gender)
            all_products.extend(amazon)
        
        return all_products[:limit]
    
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
