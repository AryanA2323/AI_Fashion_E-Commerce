import sys
sys.path.insert(0, 'C:\\Projects\\ecommerce-ai-fashion\\backend')

from services.product_api import ProductAPIService
from dotenv import load_dotenv

load_dotenv()

print("Creating ProductAPIService...")
service = ProductAPIService()

print("\nTesting search_amazon_products...")
products = service.search_amazon_products("shirt", max_results=3)

print(f"\nGot {len(products)} products")
if products:
    print(f"First product: {products[0].get('title', 'No title')}")
