# NLTK Data Cleaner

A command-line utility for cleaning text data using NLTK. This tool performs various text preprocessing steps to normalize and clean text data.

## Features

- Text Normalization:
  - Converting text to lowercase (e.g., "TEXT" → "text")
  - Removing punctuation (e.g., "hello!" → "hello")
  - Removing stopwords (common words like "the", "is", "at", "which", etc.)
  - Word lemmatization (e.g., "running" → "run", "better" → "good")

- File Handling:
  - Process single text files
  - Batch process entire directories of text files
  - Automatic creation of output directories
  - Maintains original filenames when processing directories

- Progress Tracking:
  - Progress bar for directory processing
  - Success/failure reporting
  - Error logging with detailed messages

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The tool supports two modes of operation:

### 1. Single File Processing
```bash
python main.py input.txt output.txt
```
Example:
Input: "The quick brown FOX jumps over the lazy dog!"
Output: "quick brown fox jump lazy dog"

### 2. Directory Processing
```bash
python main.py input_directory/ output_directory/
```
This will:
- Process all .txt files in the input directory
- Create the output directory if it doesn't exist
- Maintain original filenames
- Show a progress bar during processing
- Display a summary of processed files

## Example

Given an input file with this content:
```
The quick brown fox jumps over the lazy dog! 
This is a sample text file that contains various punctuation marks.
```

The cleaned output will be:
```
quick brown fox jump lazy dog
sample text file contains various punctuation mark
```

Note how the tool has:
- Removed stopwords ("the", "is", "a")
- Converted to lowercase
- Removed punctuation
- Lemmatized words ("jumps" → "jump", "marks" → "mark")

## Error Handling

- The tool will log errors to the console
- When processing a directory, it will continue processing other files if one fails
- A summary of successful and failed operations will be displayed at the end
