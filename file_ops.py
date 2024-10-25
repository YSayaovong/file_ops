# file_ops.py

def read_file(file_name):
    """
    Reads the contents of a file and returns it as a string.
    :param file_name: str, name of the file to read from.
    :return: str, contents of the file.
    """
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def read_file_into_list(file_name):
    """
    Reads the contents of a file line by line and returns a list of lines.
    Each line will retain its newline character.
    :param file_name: str, name of the file to read from.
    :return: list, lines from the file.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def write_first_line_to_file(content, output_file_name):
    """
    Writes the first line of the content to the specified output file.
    :param content: str, the content to write from.
    :param output_file_name: str, name of the output file.
    """
    lines = content.splitlines()
    if lines:
        first_line = lines[0] + '\n'  # Add newline to match expected output
        with open(output_file_name, 'w') as file:
            file.write(first_line)

def read_even_numbered_lines(file_name):
    """
    Reads the even-numbered lines of a file and returns them as a list.
    Each line will retain its newline character.
    :param file_name: str, name of the file to read from.
    :return: list, even-numbered lines of the file.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [lines[i] for i in range(1, len(lines), 2)]  # Keep newline

def read_file_in_reverse(file_name):
    """
    Reads the contents of a file and returns the lines in reverse order.
    Each line will retain its newline character.
    :param file_name: str, name of the file to read from.
    :return: list, lines of the file in reverse order.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return list(reversed(lines))

# Main function to test the file operations
if __name__ == "__main__":
    file_name = 'sampletext.txt'
    output_file_name = 'output.txt'

    # Test read_file
    content = read_file(file_name)
    print("File Content:\n", content)

    # Test read_file_into_list
    lines = read_file_into_list(file_name)
    print("\nLines in File:", lines)

    # Test write_first_line_to_file
    write_first_line_to_file(content, output_file_name)
    print(f"\nFirst line written to {output_file_name}.")

    # Test read_even_numbered_lines
    even_lines = read_even_numbered_lines(file_name)
    print("\nEven-Numbered Lines:", even_lines)

    # Test read_file_in_reverse
    reversed_lines = read_file_in_reverse(file_name)
    print("\nFile in Reverse Order:", reversed_lines)
