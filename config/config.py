"""
Configuration file for AI Job Salary Prediction Project
"""
import os
from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
ARCHIVE_DATA = PROJECT_ROOT / "archive"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"
LOGS_DIR = PROJECT_ROOT / "logs"

# Dataset configuration
DATASET_NAME = "AI Job Market Dataset.csv"
RAW_DATA_PATH = ARCHIVE_DATA / DATASET_NAME

# Feature columns
CATEGORICAL_FEATURES = [
    'job_title',
    'company_size',
    'company_industry',
    'country',
    'remote_type',
    'experience_level',
    'education_level',
]

NUMERICAL_FEATURES = [
    'years_experience',
    'skills_python',
    'skills_sql',
    'skills_ml',
    'skills_deep_learning',
    'skills_cloud',
    'job_posting_month',
    'job_posting_year',
    'job_openings',
]

SKILL_FEATURES = [
    'skills_python',
    'skills_sql',
    'skills_ml',
    'skills_deep_learning',
    'skills_cloud',
]

# Target variable
TARGET = 'salary'

# Data types
FEATURE_DTYPES = {
    'job_id': 'int64',
    'job_title': 'object',
    'company_size': 'object',
    'company_industry': 'object',
    'country': 'object',
    'remote_type': 'object',
    'experience_level': 'object',
    'years_experience': 'int64',
    'education_level': 'object',
    'skills_python': 'int64',
    'skills_sql': 'int64',
    'skills_ml': 'int64',
    'skills_deep_learning': 'int64',
    'skills_cloud': 'int64',
    'salary': 'float64',
    'job_posting_month': 'int64',
    'job_posting_year': 'int64',
    'hiring_urgency': 'object',
    'job_openings': 'int64',
}

# Train-test split configuration
TRAIN_TEST_SPLIT = 0.8
RANDOM_STATE = 42
VALIDATION_SPLIT = 0.2

# Model parameters
MODEL_PARAMS = {
    'linear_regression': {},
    'ridge': {'alpha': 1.0},
    'lasso': {'alpha': 1.0},
    'elasticnet': {'alpha': 1.0, 'l1_ratio': 0.5},
    'svr': {'kernel': 'rbf', 'C': 100},
    'random_forest': {
        'n_estimators': 100,
        'max_depth': 15,
        'min_samples_split': 5,
        'random_state': RANDOM_STATE,
        'n_jobs': -1,
    },
    'gradient_boosting': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': RANDOM_STATE,
    },
    'xgboost': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': RANDOM_STATE,
        'verbosity': 0,
    },
    'lightgbm': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': RANDOM_STATE,
        'verbose': -1,
    },
}

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
