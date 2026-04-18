"""
Data Loading Module
Handles loading and initial exploration of the dataset
"""
import pandas as pd
import numpy as np
import logging
from pathlib import Path
from config.config import RAW_DATA_PATH, DATA_PROCESSED, FEATURE_DTYPES

logger = logging.getLogger(__name__)


class DataLoader:
    """Load and preprocess data"""
    
    def __init__(self, data_path=RAW_DATA_PATH):
        """
        Initialize DataLoader
        
        Args:
            data_path: Path to the raw dataset
        """
        self.data_path = Path(data_path)
        self.raw_data = None
        self.processed_data = None
        
    def load_raw_data(self):
        """Load raw dataset from CSV"""
        try:
            self.raw_data = pd.read_csv(self.data_path)
            logger.info(f"Data loaded successfully. Shape: {self.raw_data.shape}")
            return self.raw_data
        except FileNotFoundError:
            logger.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def get_data_info(self):
        """Get information about the dataset"""
        if self.raw_data is None:
            self.load_raw_data()
            
        info_dict = {
            'shape': self.raw_data.shape,
            'columns': self.raw_data.columns.tolist(),
            'dtypes': self.raw_data.dtypes.to_dict(),
            'missing_values': self.raw_data.isnull().sum().to_dict(),
            'duplicates': self.raw_data.duplicated().sum(),
        }
        
        logger.info(f"Dataset Info: {info_dict}")
        return info_dict
    
    def get_basic_statistics(self):
        """Get basic statistics of the dataset"""
        if self.raw_data is None:
            self.load_raw_data()
            
        return self.raw_data.describe()
    
    def check_missing_values(self):
        """Check for missing values"""
        if self.raw_data is None:
            self.load_raw_data()
            
        missing = self.raw_data.isnull().sum()
        missing_percent = (missing / len(self.raw_data)) * 100
        
        missing_df = pd.DataFrame({
            'Missing_Count': missing,
            'Percentage': missing_percent
        }).sort_values('Missing_Count', ascending=False)
        
        return missing_df[missing_df['Missing_Count'] > 0]
    
    def save_processed_data(self, data, filename="processed_data.csv"):
        """Save processed data to CSV"""
        output_path = Path(DATA_PROCESSED) / filename
        data.to_csv(output_path, index=False)
        logger.info(f"Data saved to {output_path}")
        return output_path


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    
    # Load and explore data
    loader = DataLoader()
    data = loader.load_raw_data()
    print("\nDataset Shape:", data.shape)
    print("\nFirst few rows:")
    print(data.head())
    print("\nDataset Info:")
    print(loader.get_data_info())
    print("\nBasic Statistics:")
    print(loader.get_basic_statistics())
    print("\nMissing Values:")
    print(loader.check_missing_values())
