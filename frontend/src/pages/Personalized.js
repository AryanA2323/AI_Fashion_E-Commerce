import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import ProductList from '../components/ProductList';
import FilterBar from '../components/FilterBar';
import { getRecommendedProducts } from '../utils/api';

const Personalized = () => {
  const { currentUser, userProfile } = useAuth();
  const navigate = useNavigate();
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    category: 'all',
    priceRange: 'all',
    source: 'all'
  });

  const fetchRecommendations = async () => {
    setLoading(true);
    try {
      // Fetch personalized recommendations from real APIs based on user profile
      const recommendations = await getRecommendedProducts(
        userProfile?.interests || ['casual', 'comfortable'],
        userProfile?.fashionStyle || 'modern',
        userProfile?.gender || 'unisex',
        filters
      );
      
      // Products are already ranked by AI relevance score
      // Show top recommendations
      setProducts(recommendations);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      setProducts([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRecommendations();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [userProfile, filters]);

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Welcome Section */}
        <div className="bg-gradient-to-r from-primary-600 to-primary-700 rounded-xl shadow-lg p-6 mb-8 text-white">
          <h1 className="text-3xl font-bold mb-2">
            Personalized For You, {userProfile?.name || currentUser?.displayName || 'User'}! 👋
          </h1>
          <p className="text-primary-100">
            Discover fashion recommendations tailored to your preferences
          </p>
          {userProfile?.interests && userProfile.interests.length > 0 && (
            <div className="mt-4 flex flex-wrap gap-2">
              <span className="text-sm text-primary-100">Your interests:</span>
              {userProfile.interests.map((interest, index) => (
                <span
                  key={index}
                  className="bg-white/20 px-3 py-1 rounded-full text-sm"
                >
                  {interest}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Filter Bar */}
        <FilterBar filters={filters} onFilterChange={handleFilterChange} />

        {/* Products Section */}
        <div className="mt-8">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">
                Recommended For You
              </h2>
              <p className="text-sm text-gray-500 mt-1">
                AI-powered recommendations from Amazon based on your style
              </p>
            </div>
            <div className="flex items-center gap-4">
              {!loading && (
                <span className="text-sm text-gray-500">
                  {products.length} products
                </span>
              )}
              <button
                onClick={() => navigate('/all-products')}
                className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors text-sm font-medium"
              >
                View All Products →
              </button>
            </div>
          </div>

          {loading ? (
            <div className="flex items-center justify-center py-20">
              <div className="text-center">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
                <p className="text-gray-600">Finding perfect products for you from Amazon...</p>
                <p className="text-sm text-gray-500 mt-2">This may take a few seconds</p>
              </div>
            </div>
          ) : products.length > 0 ? (
            <>
              <div className="mb-4 p-4 bg-green-50 border border-green-200 rounded-lg">
                <p className="text-sm text-green-800">
                  ✨ <strong>{products.length} personalized recommendations</strong> found using AI semantic matching
                  {products[0]?.semanticScore > 0 && (
                    <span className="ml-2">
                      (Top match: {(products[0].semanticScore * 100).toFixed(0)}% relevant)
                    </span>
                  )}
                </p>
              </div>
              <ProductList products={products} />
            </>
          ) : (
            <div className="text-center py-20">
              <svg
                className="mx-auto h-12 w-12 text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                />
              </svg>
              <h3 className="mt-2 text-sm font-medium text-gray-900">No matching products found</h3>
              <p className="mt-1 text-sm text-gray-500">
                We couldn't find products matching your interests
              </p>
              <div className="mt-4 flex gap-3 justify-center">
                <button
                  onClick={() => navigate('/profile')}
                  className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors text-sm"
                >
                  Update Interests
                </button>
                <button
                  onClick={() => navigate('/all-products')}
                  className="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors text-sm"
                >
                  Browse All Products
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Personalized;
