import os

def get_file_type(file_path):

    # Get the file extension
    file_extension = os.path.splitext(file_path)[1].lower()

    # Define a dictionary to map common file extensions to their types
    file_types = {
        '.txt': 'Text File',
        '.csv': 'CSV File',
        '.json': 'JSON File',
        '.xml': 'XML File',
        '.jpg': 'JPEG Image',
        '.png': 'PNG Image',
        '.mp3': 'MP3 Audio',
        '.mp4': 'MP4 Video',
        '.pdf': 'PDF Document',
        '.docx': 'Word Document'
        # Add more file extensions and types as needed
    }

    # Check if the file extension exists in the dictionary
    file_type = file_types.get(file_extension, 'Unknown Type')
    return [file_type,file_extension]