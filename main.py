#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tqdm import tqdm
import string
import logging

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class TextCleaner:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def clean_text(self, text):
        """Clean the input text by performing various preprocessing steps."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        
        # Tokenize (using nltk's word_tokenize directly)
        tokens = text.split()
        
        # Remove stopwords and lemmatize
        cleaned_tokens = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token not in self.stop_words and token.strip()
        ]
        
        return " ".join(cleaned_tokens)

def process_file(input_path, output_path, cleaner):
    """Process a single file and save the cleaned text."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        cleaned_text = cleaner.clean_text(text)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
            
        return True
    except Exception as e:
        logging.error(f"Error processing file {input_path}: {e}")
        return False

def process_directory(input_dir, output_dir, cleaner):
    """Process all text files in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get all text files
    text_files = list(input_path.glob("*.txt"))
    
    if not text_files:
        print("No text files found in the input directory.")
        return
    
    successful = 0
    failed = 0
    
    for file in tqdm(text_files, desc="Processing files"):
        output_file = output_path / file.name
        if process_file(file, output_file, cleaner):
            successful += 1
        else:
            failed += 1
    
    print(f"\nProcessing complete:")
    print(f"Successfully processed: {successful} files")
    print(f"Failed to process: {failed} files")

def main():
    parser = argparse.ArgumentParser(description="Text cleaning utility")
    parser.add_argument(
        "input",
        help="Input file or directory path"
    )
    parser.add_argument(
        "output",
        help="Output file or directory path"
    )
    
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    cleaner = TextCleaner()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input path '{input_path}' does not exist.")
        sys.exit(1)
    
    if input_path.is_file():
        if process_file(input_path, output_path, cleaner):
            print(f"Successfully cleaned text and saved to {output_path}")
        else:
            print("Failed to process file")
            sys.exit(1)
    else:
        process_directory(input_path, output_path, cleaner)

if __name__ == "__main__":
    main()
