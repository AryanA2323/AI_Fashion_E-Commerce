import React from 'react';

/**
 * FilterBar Component
 * Provides filtering options for products
 */
const FilterBar = ({ filters, onFilterChange }) => {
  const handleFilterChange = (filterType, value) => {
    onFilterChange({
      ...filters,
      [filterType]: value
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Category Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Category
          </label>
          <select
            value={filters.category}
            onChange={(e) => handleFilterChange('category', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="all">All Categories</option>
            <option value="casual">Casual Wear</option>
            <option value="formal">Formal Wear</option>
            <option value="streetwear">Streetwear</option>
            <option value="athletic">Athletic Wear</option>
            <option value="traditional">Traditional Wear</option>
            <option value="party">Party Wear</option>
          </select>
        </div>

        {/* Price Range Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Price Range
          </label>
          <select
            value={filters.priceRange}
            onChange={(e) => handleFilterChange('priceRange', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
            <option value="all">All Prices</option>
            <option value="0-1000">Under ₹1,000</option>
            <option value="1000-2500">₹1,000 - ₹2,500</option>
            <option value="2500-5000">₹2,500 - ₹5,000</option>
            <option value="5000-10000">₹5,000 - ₹10,000</option>
            <option value="10000+">Above ₹10,000</option>
          </select>
        </div>

        {/* Source Filter - Amazon Only */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Store
          </label>
          <select
            value="amazon"
            disabled
            className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-700 cursor-not-allowed"
          >
            <option value="amazon">Amazon (Live Products)</option>
          </select>
        </div>
      </div>

      {/* Active Filters Display */}
      {(filters.category !== 'all' || filters.priceRange !== 'all' || filters.source !== 'all') && (
        <div className="mt-4 flex items-center gap-2 flex-wrap">
          <span className="text-sm text-gray-600">Active Filters:</span>
          {filters.category !== 'all' && (
            <span className="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm flex items-center gap-1">
              {filters.category}
              <button
                onClick={() => handleFilterChange('category', 'all')}
                className="hover:text-primary-900"
              >
                ×
              </button>
            </span>
          )}
          {filters.priceRange !== 'all' && (
            <span className="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm flex items-center gap-1">
              {filters.priceRange === '10000+' ? 'Above ₹10,000' : `₹${filters.priceRange.replace('-', ' - ₹')}`}
              <button
                onClick={() => handleFilterChange('priceRange', 'all')}
                className="hover:text-primary-900"
              >
                ×
              </button>
            </span>
          )}
          {filters.source !== 'all' && (
            <span className="bg-primary-100 text-primary-700 px-3 py-1 rounded-full text-sm flex items-center gap-1 capitalize">
              {filters.source}
              <button
                onClick={() => handleFilterChange('source', 'all')}
                className="hover:text-primary-900"
              >
                ×
              </button>
            </span>
          )}
          <button
            onClick={() => onFilterChange({ category: 'all', priceRange: 'all', source: 'all' })}
            className="text-sm text-primary-600 hover:text-primary-700 font-medium"
          >
            Clear All
          </button>
        </div>
      )}
    </div>
  );
};

export default FilterBar;
