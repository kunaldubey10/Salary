"""
Utility Functions
Helper functions for visualization, model saving, and common operations
"""
import logging
import pickle
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from config.config import MODELS_DIR, RESULTS_DIR

logger = logging.getLogger(__name__)


def save_model(model, model_name):
    """
    Save trained model to disk
    
    Args:
        model: Trained model object
        model_name: Name of the model
        
    Returns:
        Path to saved model
    """
    model_path = Path(MODELS_DIR) / f"{model_name}.pkl"
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    logger.info(f"Model saved to {model_path}")
    return model_path


def load_model(model_name):
    """
    Load trained model from disk
    
    Args:
        model_name: Name of the model
        
    Returns:
        Loaded model object
    """
    model_path = Path(MODELS_DIR) / f"{model_name}.pkl"
    
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at {model_path}")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    logger.info(f"Model loaded from {model_path}")
    return model


def save_results(results_df, filename="model_results.csv"):
    """
    Save evaluation results to disk
    
    Args:
        results_df: DataFrame with evaluation results
        filename: Name of the output file
        
    Returns:
        Path to saved results
    """
    results_path = Path(RESULTS_DIR) / filename
    results_df.to_csv(results_path, index=False)
    logger.info(f"Results saved to {results_path}")
    return results_path


def plot_model_comparison(results_df, metric='r2_score'):
    """
    Plot model comparison
    
    Args:
        results_df: DataFrame with evaluation results
        metric: Metric to plot
    """
    plt.figure(figsize=(12, 6))
    results_sorted = results_df.sort_values(metric, ascending=True)
    
    plt.barh(results_sorted['model'], results_sorted[metric], color='steelblue')
    plt.xlabel(metric.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Model', fontsize=12)
    plt.title(f'Model Comparison - {metric.replace("_", " ").title()}', fontsize=14)
    plt.tight_layout()
    
    plot_path = Path(RESULTS_DIR) / f"model_comparison_{metric}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    logger.info(f"Plot saved to {plot_path}")
    
    return plot_path


def plot_predictions_vs_actual(y_true, y_pred, model_name='Model'):
    """
    Plot predictions vs actual values
    
    Args:
        y_true: True values
        y_pred: Predicted values
        model_name: Name of the model
    """
    plt.figure(figsize=(10, 6))
    
    plt.scatter(y_true, y_pred, alpha=0.6, edgecolors='k')
    
    # Add diagonal line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    
    plt.xlabel('Actual Salary', fontsize=12)
    plt.ylabel('Predicted Salary', fontsize=12)
    plt.title(f'{model_name} - Predictions vs Actual', fontsize=14)
    plt.legend()
    plt.tight_layout()
    
    plot_path = Path(RESULTS_DIR) / f"predictions_vs_actual_{model_name}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    logger.info(f"Plot saved to {plot_path}")
    
    return plot_path


def plot_feature_importance(feature_importance, feature_names, model_name='Model', top_n=15):
    """
    Plot feature importance
    
    Args:
        feature_importance: Feature importance values
        feature_names: Feature names
        model_name: Name of the model
        top_n: Number of top features to plot
    """
    # Create DataFrame
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': feature_importance
    }).sort_values('importance', ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    plt.barh(importance_df['feature'], importance_df['importance'], color='steelblue')
    plt.xlabel('Importance', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.title(f'{model_name} - Top {top_n} Feature Importance', fontsize=14)
    plt.tight_layout()
    
    plot_path = Path(RESULTS_DIR) / f"feature_importance_{model_name}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    logger.info(f"Plot saved to {plot_path}")
    
    return plot_path


def plot_residuals(y_true, y_pred, model_name='Model'):
    """
    Plot residuals
    
    Args:
        y_true: True values
        y_pred: Predicted values
        model_name: Name of the model
    """
    residuals = y_true - y_pred
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Residuals vs Predicted
    axes[0].scatter(y_pred, residuals, alpha=0.6, edgecolors='k')
    axes[0].axhline(y=0, color='r', linestyle='--', lw=2)
    axes[0].set_xlabel('Predicted Values', fontsize=11)
    axes[0].set_ylabel('Residuals', fontsize=11)
    axes[0].set_title('Residuals vs Predicted', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    
    # Residuals distribution
    axes[1].hist(residuals, bins=30, edgecolor='k', alpha=0.7)
    axes[1].set_xlabel('Residuals', fontsize=11)
    axes[1].set_ylabel('Frequency', fontsize=11)
    axes[1].set_title('Distribution of Residuals', fontsize=12)
    axes[1].grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    plot_path = Path(RESULTS_DIR) / f"residuals_{model_name}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    logger.info(f"Plot saved to {plot_path}")
    
    return plot_path


def create_summary_report(results_df, best_model_name, best_metrics):
    """
    Create a summary report
    
    Args:
        results_df: DataFrame with evaluation results
        best_model_name: Name of the best model
        best_metrics: Metrics of the best model
        
    Returns:
        Path to saved report
    """
    report = f"""
    ========================================
    AI JOB SALARY PREDICTION - MODEL REPORT
    ========================================
    
    EXECUTIVE SUMMARY
    -----------------
    
    Best Model: {best_model_name}
    
    Performance Metrics:
    - R² Score: {best_metrics['r2_score']:.4f}
    - RMSE: ${best_metrics['rmse']:.2f}
    - MAE: ${best_metrics['mae']:.2f}
    
    MODEL COMPARISON
    ----------------
    
    {results_df.to_string()}
    
    INTERPRETATION
    ---------------
    
    The {best_model_name} model achieved the best performance with:
    - R² score of {best_metrics['r2_score']:.4f}, explaining {best_metrics['r2_score']*100:.2f}% of salary variance
    - Root Mean Squared Error (RMSE) of ${best_metrics['rmse']:.2f}
    - Mean Absolute Error (MAE) of ${best_metrics['mae']:.2f}
    
    ========================================
    """
    
    report_path = Path(RESULTS_DIR) / "summary_report.txt"
    with open(report_path, 'w') as f:
        f.write(report)
    
    logger.info(f"Report saved to {report_path}")
    return report_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Utils module ready for import")
