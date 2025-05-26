# Directory File Processor

## Overview
This Python script reads files from a specified directory and all its subdirectories, concatenates their contents, and writes them into a single output file. It is useful for consolidating files for analysis, review, or processing.

## Features
- Reads files with any extension (customizable in the script).
- Skips directories and subdirectories matching specified patterns or full paths.
- Excludes files based on specific filenames or patterns.
- Handles Unicode errors gracefully, skipping unreadable files and logging errors.

## Requirements
- Python 3.6 or higher
- A text editor or IDE for modifying script configurations.

## How to Use
1. **Edit the Configuration**:
   - Set the `directory_path` to the directory you want to process.
   - Set the `output_file` to the path of the file where the results will be written.
   - Customize the `exclude_patterns`, `exclude_directories`, and `exclude_files` to exclude specific items.
   
2. **Run the Script**:
   Execute the script in a terminal or IDE:



Used to read files with extensions;
".txt", ".ts", ".css", ".json", ".html", ".cs" from directory and all subdirectories.
The whole contents are saved to a text file which can then be uploaded to ChatGPT, (or whatever) and do whatever you instruct, analyse, review, suggest, etc.
