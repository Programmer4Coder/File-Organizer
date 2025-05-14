import os
import shutil
from datetime import datetime

# Define file type categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.php']
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files_by_type_and_date(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            # Get file extension and category
            _, extension = os.path.splitext(file)
            category = get_category(extension)

            # Get last modified date
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m')

            # Create category and date folders
            target_folder = os.path.join(directory, category, date_folder)
            os.makedirs(target_folder, exist_ok=True)

            # Move the file
            try:
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {category}/{date_folder}/")
            except Exception as e:
                print(f"Error moving file {file}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_files_by_type_and_date(folder_path)
