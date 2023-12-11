import os
import shutil

desktop_path = "C:\\Users\\kalmira\\Desktop"
desktop_contents = os.listdir(desktop_path)

for item in desktop_contents:

    item_path = os.path.join(desktop_path, item)

    if os.path.isfile(item_path):
        root, extension = os.path.splitext(item)
        source_path = os.path.join(desktop_path, item)

        if extension == '.txt':
            destination_path = os.path.join(desktop_path, ".txt")
        elif extension == '.xlsx' or extension == '.csv':
            destination_path = os.path.join(desktop_path, ".xlsx")
        elif extension == '.docx':
            destination_path = os.path.join(desktop_path, ".docx")
        elif extension == '.pdf':
            destination_path = os.path.join(desktop_path, ".pdf")
        elif extension == '.lnk':
            continue
        else:
            destination_path = os.path.join(desktop_path, "Others")
        
        counter = 1
        destination_file_path = os.path.join(destination_path, item)

        while os.path.exists(destination_file_path):
            filename, file_extension = os.path.splitext(item)
            new_filename = f"{filename}_{counter}{file_extension}"
            destination_file_path = os.path.join(destination_path, new_filename)
            counter += 1
        
        shutil.move(source_path, destination_file_path)

print("Files successfully organized.")

            
    




