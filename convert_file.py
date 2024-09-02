import os

def convert_to_utf8(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                with open(file_path, 'r', encoding='utf-16') as f:
                    content = f.read()
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Converted {file_path} to UTF-8.")
            except UnicodeError:
                print(f"Skipped {file_path} (not UTF-16).")

if __name__ == "__main__":
    root_dir = '.'  # Change this to the root directory of your project if necessary
    convert_to_utf8(root_dir)
