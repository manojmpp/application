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
            return True
    else:
        print(f"File '{file_name}' not found.")
        return False

# Test the function with different cases
delete_file("Test.txt") # should delete if found and return True
print(delete_file("test.txt")) # should not delete anything if found and return False