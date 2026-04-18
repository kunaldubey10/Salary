"""
GETTING STARTED - Complete Setup Guide
"""

GETTING_STARTED = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║             AI JOB SALARY PREDICTION - GETTING STARTED GUIDE                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝

🎯 GOAL
Build a machine learning model to predict AI job salaries based on job features
such as experience, skills, location, and other market factors.

═════════════════════════════════════════════════════════════════════════════════

📋 PREREQUISITES

✓ Python 3.8 or higher
✓ pip (Python package manager)
✓ Git (optional, for version control)
✓ ~500MB disk space for models and results

Check Python Version:
  $ python --version
  # Should show Python 3.8 or higher

═════════════════════════════════════════════════════════════════════════════════

🚀 STEP-BY-STEP SETUP

STEP 1: Navigate to Project Directory
────────────────────────────────────────
$ cd d:\\salary
  or
$ cd salary  (if running from parent directory)


STEP 2: Create Virtual Environment (Recommended)
────────────────────────────────────────────────
Windows:
  $ python -m venv venv
  $ venv\\Scripts\\activate

macOS/Linux:
  $ python -m venv venv
  $ source venv/bin/activate

You should see (venv) in your terminal prompt.


STEP 3: Upgrade pip
───────────────────
$ python -m pip install --upgrade pip


STEP 4: Install Dependencies
─────────────────────────────
$ pip install -r requirements.txt

Wait for all packages to install (takes 2-5 minutes).

Main packages installed:
  ✓ pandas              - Data manipulation
  ✓ scikit-learn        - ML algorithms
  ✓ xgboost/lightgbm    - Gradient boosting
  ✓ matplotlib/seaborn  - Visualization
  ✓ jupyter             - Interactive notebooks


STEP 5: Verify Installation
────────────────────────────
Run this to check if everything is installed:

$ python -c "import pandas; import sklearn; print('✓ All dependencies installed!')"

If you see "✓ All dependencies installed!" - you're ready!


STEP 6: Verify Dataset
──────────────────────
Check that the dataset exists:

$ python
  >>> import pandas as pd
  >>> df = pd.read_csv('archive/AI Job Market Dataset.csv')
  >>> print(f"Dataset shape: {df.shape}")
  >>> print(f"Columns: {df.columns.tolist()}")
  >>> exit()

You should see:
  Dataset shape: (XXX, 19)
  Columns: ['job_id', 'job_title', ...]


═════════════════════════════════════════════════════════════════════════════════

🔧 QUICK START - 3 EASY STEPS

1️⃣  RUN THE COMPLETE PIPELINE
──────────────────────────────
$ python main_pipeline.py

This will automatically:
✓ Load raw data
✓ Preprocess and clean data  
✓ Build 9 ML models
✓ Train all models
✓ Evaluate and compare models
✓ Save best model
✓ Generate visualizations
✓ Create summary report

⏱️  Takes approximately 2-5 minutes
📍 Results saved to results/ folder


2️⃣  VIEW THE RESULTS
────────────────────
After pipeline completes, check:

results/
  ├── model_results.csv               # All model metrics
  ├── model_comparison_r2_score.png   # Performance comparison
  ├── predictions_vs_actual_*.png     # Prediction accuracy
  ├── feature_importance_*.png        # Top features
  └── summary_report.txt              # Executive summary

models/
  └── xgboost.pkl                     # Best trained model


3️⃣  MAKE PREDICTIONS
────────────────────
$ python predict.py

Or use predictions in your code:

  from predict import SalaryPredictor
  predictor = SalaryPredictor(model_name='xgboost')
  predicted_salary = predictor.predict_single({
      'job_title': 'Data Scientist',
      'experience_level': 'Senior',
      'years_experience': 5,
      # ... other features
  })
  print(f"Predicted Salary: ${predicted_salary:,.2f}")


═════════════════════════════════════════════════════════════════════════════════

📓 EXPLORE DATA WITH JUPYTER NOTEBOOKS

