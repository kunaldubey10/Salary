"""
Data Preprocessing Module
Handles data cleaning, encoding, and feature engineering
"""
import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from config.config import (
    CATEGORICAL_FEATURES, NUMERICAL_FEATURES, SKILL_FEATURES, 
    TARGET, DATA_PROCESSED
)

logger = logging.getLogger(__name__)


class DataPreprocessor:
    """Preprocess and prepare data for modeling"""
    
    def __init__(self):
        """Initialize preprocessor"""
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='median')
        
    def handle_missing_values(self, data):
        """Handle missing values"""
        data = data.copy()
        
        # Fill missing numerical values with median
        for col in NUMERICAL_FEATURES:
            if col in data.columns and data[col].isnull().any():
                data[col].fillna(data[col].median(), inplace=True)
                logger.info(f"Filled missing values in {col}")
        
        # Fill missing categorical values with mode
        for col in CATEGORICAL_FEATURES:
            if col in data.columns and data[col].isnull().any():
                data[col].fillna(data[col].mode()[0], inplace=True)
                logger.info(f"Filled missing values in {col}")
        
        return data
    
    def encode_categorical_features(self, data, fit=True):
        """Encode categorical features"""
        data = data.copy()
        
        for col in CATEGORICAL_FEATURES:
            if col not in data.columns:
                continue
                
            if fit:
                le = LabelEncoder()
                data[col] = le.fit_transform(data[col].astype(str))
                self.label_encoders[col] = le
                logger.info(f"Encoded categorical feature: {col}")
            else:
                if col in self.label_encoders:
                    data[col] = self.label_encoders[col].transform(data[col].astype(str))
        
        return data
    
    def scale_numerical_features(self, data, fit=True):
        """Scale numerical features"""
        data = data.copy()
        
        if fit:
            scaled_data = self.scaler.fit_transform(data[NUMERICAL_FEATURES])
        else:
            scaled_data = self.scaler.transform(data[NUMERICAL_FEATURES])
        
        data[NUMERICAL_FEATURES] = scaled_data
        logger.info("Scaled numerical features")
        
        return data
    
    def create_feature_interactions(self, data):
        """Create feature interactions and engineered features"""
        data = data.copy()
        
        # Total skills count
        if all(skill in data.columns for skill in SKILL_FEATURES):
            data['total_skills'] = data[SKILL_FEATURES].sum(axis=1)
            logger.info("Created total_skills feature")
        
        # Experience and education interaction
        if 'years_experience' in data.columns and 'education_level' in data.columns:
            data['exp_edu_interaction'] = data['years_experience'] * data['education_level']
            logger.info("Created exp_edu_interaction feature")
        
        return data
    
    def remove_outliers(self, data, target=TARGET, threshold=3):
        """Remove outliers using z-score method"""
        data = data.copy()
        
        if target not in data.columns:
            return data
        
        z_scores = np.abs((data[target] - data[target].mean()) / data[target].std())
        initial_shape = data.shape[0]
        data = data[z_scores < threshold]
        
        logger.info(f"Removed {initial_shape - data.shape[0]} outliers")
        return data
    
    def preprocess(self, data, scale=True, remove_outliers_flag=True, fit=True):
        """
        Complete preprocessing pipeline
        
        Args:
            data: Input DataFrame
            scale: Whether to scale numerical features
            remove_outliers_flag: Whether to remove outliers
            fit: Whether to fit transformers (True for train, False for test)
        
        Returns:
            Preprocessed DataFrame
        """
        logger.info("Starting preprocessing pipeline...")
        
        # Handle missing values
        data = self.handle_missing_values(data)
        
        # Remove outliers
        if remove_outliers_flag:
            data = self.remove_outliers(data)
        
        # Create feature interactions
        data = self.create_feature_interactions(data)
        
        # Encode categorical features
        data = self.encode_categorical_features(data, fit=fit)
        
        # Scale numerical features
        if scale:
            data = self.scale_numerical_features(data, fit=fit)
        
        logger.info("Preprocessing pipeline completed")
        return data


def prepare_train_test_data(raw_data, test_size=0.2, random_state=42):
    """
    Prepare train and test datasets
    
    Args:
        raw_data: Raw dataset
        test_size: Test size as fraction
        random_state: Random state for reproducibility
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split
    
    # Separate features and target
    if TARGET in raw_data.columns:
        X = raw_data.drop(TARGET, axis=1)
        y = raw_data[TARGET]
    else:
        raise ValueError(f"Target column '{TARGET}' not found in data")
    
    # Drop ID column if present
    if 'job_id' in X.columns:
        X = X.drop('job_id', axis=1)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    logger.info(f"Data split: Train {X_train.shape}, Test {X_test.shape}")
    
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    from src.data_loader import DataLoader
    
    logging.basicConfig(level=logging.INFO)
    
    # Load and preprocess data
    loader = DataLoader()
    raw_data = loader.load_raw_data()
    
    preprocessor = DataPreprocessor()
    processed_data = preprocessor.preprocess(raw_data)
    
    print("\nProcessed data shape:", processed_data.shape)
    print("\nFirst few rows of processed data:")
    print(processed_data.head())
    
    # Save processed data
    loader.save_processed_data(processed_data)
