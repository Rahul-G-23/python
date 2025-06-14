import os
import shutil

def copy_files_by_extension(source_dir, destination_dir, extension):
    if not extension.startswith("."):
        extension = "." + extension

    try:
        os.makedirs(destination_dir, exist_ok=True)
    except PermissionError:
        print(f"Permission denied: Cannot create or write to {destination_dir}")
        return

    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                source_file = os.path.join(foldername, filename)
                destination_file = os.path.join(destination_dir, filename)

                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination_file):
                    destination_file = os.path.join(destination_dir, f"{base}_{counter}{ext}")
                    counter += 1

                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} → {destination_file}")

print("Name: Rahul G \n USN:1AY24AI088\n Section: 'O'")
source_folder = input("Enter source folder path: ").strip()
destination_folder = input("Enter destination folder path: ").strip()
file_extension = input("Enter file extension to search (e.g., pdf or jpg): ").strip()

copy_files_by_extension(source_folder, destination_folder, file_extension)
