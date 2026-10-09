import sys
from ft_filter import ft_filter


def filter_string(text, length):
    """
        Filter a string by a minimum length.
        
    Args:
        text (_string_): The string to filter.
        length (_int_): The minimum length of the words to keep.

    Returns:
        _list_: A list of words that are longer than the specified length.
    """
    words = text.split(' ')
    return ft_filter(lambda word: len(word) > length, words)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: more than one argument is provided")
        if not sys.argv[1].isascii() or not sys.argv[2].isdigit():
            raise AssertionError("AssertionError: the arguments are bad")
        text = sys.argv[1]
        length = int(sys.argv[2])
        print(filter_string(text, length))
    except (AssertionError, ValueError):
        print(f"AssertionError")
