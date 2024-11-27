import os

# Specify the folder containing the files
folder_path = "D:\Data Billion"

# List all files in the folder
files = os.listdir(folder_path)

for file_name in files:
    # Split the file name to get the number part
    parts = file_name.split('_')
    
    # Check if the file name contains at least one underscore and has the .mp3 extension
    if len(parts) > 1 and file_name.endswith('.mp3'):
        # Construct the new file name
        new_file_name = parts[0] + '.mp3'
        
        # Create full paths
        old_file = os.path.join(folder_path, file_name)
        new_file = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {file_name} to {new_file_name}")