Start Jupyter:
  $ jupyter notebook

Browse to notebooks/ folder:
  ✓ 01_exploratory_analysis.ipynb     - Data exploration
  ✓ 02_feature_engineering.ipynb      - Feature creation
  ✓ 03_model_training.ipynb           - Model development


═════════════════════════════════════════════════════════════════════════════════

📊 UNDERSTAND THE OUTPUT

Model Performance Metrics:

R² Score (Coefficient of Determination):
  • Range: 0 to 1 (higher is better)
  • 0.85 = model explains 85% of salary variance
  • Good for: Understanding model accuracy

RMSE (Root Mean Squared Error):
  • In dollars (USD)
  • ±$8,000 RMSE = predictions off by ~$8,000 on average
  • Lower is better

MAE (Mean Absolute Error):
  • In dollars (USD)
  • Similar to RMSE but less sensitive to outliers
  • Average absolute prediction error

Example Results:
┌──────────────┬──────────┬──────────┬──────────┐
│ Model        │ R² Score │ RMSE     │ MAE      │
├──────────────┼──────────┼──────────┼──────────┤
│ Linear Regr. │   0.65   │ $12,500  │ $10,100  │
│ Random Forest│   0.78   │  $9,800  │  $7,900  │
│ XGBoost ⭐   │   0.85   │  $8,200  │  $6,500  │
│ LightGBM     │   0.84   │  $8,400  │  $6,700  │
└──────────────┴──────────┴──────────┴──────────┘


═════════════════════════════════════════════════════════════════════════════════

🔍 PROJECT FILES EXPLAINED

Main Scripts:
  main_pipeline.py    ← Run this to train models
  predict.py          ← Make predictions with trained models
  setup.py            ← Initialize project

Source Code (src/):
  data_loader.py      - Load and explore data
  preprocessing.py    - Clean and prepare data
  models.py           - Build and train ML models
  utils.py            - Helper functions

Configuration:
  config/config.py    - Hyperparameters and settings

Data:
  archive/           - Original dataset
  data/raw/          - Raw data location
  data/processed/    - Preprocessed data

Output:
  models/            - Saved trained models
  results/           - Visualizations and metrics
  logs/              - Pipeline execution logs


═════════════════════════════════════════════════════════════════════════════════

⚙️  CUSTOMIZATION

Modify Hyperparameters:
  1. Open config/config.py
  2. Edit MODEL_PARAMS dictionary
  3. Re-run: python main_pipeline.py

Change Features:
  1. Open config/config.py
  2. Edit CATEGORICAL_FEATURES or NUMERICAL_FEATURES
  3. Update preprocessing.py if needed
  4. Re-run: python main_pipeline.py

Add Custom Models:
  1. Open src/models.py
  2. Add model in build_models() method
  3. Re-run: python main_pipeline.py


═════════════════════════════════════════════════════════════════════════════════

🐛 TROUBLESHOOTING

Problem: "ModuleNotFoundError: No module named 'pandas'"
Solution:
  $ pip install -r requirements.txt

Problem: "FileNotFoundError: archive/AI Job Market Dataset.csv"
Solution:
  ✓ Verify file exists in archive/ folder
  ✓ Check file name spelling exactly

Problem: "Memory Error" during training
Solution:
  ✓ Use smaller dataset: raw_data.head(1000)
  ✓ Train subset of models
  ✓ Increase system RAM or reduce features

Problem: Script runs but produces wrong results
Solution:
  ✓ Check config/config.py settings
  ✓ Verify data preprocessing
  ✓ Check test data shape matches training

Problem: Jupyter notebook not found
Solution:
  $ jupyter notebook --notebook-dir=notebooks


═════════════════════════════════════════════════════════════════════════════════

📈 TYPICAL WORKFLOW

Day 1 - Setup:
  ✓ Run setup.py
  ✓ Install dependencies
  ✓ Verify dataset
  ✓ Run main_pipeline.py

