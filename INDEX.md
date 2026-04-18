"""
INDEX & NAVIGATION GUIDE
Complete guide to all project files and documentation
"""

INDEX = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║           AI JOB SALARY PREDICTION - COMPLETE PROJECT INDEX                   ║
║                                                                               ║
║                     Your Production-Ready ML Project                          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝


📚 DOCUMENTATION INDEX
═════════════════════════════════════════════════════════════════════════════════

🟢 START HERE (Pick Your Path)
────────────────────────────────

For Quick Start (5 minutes):
  → GETTING_STARTED.md
      • Prerequisites
      • 6-step setup
      • 3-step quick start
      • Troubleshooting
      
For Project Overview:
  → README.md
      • Features
      • Installation
      • Usage
      • Dataset details
      
For Complete Understanding:
  → PROJECT_SUMMARY.md
      • Full project overview
      • What's included
      • Next steps
      • Customization options


🟡 DOCUMENTATION FILES (Read in Order)
──────────────────────────────────────

1. GETTING_STARTED.md (BEGINNER → EXPERT)
   └─ Step-by-step setup and configuration
   └─ Common issues and solutions
   └─ FAQ section
   └─ Success indicators

2. README.md (PROJECT OVERVIEW)
   └─ Quick installation
   └─ Usage examples
   └─ Dataset description
   └─ Model information
   └─ Performance examples

3. PROJECT_STRUCTURE.md (FILE ORGANIZATION)
   └─ Complete directory tree
   └─ Module descriptions
   └─ 30+ function descriptions
   └─ Customization guide

4. DOCUMENTATION.md (TECHNICAL REFERENCE)
   └─ Detailed technical docs
   └─ Custom usage examples
   └─ Troubleshooting guide
   └─ Advanced techniques

5. PROJECT_SUMMARY.md (COMPLETE REFERENCE)
   └─ Everything in one place
   └─ Checklist and progress tracking
   └─ Next steps and roadmap
   └─ Learning outcomes
   
6. This File - INDEX.md (NAVIGATION)
   └─ Where to find everything
   └─ Quick reference guide


═════════════════════════════════════════════════════════════════════════════════

🔧 CONFIGURATION & SETUP
════════════════════════════════════════════════════════════════════════════════

requirements.txt
  └─ Python package dependencies
  └─ Install with: pip install -r requirements.txt

setup.py
  └─ Project initialization script
  └─ Checks setup and dependencies
  └─ Creates missing directories
  └─ Run with: python setup.py

config/config.py
  └─ 🔧 CENTRAL CONFIGURATION FILE
  └─ Modify hyperparameters here
  └─ Feature definitions
  └─ Model settings
  └─ Path configurations

.gitignore
  └─ Git configuration
  └─ What to exclude from version control


═════════════════════════════════════════════════════════════════════════════════

🚀 MAIN SCRIPTS (THE ONES YOU RUN)
═════════════════════════════════════════════════════════════════════════════════

main_pipeline.py ⭐ START HERE
  ├─ Complete ML pipeline in one script
  ├─ Loads, processes, trains, evaluates
  ├─ Generates visualizations and reports
  ├─ Saves best model and results
  └─ Run with: python main_pipeline.py

predict.py
  ├─ Make predictions with trained model
  ├─ Load pre-trained models
  ├─ Batch or single predictions
  ├─ Easy-to-use API
  └─ Run with: python predict.py


═════════════════════════════════════════════════════════════════════════════════

📦 SOURCE CODE MODULES (src/)
═════════════════════════════════════════════════════════════════════════════════

src/__init__.py
  └─ Package initialization

src/data_loader.py
  ├─ DataLoader class
  ├─ load_raw_data()
  ├─ get_data_info()
  ├─ get_basic_statistics()
  ├─ check_missing_values()
  └─ save_processed_data()

src/preprocessing.py
  ├─ DataPreprocessor class
  ├─ handle_missing_values()
  ├─ encode_categorical_features()
  ├─ scale_numerical_features()
  ├─ create_feature_interactions()
  ├─ remove_outliers()
  ├─ preprocess()
  └─ prepare_train_test_data()

