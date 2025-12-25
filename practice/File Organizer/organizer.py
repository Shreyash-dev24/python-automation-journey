import os
import shutil


# C:\Users\Shreyash\Desktop\N_Organize\  

def scan_dir(up):
    categories = {
        "Documents": ['.pdf', '.txt', '.docx', '.xlsx'],
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.heic', '.jfif'],
        "Videos": ['.mp4'],
        "Audio": ['.mp3'],
        "Code": ['.c', '.cpp', '.js', '.py', '.java'],
        "Archives": ['.zip', '.tar']
    }

    # safety check
    if not os.path.isdir(up):
        print("Invalid directory path")
    

    for item in os.listdir(up):
        source_path = os.path.join(up, item)

        # ignore folders
        if not os.path.isfile(source_path):
            continue

        name, ext = os.path.splitext(item)
        ext = ext.lower()

        category = "Others"
        for folder, ext_list in categories.items():
            if ext in ext_list:
                category = folder
                break

        dest_folder = os.path.join(up, category)
        os.makedirs(dest_folder, exist_ok=True)

        shutil.move(source_path, os.path.join(dest_folder, item))

    print("Files organized successfully.")

organize = True

while organize:
   
    print("")
    user_path = input("Enter Path to Organize : ")
    if os.path.exists(user_path):
        print('Valid path!')
        organize = False
        scan_dir(user_path)
    else:
        print("Invalid path!")
        print("Try Again !!!")
        organize = True


