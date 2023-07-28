import os

def directory_exists(file_path):
    return os.path.exists(file_path) and os.path.isdir(file_path)

def create_directory(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Directory '{folder_path}' created successfully.")
    except Exception as e:
        print(f"Error while creating directory: {str(e)}")

def get_file_name(file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    return file_name

def get_files_from_path(file_path):
    #check if it is a file or folder path
    if not os.path.isdir(file_path):
        return [os.path.abspath(file_path)]
    else:
        # get a list of all files in the folder
        contents = os.listdir(file_path)
        files = [os.path.abspath(file) for file in contents if not os.path.isdir(file)]
        return files

def generate_ocr_text(file_path,output_path = "./out"):
    print("Checking if directory exists...")
    if not directory_exists(output_path):
        print("Directory doesn't exist...")
        create_directory(output_path)
    else:
        print("Directory exists!")
    
    print("Grabbing all files from the file path...")
    files = get_files_from_path(file_path)

    //TODO: fix this portion of code

    # print("Iterating thru each file...")
    # for file in files:
    #     print("Working on " + file + "...")
    #     output_txt_filename = output_path + "/" + get_file_name(file)
    #     shell_command = "tesseract " + file + " " + output_txt_filename + " -l tam"
    #     os.system(shell_command)
    #     print("Completed working on file: " + file)
    # print("Task completed")

# print("Test (1)")
# print(get_file_name("./tamil-text/example1.jpeg"))
# print(get_file_name("./tamil-text/tamil.png"))
# print(get_file_name("./tamil-text"))
# print()

# print("Test (2)")
# print(get_files_from_path("./tamil-text"))
# print(get_files_from_path("./tesseract-ocr-testing.py"))
# print(get_files_from_path("."))

generate_ocr_text("./tamil-text")