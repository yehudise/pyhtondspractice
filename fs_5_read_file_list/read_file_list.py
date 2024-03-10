def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip off newline character and print each line with a "-"
                print(f"- {line.rstrip()}")
    except FileNotFoundError:
        # If the file cannot be found, raise an error
        raise FileNotFoundError(f"File '{filename}' not found")
    
print (read_file_list("dogs"))
#for some reason its printing none at the end...
