"""
Main Pipeline
Complete machine learning pipeline for AI job salary prediction
"""
import sys
import os
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from config.config import RANDOM_STATE, DATA_PROCESSED, RESULTS_DIR
from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor, prepare_train_test_data
from src.models import ModelBuilder
from src.utils import (
    save_model, save_results, plot_model_comparison,
    plot_predictions_vs_actual, plot_residuals, create_summary_report
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(PROJECT_ROOT / 'logs' / 'pipeline.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Run the complete ML pipeline"""
    
    logger.info("=" * 80)
    logger.info("STARTING AI JOB SALARY PREDICTION PIPELINE")
    logger.info("=" * 80)
    
    # Step 1: Load Data
    logger.info("\n[Step 1] Loading data...")
    loader = DataLoader()
    raw_data = loader.load_raw_data()
    logger.info(f"Raw data shape: {raw_data.shape}")
    
    # Step 2: Preprocess Data
    logger.info("\n[Step 2] Preprocessing data...")
    preprocessor = DataPreprocessor()
    processed_data = preprocessor.preprocess(raw_data, scale=True, remove_outliers_flag=False)
    logger.info(f"Processed data shape: {processed_data.shape}")
    
    # Save processed data
    loader.save_processed_data(processed_data)
    
    # Step 3: Prepare Train-Test Split
    logger.info("\n[Step 3] Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = prepare_train_test_data(processed_data)
    logger.info(f"Training set: {X_train.shape}")
    logger.info(f"Test set: {X_test.shape}")
    
    # Step 4: Build Models
    logger.info("\n[Step 4] Building machine learning models...")
    model_builder = ModelBuilder()
    model_builder.build_models()
    logger.info(f"Built {len(model_builder.models)} models")
    
    # Step 5: Train Models
    logger.info("\n[Step 5] Training all models...")
    model_builder.train_all_models(X_train, y_train)
    logger.info("All models trained successfully")
    
    # Step 6: Evaluate Models
    logger.info("\n[Step 6] Evaluating all models on test set...")
    results_df = model_builder.evaluate_all_models(X_test, y_test)
    logger.info("\nModel Evaluation Results:")
    logger.info("\n" + results_df.to_string())
    
    # Save results
    save_results(results_df)
    
    # Step 7: Get Best Model
    logger.info("\n[Step 7] Identifying best model...")
    best_model_name, best_metrics = model_builder.get_best_model()
    logger.info(f"Best Model: {best_model_name}")
    logger.info(f"R² Score: {best_metrics['r2_score']:.4f}")
    logger.info(f"RMSE: ${best_metrics['rmse']:.2f}")
    logger.info(f"MAE: ${best_metrics['mae']:.2f}")
    
    # Step 8: Save Best Model
    logger.info("\n[Step 8] Saving best model...")
    best_model = model_builder.models[best_model_name]
    save_model(best_model, best_model_name)
    
    # Step 9: Generate Visualizations
    logger.info("\n[Step 9] Generating visualizations...")
    plot_model_comparison(results_df, 'r2_score')
    plot_model_comparison(results_df, 'rmse')
    
    y_pred_best = model_builder.predict(best_model_name, X_test)
    plot_predictions_vs_actual(y_test, y_pred_best, best_model_name)
    plot_residuals(y_test, y_pred_best, best_model_name)
    
    # Step 10: Create Summary Report
    logger.info("\n[Step 10] Creating summary report...")
    create_summary_report(results_df, best_model_name, best_metrics)
    
    logger.info("\n" + "=" * 80)
    logger.info("PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 80)
    
    return {
        'best_model_name': best_model_name,
        'best_model': best_model,
        'results_df': results_df,
        'best_metrics': best_metrics,
        'preprocessor': preprocessor,
        'X_test': X_test,
        'y_test': y_test,
        'y_pred_best': y_pred_best,
    }


if __name__ == "__main__":
    pipeline_results = main()
