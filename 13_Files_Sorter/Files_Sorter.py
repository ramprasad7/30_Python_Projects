import os
import shutil
import tkinter as tk
from tkinter import filedialog


def create_folder(path: str, extension: str) -> str:
    #creates a folder based on the extension passed
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path,folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

def sort_files(source_path: str):
    #Sorts the files and moves to the corresponding folders
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir,filename)
            extension: str = os.path.splitext(filename)[1]


            if extension:
                target_folder: str = create_folder(source_path,extension)
                target_path: str = os.path.join(target_folder,filename)

                shutil.move(file_path,target_path)

def resort_files(source_path: str) -> None:
    for root_dir, sub_dirs, filenames in os.walk(source_path):
        for sub_dir in sub_dirs:
            sub_dir_path: str = os.path.join(root_dir,sub_dir)
            #print(sub_dir_path)
            for filename in os.listdir(sub_dir_path):
                file_path: str = os.path.join(sub_dir_path,filename)
                target_path: str = os.path.join(source_path,filename)
                shutil.move(file_path,target_path)


def remove_empty_folder(source_path: str):
    #Removes all empty folders
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir,current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main() -> None:
    root = tk.Tk()
    root.withdraw()
    # file_path = filedialog.askopenfilename()
    user_input: str = filedialog.askdirectory()
    #user_input: str = input("Please provide a file path for Sorting: ")
    #print(user_input)
    if os.path.exists(user_input):
        sort_files(user_input)
        resort_files(user_input)
        remove_empty_folder(user_input)
        print("Files are Sorted! Successfully")
    else:
        print("Invalid File Path!, Please provide a valid file path.")

if __name__ == "__main__":
    main()