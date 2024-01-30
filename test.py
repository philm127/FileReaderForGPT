import os

def process_directory(directory_path, output_file):
  print(f"Processing files in '{directory_path}' and writing contents to '{output_file}'...")
  with open(output_file, "w") as out:
    for root, _, files in os.walk(directory_path):
      for filename in files:
        filepath = os.path.join(root, filename)
        if filename.endswith(".spec.ts"):
          continue
        extension = os.path.splitext(filename)[1]
        if extension in (".txt", ".ts", ".css", ".json", ".html", ".cs"):
          with open(filepath, "r") as f:
            content = f.read()
          out.write(f"""
/* XXXXXXXXXXXXXXXXXXXXXXXXXX
           {filename}
XXXXXXXXXXXXXXXXXXXXXXXXXXX*/
{content}
""")

# Usage
directory_path = "C:/Development/Adtones/AdtonesAdmin/src/app/features/campaign-create-edit"  # Replace with your actual directory path
output_file = "C:\Development\Adtones\AdtonesAdmin\combined_campaign-create-edit.txt"
process_directory(directory_path, output_file)

print(f"Successfully processed files and wrote contents to '{output_file}'.")