

import os

def delete_file(file_name):
    """
    This function deletes a specified file.

    Parameters:
        file_name (str): The name of the file to delete.
    """
    if os.path.isfile(file_name):
        os.remove(file_name)
        print(f"Deleted file: {file_name}")
    else:
        print(f"File not found: {file_name}")

def case_sensitive_delete(file_name):
    """
    This function handles case sensitivity while deleting a file.

    Parameters:
        file_name (str): The name of the file to delete.
    """
    if os.path.isfile(file_name):
        os.remove(file_name)
        print(f"Deleted file: {file_name}")
    else:
        files = os.listdir()
        case_insensitive_files = [file for file in files if file.lower() == file_name.lower()]
        if case_insensitive_files:
            for file in case_insensitive_files:
                os.remove(file)
                print(f"Deleted file: {file}")
        else:
            print(f"File not found: {file_name}")

# Replace 'Test.txt' with the name of the file you want to delete
case_sensitive_delete("Test.txt") 