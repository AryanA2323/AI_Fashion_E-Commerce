from flask import Flask, jsonify
from dotenv import load_dotenv
from services.product_api import ProductAPIService

load_dotenv()

app = Flask(__name__)
product_api_service = ProductAPIService()

@app.route('/')
def home():
    return jsonify({'status': 'ok'})

@app.route('/test')
def test():
    try:
        products = product_api_service.search_amazon_products("shirt", max_results=2)
        return jsonify({
            'status': 'success',
            'count': len(products),
            'products': products[:2]  # Limit to 2 for testing
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

if __name__ == '__main__':
    print("Starting test Flask app...")
    app.run(host='0.0.0.0', port=5001, debug=False)