Day 2 - Exploration:
  ✓ Open Jupyter notebooks
  ✓ Explore data distributions
  ✓ Analyze feature relationships
  ✓ Understand salary patterns

Day 3 - Enhancement:
  ✓ Experiment with features
  ✓ Try different models
  ✓ Tune hyperparameters
  ✓ Compare performance

Day 4 - Deployment:
  ✓ Select best model
  ✓ Make predictions
  ✓ Create API (optional)
  ✓ Document results


═════════════════════════════════════════════════════════════════════════════════

💾 SAVING YOUR WORK

Models are saved automatically in models/ folder
Results are saved in results/ folder
To backup everything:
  $ python -c "import shutil; shutil.copytree('.', 'salary_backup_DATE')"

To load a previously trained model:
  from src.utils import load_model
  model = load_model('xgboost')
  predictions = model.predict(X_test)


═════════════════════════════════════════════════════════════════════════════════

✅ SUCCESS INDICATORS

Pipeline ran successfully if you see:
  ✓ Messages like "Data loaded successfully"
  ✓ "All models trained successfully"
  ✓ Model performance metrics printed
  ✓ Files created in results/ folder
  ✓ Models saved in models/ folder

Good model performance indicators:
  ✓ R² Score > 0.80
  ✓ RMSE < $10,000
  ✓ MAE < $8,000


═════════════════════════════════════════════════════════════════════════════════

🎓 LEARNING RESOURCES

Inside the project:
  ✓ README.md - Overview and features
  ✓ DOCUMENTATION.md - Technical details
  ✓ PROJECT_STRUCTURE.md - File organization
  ✓ config/config.py - Configuration guide

External:
  ✓ Scikit-learn: https://scikit-learn.org
  ✓ XGBoost: https://xgboost.readthedocs.io
  ✓ Pandas: https://pandas.pydata.org


═════════════════════════════════════════════════════════════════════════════════

❓ FREQUENTLY ASKED QUESTIONS

Q: How long does the pipeline take?
A: Typically 2-5 minutes depending on dataset size and system specs

Q: Why are there so many models?
A: Comparing models helps find the best one for your specific data

Q: Can I use this for different datasets?
A: Yes! Modify config.py and preprocessing.py for your data

Q: How do I improve predictions?
A: Try hyperparameter tuning, feature engineering, or more data

Q: Can I deploy this as an API?
A: Yes! Use Flask or FastAPI with the predict.py module

Q: What's the difference between train and test data?
A: Train: teach model | Test: evaluate model performance

Q: Why use virtual environment?
A: Isolates project dependencies, prevents conflicts


═════════════════════════════════════════════════════════════════════════════════

🏁 NEXT STEPS

After successful setup:

1. Run the pipeline
2. Review results and visualizations
3. Explore data with Jupyter notebooks
4. Experiment with hyperparameters
5. Create custom features
6. Build web API with Flask
7. Deploy to production

═════════════════════════════════════════════════════════════════════════════════

💡 TIPS FOR SUCCESS

✓ Start with default configuration
✓ Review logs for debugging
✓ Experiment systematically
✓ Keep backup of good results
✓ Document changes and results
✓ Use version control (git)
✓ Test on small data first
✓ Monitor memory usage


═════════════════════════════════════════════════════════════════════════════════

📞 NEED HELP?

1. Check DOCUMENTATION.md for technical details
2. Review config/config.py for configuration
3. Look at example code in notebooks/
4. Check script logs in logs/ folder
5. Examine error messages carefully

═════════════════════════════════════════════════════════════════════════════════

🎉 YOU'RE ALL SET!

Your AI Job Salary Prediction project is ready to go.

Next command to run:

    $ python main_pipeline.py

Good luck! 🚀

═════════════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(GETTING_STARTED)
    
    # Save to file
    with open('GETTING_STARTED.txt', 'w') as f:
        f.write(GETTING_STARTED)
    print("\n✓ Guide saved to GETTING_STARTED.txt")
