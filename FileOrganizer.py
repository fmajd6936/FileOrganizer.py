# file_organizer.py

import os
import shutil

def organize_files(folder_path):
    extensions = {}
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            extension = file_name.split(".")[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)

    for extension, files in extensions.items():
        directory = os.path.join(folder_path, extension.upper() + " Files")
        os.makedirs(directory, exist_ok=True)
        for file_name in files:
            source = os.path.join(folder_path, file_name)
            destination = os.path.join(directory, file_name)
            shutil.move(source, destination)
