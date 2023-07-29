import os
from add_file_to_directory import add_file_to_directory
from get_file_type import get_file_type

if __name__ == "__main__":
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if os.path.exists(file_path):
        file_type,file_extension = get_file_type(file_path)
        print(f"The file type is: {file_type}")
        add_file_to_directory(file_path, 'C:\\Users\\Rishabh\\Desktop\\projects\\file\\'+file_type,file_extension)
    else:
        print("File not found...Please enter valid file path.")
