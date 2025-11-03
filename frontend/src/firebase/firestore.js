import { 
  doc, 
  setDoc, 
  getDoc, 
  updateDoc,
  collection,
  query,
  where,
  getDocs,
  addDoc,
  serverTimestamp
} from 'firebase/firestore';
import { db } from './config';

/**
 * Create or update user profile in Firestore
 * @param {string} userId - Firebase user ID
 * @param {Object} userData - User profile data
 * @returns {Promise} void
 */
export const createUserProfile = async (userId, userData) => {
  try {
    const userRef = doc(db, 'users', userId);
    await setDoc(userRef, {
      ...userData,
      createdAt: serverTimestamp(),
      updatedAt: serverTimestamp()
    }, { merge: true });
  } catch (error) {
    console.error('Error creating user profile:', error);
    throw error;
  }
};

/**
 * Get user profile from Firestore
 * @param {string} userId - Firebase user ID
 * @returns {Promise<Object>} User profile data
 */
export const getUserProfile = async (userId) => {
  try {
    const userRef = doc(db, 'users', userId);
    const userSnap = await getDoc(userRef);
    
    if (userSnap.exists()) {
      return { id: userSnap.id, ...userSnap.data() };
    } else {
      return null;
    }
  } catch (error) {
    console.error('Error getting user profile:', error);
    throw error;
  }
};

/**
 * Update user profile in Firestore
 * @param {string} userId - Firebase user ID
 * @param {Object} updates - Fields to update
 * @returns {Promise} void
 */
export const updateUserProfile = async (userId, updates) => {
  try {
    const userRef = doc(db, 'users', userId);
    await updateDoc(userRef, {
      ...updates,
      updatedAt: serverTimestamp()
    });
  } catch (error) {
    console.error('Error updating user profile:', error);
    throw error;
  }
};

/**
 * Save product data to Firestore
 * @param {Object} productData - Product information
 * @returns {Promise} Document reference
 */
export const saveProduct = async (productData) => {
  try {
    const productsRef = collection(db, 'products');
    const docRef = await addDoc(productsRef, {
      ...productData,
      createdAt: serverTimestamp()
    });
    return docRef;
  } catch (error) {
    console.error('Error saving product:', error);
    throw error;
  }
};

/**
 * Get products by category
 * @param {string} category - Product category
 * @returns {Promise<Array>} Array of products
 */
export const getProductsByCategory = async (category) => {
  try {
    const productsRef = collection(db, 'products');
    const q = query(productsRef, where('category', '==', category));
    const querySnapshot = await getDocs(q);
    
    const products = [];
    querySnapshot.forEach((doc) => {
      products.push({ id: doc.id, ...doc.data() });
    });
    
    return products;
  } catch (error) {
    console.error('Error getting products:', error);
    throw error;
  }
};

/**
 * Save user's product interaction (view, like, etc.)
 * @param {string} userId - Firebase user ID
 * @param {string} productId - Product ID
 * @param {string} interactionType - Type of interaction (view, like, purchase)
 * @returns {Promise} Document reference
 */
export const saveUserInteraction = async (userId, productId, interactionType) => {
  try {
    const interactionsRef = collection(db, 'interactions');
    const docRef = await addDoc(interactionsRef, {
      userId,
      productId,
      type: interactionType,
      timestamp: serverTimestamp()
    });
    return docRef;
  } catch (error) {
    console.error('Error saving interaction:', error);
    throw error;
  }
};
