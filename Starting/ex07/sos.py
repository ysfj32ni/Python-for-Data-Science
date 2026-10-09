import sys

NESTED_MORSE = {" ": "/",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----"}


def encode_morse(text):
    """
    Encodes a string into Morse code.
    Args:
        text (_str_): The string to encode.
    Returns:
        _str_: The Morse code representation of the input string.
    """
    text = text.upper()
    morse_code = []
    for char in text:
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char.upper()])
    return ' '.join(morse_code)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        if not sys.argv[1].isalnum():
            raise AssertionError
        print(encode_morse(sys.argv[1]))
    except AssertionError:
        print("AssertionError: the arguments are bad")
