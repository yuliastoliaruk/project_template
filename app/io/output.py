def console_output(data: str) -> None:
    """
    Write data to console

    Arguments:
        data {str}: Data to write to console

    Returns:
        None
    """
    print(data)
    return None


def add_to_file(data: str, path_to_file: str) -> None:
    """
    Write data to file

    Arguments:
        data (str): Data to write to file
       path_to_file (str): Path to the file to read

    Returns:
        None

    Raises:
        FileNotFoundError: File not found
    """
    try:
        with open(path_to_file, 'w', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
