"""
Product Fetcher Utility
Fetches products from Amazon and Flipkart APIs
Currently using mock data - integrate with actual APIs in production
"""

import os
import json

# Mock product data (same as frontend for consistency)
MOCK_PRODUCTS = [
    {
        'id': 'amz-casual-001',
        'title': 'Classic Cotton T-Shirt - Comfortable Everyday Wear',
        'price': 499,
        'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Casual',
        'rating': 4.5,
        'tags': ['casual', 'cotton', 'comfortable', 'everyday'],
        'description': 'Soft cotton t-shirt perfect for everyday casual wear'
    },
    {
        'id': 'amz-casual-002',
        'title': 'Slim Fit Denim Jeans - Blue Wash',
        'price': 1299,
        'image': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Casual',
        'rating': 4.3,
        'tags': ['casual', 'denim', 'jeans', 'blue'],
        'description': 'Classic blue denim jeans with slim fit design'
    },
    {
        'id': 'amz-casual-003',
        'title': 'Casual Hoodie - Fleece Fabric',
        'price': 899,
        'image': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Casual',
        'rating': 4.6,
        'tags': ['casual', 'hoodie', 'comfortable', 'winter'],
        'description': 'Warm fleece hoodie for casual winter wear'
    },
    {
        'id': 'flp-formal-001',
        'title': 'Premium Formal Shirt - White Cotton',
        'price': 1499,
        'image': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400',
        'link': '#',
        'source': 'Flipkart',
        'category': 'Formal',
        'rating': 4.7,
        'tags': ['formal', 'shirt', 'office', 'professional'],
        'description': 'Professional white formal shirt for office wear'
    },
    {
        'id': 'flp-formal-002',
        'title': 'Formal Blazer - Slim Fit Black',
        'price': 3999,
        'image': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400',
        'link': '#',
        'source': 'Flipkart',
        'category': 'Formal',
        'rating': 4.8,
        'tags': ['formal', 'blazer', 'business', 'professional'],
        'description': 'Elegant black blazer for business meetings'
    },
    {
        'id': 'amz-street-001',
        'title': 'Graphic Print Oversized T-Shirt',
        'price': 799,
        'image': 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Streetwear',
        'rating': 4.5,
        'tags': ['streetwear', 'graphic', 'oversized', 'urban'],
        'description': 'Trendy oversized t-shirt with bold graphics'
    },
    {
        'id': 'amz-street-002',
        'title': 'Urban Cargo Pants - Multiple Pockets',
        'price': 1899,
        'image': 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Streetwear',
        'rating': 4.6,
        'tags': ['streetwear', 'cargo', 'urban', 'utility'],
        'description': 'Stylish cargo pants with multiple utility pockets'
    },
    {
        'id': 'flp-athletic-001',
        'title': 'Performance Sports T-Shirt - Quick Dry',
        'price': 599,
        'image': 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400',
        'link': '#',
        'source': 'Flipkart',
        'category': 'Athletic',
        'rating': 4.5,
        'tags': ['athletic', 'sports', 'gym', 'fitness'],
        'description': 'Moisture-wicking sports t-shirt for workouts'
    },
    {
        'id': 'flp-athletic-002',
        'title': 'Training Shorts - Breathable Fabric',
        'price': 699,
        'image': 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400',
        'link': '#',
        'source': 'Flipkart',
        'category': 'Athletic',
        'rating': 4.4,
        'tags': ['athletic', 'shorts', 'training', 'gym'],
        'description': 'Lightweight training shorts with breathable fabric'
    },
    {
        'id': 'amz-party-001',
        'title': 'Party Wear Silk Kurta Set',
        'price': 3499,
        'image': 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
        'link': '#',
        'source': 'Amazon',
        'category': 'Party',
        'rating': 4.8,
        'tags': ['party', 'ethnic', 'silk', 'traditional'],
        'description': 'Elegant silk kurta set for special occasions'
    },
    {
        'id': 'flp-traditional-001',
        'title': 'Traditional Cotton Kurta',
        'price': 1299,
        'image': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
        'link': '#',
        'source': 'Flipkart',
        'category': 'Traditional',
        'rating': 4.6,
        'tags': ['traditional', 'ethnic', 'kurta', 'cotton'],
        'description': 'Comfortable cotton kurta for traditional occasions'
    },
]

