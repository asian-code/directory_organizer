from pathlib import Path
from tkinter import filedialog
from tkinter import *

r = '\033[0m'  # reset
red = '\033[31m'
green = '\033[32m'

# The keys = file extensions you want to move into the specified folder.
# The values = the folder you want the files with the extension to go in to.
actions = {
    ".png": "Images",
    ".jpg": "Images",
    ".gif": "Images",
    ".ico": "Images",
    ".jpeg":"Images",
    ".psd":"Images",
    ".kra":"Images",

    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv":"Videos",

    ".rar": "Zip",
    ".zip": "Zip",
    ".001": "Zip",
    ".7z": "Zip",

    ".docx":"Documents",
    ".txt":"Documents",
    ".pdf":"Documents",
    ".doc":"Documents",
    ".xls":"Documents",
    ".ppt":"Documents",

    ".wav": "Audio",
    ".mp3": "Audio",
    ".ogg": "Audio",
    ".flac": "Audio",
    ".ape": "Audio",

    ".exe":"Programs",
    ".dmg":"Programs",
    ".deb":"Programs",
    ".apk":"Programs",

    ".blender":"3D",
    ".obj":"3D",
    ".fbx":"3D",

   ".py": "Scripts",
   ".java": "Scripts",
   ".sh": "Scripts",
   ".bat": "Scripts",
   ".pl": "Scripts",
   ".php": "Scripts",
   ".cpp": "Scripts",
   ".c": "Scripts",
   ".kt": "Scripts"}

def organize_folder(dir):
    # dir.glob("*,*") is used to get all the files (and folders) and store the value in a list
    for file in dir.glob("*.*"):
        if file.is_file():
            # If the file has an extension that's in the actions and destination, move the file.
            try:
                # Creates folder for file type if doesnt exist
                exten=file.suffix
                if exten in actions.keys():
                    if dir.joinpath(actions[exten]) not in dir.iterdir():
                        dir.joinpath(actions[exten]).mkdir()
                        print("[+] Created Folder: "+actions[exten])
                    dest_path = dir.joinpath(actions[exten], file.name)
                else:
                    folder="Other"
                    if dir.joinpath(folder) not in dir.iterdir():
                        dir.joinpath(folder).mkdir()
                        print("[+] Created Folder: "+folder)
                    dest_path = dir.joinpath(folder, file.name)
                    
                
                #print(dest_path)
                file.rename(dest_path)
            
            # If the file doesn't have an extension or a filetype not in Actions ,move it into the "other" folder. 
            except:
                print(red+"[!] Problem trying to move files"+r)
                raise

def main():
    try:
        # Select the folder you want organized with a system Popup
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        directory=Path(folder_selected) # the folder you want organized
        print(green+"[+] Selected folder: "+r+str(directory))
    except:
        print(red+"[!] You didnt pick a folder/location"+r)
        raise
        return
    
    organize_folder(directory)
    print(green+"[+] Successfully Organized: "+r+str(directory))

main()
