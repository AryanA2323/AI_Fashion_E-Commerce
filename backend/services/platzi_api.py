"""
Platzi Fake Store API Integration
Free API with 200+ products including fashion items
Website: https://fakeapi.platzi.com/
Documentation: https://fakeapi.platzi.com/doc/
"""
import requests
import logging

logger = logging.getLogger(__name__)

class PlatziAPI:
    """
    Integration with Platzi Fake Store API
    200+ products, completely free, no API key required
    """
    
    BASE_URL = "https://api.escuelajs.co/api/v1"
    
    # Category IDs for fashion items
    CATEGORY_CLOTHES = 1
    CATEGORY_SHOES = 4
    
    def __init__(self):
        self.session = requests.Session()
        logger.info("✓ Platzi Fake Store API initialized (no credentials required)")
        print("✓ Platzi API: 200+ products available")
    
    def get_all_fashion_products(self, limit=100):
        """Get all fashion products (clothes + shoes)"""
        try:
            clothes = self.get_clothes(limit=limit//2)
            shoes = self.get_shoes(limit=limit//2)
            return clothes + shoes
        except Exception as e:
            logger.error(f"Error fetching all fashion: {e}")
            return []
    
    def get_clothes(self, limit=50):
        """Get clothing products"""
        return self._get_products_by_category(self.CATEGORY_CLOTHES, limit)
    
    def get_shoes(self, limit=50):
        """Get shoe products"""
        return self._get_products_by_category(self.CATEGORY_SHOES, limit)
    
    def search_fashion(self, query, gender='unisex', limit=50):
        """
        Search fashion products
        
        Args:
            query (str): Search query
            gender (str): 'male', 'female', or 'unisex'
            limit (int): Maximum results
        
        Returns:
            list: Filtered products
        """
        # Get all fashion products
        products = self.get_all_fashion_products(limit)
        
        # Filter by query
        if query:
            query_lower = query.lower()
            products = [
                p for p in products 
                if query_lower in p['title'].lower() or 
                   query_lower in p.get('description', '').lower()
            ]
        
        # Filter by gender
        if gender != 'unisex':
            products = [p for p in products if p.get('gender') == gender]
        
        return products
    
    def _get_products_by_category(self, category_id, limit=50):
        """
        Fetch products by category from Platzi API
        
        Args:
            category_id (int): Category ID (1=Clothes, 4=Shoes)
            limit (int): Maximum results
        
        Returns:
            list: Formatted products
        """
        try:
            url = f"{self.BASE_URL}/products"
            params = {
                'categoryId': category_id,
                'offset': 0,
                'limit': limit
            }
            
            logger.info(f"🔍 Fetching from Platzi API: {url}")
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            products = response.json()
            
            formatted = self._format_products(products, category_id)
            logger.info(f"✓ Fetched {len(formatted)} products from category: {category_id}")
            
            return formatted
            
        except Exception as e:
            logger.error(f"Error fetching category {category_id}: {e}")
            return []
    
    def _format_products(self, products, category_id):
        """
        Format Platzi API products to our unified structure
        
        Args:
            products (list): Raw products from Platzi API
            category_id (int): Category ID
        
        Returns:
            list: Formatted products
        """
        formatted = []
        
        for product in products:
            try:
                # Skip if no valid data
                if not product.get('title') or not product.get('price'):
                    continue
                
                # Convert USD to INR (approximate rate: 1 USD = 83 INR)
                price_usd = float(product.get('price', 0))
                if price_usd <= 0:
                    continue
                    
                price_inr = round(price_usd * 83, 2)
                original_price_inr = round(price_inr * 1.3, 2)  # Add 30% as original price
                
                # Get images (Platzi returns array of images)
                images = product.get('images', [])
                image_url = images[0] if images and len(images) > 0 else ''
                
                # Clean image URL (remove brackets if present)
                if image_url:
                    image_url = image_url.replace('["', '').replace('"]', '').replace('[', '').replace(']', '').replace('"', '')
                
                # Detect category and gender
                title_lower = product['title'].lower()
                description = product.get('description', '').lower()
                
                internal_category = self._detect_category(title_lower, description, category_id)
                gender = self._detect_gender(title_lower, description)
                
                formatted_product = {
                    'id': f"platzi_{product['id']}",
                    'title': product['title'],
                    'description': product.get('description', '')[:200],  # Limit description
                    'price': price_inr,
                    'originalPrice': original_price_inr,
                    'currency': 'INR',
                    'image': image_url,
                    'rating': self._generate_rating(),  # Random realistic rating
                    'reviews': self._generate_review_count(),
                    'url': f"https://fakeapi.platzi.com/products/{product['id']}",
                    'source': 'Platzi',
                    'category': internal_category,
                    'gender': gender,
                    'tags': self._extract_tags(title_lower, internal_category),
                    'inStock': True
                }
                
                formatted.append(formatted_product)
                
            except Exception as e:
                logger.error(f"Error formatting product {product.get('id')}: {e}")
                continue
        
        return formatted
    
    def _detect_category(self, title, description, category_id):
        """Detect internal category"""
        text = f"{title} {description}"
        
        # Category mapping
        if category_id == self.CATEGORY_SHOES:
            if any(word in text for word in ['sneaker', 'sport', 'running', 'athletic']):
                return 'athletic'
            elif any(word in text for word in ['formal', 'dress', 'oxford', 'leather']):
                return 'formal'
            else:
                return 'casual'
        
        # Clothes category
        if any(word in text for word in ['suit', 'blazer', 'formal', 'dress shirt', 'tie']):
            return 'formal'
        elif any(word in text for word in ['hoodie', 'street', 'urban', 'hip hop']):
            return 'streetwear'
        elif any(word in text for word in ['sport', 'athletic', 'gym', 'training', 'running']):
            return 'athletic'
        elif any(word in text for word in ['party', 'evening', 'cocktail', 'gown']):
            return 'party'
        elif any(word in text for word in ['ethnic', 'traditional', 'kurta', 'saree']):
            return 'traditional'
        else:
            return 'casual'
    
    def _detect_gender(self, title, description):
        """Detect gender from product title/description"""
        text = f"{title} {description}"
        
        # Check for gender keywords
        male_keywords = ['men', 'mens', "men's", 'male', 'him', 'boy', 'guys']
        female_keywords = ['women', 'womens', "women's", 'female', 'her', 'girl', 'ladies']
        
        has_male = any(keyword in text for keyword in male_keywords)
        has_female = any(keyword in text for keyword in female_keywords)
        
        if has_male and not has_female:
            return 'male'
        elif has_female and not has_male:
            return 'female'
        else:
            return 'unisex'
    
    def _extract_tags(self, title, category):
        """Extract tags from product title"""
        tags = [category]
        
        tag_keywords = {
            'cotton': 'cotton',
            'silk': 'silk',
            'leather': 'leather',
            'denim': 'denim',
            'casual': 'casual',
            'formal': 'formal',
            'slim': 'slim fit',
            'comfortable': 'comfortable',
            'premium': 'premium',
            'designer': 'designer',
            'vintage': 'vintage',
            'modern': 'modern'
        }
        
        for keyword, tag in tag_keywords.items():
            if keyword in title and tag not in tags:
                tags.append(tag)
        
        return tags[:5]
    
    def _generate_rating(self):
        """Generate realistic rating between 3.5 and 5.0"""
        import random
        return round(random.uniform(3.5, 5.0), 1)
    
    def _generate_review_count(self):
        """Generate realistic review count"""
        import random
        return random.randint(50, 2500)
