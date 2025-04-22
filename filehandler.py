def modify_content(content):
    # Example modification: Convert to uppercase
    return content.upper()

def main():
    # Ask user for the input filename
    input_filename = input("Enter the filename to read from: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Ask user for the output filename
        output_filename = input("Enter the filename to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Success! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