def fetch_products_from_apis(interests, filters=None):
    """
    Fetch products from Amazon and Flipkart APIs
    Currently returns mock data - implement actual API calls in production
    
    Args:
        interests (list): User's interests
        filters (dict): Active filters
        
    Returns:
        list: List of products
    """
    # In production, implement actual API calls:
    # - Amazon Product Advertising API
    # - Flipkart Affiliate API
    
    # For now, return mock products
    products = MOCK_PRODUCTS.copy()
    
    # Basic filtering by source
    if filters and filters.get('source') and filters['source'] != 'all':
        source = filters['source']
        products = [p for p in products if p['source'].lower() == source.lower()]
    
    return products

def fetch_amazon_products(keywords, max_results=10):
    """
    Fetch products from Amazon Product Advertising API
    
    Args:
        keywords (str): Search keywords
        max_results (int): Maximum number of results
        
    Returns:
        list: List of Amazon products
    """
    # TODO: Implement Amazon Product Advertising API integration
    # Reference: https://webservices.amazon.com/paapi5/documentation/
    
    """
    Example Implementation:
    
    from paapi5_python_sdk.api.default_api import DefaultApi
    from paapi5_python_sdk.search_items_request import SearchItemsRequest
    
    api = DefaultApi(
        access_key=os.getenv('AMAZON_ACCESS_KEY'),
        secret_key=os.getenv('AMAZON_SECRET_KEY'),
        host='webservices.amazon.in',
        region='us-east-1'
    )
    
    request = SearchItemsRequest(
        partner_tag=os.getenv('AMAZON_ASSOCIATE_TAG'),
        partner_type='Associates',
        keywords=keywords,
        search_index='Fashion',
        item_count=max_results,
        resources=[
            'Images.Primary.Large',
            'ItemInfo.Title',
            'Offers.Listings.Price'
        ]
    )
    
    response = api.search_items(request)
    # Parse and return products
    """
    
    return []

def fetch_flipkart_products(keywords, max_results=10):
    """
    Fetch products from Flipkart Affiliate API
    
    Args:
        keywords (str): Search keywords
        max_results (int): Maximum number of results
        
    Returns:
        list: List of Flipkart products
    """
    # TODO: Implement Flipkart Affiliate API integration
    # Reference: https://affiliate.flipkart.com/api-docs/
    
    """
    Example Implementation:
    
    import requests
    
    headers = {
        'Fk-Affiliate-Id': os.getenv('FLIPKART_AFFILIATE_ID'),
        'Fk-Affiliate-Token': os.getenv('FLIPKART_AFFILIATE_TOKEN')
    }
    
    url = 'https://affiliate-api.flipkart.net/affiliate/search/json'
    params = {
        'query': keywords,
        'resultCount': max_results
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # Parse and return products
    """
    
    return []

def parse_amazon_product(item):
    """
    Parse Amazon API response item into standardized format
    """
    return {
        'id': item.get('ASIN'),
        'title': item.get('ItemInfo', {}).get('Title', {}).get('DisplayValue', ''),
        'price': item.get('Offers', {}).get('Listings', [{}])[0].get('Price', {}).get('Amount', 0),
        'image': item.get('Images', {}).get('Primary', {}).get('Large', {}).get('URL', ''),
        'link': item.get('DetailPageURL', ''),
        'source': 'Amazon',
        'rating': 0,  # Parse from customer reviews if available
    }

def parse_flipkart_product(item):
    """
    Parse Flipkart API response item into standardized format
    """
    return {
        'id': item.get('productId'),
        'title': item.get('title', ''),
        'price': float(item.get('sellingPrice', {}).get('amount', 0)),
        'image': item.get('images', [{}])[0].get('url', ''),
        'link': item.get('productUrl', ''),
        'source': 'Flipkart',
        'rating': float(item.get('rating', 0)),
    }
