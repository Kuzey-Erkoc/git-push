import os 
 
def new_directory(folder_path, file_name):
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as f:
        f.write("# New file created")


new_directory("new", "new.py")