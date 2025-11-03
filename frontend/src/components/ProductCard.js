import React from 'react';

/**
 * ProductCard Component
 * Displays individual product information
 */
const ProductCard = ({ product }) => {
  const {
    title,
    price,
    image,
    url,
    link,
    source,
    rating,
    category,
    relevanceScore
  } = product;
  
  // Use url field from backend, fallback to link
  const productUrl = url || link;

  // Format price
  const formatPrice = (price) => {
    if (typeof price === 'number') {
      return `₹${price.toLocaleString('en-IN')}`;
    }
    return price;
  };

  // Get source badge color
  const getSourceColor = (source) => {
    switch (source?.toLowerCase()) {
      case 'amazon':
        return 'bg-orange-100 text-orange-700';
      case 'flipkart':
        return 'bg-blue-100 text-blue-700';
      default:
        return 'bg-gray-100 text-gray-700';
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow duration-300 flex flex-col h-full">
      {/* Product Image */}
      <div className="relative h-80 bg-gray-100 overflow-hidden">
        <img
          src={image || 'https://via.placeholder.com/300x400?text=No+Image'}
          alt={title}
          className="w-full h-full object-contain hover:scale-105 transition-transform duration-300"
          onError={(e) => {
            e.target.src = 'https://via.placeholder.com/300x400?text=No+Image';
          }}
        />
        
        {/* Source Badge */}
        {source && (
          <div className="absolute top-2 left-2">
            <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getSourceColor(source)}`}>
              {source}
            </span>
          </div>
        )}

        {/* Relevance Score Badge */}
        {relevanceScore && (
          <div className="absolute top-2 right-2">
            <span className="bg-green-500 text-white px-2 py-1 rounded-full text-xs font-semibold">
              {Math.round(relevanceScore * 100)}% Match
            </span>
          </div>
        )}
      </div>

      {/* Product Details */}
      <div className="p-4 flex-1 flex flex-col">
        {/* Category */}
        {category && (
          <span className="text-xs text-gray-500 uppercase tracking-wide mb-1">
            {category}
          </span>
        )}

        {/* Title */}
        <h3 className="text-sm font-semibold text-gray-900 mb-2 line-clamp-2 flex-1">
          {title}
        </h3>

        {/* Rating */}
        {rating && (
          <div className="flex items-center mb-2">
            <div className="flex items-center">
              {[...Array(5)].map((_, i) => (
                <svg
                  key={i}
                  className={`h-4 w-4 ${
                    i < Math.floor(rating) ? 'text-yellow-400' : 'text-gray-300'
                  }`}
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
              ))}
            </div>
            <span className="ml-1 text-xs text-gray-600">({rating.toFixed(1)})</span>
          </div>
        )}

        {/* Price */}
        <div className="mb-3">
          <span className="text-xl font-bold text-gray-900">
            {formatPrice(price)}
          </span>
        </div>

        {/* View Button */}
        <a
          href={productUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="block w-full text-center bg-primary-600 text-white py-2 px-4 rounded-lg hover:bg-primary-700 transition-colors font-medium text-sm"
        >
          View on {source || 'Store'}
        </a>
      </div>
    </div>
  );
};

export default ProductCard;
