import os
import shutil

def move_all_files(source_root, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    for root, dirs, files in os.walk(source_root, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            dest_path = os.path.join(destination_folder, file)

            # Rename file if one with the same name exists
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(file)
                count = 1
                while os.path.exists(dest_path):
                    new_name = f"{base}_{count}{ext}"
                    dest_path = os.path.join(destination_folder, new_name)
                    count += 1

            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} → {dest_path}")

if __name__ == "__main__":
    print("🗂️  Move All Files from Folder and Subfolders\n")
    source_root = input("Enter the full path of the ROOT folder (source): ").strip('"')
    destination_folder = input("Enter the full path of the DESTINATION folder: ").strip('"')

    if not os.path.isdir(source_root):
        print(f"❌ The source folder does not exist: {source_root}")
    else:
        move_all_files(source_root, destination_folder)
        print("\n✅ All files moved successfully.")