from pathlib import Path

def create_txt(tokens):
    if len(tokens) < 2:
        print("Error: Please specify a file name.")
    elif tokens[1] == '--help':
        print("Usage: create [FILE]")
        print("Create a new file named FILE.")
        print("  --help   display this help and exit")
    elif len(tokens) > 2:
        print("Error: Too many arguments.")
    else:
        try:
            file_path = Path(tokens[1])
            file_path.touch(exist_ok=True)
        except PermissionError:
            print(f"Error: Permission denied to create file '{tokens[1]}'.")

def write_txt(tokens):
    if len(tokens) < 3:
        print("Error: Please specify a file name and data to write.")
    elif tokens[1] == '--help':
        print("Usage: write [FILE] [DATA]")
        print("Write DATA to the specified FILE.")
        print("  --help   display this help and exit")
    elif len(tokens) > 3:
        print("Error: Too many arguments.")
    else:
        try:
            file_path = Path(tokens[1])
            text_to_write = tokens[2].removeprefix('"').removesuffix('"').removeprefix("'").removesuffix("'")
            text_to_write = text_to_write.replace("\\n", "\n")  # Handle newline characters
            text_to_write = text_to_write.replace("\\t", "\t")  # Handle tab characters
            text_to_write = text_to_write.replace("\\\"", "\"")  # Handle escaped quotes
            text_to_write = text_to_write.replace("\\\\", "\\")  # Handle escaped back
            text_to_write = text_to_write.replace("\\'", "'")  # Handle escaped single quotes
            with open(file_path, 'w') as f:
                f.write(text_to_write)
        except PermissionError:
            print(f"Error: Permission denied to write to file '{tokens[1]}'.")