import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

# Don't import sentence_transformers at module level - it causes issues with Python 3.13
SENTENCE_TRANSFORMERS_AVAILABLE = False
print("⚠ sentence-transformers not available, using TF-IDF only")

class RecommendationEngine:
    """
    Enhanced AI-based recommendation engine using Sentence Transformers
    for better semantic understanding of products and user preferences
    
    Features:
    - Sentence Transformers (pre-trained BERT) for semantic similarity
    - Fallback to TF-IDF for reliability
    - Hybrid scoring combining both methods
    - No compilation required - uses pre-trained models
    """
    
    def __init__(self):
        # TF-IDF vectorizer (fallback method)
        self.vectorizer = TfidfVectorizer(
            max_features=500,
            stop_words='english',
            ngram_range=(1, 2)
        )
        
        # Sentence Transformer model (semantic embeddings)
        self.semantic_model = None
        self.use_semantic = False  # Disabled due to Python 3.13 compatibility
    
    def _get_semantic_embedding(self, text):
        """
        Get semantic embedding for text using Sentence Transformers
        
        Args:
            text (str): Input text
            
        Returns:
            np.array: Embedding vector
        """
        if not self.use_semantic or not self.semantic_model:
            return None
        
        try:
            embedding = self.semantic_model.encode(text, convert_to_numpy=True)
            return embedding
        except Exception as e:
            print(f"⚠ Error generating semantic embedding: {str(e)}")
            return None

    def get_recommendations(self, user_profile, products, filters=None, top_n=20):
        """
        Get personalized product recommendations using hybrid Semantic + TF-IDF
        
        Args:
            user_profile (dict): User's interests and fashion style
            products (list): List of product dictionaries
            filters (dict): Active filters
            top_n (int): Number of recommendations to return
            
        Returns:
            list: Sorted list of recommended products with relevance scores
        """
        print(f"🤖 Recommendation engine: Received {len(products)} products")
        print(f"🤖 User profile: {user_profile}")
        print(f"🤖 Filters: {filters}")
        
        if not products:
            print("⚠️  No products to recommend!")
            return []
        
        # Create user preference text
        user_text = self._create_user_profile_text(user_profile)
        
        # Create product texts
        product_texts = [self._create_product_text(p) for p in products]
        
        try:
            # Method 1: Semantic similarity using Sentence Transformers
            semantic_scores = []
            if self.use_semantic and self.semantic_model is not None:
                # Get user embedding
                user_embedding = self._get_semantic_embedding(user_text)
                
                if user_embedding is not None:
                    # Get product embeddings
                    product_embeddings = self.semantic_model.encode(
                        product_texts, 
                        convert_to_numpy=True,
                        show_progress_bar=False
                    )
                    
                    # Calculate cosine similarities
                    for product_embedding in product_embeddings:
                        similarity = np.dot(user_embedding, product_embedding) / (
                            np.linalg.norm(user_embedding) * np.linalg.norm(product_embedding) + 1e-10
                        )
                        semantic_scores.append(float(similarity))
                else:
                    semantic_scores = [0.0] * len(products)
            else:
                semantic_scores = [0.0] * len(products)
            
            # Method 2: TF-IDF similarity (fallback/complement)
            all_texts = [user_text] + product_texts
            tfidf_matrix = self.vectorizer.fit_transform(all_texts)
            user_vector = tfidf_matrix[0:1]
            product_vectors = tfidf_matrix[1:]
            tfidf_scores = cosine_similarity(user_vector, product_vectors)[0]
            
            # Hybrid scoring: 70% Semantic + 30% TF-IDF
            # If Semantic is not available, use 100% TF-IDF
            products_with_scores = []
            for i, product in enumerate(products):
                product_copy = product.copy()
                
                if self.use_semantic and self.semantic_model is not None and semantic_scores[i] > 0:
                    # Hybrid score
                    hybrid_score = 0.7 * semantic_scores[i] + 0.3 * tfidf_scores[i]
                else:
                    # TF-IDF only
                    hybrid_score = tfidf_scores[i]
                
                product_copy['relevanceScore'] = float(hybrid_score)
                product_copy['semanticScore'] = float(semantic_scores[i]) if semantic_scores else 0.0
                product_copy['tfidfScore'] = float(tfidf_scores[i])
                products_with_scores.append(product_copy)
            
            # Sort by relevance score
            products_with_scores.sort(key=lambda x: x['relevanceScore'], reverse=True)
            
            # Apply post-processing filters
            print(f"🤖 Before filtering: {len(products_with_scores)} products")
            filtered_products = self._apply_filters(products_with_scores, filters)
            print(f"🤖 After filtering: {len(filtered_products)} products")
            
            if len(filtered_products) > 0:
                print(f"🤖 Top product: {filtered_products[0].get('title', 'Unknown')} (score: {filtered_products[0].get('relevanceScore', 0):.3f})")
            
            # Return top N recommendations
            return filtered_products[:top_n]
            
        except Exception as e:
            print(f"Error in recommendation engine: {str(e)}")
            import traceback
            traceback.print_exc()
            # Fallback: return products as-is with default scores
            for product in products:
                product['relevanceScore'] = 0.5
            return products[:top_n]
    
    def _create_user_profile_text(self, user_profile):
        """
        Create a text representation of user profile
        
        Args:
            user_profile (dict): User's interests and fashion style
            
        Returns:
            str: Combined text of user preferences
        """
        interests = user_profile.get('interests', [])
        fashion_style = user_profile.get('fashion_style', '')
        
        # Repeat interests and style to give them more weight
        text_parts = []
        
        # Add interests (repeat 3 times for emphasis)
        for interest in interests:
            text_parts.extend([interest] * 3)
        
        # Add fashion style (repeat 2 times)
        if fashion_style:
            text_parts.extend([fashion_style] * 2)
        
        return ' '.join(text_parts).lower()
    
    def _create_product_text(self, product):
        """
        Create a text representation of product
        
        Args:
            product (dict): Product information
            
        Returns:
            str: Combined text of product features
        """
        parts = []
        
        # Add title
        if 'title' in product:
            parts.append(product['title'])
        
        # Add category
        if 'category' in product:
            parts.append(product['category'])
        
        # Add tags
        if 'tags' in product and isinstance(product['tags'], list):
            parts.extend(product['tags'])
        
        # Add description if available
        if 'description' in product:
            parts.append(product['description'])
        
        return ' '.join(parts).lower()
    
    def _apply_filters(self, products, filters):
        """
        Apply user filters to products
        
        Args:
            products (list): List of products
            filters (dict): Filter criteria
            
        Returns:
            list: Filtered products
        """
        if not filters:
            return products
        
        filtered = products.copy()
        
        # Filter by category
        if filters.get('category') and filters['category'] != 'all':
            category = filters['category'].lower()
            filtered = [p for p in filtered if p.get('category', '').lower() == category]
        
        # Filter by price range
        if filters.get('priceRange') and filters['priceRange'] != 'all':
            price_range = filters['priceRange']
            filtered = self._filter_by_price(filtered, price_range)
        
        # Filter by source
        if filters.get('source') and filters['source'] != 'all':
            source = filters['source'].lower()
            filtered = [p for p in filtered if p.get('source', '').lower() == source]
        
        return filtered
    
    def _filter_by_price(self, products, price_range):
        """
        Filter products by price range
        
        Args:
            products (list): List of products
            price_range (str): Price range string (e.g., "1000-2500")
            
        Returns:
            list: Filtered products
        """
        if price_range == '0-1000':
            return [p for p in products if p.get('price', 0) < 1000]
        elif price_range == '1000-2500':
            return [p for p in products if 1000 <= p.get('price', 0) < 2500]
        elif price_range == '2500-5000':
            return [p for p in products if 2500 <= p.get('price', 0) < 5000]
        elif price_range == '5000-10000':
            return [p for p in products if 5000 <= p.get('price', 0) < 10000]
        elif price_range == '10000+':
            return [p for p in products if p.get('price', 0) >= 10000]
        else:
            return products
    
    def get_similar_products(self, product, all_products, top_n=5):
        """
        Find similar products based on semantic embeddings
        
        Args:
            product (dict): Target product
            all_products (list): List of all products
            top_n (int): Number of similar products to return
            
        Returns:
            list: Similar products with similarity scores
        """
        if not self.use_semantic or not self.semantic_model:
            # Fallback to TF-IDF
            return self._get_similar_products_tfidf(product, all_products, top_n)
        
        try:
            # Get target product embedding
            target_text = self._create_product_text(product)
            target_embedding = self._get_semantic_embedding(target_text)
            
            if target_embedding is None:
                return self._get_similar_products_tfidf(product, all_products, top_n)
            
            # Calculate similarities with all other products
            similarities = []
            for other_product in all_products:
                # Skip the same product
                if other_product.get('id') == product.get('id'):
                    continue
                
                other_text = self._create_product_text(other_product)
                other_embedding = self._get_semantic_embedding(other_text)
                
                if other_embedding is None:
                    continue
                
                # Cosine similarity
                similarity = np.dot(target_embedding, other_embedding) / (
                    np.linalg.norm(target_embedding) * np.linalg.norm(other_embedding) + 1e-10
                )
                
                product_copy = other_product.copy()
                product_copy['similarityScore'] = float(similarity)
                similarities.append(product_copy)
            
            # Sort by similarity
            similarities.sort(key=lambda x: x['similarityScore'], reverse=True)
            
            return similarities[:top_n]
            
        except Exception as e:
            print(f"Error finding similar products: {str(e)}")
            return self._get_similar_products_tfidf(product, all_products, top_n)
    
    def _get_similar_products_tfidf(self, product, all_products, top_n=5):
        """
        Fallback method using TF-IDF for finding similar products
        """
        try:
            target_text = self._create_product_text(product)
            product_texts = [self._create_product_text(p) for p in all_products]
            
            all_texts = [target_text] + product_texts
            tfidf_matrix = self.vectorizer.fit_transform(all_texts)
            
            target_vector = tfidf_matrix[0:1]
            product_vectors = tfidf_matrix[1:]
            
            similarities_scores = cosine_similarity(target_vector, product_vectors)[0]
            
            similarities = []
            for i, other_product in enumerate(all_products):
                if other_product.get('id') == product.get('id'):
                    continue
                
                product_copy = other_product.copy()
                product_copy['similarityScore'] = float(similarities_scores[i])
                similarities.append(product_copy)
            
            similarities.sort(key=lambda x: x['similarityScore'], reverse=True)
            return similarities[:top_n]
        except Exception as e:
            print(f"Error in TF-IDF similarity: {str(e)}")
            return []

    def train_on_interactions(self, interactions):
        """
        Track user interactions for continuous learning
        In production, this would update a database for future model retraining
        
        Args:
            interactions (list): List of user-product interactions
                Format: [{'user_id': str, 'product': dict, 'action': str, 'timestamp': str}]
        """
        try:
            if not interactions:
                return
            
            # Log interactions for future ML model updates
            print(f"Logged {len(interactions)} user interactions for ML training")
            
            # In production: Save to database (Firebase, PostgreSQL, etc.)
            # This data can be used to:
            # 1. Fine-tune the semantic model
            # 2. Build collaborative filtering
            # 3. Track trending products
            # 4. Personalize recommendations further
                
        except Exception as e:
            print(f"Error training on interactions: {str(e)}")
    
    def get_trending_items(self, products, interactions, top_n=10):
        """
        Get trending products based on recent interactions and semantic relevance
        
        Args:
            products (list): All products
            interactions (list): Recent user interactions
            top_n (int): Number of trending items to return
            
        Returns:
            list: Trending products
        """
        try:
            # Count interactions per product
            product_scores = {}
            for interaction in interactions:
                product_id = interaction.get('product', {}).get('id')
                if product_id:
                    product_scores[product_id] = product_scores.get(product_id, 0) + 1
            
            # Add trending score to products
            trending_products = []
            for product in products:
                product_id = product.get('id')
                interaction_count = product_scores.get(product_id, 0)
                
                product_copy = product.copy()
                # Combine interaction count with rating for trending score
                trending_score = interaction_count * 0.7 + product.get('rating', 0) * 0.3
                product_copy['trendingScore'] = trending_score
                trending_products.append(product_copy)
            
            # Sort by trending score
            trending_products.sort(key=lambda x: x['trendingScore'], reverse=True)
            
            return trending_products[:top_n]
            
        except Exception as e:
            print(f"Error getting trending items: {str(e)}")
            return products[:top_n]
