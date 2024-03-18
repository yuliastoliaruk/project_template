from app.io import input, output


def main():
    path_to_input_file = ""  # write path to input file
    path_to_output_file = ""  # write path to output file

    text_from_console = input.console_input()
    file_text = input.read_file(path_to_input_file)
    file_text_with_pandas = input.read_file(path_to_input_file)

    text_for_output = (f'Text from console:\n{text_from_console}\n'
                       f'{100*"-"}\n'
                       f'Text from file read by built-in python functions:\n{file_text}\n'
                       f'{100*"-"}\n'
                       f'Text from file read by pandas:\n{file_text_with_pandas}\n')
    output.console_output(text_for_output)
    output.add_to_file(text_for_output, path_to_output_file)


if __name__ == '__main__':
    main()
