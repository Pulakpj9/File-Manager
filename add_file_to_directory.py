import os
import shutil
import uuid
from datetime import datetime

def add_file_to_directory(source_file, destination_directory,file_extension):

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Get the file name from the source path
    file_name = os.path.basename(source_file)
    print(file_name)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Generate a UUID
    unique_id = str(uuid.uuid4().hex)

    # Combine timestamp, UUID, and file extension to create a unique filename
    unique_filename = f"{timestamp}_{unique_id}{file_extension}"

    # Combine the destination directory path and file name
    destination_path = os.path.join(destination_directory, unique_filename)

    # Copy the file to the destination directory
    shutil.copy(source_file, destination_path)

    print(f"File '{file_name}' added to '{destination_directory}'.")

    with open("logs.txt", "a") as file:
        file.write(f"File '{file_name}' added to '{destination_directory}' at {datetime.now()}.")
        file.write(f"\n")