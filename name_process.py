def process_name(input_name):
    # Remove backslashes
    cleaned_name = input_name.replace("\\", "")
    
    # Generate shrinking names
    shrinking_names = []
    while cleaned_name:
        shrinking_names.append(cleaned_name)
        cleaned_name = cleaned_name[:-1]
    
    # Generate expanding names
    expanding_names = shrinking_names[::-1][1:]  # Exclude the full name to avoid duplication
    
    # Combine shrinking and expanding
    full_process = shrinking_names + expanding_names
    
    return full_process

# Main code
if __name__ == "__main__":
    name = r"iiiiii0vicky0-0singh0iiiii"
    names_list = process_name(name)

    # Save the output to a file
    with open("output.txt", "w") as f:
        for n in names_list:
            f.write(n + "\n")
