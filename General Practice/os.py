import os

# File and Directory Operations
print("Current Working Directory:", os.getcwd())
print("List of Files in Current Directory:", os.listdir(os.getcwd()), sep="\n")

new_path = os.path.join(os.getcwd(), "new_directory1")
os.mkdir(new_path)
print("Is the new directory created?", os.path.exists(new_path))

os.system("ls -l")