src/models.py
  ├─ ModelBuilder class
  ├─ build_models()          [Build 9 models]
  ├─ train_model()           [Train single model]
  ├─ train_all_models()      [Train all models]
  ├─ predict()               [Make predictions]
  ├─ evaluate_model()        [Evaluate single model]
  ├─ evaluate_all_models()   [Compare all models]
  ├─ get_best_model()        [Select top model]
  └─ get_feature_importance()

src/utils.py
  ├─ save_model()              [Persist model]
  ├─ load_model()              [Load saved model]
  ├─ save_results()            [Export results]
  ├─ plot_model_comparison()   [Visualize models]
  ├─ plot_predictions_vs_actual()
  ├─ plot_feature_importance()
  ├─ plot_residuals()
  └─ create_summary_report()


═════════════════════════════════════════════════════════════════════════════════

📓 JUPYTER NOTEBOOKS (notebooks/)
═════════════════════════════════════════════════════════════════════════════════

notebooks/NOTEBOOK_TEMPLATE.txt
  └─ Template for creating new notebooks
  └─ Standard notebook outline
  └─ Best practices

Available notebooks (create these):
  1. 01_exploratory_analysis.ipynb
     └─ Data exploration and visualization
     
  2. 02_feature_engineering.ipynb
     └─ Feature creation and selection
     
  3. 03_model_training.ipynb
     └─ Model development and comparison


═════════════════════════════════════════════════════════════════════════════════

📂 DATA DIRECTORIES
═════════════════════════════════════════════════════════════════════════════════

archive/
  └─ AI Job Market Dataset.csv    [Original dataset]

data/raw/
  └─ Raw data location (empty, for reference)

data/processed/
  └─ processed_data.csv           [Output from preprocessing]


═════════════════════════════════════════════════════════════════════════════════

💾 MODEL & RESULTS DIRECTORIES
═════════════════════════════════════════════════════════════════════════════════

models/
  ├─ xgboost.pkl                  [Best trained model]
  ├─ lightgbm.pkl
  ├─ random_forest.pkl
  └─ [other saved models]

results/
  ├─ model_results.csv            [Performance metrics table]
  ├─ model_comparison_r2_score.png
  ├─ model_comparison_rmse.png
  ├─ predictions_vs_actual_xgboost.png
  ├─ feature_importance_xgboost.png
  ├─ residuals_xgboost.png
  └─ summary_report.txt           [Executive summary]

logs/
  └─ pipeline.log                 [Execution log]


═════════════════════════════════════════════════════════════════════════════════

✅ TESTING (tests/)
═════════════════════════════════════════════════════════════════════════════════

tests/__init__.py
tests/test_data_loader.py
  ├─ test_load_raw_data()
  ├─ test_data_shape()
  ├─ test_target_column_exists()
  └─ test_get_data_info()

tests/test_preprocessing.py
  ├─ test_handle_missing_values()
  ├─ test_encode_categorical_features()
  └─ test_preprocess_pipeline()

Run tests:
  pytest tests/
  pytest tests/test_data_loader.py


═════════════════════════════════════════════════════════════════════════════════

🎯 WHERE TO FIND THINGS
═════════════════════════════════════════════════════════════════════════════════

I want to...

... GET STARTED QUICKLY
    ➜ Read: GETTING_STARTED.md
    ➜ Run: python main_pipeline.py

... UNDERSTAND THE PROJECT
    ➜ Read: README.md
    ➜ Then: PROJECT_SUMMARY.md

... CHANGE HYPERPARAMETERS
    ➜ Edit: config/config.py
    ➜ Look for: MODEL_PARAMS dictionary

... MODIFY DATA PREPROCESSING
    ➜ Edit: src/preprocessing.py
    ➜ Modify: preprocess() method

... ADD A NEW MODEL
    ➜ Edit: src/models.py
    ➜ Add to: build_models() method

... MAKE PREDICTIONS
    ➜ Run: python predict.py
    ➜ Or: from predict import SalaryPredictor

... VISUALIZE RESULTS
    ➜ Check: results/ folder
    ➜ Or: View visualizations after running pipeline

