"""
Unit tests for preprocessing
"""
import sys
from pathlib import Path
import unittest
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor
from config.config import TARGET


class TestDataPreprocessor(unittest.TestCase):
    """Test cases for DataPreprocessor class"""
    
    def setUp(self):
        """Set up test fixtures"""
        loader = DataLoader()
        self.raw_data = loader.load_raw_data().head(100)
        self.preprocessor = DataPreprocessor()
    
    def test_handle_missing_values(self):
        """Test missing value handling"""
        data = self.raw_data.copy()
        
        # Introduce missing values
        data.loc[0, 'years_experience'] = np.nan
        
        processed = self.preprocessor.handle_missing_values(data)
        
        self.assertFalse(processed.isnull().any().any())
    
    def test_encode_categorical_features(self):
        """Test categorical encoding"""
        data = self.raw_data.copy()
        
        processed = self.preprocessor.encode_categorical_features(data, fit=True)
        
        self.assertEqual(processed.shape, data.shape)
    
    def test_preprocess_pipeline(self):
        """Test complete preprocessing pipeline"""
        data = self.raw_data.copy()
        
        processed = self.preprocessor.preprocess(
            data, scale=True, remove_outliers_flag=False
        )
        
        self.assertEqual(processed.shape[1], data.shape[1])
        self.assertFalse(processed.isnull().any().any())


if __name__ == '__main__':
    unittest.main()
