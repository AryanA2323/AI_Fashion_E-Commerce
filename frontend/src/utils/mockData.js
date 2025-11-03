/**
 * Mock Product Data
 * This data simulates products from Amazon and Flipkart
 * In production, this would be fetched from actual APIs
 * 
 * Extended catalog with 60+ products across all categories
 */

export const mockProducts = [
  // Casual Wear - Amazon
  {
    id: 'amz-casual-001',
    title: 'Classic Cotton T-Shirt - Comfortable Everyday Wear',
    price: 499,
    image: 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.5,
    tags: ['casual', 'cotton', 'comfortable', 'everyday']
  },
  {
    id: 'amz-casual-002',
    title: 'Slim Fit Denim Jeans - Blue Wash',
    price: 1299,
    image: 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.3,
    tags: ['casual', 'denim', 'jeans', 'blue']
  },
  {
    id: 'amz-casual-003',
    title: 'Casual Hoodie - Fleece Fabric',
    price: 899,
    image: 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.6,
    tags: ['casual', 'hoodie', 'comfortable', 'winter']
  },

  // Formal Wear - Flipkart
  {
    id: 'flp-formal-001',
    title: 'Premium Formal Shirt - White Cotton',
    price: 1499,
    image: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.7,
    tags: ['formal', 'shirt', 'office', 'professional']
  },
  {
    id: 'flp-formal-002',
    title: 'Formal Blazer - Slim Fit Black',
    price: 3999,
    image: 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.8,
    tags: ['formal', 'blazer', 'business', 'professional']
  },
  {
    id: 'flp-formal-003',
    title: 'Formal Trousers - Grey Pleated',
    price: 1799,
    image: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.4,
    tags: ['formal', 'trousers', 'office', 'business']
  },

  // Streetwear - Amazon
  {
    id: 'amz-street-001',
    title: 'Graphic Print Oversized T-Shirt',
    price: 799,
    image: 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.5,
    tags: ['streetwear', 'graphic', 'oversized', 'urban']
  },
  {
    id: 'amz-street-002',
    title: 'Urban Cargo Pants - Multiple Pockets',
    price: 1899,
    image: 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.6,
    tags: ['streetwear', 'cargo', 'urban', 'utility']
  },
  {
    id: 'amz-street-003',
    title: 'Bomber Jacket - Street Style',
    price: 2499,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.7,
    tags: ['streetwear', 'bomber', 'jacket', 'urban']
  },

  // Athletic Wear - Flipkart
  {
    id: 'flp-athletic-001',
    title: 'Performance Sports T-Shirt - Quick Dry',
    price: 599,
    image: 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.5,
    tags: ['athletic', 'sports', 'gym', 'fitness']
  },
  {
    id: 'flp-athletic-002',
    title: 'Training Shorts - Breathable Fabric',
    price: 699,
    image: 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.4,
    tags: ['athletic', 'shorts', 'training', 'gym']
  },
  {
    id: 'flp-athletic-003',
    title: 'Track Pants - Comfortable Fit',
    price: 999,
    image: 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.6,
    tags: ['athletic', 'track', 'pants', 'comfortable']
  },

  // Party Wear - Amazon
  {
    id: 'amz-party-001',
    title: 'Party Wear Silk Kurta Set',
    price: 3499,
    image: 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Party',
    rating: 4.8,
    tags: ['party', 'ethnic', 'silk', 'traditional']
  },
  {
    id: 'amz-party-002',
    title: 'Sequin Embellished Evening Dress',
    price: 4999,
    image: 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Party',
    rating: 4.7,
    tags: ['party', 'evening', 'dress', 'elegant']
  },

  // Traditional Wear - Flipkart
  {
    id: 'flp-traditional-001',
    title: 'Traditional Cotton Kurta',
    price: 1299,
    image: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Traditional',
    rating: 4.6,
    tags: ['traditional', 'ethnic', 'kurta', 'cotton']
  },
  {
    id: 'flp-traditional-002',
    title: 'Ethnic Palazzo Pants',
    price: 899,
    image: 'https://images.unsplash.com/photo-1583391733981-8b992f2d9df6?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Traditional',
    rating: 4.5,
    tags: ['traditional', 'ethnic', 'palazzo', 'comfortable']
  },

  // Business Casual - Amazon
  {
    id: 'amz-business-001',
    title: 'Business Casual Polo Shirt',
    price: 999,
    image: 'https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.5,
    tags: ['business', 'casual', 'polo', 'comfortable']
  },
  {
    id: 'amz-business-002',
    title: 'Chinos - Slim Fit Business Casual',
    price: 1599,
    image: 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.6,
    tags: ['business', 'casual', 'chinos', 'professional']
  },

  // More Casual Options
  {
    id: 'flp-casual-004',
    title: 'Casual Polo T-Shirt - Multiple Colors',
    price: 699,
    image: 'https://images.unsplash.com/photo-1607345366928-199ea26cfe3e?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.4,
    tags: ['casual', 'polo', 'comfortable', 'versatile']
  },
  {
    id: 'flp-casual-005',
    title: 'Casual Shorts - Summer Collection',
    price: 599,
    image: 'https://images.unsplash.com/photo-1591195120140-d531256e280e?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.3,
    tags: ['casual', 'shorts', 'summer', 'comfortable']
  },
  {
    id: 'amz-casual-006',
    title: 'Casual Sneakers - Comfortable Walking Shoes',
    price: 1999,
    image: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.7,
    tags: ['casual', 'sneakers', 'shoes', 'comfortable']
  },

  // Vintage Fashion
  {
    id: 'amz-vintage-001',
    title: 'Vintage Denim Jacket - Retro Style',
    price: 2799,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.8,
    tags: ['vintage', 'denim', 'jacket', 'retro']
  },
  {
    id: 'flp-vintage-001',
    title: 'Vintage Print Shirt - Classic Pattern',
    price: 1299,
    image: 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.5,
    tags: ['vintage', 'print', 'shirt', 'classic']
  },

  // More Casual Wear
  {
    id: 'amz-casual-007',
    title: 'Graphic Crew Neck Sweatshirt',
    price: 999,
    image: 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.4,
    tags: ['casual', 'sweatshirt', 'graphic', 'comfortable']
  },
  {
    id: 'flp-casual-006',
    title: 'Cotton Joggers - Relaxed Fit',
    price: 799,
    image: 'https://images.unsplash.com/photo-1555689502-c4b22d76c56f?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.5,
    tags: ['casual', 'joggers', 'cotton', 'comfortable']
  },
  {
    id: 'amz-casual-008',
    title: 'Casual Button-Down Shirt',
    price: 849,
    image: 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.3,
    tags: ['casual', 'shirt', 'button-down', 'versatile']
  },
  {
    id: 'flp-casual-007',
    title: 'Casual Ankle Boots',
    price: 2499,
    image: 'https://images.unsplash.com/photo-1542840410-3092f99611a3?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.6,
    tags: ['casual', 'boots', 'footwear', 'stylish']
  },
  {
    id: 'amz-casual-009',
    title: 'Casual Windbreaker Jacket',
    price: 1599,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.7,
    tags: ['casual', 'windbreaker', 'jacket', 'outdoor']
  },
  {
    id: 'flp-casual-008',
    title: 'Casual Chino Pants',
    price: 1199,
    image: 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.4,
    tags: ['casual', 'chinos', 'pants', 'comfortable']
  },

  // More Formal Wear
  {
    id: 'amz-formal-004',
    title: 'Premium Silk Tie Set',
    price: 899,
    image: 'https://images.unsplash.com/photo-1556679261-1b52b56e75e5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.8,
    tags: ['formal', 'tie', 'silk', 'accessory']
  },
  {
    id: 'flp-formal-004',
    title: 'Formal Oxford Shoes - Leather',
    price: 3499,
    image: 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.7,
    tags: ['formal', 'shoes', 'leather', 'oxford']
  },
  {
    id: 'amz-formal-005',
    title: 'Double-Breasted Suit Jacket',
    price: 5999,
    image: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.9,
    tags: ['formal', 'suit', 'jacket', 'business']
  },
  {
    id: 'flp-formal-005',
    title: 'Formal Dress Shirt - Striped',
    price: 1299,
    image: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.5,
    tags: ['formal', 'shirt', 'striped', 'professional']
  },
  {
    id: 'amz-formal-006',
    title: 'Formal Waistcoat - Slim Fit',
    price: 2499,
    image: 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.6,
    tags: ['formal', 'waistcoat', 'vest', 'elegant']
  },
  {
    id: 'flp-formal-006',
    title: 'Formal Belt - Genuine Leather',
    price: 799,
    image: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Formal',
    rating: 4.4,
    tags: ['formal', 'belt', 'leather', 'accessory']
  },

  // More Streetwear
  {
    id: 'amz-street-004',
    title: 'Streetwear Puffer Jacket',
    price: 3499,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.8,
    tags: ['streetwear', 'puffer', 'jacket', 'winter']
  },
  {
    id: 'flp-street-003',
    title: 'Distressed Denim Jeans',
    price: 2199,
    image: 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Streetwear',
    rating: 4.5,
    tags: ['streetwear', 'denim', 'distressed', 'jeans']
  },
  {
    id: 'amz-street-005',
    title: 'Streetwear Hoodie - Bold Graphics',
    price: 1899,
    image: 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.7,
    tags: ['streetwear', 'hoodie', 'graphic', 'urban']
  },
  {
    id: 'flp-street-004',
    title: 'High-Top Sneakers - Limited Edition',
    price: 4499,
    image: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Streetwear',
    rating: 4.9,
    tags: ['streetwear', 'sneakers', 'shoes', 'limited']
  },
  {
    id: 'amz-street-006',
    title: 'Streetwear Track Jacket',
    price: 1999,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.6,
    tags: ['streetwear', 'track', 'jacket', 'sporty']
  },
  {
    id: 'flp-street-005',
    title: 'Utility Vest - Multiple Pockets',
    price: 1699,
    image: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Streetwear',
    rating: 4.5,
    tags: ['streetwear', 'vest', 'utility', 'tactical']
  },

  // More Athletic Wear
  {
    id: 'amz-athletic-004',
    title: 'Compression Athletic Shirt',
    price: 799,
    image: 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Athletic',
    rating: 4.7,
    tags: ['athletic', 'compression', 'gym', 'performance']
  },
  {
    id: 'flp-athletic-004',
    title: 'Running Tights - Moisture Wicking',
    price: 899,
    image: 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.6,
    tags: ['athletic', 'running', 'tights', 'performance']
  },
  {
    id: 'amz-athletic-005',
    title: 'Sports Windbreaker - Reflective',
    price: 1499,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Athletic',
    rating: 4.8,
    tags: ['athletic', 'windbreaker', 'running', 'reflective']
  },
  {
    id: 'flp-athletic-005',
    title: 'Yoga Pants - High Waist',
    price: 999,
    image: 'https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.7,
    tags: ['athletic', 'yoga', 'pants', 'flexible']
  },
  {
    id: 'amz-athletic-006',
    title: 'Athletic Tank Top - Mesh',
    price: 549,
    image: 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Athletic',
    rating: 4.5,
    tags: ['athletic', 'tank', 'gym', 'breathable']
  },
  {
    id: 'flp-athletic-006',
    title: 'Sports Bra - High Support',
    price: 899,
    image: 'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.8,
    tags: ['athletic', 'sports bra', 'support', 'workout']
  },

  // More Party Wear
  {
    id: 'amz-party-003',
    title: 'Velvet Party Blazer',
    price: 4999,
    image: 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Party',
    rating: 4.8,
    tags: ['party', 'blazer', 'velvet', 'elegant']
  },
  {
    id: 'flp-party-002',
    title: 'Cocktail Dress - Shimmer',
    price: 3999,
    image: 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Party',
    rating: 4.7,
    tags: ['party', 'dress', 'cocktail', 'shimmer']
  },
  {
    id: 'amz-party-004',
    title: 'Designer Sherwani - Wedding',
    price: 8999,
    image: 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Party',
    rating: 4.9,
    tags: ['party', 'sherwani', 'wedding', 'designer']
  },
  {
    id: 'flp-party-003',
    title: 'Party Wear Lehenga',
    price: 6999,
    image: 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Party',
    rating: 4.8,
    tags: ['party', 'lehenga', 'ethnic', 'wedding']
  },
  {
    id: 'amz-party-005',
    title: 'Formal Evening Gown',
    price: 5499,
    image: 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Party',
    rating: 4.7,
    tags: ['party', 'gown', 'evening', 'formal']
  },

  // More Traditional Wear
  {
    id: 'amz-traditional-003',
    title: 'Silk Saree - Banarasi',
    price: 4999,
    image: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Traditional',
    rating: 4.9,
    tags: ['traditional', 'saree', 'silk', 'ethnic']
  },
  {
    id: 'flp-traditional-003',
    title: 'Traditional Kurta Pajama Set',
    price: 1799,
    image: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Traditional',
    rating: 4.6,
    tags: ['traditional', 'kurta', 'pajama', 'ethnic']
  },
  {
    id: 'amz-traditional-004',
    title: 'Embroidered Anarkali Suit',
    price: 3999,
    image: 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Traditional',
    rating: 4.8,
    tags: ['traditional', 'anarkali', 'embroidered', 'ethnic']
  },
  {
    id: 'flp-traditional-004',
    title: 'Traditional Dhoti Kurta',
    price: 1999,
    image: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Traditional',
    rating: 4.5,
    tags: ['traditional', 'dhoti', 'kurta', 'ethnic']
  },
  {
    id: 'amz-traditional-005',
    title: 'Designer Dupatta - Silk',
    price: 1299,
    image: 'https://images.unsplash.com/photo-1583391733956-6c78276477e5?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Traditional',
    rating: 4.7,
    tags: ['traditional', 'dupatta', 'silk', 'accessory']
  },
  {
    id: 'flp-traditional-005',
    title: 'Traditional Nehru Jacket',
    price: 2499,
    image: 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Traditional',
    rating: 4.6,
    tags: ['traditional', 'nehru', 'jacket', 'ethnic']
  },

  // Additional Variety
  {
    id: 'amz-casual-010',
    title: 'Casual Linen Shirt - Summer',
    price: 1099,
    image: 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Casual',
    rating: 4.5,
    tags: ['casual', 'linen', 'summer', 'breathable']
  },
  {
    id: 'flp-casual-009',
    title: 'Casual Bomber Jacket',
    price: 2299,
    image: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Casual',
    rating: 4.6,
    tags: ['casual', 'bomber', 'jacket', 'stylish']
  },
  {
    id: 'amz-street-007',
    title: 'Streetwear Bucket Hat',
    price: 599,
    image: 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Streetwear',
    rating: 4.4,
    tags: ['streetwear', 'hat', 'bucket', 'accessory']
  },
  {
    id: 'flp-athletic-007',
    title: 'Performance Running Shoes',
    price: 3499,
    image: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400',
    link: '#',
    source: 'Flipkart',
    category: 'Athletic',
    rating: 4.8,
    tags: ['athletic', 'running', 'shoes', 'performance']
  },
  {
    id: 'amz-formal-007',
    title: 'Formal Cufflinks Set - Gold',
    price: 899,
    image: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400',
    link: '#',
    source: 'Amazon',
    category: 'Formal',
    rating: 4.7,
    tags: ['formal', 'cufflinks', 'accessory', 'luxury']
  }
];

/**
 * Get random subset of products
 * Useful for testing different recommendations
 */
export const getRandomProducts = (count = 10) => {
  const shuffled = [...mockProducts].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
};

/**
 * Get products by category
 */
export const getProductsByCategory = (category) => {
  return mockProducts.filter(product => 
    product.category.toLowerCase() === category.toLowerCase()
  );
};
