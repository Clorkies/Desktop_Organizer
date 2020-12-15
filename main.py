import os
import re
import shutil

##########################################################################
# CURRENT WORKING DIRECTORY: This changes the directory of this program
##########################################################################

os.chdir('C:/Users/user/Desktop')

##########################################################################
# EXTENSIONS: This is where the extensions will be
##########################################################################

media = "(.\.png|.\.jpg|.\.jpeg|.\.mp4|.\.mpk)"
docs = "(.\.docx|.\.pdf|.\.doc)"
illust = "(.\.ai)"
txt = "(.\.txt)"

##########################################################################


def move_files(file, folder):
    folder_dir = os.getcwd() + "/" + folder
    if not os.path.exists(folder):
        os.makedirs(folder_dir)

    shutil.move(file, folder_dir)

    return print(f"Moving file:  {file[:15]}...  to\t\t\t\t\t{folder}")


def desktop_organizer():
    files_moved = 0
    for directories in os.listdir(os.getcwd()):
        if re.search(media, directories):
            move_files(directories, "Media")
        elif re.search(docs, directories):
            move_files(directories, "Documents")
        elif re.search(illust, directories):
            move_files(directories, "Illustrator Files")
        elif re.search(txt, directories):
            move_files(directories, "Text Documents")
        else:
            move_files(directories, "Others")

        files_moved += 1
    print(f"Moved a total of {files_moved} files.\n Thank You!\n//////////////////////////////////////////////////////")


desktop_organizer()
