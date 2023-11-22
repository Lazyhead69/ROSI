import os

def list_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    print(f"Files in '{directory}':")
    for file_name in files:
        print(file_name)
    print("\n")

def replace_spaces_with_underscores(directory):
    # List files before renaming
    print("Before renaming:")
    list_files(directory)

    # Iterate through each file in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            # Replace spaces with underscores in the file name
            new_name = file_name.replace(".txt", ".md")

            # Construct the old and new paths
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{file_name}' to '{new_name}'")

    # List files after renaming
    print("\nAfter renaming:")
    list_files(directory)

# Replace spaces with underscores in files in the specified directory
directory_path = r"C:\Users\Administrateur\Documents\GitHub\ROSI\Python\27000_Toolkit"
replace_spaces_with_underscores(directory_path)
