import os

root_dir = os.getcwd()

for root, dirs, files in os.walk(root_dir):
    if '.git' in dirs:
        dirs.remove('.git')
    for file in files:
        if file.endswith(".txt"):
            new_file_name = file.replace(".txt", ".py")
            new_file_path = os.path.join(root, new_file_name)
            if not os.path.exists(new_file_path):  # Check if the new file already exists
                os.rename(os.path.join(root, file), new_file_path)
            else:
                print(f"Skipping renaming {file} to {new_file_name} - file already exists.")