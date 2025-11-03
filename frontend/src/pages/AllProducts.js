import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import ProductList from '../components/ProductList';
import FilterBar from '../components/FilterBar';

const AllProducts = () => {
  const location = useLocation();
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [filters, setFilters] = useState({
    category: 'all',
    priceRange: 'all',
    source: 'both'
  });
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('default');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Check if category was passed from navigation
  useEffect(() => {
    if (location.state?.selectedCategory) {
      setFilters(prev => ({
        ...prev,
        category: location.state.selectedCategory
      }));
    }
  }, [location.state]);

  // Fetch products from backend on mount and when filters change
  useEffect(() => {
    fetchProducts();
  }, [filters.category, filters.source]);

  // Apply local filters when search or sort changes
  useEffect(() => {
    applyLocalFilters();
  }, [products, searchTerm, sortBy, filters.priceRange]);

  const fetchProducts = async () => {
    setLoading(true);
    setError(null);

    try {
      const params = new URLSearchParams({
        source: filters.source || 'both',
        limit: '60'
      });

      if (filters.category && filters.category !== 'all') {
        params.append('category', filters.category);
      }

      const response = await fetch(`http://localhost:5000/api/products/all?${params}`);
      const data = await response.json();

      if (data.status === 'success') {
        setProducts(data.products || []);
      } else {
        setError(data.message || 'Failed to fetch products');
      }
    } catch (err) {
      console.error('Error fetching products:', err);
      setError('Unable to connect to server. Please ensure backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const applyLocalFilters = () => {
    let filtered = [...products];

    // Apply price range filter (client-side)
    if (filters.priceRange !== 'all') {
      const priceRange = filters.priceRange;
      if (priceRange === '10000+') {
        filtered = filtered.filter(product => product.price >= 10000);
      } else {
        const [min, max] = priceRange.split('-').map(Number);
        filtered = filtered.filter(product => 
          product.price >= min && product.price <= max
        );
      }
    }

    // Apply search filter (client-side)
    if (searchTerm) {
      filtered = filtered.filter(product =>
        product.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        (product.tags && product.tags.some(tag => 
          tag.toLowerCase().includes(searchTerm.toLowerCase())
        ))
      );
    }

    // Apply sorting
    switch (sortBy) {
      case 'price-low':
        filtered.sort((a, b) => a.price - b.price);
        break;
      case 'price-high':
        filtered.sort((a, b) => b.price - a.price);
        break;
      case 'rating':
        filtered.sort((a, b) => b.rating - a.rating);
        break;
      case 'name':
        filtered.sort((a, b) => a.title.localeCompare(b.title));
        break;
      default:
        // Keep default order
        break;
    }

    setFilteredProducts(filtered);
  };

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header Section */}
        <div className="bg-gradient-to-r from-primary-600 to-primary-700 rounded-xl shadow-lg p-6 mb-8 text-white">
          <h1 className="text-3xl font-bold mb-2">All Products</h1>
          <p className="text-primary-100">
            Browse real fashion products from Amazon
          </p>
          {!loading && (
            <p className="text-sm text-primary-200 mt-2">
              {filteredProducts.length} products found
            </p>
          )}
        </div>

        {/* Search Bar */}
        <div className="mb-6">
          <div className="relative max-w-2xl">
            <input
              type="text"
              placeholder="Search products by name or tags..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-4 py-3 pl-12 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 bg-white shadow-sm"
            />
            <svg
              className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </div>
        </div>

        {/* Filter Bar */}
        <FilterBar filters={filters} onFilterChange={handleFilterChange} />

        {/* Results Info and Sort */}
        <div className="flex justify-between items-center mb-6">
          <p className="text-sm text-gray-500">
            Showing <span className="font-semibold text-gray-800">{filteredProducts.length}</span> of{' '}
            <span className="font-semibold text-gray-800">{products.length}</span> products
          </p>
          
          <div className="flex items-center gap-2">
            <label className="text-gray-600 text-sm">Sort by:</label>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 bg-white shadow-sm"
            >
              <option value="default">Default</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
              <option value="rating">Highest Rated</option>
              <option value="name">Name: A to Z</option>
            </select>
          </div>
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-20">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mb-4"></div>
            <p className="text-gray-600">Loading real products from Amazon...</p>
          </div>
        )}

        {/* Error State */}
        {error && !loading && (
          <div className="text-center py-20">
            <div className="bg-red-50 border border-red-200 rounded-lg p-6 max-w-md mx-auto">
              <svg className="mx-auto h-12 w-12 text-red-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <h3 className="text-lg font-medium text-red-900 mb-2">Error Loading Products</h3>
              <p className="text-sm text-red-700 mb-4">{error}</p>
              <button
                onClick={fetchProducts}
                className="px-6 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
              >
                Try Again
              </button>
            </div>
          </div>
        )}

        {/* Products Grid */}
        {!loading && !error && filteredProducts.length > 0 && (
          <ProductList products={filteredProducts} />
        )}

        {/* No Products Found */}
        {!loading && !error && filteredProducts.length === 0 && (
          <div className="text-center py-20">
            <svg
              className="mx-auto h-12 w-12 text-gray-400 mb-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <h3 className="text-sm font-medium text-gray-900 mb-2">No products found</h3>
            <p className="text-sm text-gray-500 mb-4">Try adjusting your filters or search term</p>
            <button
              onClick={() => {
                setFilters({
                  category: 'all',
                  priceRange: 'all',
                  source: 'both'
                });
                setSearchTerm('');
                setSortBy('default');
              }}
              className="px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
            >
              Clear All Filters
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default AllProducts;
