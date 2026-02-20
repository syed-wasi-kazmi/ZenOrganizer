import os
import shutil

# Define categories and their associated file extensions
CATEGORIES = {
    "Images": [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp',
        '.jfif', '.avif', '.ico', '.tif', '.heic', '.raw'
    ],
    "Videos": [
        '.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.webm', '.3gp',
        '.mpeg', '.mpg', '.m4v', '.ts', '.ogv', '.vob', '.m2ts', '.mts'
    ],
    "Documents": [
        '.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt',
        '.odt', '.ods', '.odp', '.rtf', '.tex', '.csv', '.md'
    ],
    "Compressed Files": [
        '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso', '.dmg'
    ],
    "Audio": [
        '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac'
    ],
    "Code": [
        '.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.ts', '.jsx',
        '.tsx', '.json', '.xml', '.sh', '.bat', '.ps1', '.php', '.rb', '.go',
        '.rs', '.pl', '.swift', '.kt', '.m', '.vb'
    ],
    "Executables": [
        '.exe', '.msi', '.bat', '.cmd', '.com', '.jar', '.apk', '.bin'
    ],
    "Others": []  # Catch-all category for files that don't match above
}

def get_category(file_extension):
    """
    Given a file extension, return the category name it belongs to.
    If the extension is not found, return 'Others'.
    """
    file_extension = file_extension.lower()
    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    """
    Organizes files in the given folder by moving them into
    category folders based on file extension.
    """
    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    # List all items in the folder (files and folders)
    files = os.listdir(folder_path)
    print(f"\n📂 Organizing {len(files)} items in: {folder_path}\n")

    for file in files:
        full_path = os.path.join(folder_path, file)

        # Skip if it's a folder; we only want to organize files here
        if os.path.isdir(full_path):
            continue

        # Extract the file extension (e.g., '.txt', '.jpg')
        _, ext = os.path.splitext(file)

        # Get the category based on the file extension
        category = get_category(ext)

        # Create the category folder inside the main folder if it doesn't exist
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file into its category folder
        try:
            shutil.move(full_path, os.path.join(category_folder, file))
            print(f"✅ Moved: {file} → {category}/")
        except Exception as e:
            print(f"❌ Error moving {file}: {e}")

    print("\n🎉 Done organizing!")

def main():
    """
    Main function to run the program.
    It asks the user to input the folder path to organize.
    """
    print("📁 Welcome to Folder Organizer!")
    # Ask user to paste the folder path, stripping any surrounding quotes
    folder_path = input("Paste the folder path you want to organize: ").strip('"')

    # Start organizing the folder
    organize_folder(folder_path)

if __name__ == "__main__":
    main()
