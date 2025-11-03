from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import recommendation engine
from model.recommendation_engine import RecommendationEngine
from services.product_api import ProductAPIService

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')
    }
})

# Initialize services
recommendation_engine = RecommendationEngine()
product_api_service = ProductAPIService()

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'AI Fashion Recommendation API is running',
        'version': '1.0.0'
    })

@app.route('/api/test', methods=['GET'])
def test_api():
    """Test endpoint to verify ProductAPIService works"""
    try:
        products = product_api_service.search_amazon_products("shirt", max_results=3)
        return jsonify({
            'status': 'success',
            'count': len(products),
            'products': products,
            'message': 'Direct service call test'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """
    Get personalized product recommendations using real API data
    
    Request Body:
    {
        "interests": ["casual", "streetwear"],
        "fashionStyle": "minimalist",
        "gender": "male",
        "filters": {
            "category": "all",
            "priceRange": "all",
            "source": "all"
        }
    }
    """
    try:
        data = request.get_json()
        
        interests = data.get('interests', [])
        fashion_style = data.get('fashionStyle', '')
        gender = data.get('gender', 'unisex')
        filters = data.get('filters', {})
        
        # Combine interests and fashion style into user profile
        user_profile = {
            'interests': interests,
            'fashion_style': fashion_style,
            'gender': gender
        }
        
        # Fetch products from real APIs based on user interests and gender
        products = []
        
        # Fetch products based on category filter or interests
        category = filters.get('category', 'all')
        source = 'amazon'  # Only Amazon for now
        
        if category and category != 'all':
            # Fetch by category with gender filter
            products = product_api_service.get_products_by_category(
                category=category,
                source=source,
                max_results=50,
                gender=gender
            )
        else:
            # Fetch based on user interests with gender filter
            for interest in interests[:3]:  # Limit to first 3 interests to reduce API calls
                amazon_products = product_api_service.search_amazon_products(
                    query=interest,
                    max_results=20,
                    gender=gender
                )
                products.extend(amazon_products)
        
        # If no products found, get some trending items
        if not products:
            products = product_api_service.get_trending_products(limit=30, gender=gender)
        
        # Get recommendations using ML model
        recommendations = recommendation_engine.get_recommendations(
            user_profile=user_profile,
            products=products,
            filters=filters,
            top_n=20
        )
        
        return jsonify({
            'status': 'success',
            'count': len(recommendations),
            'products': recommendations,
            'message': 'Showing recommendations from Amazon'
        })
        
    except Exception as e:
        app.logger.error(f'Error in get_recommendations: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/similar-products', methods=['POST'])
def get_similar_products():
    """
    Get similar products using semantic embeddings
    
    Request Body:
    {
        "product": {...product object...},
        "limit": 5
    }
    """
    try:
        data = request.get_json()
        
        product = data.get('product')
        limit = data.get('limit', 5)
        
        if not product:
            return jsonify({
                'status': 'error',
                'message': 'Product data is required'
            }), 400
        
        # Fetch products from same category
        category = product.get('category', 'Casual Wear')
        all_products = product_api_service.get_products_by_category(
            category=category,
            source='both',
            max_results=100
        )
        
        # Get similar products using semantic embeddings
        similar_products = recommendation_engine.get_similar_products(
            product=product,
            all_products=all_products,
            top_n=limit
        )
        
        return jsonify({
            'status': 'success',
            'count': len(similar_products),
            'products': similar_products
        })
        
    except Exception as e:
        app.logger.error(f'Error in get_similar_products: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/track-interaction', methods=['POST'])
def track_interaction():
    """
    Track user interactions for improving recommendations
    
    Request Body:
    {
        "userId": "user123",
        "productId": "prod456",
        "interactionType": "view|click|like",
        "timestamp": "2025-10-29T10:00:00Z"
    }
    """
    try:
        data = request.get_json()
        
        user_id = data.get('userId')
        product_id = data.get('productId')
        interaction_type = data.get('interactionType')
        timestamp = data.get('timestamp')
        
        # In production, save this to a database for ML training
        app.logger.info(f'Interaction: User {user_id} {interaction_type} product {product_id}')
        
        # TODO: Save to database/Firestore for future ML model training
        
        return jsonify({
            'status': 'success',
            'message': 'Interaction tracked successfully'
        })
        
    except Exception as e:
        app.logger.error(f'Error in track_interaction: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/trending', methods=['GET'])
def get_trending():
    """
    Get trending products from Amazon
    
    Query Parameters:
    - limit: number of results (default: 20)
    """
    try:
        limit = int(request.args.get('limit', 20))
        
        # Fetch trending products from Amazon
        trending = product_api_service.get_trending_products(limit=limit)
        
        return jsonify({
            'status': 'success',
            'count': len(trending),
            'products': trending,
            'message': 'Showing trending products from Amazon'
        })
        
    except Exception as e:
        app.logger.error(f'Error in get_trending: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """
    Search products by keyword from Amazon
    
    Query Parameters:
    - q: search query
    - source: amazon (default: amazon)
    - limit: number of results (default: 20)
    """
    try:
        app.logger.info("=== /api/products/search endpoint called ===")
        query = request.args.get('q', '')
        source = 'amazon'  # Only Amazon for now
        limit = int(request.args.get('limit', 20))
        
        app.logger.info(f"Query: {query}, Limit: {limit}")
        
        if not query:
            return jsonify({
                'status': 'error',
                'message': 'Search query is required'
            }), 400
        
        # Fetch products from Amazon
        app.logger.info(f"Calling product_api_service.search_amazon_products...")
        products = product_api_service.search_amazon_products(
            query=query,
            max_results=limit
        )
        app.logger.info(f"Received {len(products)} products from service")
        
        return jsonify({
            'status': 'success',
            'count': len(products),
            'products': products,
            'message': 'Search results from Amazon'
        })
        
    except Exception as e:
        app.logger.error(f'Error in search_products: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/products/all', methods=['GET'])
def get_all_products():
    """
    Get all products from Amazon
    
    Query Parameters:
    - category: product category (optional)
    - source: amazon (default: amazon)
    - limit: number of results (default: 60)
    """
    try:
        print("=== /api/products/all endpoint called ===")
        category = request.args.get('category', 'all')
        source = 'amazon'  # Only Amazon for now
        limit = int(request.args.get('limit', 60))
        
        print(f"Category: {category}, Limit: {limit}")
        
        products = []
        
        if category and category != 'all':
            # Fetch by specific category
            print(f"Fetching products for category: {category}")
            products = product_api_service.get_products_by_category(
                category=category,
                source=source,
                max_results=limit
            )
        else:
            # Fetch from multiple categories
            print("Fetching products from multiple categories")
            categories = [
                'Casual Wear', 'Formal Wear', 'Streetwear',
                'Athletic Wear', 'Party Wear', 'Traditional Wear'
            ]
            
            per_category = limit // len(categories)
            
            for cat in categories:
                print(f"Fetching {per_category} products for: {cat}")
                cat_products = product_api_service.get_products_by_category(
                    category=cat,
                    source=source,
                    max_results=per_category
                )
                print(f"Got {len(cat_products)} products for {cat}")
                products.extend(cat_products)
        
        print(f"Total products collected: {len(products)}")
        
        # Limit to requested amount
        products = products[:limit]
        
        return jsonify({
            'status': 'success',
            'count': len(products),
            'products': products,
            'message': 'All products from Amazon'
        })
        
    except Exception as e:
        app.logger.error(f'Error in get_all_products: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/products/category/<category>', methods=['GET'])
def get_category_products(category):
    """
    Get products by category from Amazon
    
    Path Parameters:
    - category: product category
    
    Query Parameters:
    - source: amazon (default: amazon)
    - limit: number of results (default: 30)
    """
    try:
        source = 'amazon'  # Only Amazon for now
        limit = int(request.args.get('limit', 30))
        
        products = product_api_service.get_products_by_category(
            category=category,
            source=source,
            max_results=limit
        )
        
        return jsonify({
            'status': 'success',
            'count': len(products),
            'products': products,
            'category': category,
            'message': f'{category} products from Amazon'
        })
        
    except Exception as e:
        app.logger.error(f'Error in get_category_products: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404

@app.route('/api/calculate-size', methods=['POST'])
def calculate_size():
    """
    Calculate clothing size using AI/ML based on body measurements
    
    Request Body:
    {
        "gender": "male",
        "height": 170,
        "weight": 65,
        "chest": 95,
        "waist": 80,
        "hips": 95,
        "shoulder": 45,
        "age": 25
    }
    """
    try:
        data = request.get_json()
        
        # Extract measurements
        gender = data.get('gender', '').lower()
        height = float(data.get('height', 0))
        weight = float(data.get('weight', 0))
        chest = float(data.get('chest', 0))
        waist = float(data.get('waist', 0))
        hips = float(data.get('hips', 0)) if data.get('hips') else 0
        shoulder = float(data.get('shoulder', 0)) if data.get('shoulder') else 0
        age = int(data.get('age', 0)) if data.get('age') else 25
        
        # Validate required fields
        if not gender or height <= 0 or weight <= 0 or chest <= 0 or waist <= 0:
            return jsonify({
                'status': 'error',
                'message': 'Missing or invalid required measurements'
            }), 400
        
        # Calculate BMI
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        # Determine body type
        if gender == 'male':
            body_type = determine_male_body_type(chest, waist, shoulder)
        else:
            body_type = determine_female_body_type(chest, waist, hips)
        
        # Calculate size using ML logic
        size_result = calculate_size_ml(gender, chest, waist, hips, height, weight, bmi)
        
        # Generate recommendations
        recommendations = generate_fit_recommendations(size_result['size'], body_type, gender, bmi)
        
        return jsonify({
            'status': 'success',
            'recommended_size': size_result['size'],
            'confidence': size_result['confidence'],
            'alternative_sizes': size_result['alternatives'],
            'body_type': body_type,
            'bmi': round(bmi, 1),
            'recommendations': recommendations
        })
        
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': 'Invalid measurement values'
        }), 400
    except Exception as e:
        app.logger.error(f'Error in calculate_size: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

def determine_male_body_type(chest, waist, shoulder):
    """Determine male body type"""
    chest_waist_ratio = chest / waist if waist > 0 else 1
    
    if chest_waist_ratio > 1.3:
        return "Athletic/V-Shape"
    elif chest_waist_ratio > 1.15:
        return "Rectangle/Straight"
    elif chest_waist_ratio < 1.0:
        return "Round/Apple"
    else:
        return "Trapezoid"

def determine_female_body_type(chest, waist, hips):
    """Determine female body type"""
    if hips == 0:
        hips = chest  # Estimate if not provided
    
    chest_waist_diff = abs(chest - waist)
    hip_waist_diff = abs(hips - waist)
    chest_hip_diff = abs(chest - hips)
    
    if chest_hip_diff <= 5 and waist < chest * 0.75:
        return "Hourglass"
    elif hips > chest and hip_waist_diff > chest_waist_diff:
        return "Pear/Triangle"
    elif chest > hips and chest_waist_diff > hip_waist_diff:
        return "Inverted Triangle"
    elif chest_hip_diff <= 5:
        return "Rectangle"
    else:
        return "Apple/Round"

def calculate_size_ml(gender, chest, waist, hips, height, weight, bmi):
    """
    ML-based size calculation using measurement analysis
    This is a simplified ML approach using rule-based logic
    In production, this would use a trained model
    """
    
    # Size charts (in cm)
    if gender == 'male':
        size_chart = {
            'XS': {'chest': (81, 86), 'waist': (66, 71)},
            'S': {'chest': (86, 91), 'waist': (71, 76)},
            'M': {'chest': (91, 97), 'waist': (76, 81)},
            'L': {'chest': (97, 102), 'waist': (81, 86)},
            'XL': {'chest': (102, 109), 'waist': (86, 94)},
            'XXL': {'chest': (109, 117), 'waist': (94, 102)},
            'XXXL': {'chest': (117, 127), 'waist': (102, 114)}
        }
    else:  # female
        size_chart = {
            'XS': {'chest': (78, 82), 'waist': (60, 64), 'hips': (86, 90)},
            'S': {'chest': (82, 86), 'waist': (64, 68), 'hips': (90, 94)},
            'M': {'chest': (86, 92), 'waist': (68, 74), 'hips': (94, 99)},
            'L': {'chest': (92, 98), 'waist': (74, 80), 'hips': (99, 104)},
            'XL': {'chest': (98, 106), 'waist': (80, 88), 'hips': (104, 112)},
            'XXL': {'chest': (106, 116), 'waist': (88, 98), 'hips': (112, 120)},
            'XXXL': {'chest': (116, 128), 'waist': (98, 110), 'hips': (120, 132)}
        }
    
    # Calculate fit scores for each size
    size_scores = {}
    for size, measurements in size_chart.items():
        chest_min, chest_max = measurements['chest']
        waist_min, waist_max = measurements['waist']
        
        # Calculate how well measurements fit in the range
        chest_score = 0
        if chest_min <= chest <= chest_max:
            chest_score = 100
        else:
            # Calculate distance from range
            if chest < chest_min:
                chest_score = max(0, 100 - (chest_min - chest) * 2)
            else:
                chest_score = max(0, 100 - (chest - chest_max) * 2)
        
        waist_score = 0
        if waist_min <= waist <= waist_max:
            waist_score = 100
        else:
            if waist < waist_min:
                waist_score = max(0, 100 - (waist_min - waist) * 2)
            else:
                waist_score = max(0, 100 - (waist - waist_max) * 2)
        
        # For females, include hip measurement
        if gender == 'female' and hips > 0:
            hip_min, hip_max = measurements['hips']
            hip_score = 0
            if hip_min <= hips <= hip_max:
                hip_score = 100
            else:
                if hips < hip_min:
                    hip_score = max(0, 100 - (hip_min - hips) * 2)
                else:
                    hip_score = max(0, 100 - (hips - hip_max) * 2)
            
            total_score = (chest_score * 0.4 + waist_score * 0.3 + hip_score * 0.3)
        else:
            total_score = (chest_score * 0.6 + waist_score * 0.4)
        
        size_scores[size] = total_score
    
    # Get best fitting size
    sorted_sizes = sorted(size_scores.items(), key=lambda x: x[1], reverse=True)
    recommended_size = sorted_sizes[0][0]
    confidence = int(sorted_sizes[0][1])
    
    # Get alternative sizes (within 20% of best score)
    alternatives = []
    for size, score in sorted_sizes[1:3]:
        if score >= confidence * 0.8:
            alternatives.append(size)
    
    return {
        'size': recommended_size,
        'confidence': confidence,
        'alternatives': alternatives
    }

def generate_fit_recommendations(size, body_type, gender, bmi):
    """Generate personalized fit recommendations"""
    recommendations = []
    
    # BMI-based recommendations
    if bmi < 18.5:
        recommendations.append("Consider slim-fit styles for a more tailored look")
    elif bmi > 25:
        recommendations.append("Regular fit styles provide comfortable wear")
    
    # Body type recommendations
    if gender == 'male':
        if 'Athletic' in body_type:
            recommendations.append("Fitted shirts will complement your V-shape")
        elif 'Round' in body_type:
            recommendations.append("Vertical patterns can create a lengthening effect")
    else:
        if 'Hourglass' in body_type:
            recommendations.append("Fitted or wrap styles accentuate your shape")
        elif 'Pear' in body_type:
            recommendations.append("A-line silhouettes balance your proportions")
        elif 'Inverted' in body_type:
            recommendations.append("V-necks draw attention upward")
    
    # Size-specific recommendations
    if size in ['XS', 'S']:
        recommendations.append("Check if petite sizes are available")
    elif size in ['XXL', 'XXXL']:
        recommendations.append("Look for extended size ranges for best fit")
    
    return recommendations[:3]  # Return top 3 recommendations

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
