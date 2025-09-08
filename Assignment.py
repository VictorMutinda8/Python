def modify_content(content: str) -> str:
    """
    Modify the file content before saving it.
    Example: make all text uppercase.
    """
    return content.upper()


def main():
    # Ask user for input file
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try reading the file
        with open(input_filename, "r", encoding="utf-8") as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: You don’t have permission to read '{input_filename}'.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    # Modify content
    modified_content = modify_content(content)

    # Generate output filename
    output_filename = "modified_" + input_filename

    try:
        # Write to new file
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)
        print(f"Success 🎉 Modified file saved as '{output_filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
