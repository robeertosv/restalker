#!/usr/bin/env python3
"""
Script to prepare the environment for restalking with spaCy.
This script installs the necessary spaCy models.
"""

import sys
import subprocess
import spacy

def install_spacy_models():
    print("Installing spaCy models...")
    
    # Trying to install Spanish model first
    try:
        subprocess.check_call([
            sys.executable, "-m", "spacy", "download", "es_core_news_md"
        ])
        print("Spanish model installed successfully.")
    except subprocess.CalledProcessError:
        print("Couldn't install Spanish model. Installing English models...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_md"
            ])
            print("English medium model installed successfully.")
        except subprocess.CalledProcessError:
            print("Couldn't install English medium model. Installing small English model...")
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            print("English small model installed successfully.")

def check_spacy_models():
    """Check which spaCy models are available"""
    print("Checking available spaCy models...")
    
    models_to_check = ["es_core_news_md", "en_core_web_md", "en_core_web_sm"]
    available_models = []
    
    for model_name in models_to_check:
        try:
            spacy.load(model_name)
            available_models.append(model_name)
            print(f"✓ Model '{model_name}' is installed and available.")
        except OSError:
            print(f"✗ Model '{model_name}' not installed.")
    
    return available_models

if __name__ == "__main__":
    print("=== Preparing the environment for restalker with spaCy ===")
    
    # Check available models
    available_models = check_spacy_models()
    
    # If no models are installed, install them.
    if not available_models:
        print("No spaCy models were found installed.")
        install_spacy_models()
        check_spacy_models()
    else:
        print("At least one spaCy model is already installed. No need to install any more models.")
    
    print("\n=== Preparation complete ===")
    print("You can now run the tests with:")
    print("  python test.py [test_file]")
    print("  python test_textan.py")