... DEBUG AN ERROR
    ➜ Check: logs/pipeline.log
    ➜ Read: DOCUMENTATION.md → Troubleshooting

... RUN TESTS
    ➜ Run: pytest tests/

... EXPLORE DATA
    ➜ Run: jupyter notebook
    ➜ Create notebooks in: notebooks/

... SAVE/LOAD MODELS
    ➜ See: src/utils.py
    ➜ Functions: save_model(), load_model()

... UNDERSTAND METRICS
    ➜ Read: README.md → Evaluation Metrics
    ➜ Or: PROJECT_SUMMARY.md → Expected Performance

... DEPLOY TO PRODUCTION
    ➜ See: DOCUMENTATION.md
    ➜ Create Flask/FastAPI app with predict.py


═════════════════════════════════════════════════════════════════════════════════

🔍 QUICK REFERENCE - FILE STRUCTURES
═════════════════════════════════════════════════════════════════════════════════

Most Important Files:
┌─────────────────────────────────────┐
│ main_pipeline.py          ⭐⭐⭐     │  Run this first
│ predict.py                ⭐⭐      │  Make predictions
│ config/config.py          ⭐⭐      │  Customize settings
│ src/models.py             ⭐        │  Model logic
│ README.md                 ⭐⭐      │  Start here
├─────────────────────────────────────┤
│ GETTING_STARTED.md        ⭐⭐⭐    │  Setup guide
│ PROJECT_SUMMARY.md        ⭐        │  Complete reference
│ PROJECT_STRUCTURE.md      ⭐        │  File organization
│ DOCUMENTATION.md          ⭐        │  Technical details
└─────────────────────────────────────┘


═════════════════════════════════════════════════════════════════════════════════

📊 COMMON WORKFLOWS
═════════════════════════════════════════════════════════════════════════════════

WORKFLOW 1: Initial Setup & Run (30 minutes)
  1. Read: GETTING_STARTED.md
  2. Run: pip install -r requirements.txt
  3. Run: python main_pipeline.py
  4. View: results/
  5. Read: results/summary_report.txt

WORKFLOW 2: Exploration (1+ hours)
  1. Run: jupyter notebook
  2. Create: 01_exploratory_analysis.ipynb
  3. Explore: Data distributions
  4. Analyze: Feature relationships
  5. Find: Patterns and insights

WORKFLOW 3: Customization (Variable time)
  1. Edit: config/config.py
  2. Modify: src/preprocessing.py or src/models.py
  3. Run: python main_pipeline.py
  4. Compare: results with previous run
  5. Iterate: Optimize settings

WORKFLOW 4: Predictions (Minutes)
  1. Run: python predict.py
  2. Or: from predict import SalaryPredictor
  3. Create: predictor = SalaryPredictor()
  4. Predict: new_salary = predictor.predict_single(features)


═════════════════════════════════════════════════════════════════════════════════

🔗 DEPENDENCIES BETWEEN FILES
═════════════════════════════════════════════════════════════════════════════════

archive/Dataset.csv
    ↓
    └─→ data_loader.py
        ↓
        └─→ preprocessing.py
            ↓
            └─→ models.py
                ↓
                ├─→ utils.py (visualization)
                └─→ predict.py (inference)

config.py (used by ALL modules)


═════════════════════════════════════════════════════════════════════════════════

⚙️  CONFIGURATION IN 5 MINUTES
═════════════════════════════════════════════════════════════════════════════════

To customize the project:

1. Open config/config.py

2. Change MODEL_PARAMS:
   MODEL_PARAMS = {
       'xgboost': {
           'n_estimators': 100,      ← Increase for better accuracy
           'learning_rate': 0.1,      ← Decrease for better accuracy
           # ... more parameters
       }
   }

3. Change TRAIN_TEST_SPLIT:
   TRAIN_TEST_SPLIT = 0.8            ← (80% train, 20% test)

4. Change RANDOM_STATE:
   RANDOM_STATE = 42                 ← For reproducibility

5. Save and run:
   python main_pipeline.py


═════════════════════════════════════════════════════════════════════════════════

🎓 LEARNING PATH
═════════════════════════════════════════════════════════════════════════════════

