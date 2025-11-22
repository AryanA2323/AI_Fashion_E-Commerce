"""
Fake Store API Integration
Free API with no credentials required
Website: https://fakestoreapi.com/
"""
import requests
import logging

logger = logging.getLogger(__name__)

class FakeStoreAPI:
    """
    Integration with Fake Store API for product data
    Completely free, no API key required
    """
    
    BASE_URL = "https://fakestoreapi.com"
    
    def __init__(self):
        self.session = requests.Session()
        logger.info("✓ FakeStore API initialized (no credentials required)")
    
    def get_all_clothing_products(self):
        """Get all clothing products (men's and women's)"""
        try:
            mens_products = self.get_mens_clothing()
            womens_products = self.get_womens_clothing()
            return mens_products + womens_products
        except Exception as e:
            logger.error(f"Error fetching all clothing: {e}")
            return []
    
    def get_mens_clothing(self):
        """Get men's clothing products"""
        return self._get_products_by_category("men's clothing")
    
    def get_womens_clothing(self):
        """Get women's clothing products"""
        return self._get_products_by_category("women's clothing")
    
    def search_clothing(self, query, gender='unisex'):
        """
        Search clothing products by query
        
        Args:
            query (str): Search query
            gender (str): 'male', 'female', or 'unisex'
        
        Returns:
            list: Filtered products
        """
        all_products = []
        
        if gender == 'male' or gender == 'unisex':
            all_products.extend(self.get_mens_clothing())
        
        if gender == 'female' or gender == 'unisex':
            all_products.extend(self.get_womens_clothing())
        
        # Filter by query
        if query:
            query_lower = query.lower()
            all_products = [
                p for p in all_products 
                if query_lower in p['title'].lower() or 
                   query_lower in p.get('description', '').lower() or
                   query_lower in p.get('category', '').lower()
            ]
        
        return all_products
    
    def _get_products_by_category(self, category):
        """
        Fetch products by category from Fake Store API
        
        Args:
            category (str): API category ('men\'s clothing' or 'women\'s clothing')
        
        Returns:
            list: Formatted products
        """
        try:
            url = f"{self.BASE_URL}/products/category/{category}"
            logger.info(f"🔍 Fetching from Fake Store API: {url}")
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            products = response.json()
            
            formatted = self._format_products(products, category)
            logger.info(f"✓ Fetched {len(formatted)} products from category: {category}")
            
            return formatted
            
        except Exception as e:
            logger.error(f"Error fetching category {category}: {e}")
            return []
    
    def _format_products(self, products, api_category):
        """
        Format Fake Store API products to our unified structure
        
        Args:
            products (list): Raw products from Fake Store API
            api_category (str): API category name
        
        Returns:
            list: Formatted products
        """
        formatted = []
        
        for product in products:
            try:
                # Convert USD to INR (approximate rate: 1 USD = 83 INR)
                price_usd = float(product.get('price', 0))
                price_inr = round(price_usd * 83, 2)
                original_price_inr = round(price_inr * 1.25, 2)  # Add 25% as original price
                
                # Extract rating
                rating_data = product.get('rating', {})
                rating = float(rating_data.get('rate', 4.0))
                review_count = int(rating_data.get('count', 0))
                
                # Detect our internal category
                internal_category = self._detect_category(product['title'], api_category)
                
                # Extract gender
                gender = 'male' if "men's" in api_category.lower() else 'female'
                
                formatted_product = {
                    'id': f"fs_{product['id']}",
                    'title': product['title'],
                    'description': product.get('description', ''),
                    'price': price_inr,
                    'originalPrice': original_price_inr,
                    'currency': 'INR',
                    'image': product['image'],
                    'rating': min(rating, 5.0),
                    'reviews': review_count,
                    'url': f"https://fakestoreapi.com/products/{product['id']}",
                    'source': 'FakeStore',
                    'category': internal_category,
                    'gender': gender,
                    'tags': self._extract_tags(product['title'], internal_category),
                    'inStock': True
                }
                
                formatted.append(formatted_product)
                
            except Exception as e:
                logger.error(f"Error formatting product {product.get('id')}: {e}")
                continue
        
        return formatted
    
    def _detect_category(self, title, api_category):
        """
        Detect internal category from product title and API category
        
        Args:
            title (str): Product title
            api_category (str): Fake Store API category
        
        Returns:
            str: Internal category
        """
        title_lower = title.lower()
        
        # Men's clothing categories
        if "men's clothing" in api_category.lower():
            if any(word in title_lower for word in ['jacket', 'coat', 'blazer']):
                return 'formal'
            elif any(word in title_lower for word in ['cotton', 'slim', 'casual']):
                return 'casual'
            else:
                return 'casual'
        
        # Women's clothing categories
        elif "women's clothing" in api_category.lower():
            if any(word in title_lower for word in ['short sleeve', 'tank']):
                return 'casual'
            elif any(word in title_lower for word in ['jacket', 'leather']):
                return 'streetwear'
            elif any(word in title_lower for word in ['rain', 'removable']):
                return 'athletic'
            else:
                return 'casual'
        
        return 'casual'
    
    def _extract_tags(self, title, category):
        """
        Extract tags from product title
        
        Args:
            title (str): Product title
            category (str): Product category
        
        Returns:
            list: Tags
        """
        tags = [category]
        title_lower = title.lower()
        
        # Common fashion tags
        tag_keywords = {
            'cotton': 'cotton',
            'slim': 'slim fit',
            'jacket': 'jacket',
            'casual': 'casual',
            'formal': 'formal',
            'fit': 'fitted',
            'sleeve': 'sleeve',
            'short': 'short',
            'long': 'long',
            'collar': 'collar',
            'removable': 'removable',
            'hood': 'hooded',
            'pocket': 'pockets',
            'zipper': 'zipper',
            'button': 'button'
        }
        
        for keyword, tag in tag_keywords.items():
            if keyword in title_lower and tag not in tags:
                tags.append(tag)
        
        return tags[:5]  # Limit to 5 tags
