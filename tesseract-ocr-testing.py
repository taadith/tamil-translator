import os

def get_file_name(file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    return file_name

def get_files_from_path(file_path):
    #check if it is a file or folder path
    if not os.path.isdir(file_path):
        return [file_path]
    else:
        # get a list of all files in the folder
        contents = os.listdir(file_path)
        files = [file for file in contents if not os.path.isdir(file)]
        return files

def generate_ocr_text(file_path,output_path = "./out"):
    pass

print("Test (1)")
print(get_file_name("./tamil-text/example1.jpeg"))
print(get_file_name("./tamil-text/tamil.png"))
print(get_file_name("./tamil-text"))
print()

print("Test (2)")
print(get_files_from_path("./tamil-text"))
print(get_files_from_path("./tesseract-ocr-testing.py"))
print(get_files_from_path("."))