Beginner Level:
  1. Read: GETTING_STARTED.md
  2. Read: README.md
  3. Run: python main_pipeline.py
  4. Explore: results/
  5. Read: PROJECT_SUMMARY.md

Intermediate Level:
  6. Read: PROJECT_STRUCTURE.md
  7. Explore: src/ modules
  8. Run: jupyter notebook
  9. Create: exploratory notebooks
  10. Modify: config.py

Advanced Level:
  11. Read: DOCUMENTATION.md
  12. Modify: src/preprocessing.py
  13. Add: new models in src/models.py
  14. Create: Flask/FastAPI app
  15. Deploy: to production


═════════════════════════════════════════════════════════════════════════════════

✨ TIPS & TRICKS
═════════════════════════════════════════════════════════════════════════════════

💡 Tip 1: Faster Development
   └─ Work with subset of data first
   └─ Use: raw_data.head(100) for testing
   └─ Save time on preprocessing testing

💡 Tip 2: Save Good Results
   └─ Copy entire results/ folder
   └─ Timestamp folder names: results_2024_04_18/
   └─ Keep history of experiments

💡 Tip 3: Use Git
   └─ git add .
   └─ git commit -m "Initial ML model setup"
   └─ Track changes over time

💡 Tip 4: Experiment Systematically
   └─ Change ONE thing at a time
   └─ Document changes
   └─ Compare results

💡 Tip 5: Monitor Progress
   └─ Check logs/pipeline.log frequently
   └─ Review results/ after each run
   └─ Track improvements


═════════════════════════════════════════════════════════════════════════════════

❓ QUICK ANSWERS
═════════════════════════════════════════════════════════════════════════════════

Q: What should I run first?
A: python main_pipeline.py

Q: Where are the results?
A: In the results/ folder

Q: How do I change settings?
A: Edit config/config.py

Q: How do I make predictions?
A: Run python predict.py

Q: Where's the documentation?
A: Start with README.md

Q: How do I explore data?
A: Use jupyter notebook in notebooks/

Q: Can I run tests?
A: Yes - pytest tests/

Q: How do I load a saved model?
A: from src.utils import load_model

Q: What's the best model?
A: Check results/summary_report.txt

Q: How do I improve performance?
A: Modify config/config.py or src/preprocessing.py


═════════════════════════════════════════════════════════════════════════════════

🎯 SUCCESS METRIC
═════════════════════════════════════════════════════════════════════════════════

You've successfully set up the project when:
  ✓ python main_pipeline.py runs without errors
  ✓ results/ folder contains visualizations
  ✓ models/ folder contains trained models
  ✓ You can understand the output metrics
  ✓ You can make predictions with predict.py


═════════════════════════════════════════════════════════════════════════════════

🚀 NEXT ACTION ITEMS
═════════════════════════════════════════════════════════════════════════════════

1. NOW:
   → Read this index file (you're reading it!)
   
2. NEXT (5 minutes):
   → Read GETTING_STARTED.md
   
3. THEN (30 minutes):
   → Run: python main_pipeline.py
   
4. AFTER (30 minutes):
   → Review results
   → Explore visualizations
   → Read summary report

5. CONTINUE (1+ hours):
   → Explore data with Jupyter
   → Experiment with parameters
   → Make predictions
   → Plan customizations


═════════════════════════════════════════════════════════════════════════════════

📞 HELP & SUPPORT
═════════════════════════════════════════════════════════════════════════════════

For Setup Help:
  → GETTING_STARTED.md → Troubleshooting section

For How-To Guides:
  → README.md

For Technical Issues:
  → DOCUMENTATION.md → Troubleshooting

For Understanding Results:
  → PROJECT_SUMMARY.md → Expected Performance

For Configuration:
  → config/config.py (read the comments)

For Code Examples:
  → DOCUMENTATION.md → Custom Usage Example


═════════════════════════════════════════════════════════════════════════════════

                    🎉 YOU'RE ALL SET!

             Your production-ready ML project is complete.

                 Read your first guide and get started!

═════════════════════════════════════════════════════════════════════════════════

                         📖 FIRST DOCUMENT TO READ:
                            GETTING_STARTED.md

═════════════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(INDEX)
