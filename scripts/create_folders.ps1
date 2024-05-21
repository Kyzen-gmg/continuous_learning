# Specify the path to your text file here
$filePath = "path\to\your\textfile.txt"

# Check if the file exists
if (-Not (Test-Path -Path $filePath)) {
    Write-Output "File not found: $filePath"
    exit
}

# Read the file line by line
Get-Content -Path $filePath | ForEach-Object {
    # Process each line: convert to lowercase and replace spaces with underscores
    $folderName = $_.Trim().ToLower().Replace(' ', '_')
    
    # Create the folder if it doesn't exist
    if (-Not (Test-Path -Path $folderName)) {
        New-Item -ItemType Directory -Path $folderName
        Write-Output "Created folder: $folderName"
    } else {
        Write-Output "Folder already exists: $folderName"
    }
}
