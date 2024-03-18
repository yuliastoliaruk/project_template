import pandas as pd


def console_input() -> str:
    """
    Text input from the console

    Returns:
        text (str): Text input from the console
    """
    text = input("Enter your text: ")
    return text


def read_file(path_to_file: str) -> str:
    """
    Read text file

    Arguments:
        path_to_file (str): Path to the file to read

    Returns:
        data (str): Data from file

    Raises:
        FileNotFoundError: File not found
    """
    try:
        with open(path_to_file) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def read_file_pandas(path_to_file: str) -> str:
    """
    Read file using pandas

    Arguments:
       path_to_file (str): Path to the file to read

    Returns:
        data (str): Data from file

    Raises:
        FileNotFoundError: File not found
    """
    try:
        file = pd.read_csv(path_to_file)
        data = ' '.join(file.iloc[:, 0].astype(str).tolist())
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
