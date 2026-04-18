"""
Prediction Script
Make predictions on new data using the trained model
"""
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

import logging
import pandas as pd
import numpy as np
from src.preprocessing import DataPreprocessor
from src.utils import load_model
from config.config import TARGET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SalaryPredictor:
    """Make salary predictions using trained model"""
    
    def __init__(self, model_name='xgboost', preprocessor=None):
        """
        Initialize predictor
        
        Args:
            model_name: Name of the trained model to use
            preprocessor: Fitted preprocessor object
        """
        self.model = load_model(model_name)
        self.model_name = model_name
        self.preprocessor = preprocessor or DataPreprocessor()
        logger.info(f"Loaded model: {model_name}")
    
    def predict(self, data):
        """
        Make predictions
        
        Args:
            data: Input DataFrame with features
            
        Returns:
            Predicted salaries as numpy array
        """
        # Preprocess the data
        processed_data = self.preprocessor.preprocess(data, scale=True, fit=False)
        
        # Drop ID and target columns if present
        if 'job_id' in processed_data.columns:
            processed_data = processed_data.drop('job_id', axis=1)
        if TARGET in processed_data.columns:
            processed_data = processed_data.drop(TARGET, axis=1)
        
        # Make predictions
        predictions = self.model.predict(processed_data)
        
        return predictions
    
    def predict_single(self, features_dict):
        """
        Make a single prediction from a dictionary of features
        
        Args:
            features_dict: Dictionary with feature values
            
        Returns:
            Predicted salary value
        """
        df = pd.DataFrame([features_dict])
        prediction = self.predict(df)
        return prediction[0]


def example_prediction():
    """Example usage of salary predictor"""
    
    # Load and prepare data
    from src.data_loader import DataLoader
    
    logger.info("Loading example data...")
    loader = DataLoader()
    raw_data = loader.load_raw_data()
    
    # Use first 5 samples for prediction
    new_data = raw_data.head(5).copy()
    
    # Initialize predictor
    predictor = SalaryPredictor(model_name='xgboost')
    
    # Make predictions
    logger.info("Making predictions...")
    predictions = predictor.predict(new_data)
    
    # Display results
    results_df = new_data[['job_title', 'experience_level', 'salary']].copy()
    results_df['predicted_salary'] = predictions
    results_df['difference'] = results_df['salary'] - results_df['predicted_salary']
    
    print("\nPrediction Results:")
    print(results_df.to_string())
    
    return results_df


if __name__ == "__main__":
    example_prediction()
