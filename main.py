import os

def process_directory(directory_path, output_file, exclude_patterns, exclude_directories, exclude_files, exclude_extensions):
    """
    Recursively processes files in a directory, writing their contents to a single output file.
    Provides options to exclude directories, files, patterns, and extensions.

    Args:
        directory_path (str): The root directory to scan.
        output_file (str): The path to the output file where content will be written.
        exclude_patterns (list): List of patterns to exclude (e.g., "Test").
        exclude_directories (list): List of directory paths to exclude, relative to `directory_path`.
        exclude_files (list): List of specific filenames to exclude.
        exclude_extensions (list): List of file extensions to exclude (e.g., [".idx", ".po"]).
    """
    print(f"Processing files in '{directory_path}' and writing contents to '{output_file}'...")

    # Normalize paths for consistency
    directory_path = os.path.normpath(directory_path)
    exclude_directories = [os.path.normpath(os.path.join(directory_path, dir_path)) for dir_path in exclude_directories]
    exclude_files = [os.path.normpath(file) for file in exclude_files]

    with open(output_file, "w", encoding='utf-8') as out:
        for root, _, files in os.walk(directory_path):
            root_normalized = os.path.normpath(root)

            # Skip directories matching exclusion criteria
            if any(exclude_pattern in root_normalized for exclude_pattern in exclude_patterns) or \
               any(root_normalized.startswith(ex_dir) for ex_dir in exclude_directories):
                print(f"Skipping directory and its subdirectories: {root}")
                continue

            for filename in files:
                filepath = os.path.normpath(os.path.join(root, filename))
                extension = os.path.splitext(filename)[1]

                # Skip files by name or extension
                if filename in exclude_files or extension in exclude_extensions:
                    print(f"Skipping file due to exclusion list: {filepath}")
                    continue

                try:
                    with open(filepath, "r", encoding='utf-8') as f:
                        content = f.read()
                    out.write(f"""
/* XXXXXXXXXXXXXXXXXXXXXXXXXX
    {filepath}
XXXXXXXXXXXXXXXXXXXXXXXXXXX */
{content}
""")
                except UnicodeDecodeError:
                    print(f"Skipping file due to encoding error: {filepath}")
                except Exception as e:
                    print(f"An error occurred while processing the file {filepath}: {e}")

# Usage
directory_path =  r"D:\InvestmentServices\Tennis"      #r"C:\Development\Proactiviti\gta-truckroll-back"
output_file = r"C:\Development\Proactiviti\combined_tennis_latest.txt"
exclude_patterns = ["bin", "release","obj"]  # Patterns to exclude (e.g., directories containing "Test")
exclude_directories = [  # Relative to `directory_path`
    ".git",
    ".vs",
    ".vscode",
    ".github",
    "__pycache__",
    "app/__pycache__",
    "alembic/versions",
    ".husky",
    "node_modules",
    "WrapperClassRunner",
    "AdtranApiWrapper",
    "AdtranApiWrapper.Test",
    "CienaApiWrapper",
    "CienaApiWrapper.Test",
    "EventBus-WebSocket",
    "EventBus-WebSocket.Tests",
    "notebooks",
    ".venv",
    "data_files"
]
exclude_files = [
    ".gitignore",
    ".dockerignore"
]
exclude_extensions = [".idx", ".po"]  # Extensions to exclude

process_directory(directory_path, output_file, exclude_patterns, exclude_directories, exclude_files, exclude_extensions)

print(f"Successfully processed files and wrote contents to '{output_file}'.")
