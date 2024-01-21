import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder_path, destination_folder):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                extension = file.split('.')[-1].lower()
                extension_folder = os.path.join(destination_folder, extension)
                
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                destination_path = os.path.join(extension_folder, file)
                shutil.move(file_path, destination_path)
    except Exception as e:
        print(f"Error processing folder {folder_path}: {e}")

def main():
    source_folder = "Хлам"
    destination_folder = "Сортовано"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    with ThreadPoolExecutor(max_workers=5) as executor:
        folders = [f.path for f in os.scandir(source_folder) if f.is_dir()]
        for folder in folders:
            executor.submit(process_folder, folder, destination_folder)

if __name__ == "__main__":
    main()