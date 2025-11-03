import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SizeCalculator = () => {
  const navigate = useNavigate();
  const [measurements, setMeasurements] = useState({
    gender: '',
    height: '',
    weight: '',
    chest: '',
    waist: '',
    hips: '',
    shoulder: '',
    age: ''
  });
  
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setMeasurements(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear error for this field
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!measurements.gender) newErrors.gender = 'Gender is required';
    if (!measurements.height || measurements.height <= 0) newErrors.height = 'Valid height is required';
    if (!measurements.weight || measurements.weight <= 0) newErrors.weight = 'Valid weight is required';
    if (!measurements.chest || measurements.chest <= 0) newErrors.chest = 'Valid chest measurement is required';
    if (!measurements.waist || measurements.waist <= 0) newErrors.waist = 'Valid waist measurement is required';
    
    // Hips required for female
    if (measurements.gender === 'female' && (!measurements.hips || measurements.hips <= 0)) {
      newErrors.hips = 'Valid hip measurement is required';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const calculateSize = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setLoading(true);
    
    try {
      // Call AI-powered size calculator API
      const response = await fetch('http://localhost:5000/api/calculate-size', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(measurements)
      });

      const data = await response.json();
      
      if (data.status === 'success') {
        setResult(data);
      } else {
        setErrors({ submit: data.message || 'Failed to calculate size' });
      }
    } catch (error) {
      console.error('Error calculating size:', error);
      setErrors({ submit: 'Failed to connect to server. Please try again.' });
    } finally {
      setLoading(false);
    }
  };

  const resetForm = () => {
    setMeasurements({
      gender: '',
      height: '',
      weight: '',
      chest: '',
      waist: '',
      hips: '',
      shoulder: '',
      age: ''
    });
    setResult(null);
    setErrors({});
  };

  const getSizeColor = (size) => {
    const colors = {
      'XS': 'bg-purple-100 text-purple-800',
      'S': 'bg-blue-100 text-blue-800',
      'M': 'bg-green-100 text-green-800',
      'L': 'bg-yellow-100 text-yellow-800',
      'XL': 'bg-orange-100 text-orange-800',
      'XXL': 'bg-red-100 text-red-800',
      'XXXL': 'bg-red-200 text-red-900'
    };
    return colors[size] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="bg-gradient-to-r from-primary-600 to-primary-700 rounded-xl shadow-lg p-8 mb-8 text-white">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold mb-2">AI Size Calculator 📏</h1>
              <p className="text-primary-100">
                Get your perfect clothing size using AI-powered measurements analysis
              </p>
            </div>
            <div className="hidden md:block">
              <svg className="w-20 h-20 text-white opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Form Section */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-md p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Enter Your Measurements</h2>
              
              <form onSubmit={calculateSize} className="space-y-6">
                {/* Gender */}
                <div>
                  <label htmlFor="gender" className="block text-sm font-medium text-gray-700 mb-2">
                    Gender *
                  </label>
                  <select
                    id="gender"
                    name="gender"
                    value={measurements.gender}
                    onChange={handleChange}
                    className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                      errors.gender ? 'border-red-500' : 'border-gray-300'
                    }`}
                  >
                    <option value="">Select Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                  </select>
                  {errors.gender && <p className="mt-1 text-sm text-red-600">{errors.gender}</p>}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Height */}
                  <div>
                    <label htmlFor="height" className="block text-sm font-medium text-gray-700 mb-2">
                      Height (cm) *
                    </label>
                    <input
                      type="number"
                      id="height"
                      name="height"
                      value={measurements.height}
                      onChange={handleChange}
                      placeholder="e.g., 170"
                      className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                        errors.height ? 'border-red-500' : 'border-gray-300'
                      }`}
                    />
                    {errors.height && <p className="mt-1 text-sm text-red-600">{errors.height}</p>}
                  </div>

                  {/* Weight */}
                  <div>
                    <label htmlFor="weight" className="block text-sm font-medium text-gray-700 mb-2">
                      Weight (kg) *
                    </label>
                    <input
                      type="number"
                      id="weight"
                      name="weight"
                      value={measurements.weight}
                      onChange={handleChange}
                      placeholder="e.g., 65"
                      className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                        errors.weight ? 'border-red-500' : 'border-gray-300'
                      }`}
                    />
                    {errors.weight && <p className="mt-1 text-sm text-red-600">{errors.weight}</p>}
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Chest */}
                  <div>
                    <label htmlFor="chest" className="block text-sm font-medium text-gray-700 mb-2">
                      Chest/Bust (cm) *
                    </label>
                    <input
                      type="number"
                      id="chest"
                      name="chest"
                      value={measurements.chest}
                      onChange={handleChange}
                      placeholder="e.g., 95"
                      className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                        errors.chest ? 'border-red-500' : 'border-gray-300'
                      }`}
                    />
                    {errors.chest && <p className="mt-1 text-sm text-red-600">{errors.chest}</p>}
                  </div>

                  {/* Waist */}
                  <div>
                    <label htmlFor="waist" className="block text-sm font-medium text-gray-700 mb-2">
                      Waist (cm) *
                    </label>
                    <input
                      type="number"
                      id="waist"
                      name="waist"
                      value={measurements.waist}
                      onChange={handleChange}
                      placeholder="e.g., 80"
                      className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                        errors.waist ? 'border-red-500' : 'border-gray-300'
                      }`}
                    />
                    {errors.waist && <p className="mt-1 text-sm text-red-600">{errors.waist}</p>}
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Hips */}
                  <div>
                    <label htmlFor="hips" className="block text-sm font-medium text-gray-700 mb-2">
                      Hips (cm) {measurements.gender === 'female' && '*'}
                    </label>
                    <input
                      type="number"
                      id="hips"
                      name="hips"
                      value={measurements.hips}
                      onChange={handleChange}
                      placeholder="e.g., 95"
                      className={`w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent ${
                        errors.hips ? 'border-red-500' : 'border-gray-300'
                      }`}
                    />
                    {errors.hips && <p className="mt-1 text-sm text-red-600">{errors.hips}</p>}
                  </div>

                  {/* Shoulder */}
                  <div>
                    <label htmlFor="shoulder" className="block text-sm font-medium text-gray-700 mb-2">
                      Shoulder Width (cm)
                    </label>
                    <input
                      type="number"
                      id="shoulder"
                      name="shoulder"
                      value={measurements.shoulder}
                      onChange={handleChange}
                      placeholder="e.g., 45"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    />
                  </div>
                </div>

                {/* Age */}
                <div className="md:w-1/2">
                  <label htmlFor="age" className="block text-sm font-medium text-gray-700 mb-2">
                    Age (optional)
                  </label>
                  <input
                    type="number"
                    id="age"
                    name="age"
                    value={measurements.age}
                    onChange={handleChange}
                    placeholder="e.g., 25"
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  />
                </div>

                {/* Error Message */}
                {errors.submit && (
                  <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
                    <p className="text-sm text-red-600">{errors.submit}</p>
                  </div>
                )}

                {/* Buttons */}
                <div className="flex gap-4">
                  <button
                    type="submit"
                    disabled={loading}
                    className="flex-1 bg-primary-600 text-white py-3 px-6 rounded-lg hover:bg-primary-700 transition-colors font-medium disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {loading ? (
                      <span className="flex items-center justify-center">
                        <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        Calculating...
                      </span>
                    ) : (
                      'Calculate My Size'
                    )}
                  </button>
                  
                  {result && (
                    <button
                      type="button"
                      onClick={resetForm}
                      className="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium text-gray-700"
                    >
                      Reset
                    </button>
                  )}
                </div>
              </form>
            </div>
          </div>

          {/* Info & Results Section */}
          <div className="lg:col-span-1 space-y-6">
            {/* Measurement Guide */}
            <div className="bg-white rounded-xl shadow-md p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
                <svg className="w-5 h-5 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                How to Measure
              </h3>
              <ul className="space-y-3 text-sm text-gray-600">
                <li className="flex items-start">
                  <span className="font-semibold text-primary-600 mr-2">•</span>
                  <span><strong>Chest/Bust:</strong> Measure around the fullest part</span>
                </li>
                <li className="flex items-start">
                  <span className="font-semibold text-primary-600 mr-2">•</span>
                  <span><strong>Waist:</strong> Measure around natural waistline</span>
                </li>
                <li className="flex items-start">
                  <span className="font-semibold text-primary-600 mr-2">•</span>
                  <span><strong>Hips:</strong> Measure around the fullest part</span>
                </li>
                <li className="flex items-start">
                  <span className="font-semibold text-primary-600 mr-2">•</span>
                  <span><strong>Shoulder:</strong> Measure from shoulder tip to shoulder tip</span>
                </li>
              </ul>
            </div>

            {/* Results */}
            {result && (
              <div className="bg-gradient-to-br from-primary-50 to-primary-100 rounded-xl shadow-md p-6 border-2 border-primary-200">
                <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
                  <svg className="w-5 h-5 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  Your Perfect Size
                </h3>
                
                <div className="mb-4">
                  <div className="text-center mb-3">
                    <span className={`inline-block px-8 py-4 rounded-xl text-4xl font-bold ${getSizeColor(result.recommended_size)}`}>
                      {result.recommended_size}
                    </span>
                  </div>
                  <p className="text-sm text-gray-700 text-center mb-4">
                    Confidence: <strong>{result.confidence}%</strong>
                  </p>
                </div>

                <div className="space-y-3">
                  <div className="bg-white rounded-lg p-3">
                    <p className="text-xs text-gray-500 mb-1">Body Type</p>
                    <p className="font-semibold text-gray-900">{result.body_type}</p>
                  </div>
                  
                  <div className="bg-white rounded-lg p-3">
                    <p className="text-xs text-gray-500 mb-1">Alternative Sizes</p>
                    <div className="flex gap-2 flex-wrap">
                      {result.alternative_sizes?.map((size, index) => (
                        <span key={index} className={`px-3 py-1 rounded-lg text-sm font-medium ${getSizeColor(size)}`}>
                          {size}
                        </span>
                      ))}
                    </div>
                  </div>

                  {result.recommendations && (
                    <div className="bg-white rounded-lg p-3">
                      <p className="text-xs text-gray-500 mb-2">Tips</p>
                      <ul className="space-y-1 text-xs text-gray-700">
                        {result.recommendations.map((rec, index) => (
                          <li key={index} className="flex items-start">
                            <span className="text-primary-600 mr-1">→</span>
                            <span>{rec}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>

                <button
                  onClick={() => navigate('/all-products')}
                  className="w-full mt-4 bg-primary-600 text-white py-2 px-4 rounded-lg hover:bg-primary-700 transition-colors font-medium text-sm"
                >
                  Shop {result.recommended_size} Size Products →
                </button>
              </div>
            )}

            {/* Size Chart */}
            {!result && (
              <div className="bg-white rounded-xl shadow-md p-6">
                <h3 className="text-lg font-bold text-gray-900 mb-4">Standard Size Chart</h3>
                <div className="overflow-x-auto">
                  <table className="w-full text-xs">
                    <thead>
                      <tr className="border-b">
                        <th className="py-2 text-left">Size</th>
                        <th className="py-2 text-center">Chest</th>
                        <th className="py-2 text-center">Waist</th>
                      </tr>
                    </thead>
                    <tbody className="text-gray-600">
                      <tr className="border-b">
                        <td className="py-2 font-semibold">S</td>
                        <td className="py-2 text-center">86-91</td>
                        <td className="py-2 text-center">71-76</td>
                      </tr>
                      <tr className="border-b">
                        <td className="py-2 font-semibold">M</td>
                        <td className="py-2 text-center">91-97</td>
                        <td className="py-2 text-center">76-81</td>
                      </tr>
                      <tr className="border-b">
                        <td className="py-2 font-semibold">L</td>
                        <td className="py-2 text-center">97-102</td>
                        <td className="py-2 text-center">81-86</td>
                      </tr>
                      <tr className="border-b">
                        <td className="py-2 font-semibold">XL</td>
                        <td className="py-2 text-center">102-109</td>
                        <td className="py-2 text-center">86-94</td>
                      </tr>
                      <tr>
                        <td className="py-2 font-semibold">XXL</td>
                        <td className="py-2 text-center">109-117</td>
                        <td className="py-2 text-center">94-102</td>
                      </tr>
                    </tbody>
                  </table>
                  <p className="text-xs text-gray-500 mt-2">All measurements in cm</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default SizeCalculator;
