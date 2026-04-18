"""
Machine Learning Models Module
Handles model training, evaluation, and comparison
"""
import logging
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import xgboost as xgb
import lightgbm as lgb
from config.config import MODEL_PARAMS, RANDOM_STATE

logger = logging.getLogger(__name__)


class ModelBuilder:
    """Build and train various ML models"""
    
    def __init__(self):
        """Initialize model builder"""
        self.models = {}
        self.results = {}
        
    def build_models(self):
        """Build all available models"""
        
        # Linear Models
        self.models['linear_regression'] = LinearRegression()
        self.models['ridge'] = Ridge(**MODEL_PARAMS['ridge'])
        self.models['lasso'] = Lasso(**MODEL_PARAMS['lasso'])
        self.models['elasticnet'] = ElasticNet(**MODEL_PARAMS['elasticnet'])
        
        # SVM
        self.models['svr'] = SVR(**MODEL_PARAMS['svr'])
        
        # Tree-based Models
        self.models['random_forest'] = RandomForestRegressor(**MODEL_PARAMS['random_forest'])
        self.models['gradient_boosting'] = GradientBoostingRegressor(**MODEL_PARAMS['gradient_boosting'])
        
        # Boosting Models
        self.models['xgboost'] = xgb.XGBRegressor(**MODEL_PARAMS['xgboost'])
        self.models['lightgbm'] = lgb.LGBMRegressor(**MODEL_PARAMS['lightgbm'])
        
        logger.info(f"Built {len(self.models)} models")
        return self.models
    
    def train_model(self, model_name, X_train, y_train):
        """
        Train a specific model
        
        Args:
            model_name: Name of the model
            X_train: Training features
            y_train: Training target
            
        Returns:
            Trained model
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found")
        
        model = self.models[model_name]
        model.fit(X_train, y_train)
        logger.info(f"Trained model: {model_name}")
        
        return model
    
    def train_all_models(self, X_train, y_train):
        """
        Train all models
        
        Args:
            X_train: Training features
            y_train: Training target
            
        Returns:
            Dictionary of trained models
        """
        if not self.models:
            self.build_models()
        
        trained_models = {}
        for model_name in self.models.keys():
            try:
                trained_models[model_name] = self.train_model(model_name, X_train, y_train)
            except Exception as e:
                logger.error(f"Error training {model_name}: {str(e)}")
        
        self.models = trained_models
        return trained_models
    
    def predict(self, model_name, X):
        """
        Make predictions using a specific model
        
        Args:
            model_name: Name of the model
            X: Features for prediction
            
        Returns:
            Predictions
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found")
        
        return self.models[model_name].predict(X)
    
    def evaluate_model(self, model_name, X_test, y_test):
        """
        Evaluate a specific model
        
        Args:
            model_name: Name of the model
            X_test: Test features
            y_test: Test target
            
        Returns:
            Dictionary of evaluation metrics
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found")
        
        y_pred = self.predict(model_name, X_test)
        
        metrics = {
            'model': model_name,
            'mae': mean_absolute_error(y_test, y_pred),
            'mse': mean_squared_error(y_test, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
            'r2_score': r2_score(y_test, y_pred),
        }
        
        return metrics
    
    def evaluate_all_models(self, X_test, y_test):
        """
        Evaluate all models
        
        Args:
            X_test: Test features
            y_test: Test target
            
        Returns:
            DataFrame of evaluation results
        """
        results = []
        
        for model_name in self.models.keys():
            try:
                metrics = self.evaluate_model(model_name, X_test, y_test)
                results.append(metrics)
                logger.info(f"Evaluated {model_name}: R² = {metrics['r2_score']:.4f}")
            except Exception as e:
                logger.error(f"Error evaluating {model_name}: {str(e)}")
        
        self.results = pd.DataFrame(results)
        return self.results
    
    def get_best_model(self):
        """
        Get the best performing model
        
        Returns:
            Best model name and its metrics
        """
        if self.results.empty:
            raise ValueError("No evaluation results available. Run evaluate_all_models first.")
        
        best_idx = self.results['r2_score'].idxmax()
        best_model_name = self.results.loc[best_idx, 'model']
        best_metrics = self.results.loc[best_idx]
        
        logger.info(f"Best model: {best_model_name} with R² = {best_metrics['r2_score']:.4f}")
        
        return best_model_name, best_metrics
    
    def get_feature_importance(self, model_name):
        """
        Get feature importance for tree-based models
        
        Args:
            model_name: Name of the model
            
        Returns:
            Feature importance dictionary
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found")
        
        model = self.models[model_name]
        
        # Check if model has feature_importances_
        if not hasattr(model, 'feature_importances_'):
            logger.warning(f"Model '{model_name}' doesn't have feature_importances_")
            return None
        
        return model.feature_importances_


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    print("Models module ready for import")
