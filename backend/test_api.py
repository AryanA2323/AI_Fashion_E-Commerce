import requests
import os
from dotenv import load_dotenv

load_dotenv()

rapidapi_key = os.getenv('RAPIDAPI_KEY')

print(f"Testing RapidAPI connection...")
print(f"API Key: {rapidapi_key[:15]}...")

# Test Amazon API
url = "https://real-time-amazon-data.p.rapidapi.com/search"
params = {
    "query": "shirt",
    "country": "US",
    "page": "1"
}
headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
}

try:
    print("\nCalling Amazon API...")
    response = requests.get(url, params=params, headers=headers, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nSuccess! Found {len(data.get('data', {}).get('products', []))} products")
    else:
        print(f"\nError: {response.text}")
        
except Exception as e:
    print(f"\nException occurred: {str(e)}")
