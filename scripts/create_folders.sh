#!/bin/bash

# Specify the path to your text file here
FILE_PATH="D:\continuous_learning\coursera\prompt_engineering_for_chatgpt\toc.md"

# Check if the file exists
if [ ! -f "$FILE_PATH" ]; then
  echo "File not found: $FILE_PATH"
  exit 1
fi

# Read the file line by line
while IFS= read -r line
do
  # Process each line: convert to lowercase and replace spaces with underscores
  folder_name=$(echo "$line" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
  
  # Create the folder if it doesn't exist
  if [ ! -d "$folder_name" ]; then
    mkdir "$folder_name"
    echo "Created folder: $folder_name"
  else
    echo "Folder already exists: $folder_name"
  fi
done < "$FILE_PATH"
