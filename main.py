import os
from shutil import move

##########################################################################
# CURRENT WORKING DIRECTORY: This changes the directory of this program
##########################################################################
os.chdir('C:/Users/user/Desktop')
##########################################################################
# EXTENSIONS: This is where the extensions will be
##########################################################################
extensions = {
    "Media": ("png", "jpg", "jpeg", "mp4", "mpeg", "mkv"),
    "Documents": ("doc", "docx", "pdf"),
    "Illustrator": "ai",
    "Text": "txt",
    "Photoshop": "psd",
}
##########################################################################
# ALGORITHM: This is where the magic takes place
##########################################################################
def move_files(file, folder):
    folder_dir = os.getcwd() + "/" + folder
    if not os.path.exists(folder):
        os.makedirs(folder_dir)
    move(file, folder_dir)
    return print(f"Moving file:  {file[:13]}...  to\t\t\t\t\t{folder}")


def desktop_organizer():
    files_moved = 0
    for files in os.listdir(os.getcwd()):
        for key, value in extensions.items():
            if files.endswith(value):
                move_files(files, key)
                files_moved += 1
    print("\n")
    print(f"Moved a total of {files_moved} files.\n Thank You!\n//////////////////////////////////////////////////////")


if __name__ == "__main__":
    desktop_organizer()
