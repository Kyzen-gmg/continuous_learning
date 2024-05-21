import os

def create_folders_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            # Process each line: strip newline characters, convert to lowercase, and replace spaces with underscores
            folder_name = line.strip().lower().replace(' ', '_')
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Created folder: {folder_name}")
            else:
                print(f"Folder already exists: {folder_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your text file here
    file_path = 'D:\continuous_learning\coursera\prompt_engineering_for_chatgpt\toc.md'
    create_folders_from_file(file_path)
