# AI Job Salary Prediction

## Project Overview

This project builds a machine learning model to predict salaries for AI job roles based on historical job market data. The model considers various factors including:

- **Job Details**: Job title, role, company size and industry
- **Experience**: Years of experience and experience level
- **Skills**: Python, SQL, ML, Deep Learning, Cloud
- **Location**: Country and work type (Remote/Onsite/Hybrid)
- **Education**: Educational background (Bachelor's/Master's/PhD)
- **Market Factors**: Hiring urgency, number of openings, job posting timing

## Project Structure

```
salary/
├── archive/                          # Original dataset
│   └── AI Job Market Dataset.csv
│
├── data/
│   ├── raw/                          # Raw input data
│   └── processed/                    # Processed data for modeling
│
├── notebooks/                        # Jupyter notebooks for EDA and analysis
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── src/                              # Source code modules
│   ├── __init__.py
│   ├── data_loader.py               # Data loading utilities
│   ├── preprocessing.py             # Data preprocessing and cleaning
│   ├── models.py                    # ML model building and training
│   └── utils.py                     # Utility functions
│
├── config/
│   └── config.py                    # Configuration and hyperparameters
│
├── models/                           # Saved trained models
│   ├── xgboost.pkl
│   ├── lightgbm.pkl
│   └── ...
│
├── results/                          # Model results and visualizations
│   ├── model_results.csv
│   ├── model_comparison_r2_score.png
│   └── ...
│
├── logs/                             # Execution logs
│   └── pipeline.log
│
├── tests/                            # Unit tests
│   ├── test_data_loader.py
│   └── test_preprocessing.py
│
├── main_pipeline.py                  # Complete ML pipeline
├── predict.py                        # Prediction script
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore file
└── README.md                         # This file
```

## Installation

### 1. Clone/Download the Project
```bash
cd salary
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Complete Pipeline

```bash
python main_pipeline.py
```

This will:
1. Load raw data
2. Preprocess and clean data
3. Split into train/test sets
4. Build and train multiple models
5. Evaluate all models
6. Identify the best performing model
7. Generate visualizations and reports
8. Save models and results

### Making Predictions

```bash
python predict.py
```

Or use the predictor in your own code:

```python
from predict import SalaryPredictor

predictor = SalaryPredictor(model_name='xgboost')

# Predict for a single job
new_job = {
    'job_title': 'Data Scientist',
    'company_size': 'MNC',
    'company_industry': 'Technology',
    'country': 'USA',
    'remote_type': 'Remote',
    'experience_level': 'Mid',
    'years_experience': 5,
    'education_level': 'Master',
    'skills_python': 1,
    'skills_sql': 1,
    'skills_ml': 1,
    'skills_deep_learning': 0,
    'skills_cloud': 1,
    'job_posting_month': 6,
    'job_posting_year': 2024,
    'hiring_urgency': 'High',
    'job_openings': 5
}

predicted_salary = predictor.predict_single(new_job)
print(f"Predicted Salary: ${predicted_salary:,.2f}")
```

### Jupyter Notebooks

For exploratory data analysis and detailed analysis:

```bash
jupyter notebook notebooks/
```

Available notebooks:
- **01_exploratory_analysis.ipynb**: Data exploration and visualization
- **02_feature_engineering.ipynb**: Feature creation and selection
- **03_model_training.ipynb**: Model development and comparison

## Dataset

The dataset contains 500+ AI job postings with the following features:

| Feature | Type | Description |
|---------|------|-------------|
| job_id | int | Unique job identifier |
| job_title | string | Job position title |
| company_size | string | Company size (Startup, Medium, Enterprise, MNC) |
| company_industry | string | Industry sector |
| country | string | Job location country |
| remote_type | string | Work type (Remote, Onsite, Hybrid) |
| experience_level | string | Required experience (Entry, Mid, Senior) |
| years_experience | int | Years of experience required |
| education_level | string | Required education (Bachelor, Master, PhD) |
| skills_python | binary | Python skill required (0/1) |
| skills_sql | binary | SQL skill required (0/1) |
| skills_ml | binary | ML skill required (0/1) |
| skills_deep_learning | binary | Deep Learning skill required (0/1) |
| skills_cloud | binary | Cloud skill required (0/1) |
| salary | float | **Target variable** - Annual salary (USD) |
| job_posting_month | int | Month of posting |
| job_posting_year | int | Year of posting |
| hiring_urgency | string | Urgency level (Low, Medium, High) |
| job_openings | int | Number of openings |

## Models Implemented

The pipeline trains and compares the following models:

1. **Linear Regression** - Simple baseline model
2. **Ridge Regression** - L2 regularized linear model
3. **Lasso Regression** - L1 regularized linear model
4. **Elastic Net** - Combined L1 and L2 regularization
5. **Support Vector Regression (SVR)** - Non-linear SVM
6. **Random Forest** - Ensemble of decision trees
7. **Gradient Boosting** - Sequential boosting
8. **XGBoost** - Optimized gradient boosting
9. **LightGBM** - Light gradient boosting

## Evaluation Metrics

- **Mean Absolute Error (MAE)** - Average absolute prediction error
- **Mean Squared Error (MSE)** - Average squared error
- **Root Mean Squared Error (RMSE)** - Square root of MSE
- **R² Score** - Coefficient of determination (variance explained)

## Results

Results are saved in the `results/` directory:

- `model_results.csv` - Detailed metrics for all models
- `model_comparison_*.png` - Visualization of model performance
- `predictions_vs_actual_*.png` - Predictions vs actual values plot
- `residuals_*.png` - Residual analysis plots
- `feature_importance_*.png` - Top features for tree-based models
- `summary_report.txt` - Executive summary report

## Configuration

Modify `config/config.py` to customize:

- Train/test split ratio
- Model hyperparameters
- Feature selections
- Random state for reproducibility

## Key Features

✓ **Complete Pipeline**: End-to-end ML workflow
✓ **Multiple Models**: 9 different algorithms for comparison
✓ **Data Preprocessing**: Handling missing values, encoding, scaling
✓ **Feature Engineering**: Automated feature creation
✓ **Model Evaluation**: Comprehensive metrics and visualizations
✓ **Model Persistence**: Save and load trained models
✓ **Prediction API**: Easy-to-use prediction interface
✓ **Logging**: Detailed execution logs
✓ **Reproducibility**: Fixed random states

## Performance Example

Expected model performance (approximate):

| Model | R² Score | RMSE |
|-------|----------|------|
| Linear Regression | 0.65 | $12,500 |
| Random Forest | 0.78 | $9,800 |
| Gradient Boosting | 0.82 | $8,900 |
| **XGBoost** | **0.85** | **$8,200** |
| LightGBM | 0.84 | $8,400 |

## Next Steps

1. **Model Optimization**: Tune hyperparameters using GridSearchCV
2. **Cross-Validation**: Implement k-fold cross-validation
3. **Ensemble Methods**: Combine multiple models
4. **Advanced Features**: Add more domain-specific features
5. **Web API**: Deploy model as REST API
6. **Docker**: Containerize for deployment

## Dependencies

See `requirements.txt` for complete list:
- pandas: Data manipulation
- numpy: Numerical computing
- scikit-learn: ML algorithms
- xgboost, lightgbm, catboost: Boosting models
- matplotlib, seaborn, plotly: Visualization
- jupyter: Interactive notebooks
- pytest: Testing framework

## Authors

Data Science Team

## License

MIT License

## Support

For issues or questions, please refer to the documentation or create an issue in the repository.

---

**Last Updated**: April 2026
