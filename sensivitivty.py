

import os

def delete_file(file_name):
    # Retrieve all file names in the directory
    directory_files = os.listdir()

    # Iterate through each file name
    for directory_file in directory_files:
        # Check if the current file name matches the target file name (case-sensitive)
        if directory_file == file_name:
            # Delete the file from the directory
            os.remove(directory_file)
            print(f"File '{directory_file}' deleted successfully.")
            break
    else:
        print(f"File '{file_name}' not found.")

# Test the function with different cases
delete_file("Test.txt") # should delete if found
delete_file("test.txt") # should not delete anything if found