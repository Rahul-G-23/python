import os
import re

def search_text_files(folder_path, regex_pattern):
    try:
        pattern = re.compile(regex_pattern)
    except re.error as e:
        print(f"Invalid regular expression: {e}")
        return

    print("\n--- Matching Lines ---\n")
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, 1):
                        if pattern.search(line):
                            print(f"{filename} [Line {line_number}]: {line.strip()}")
            except Exception as e:
                print(f"Could not read file {filename}: {e}")
if __name__ == "__main__":
    print("Name: Rahul G \n USN:1AY24AI088\n Section: 'O'")
    folder = input("Enter the path to the folder: ").strip().strip('""')
    regex = input("Enter a regular expression to search for: ").strip()
    search_text_files(folder, regex)
