"""
Documentation for the AI Job Salary Prediction Project
"""

# PROJECT DOCUMENTATION

## Quick Start Guide

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Pipeline
```bash
# Run complete ML pipeline
python main_pipeline.py

# Make predictions
python predict.py
```

### 3. Explore Results
- Check `results/` folder for visualizations
- Review `logs/pipeline.log` for execution details
- Examine `models/` for saved trained models

## File Descriptions

### Source Code (/src/)
- **data_loader.py**: Data loading and exploration
- **preprocessing.py**: Data preprocessing and feature engineering
- **models.py**: Model training and evaluation
- **utils.py**: Utility functions for visualization and model persistence

### Configuration (/config/)
- **config.py**: Central configuration file for all project parameters

### Main Scripts
- **main_pipeline.py**: Complete ML pipeline
- **predict.py**: Prediction interface

### Testing (/tests/)
- **test_data_loader.py**: Data loader unit tests
- **test_preprocessing.py**: Preprocessing unit tests

## Understanding the Model Output

### Model Evaluation Metrics
- **R² Score**: Variance explained (0-1, higher is better)
- **RMSE**: Root Mean Squared Error in dollars
- **MAE**: Mean Absolute Error in dollars

### Interpretation Example
If a model has:
- R² = 0.85: Model explains 85% of salary variance
- RMSE = $8,200: Average prediction error is ~$8,200
- MAE = $6,500: Average absolute error is ~$6,500

## Custom Usage Example

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.models import ModelBuilder

# Load data
loader = DataLoader()
raw_data = loader.load_raw_data()

# Preprocess
preprocessor = DataPreprocessor()
processed_data = preprocessor.preprocess(raw_data)

# Build and train models
builder = ModelBuilder()
builder.build_models()
builder.train_all_models(X_train, y_train)

# Evaluate
results = builder.evaluate_all_models(X_test, y_test)
print(results)
```

## Troubleshooting

### Issue: Module not found error
**Solution**: Ensure PROJECT_ROOT is added to sys.path at the top of scripts

### Issue: Data not found
**Solution**: Check that dataset is in `archive/AI Job Market Dataset.csv`

### Issue: Memory error during training
**Solution**: Reduce dataset size or use subset of models

## Next Steps

1. Hyperparameter tuning
2. Cross-validation
3. Feature selection
4. Model ensemble
5. Production deployment

"""
