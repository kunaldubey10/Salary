"""
Unit tests for data loading
"""
import sys
from pathlib import Path
import unittest
import pandas as pd

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.data_loader import DataLoader
from config.config import RAW_DATA_PATH, TARGET


class TestDataLoader(unittest.TestCase):
    """Test cases for DataLoader class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.loader = DataLoader()
    
    def test_load_raw_data(self):
        """Test loading raw data"""
        data = self.loader.load_raw_data()
        
        self.assertIsNotNone(data)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)
    
    def test_data_shape(self):
        """Test if data has expected shape"""
        data = self.loader.load_raw_data()
        
        self.assertEqual(len(data.columns), 19)
        self.assertGreater(len(data), 0)
    
    def test_target_column_exists(self):
        """Test if target column exists"""
        data = self.loader.load_raw_data()
        
        self.assertIn(TARGET, data.columns)
    
    def test_get_data_info(self):
        """Test get_data_info method"""
        info = self.loader.get_data_info()
        
        self.assertIn('shape', info)
        self.assertIn('columns', info)
        self.assertIn('missing_values', info)


if __name__ == '__main__':
    unittest.main()
