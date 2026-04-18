"""
Quick Start Setup Script
Initializes the project environment
"""
import os
import sys
from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).parent


def print_header(text):
    """Print section header"""
    print("\n" + "="*60)
    print(f" {text}")
    print("="*60)


def main():
    """Initialize project"""
    
    print_header("AI Job Salary Prediction - Quick Start Setup")
    
    # Check Python version
    print("\n[1/5] Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Check dependencies
    print("\n[2/5] Checking if dependencies need installation...")
    try:
        import pandas
        print("✓ Dependencies already installed")
    except ImportError:
        print("Installing dependencies from requirements.txt...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(PROJECT_ROOT / "requirements.txt")]
        )
        print("✓ Dependencies installed")
    
    # Verify project structure
    print("\n[3/5] Verifying project structure...")
    required_dirs = [
        'data/raw', 'data/processed', 'notebooks', 'src',
        'models', 'results', 'logs', 'tests', 'config', 'archive'
    ]
    
    missing_dirs = []
    for dir_name in required_dirs:
        dir_path = PROJECT_ROOT / dir_name
        if dir_path.exists():
            print(f"✓ {dir_name}/ exists")
        else:
            missing_dirs.append(dir_name)
            print(f"⚠ {dir_name}/ missing (will be created)")
    
    # Create missing directories
    for dir_name in missing_dirs:
        (PROJECT_ROOT / dir_name).mkdir(parents=True, exist_ok=True)
    
    # Verify dataset
    print("\n[4/5] Verifying dataset...")
    dataset_path = PROJECT_ROOT / "archive" / "AI Job Market Dataset.csv"
    if dataset_path.exists():
        import pandas as pd
        df = pd.read_csv(dataset_path)
        print(f"✓ Dataset found: {len(df)} rows, {len(df.columns)} columns")
    else:
        print("⚠ Dataset not found in archive/")
    
    # Display next steps
    print("\n[5/5] Setup Complete!")
    
    print_header("Next Steps")
    
    print("""
1. Run the complete ML pipeline:
   python main_pipeline.py

2. Load Jupyter notebooks for exploration:
   jupyter notebook notebooks/

3. Make predictions:
   python predict.py

4. View results:
   - Check results/ folder for visualizations
   - Review logs/pipeline.log for details
   - Examine models/ for saved models

5. Custom analysis:
   - Edit config/config.py for hyperparameters
   - Modify main_pipeline.py for custom workflows
   - Add features in src/preprocessing.py
""")
    
    print_header("Documentation")
    print("""
📖 README.md - Project overview and usage guide
📖 DOCUMENTATION.md - Detailed technical documentation
📖 config/config.py - Configuration parameters
""")
    
    print("\n✅ Setup Complete! Ready to build your ML model.\n")


if __name__ == "__main__":
    main()
