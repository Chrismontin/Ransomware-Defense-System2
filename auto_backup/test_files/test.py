import os
from pathlib import Path

# Get the current directory
current_dir = Path.cwd()

# List all text files in the current directory
text_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]

# Display the text files
for file in text_files:
    print(file)

# Optional: Get more detailed information
print(f"\nTotal text files found: {len(text_files)}")