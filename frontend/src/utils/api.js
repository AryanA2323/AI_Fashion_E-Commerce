import axios from 'axios';
import { mockProducts } from './mockData';

const API_BASE_URL = process.env.REACT_APP_BACKEND_API_URL || 'http://localhost:5000';

/**
 * Get recommended products based on user preferences
 * @param {Array} interests - User's areas of interest
 * @param {string} fashionStyle - User's fashion style preference
 * @param {string} gender - User's gender
 * @param {Object} filters - Active filters
 * @returns {Promise<Array>} Array of recommended products
 */
export const getRecommendedProducts = async (interests, fashionStyle, gender, filters = {}) => {
  try {
    // Try to fetch from backend API
    const response = await axios.post(`${API_BASE_URL}/api/recommendations`, {
      interests,
      fashionStyle,
      gender,
      filters
    }, {
      timeout: 5000 // 5 second timeout
    });

    return response.data.products;
  } catch (error) {
    console.warn('Backend API not available, using mock data:', error.message);
    
    // Fallback to mock data with client-side filtering
    return filterMockProducts(mockProducts, interests, fashionStyle, gender, filters);
  }
};

/**
 * Filter mock products based on user preferences and filters
 * @param {Array} products - Array of products
 * @param {Array} interests - User interests
 * @param {string} fashionStyle - Fashion style
 * @param {string} gender - User gender
 * @param {Object} filters - Active filters
 * @returns {Array} Filtered products
 */
const filterMockProducts = (products, interests, fashionStyle, gender, filters) => {
  let filtered = [...products];

  // Filter by category
  if (filters.category && filters.category !== 'all') {
    filtered = filtered.filter(product => 
      product.category?.toLowerCase() === filters.category.toLowerCase()
    );
  }

  // Filter by price range
  if (filters.priceRange && filters.priceRange !== 'all') {
    filtered = filtered.filter(product => {
      const price = product.price;
      if (filters.priceRange === '0-1000') return price < 1000;
      if (filters.priceRange === '1000-2500') return price >= 1000 && price < 2500;
      if (filters.priceRange === '2500-5000') return price >= 2500 && price < 5000;
      if (filters.priceRange === '5000-10000') return price >= 5000 && price < 10000;
      if (filters.priceRange === '10000+') return price >= 10000;
      return true;
    });
  }

  // Filter by source
  if (filters.source && filters.source !== 'all') {
    filtered = filtered.filter(product => 
      product.source?.toLowerCase() === filters.source.toLowerCase()
    );
  }

  // Calculate relevance scores based on interests
  if (interests && interests.length > 0) {
    filtered = filtered.map(product => {
      let relevanceScore = 0;
      const productText = `${product.title} ${product.category} ${product.tags?.join(' ')}`.toLowerCase();
      
      interests.forEach(interest => {
        if (productText.includes(interest.toLowerCase())) {
          relevanceScore += 0.3;
        }
      });

      // Boost score if fashion style matches
      if (fashionStyle && productText.includes(fashionStyle.toLowerCase())) {
        relevanceScore += 0.2;
      }

      // Ensure score is between 0 and 1
      relevanceScore = Math.min(relevanceScore, 1);
      
      return {
        ...product,
        relevanceScore: relevanceScore || 0.5 // Default relevance if no match
      };
    });

    // Sort by relevance score
    filtered.sort((a, b) => b.relevanceScore - a.relevanceScore);
  }

  return filtered;
};

/**
 * Fetch products from Amazon (placeholder)
 * In production, this would call the Amazon Product Advertising API
 */
export const fetchAmazonProducts = async (keywords) => {
  // Placeholder - implement Amazon API integration
  console.log('Fetching Amazon products for:', keywords);
  return [];
};

/**
 * Fetch products from Flipkart (placeholder)
 * In production, this would call the Flipkart Affiliate API
 */
export const fetchFlipkartProducts = async (keywords) => {
  // Placeholder - implement Flipkart API integration
  console.log('Fetching Flipkart products for:', keywords);
  return [];
};

/**
 * Send user interaction to backend for ML training
 * @param {string} userId - User ID
 * @param {string} productId - Product ID
 * @param {string} interactionType - Type of interaction (view, click, like)
 */
export const trackUserInteraction = async (userId, productId, interactionType) => {
  try {
    await axios.post(`${API_BASE_URL}/api/track-interaction`, {
      userId,
      productId,
      interactionType,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('Error tracking interaction:', error);
  }
};
