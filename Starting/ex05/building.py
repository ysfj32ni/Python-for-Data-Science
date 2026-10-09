import sys


def count_characters(text):
    """
    Counts the number of uppercase, lowercase, punctuation, space,
    and digit characters in a string.
    Returns:
        __tuple__: A tuple containing the counts of uppercase, lowercase,
        punctuation,space, and digit characters.
    """
    UpCount = 0
    LowCount = 0
    PunctCount = 0
    SpaceCount = 0
    DigitCount = 0
    for char in text:
        if char.isupper():
            UpCount += 1
        elif char.islower():
            LowCount += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            PunctCount += 1
        elif char == " " or char == '\n':
            SpaceCount += 1
        elif char.isdigit():
            DigitCount += 1
    return UpCount, LowCount, PunctCount, SpaceCount, DigitCount


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 2:
        print(f"The text contains {len(sys.argv[1])} characters:")
        print(f"{count_characters(sys.argv[1])[0]} upper letters")
        print(f"{count_characters(sys.argv[1])[1]} lower letters")
        print(f"{count_characters(sys.argv[1])[2]} punctuation marks")
        print(f"{count_characters(sys.argv[1])[3]} spaces")
        print(f"{count_characters(sys.argv[1])[4]} digits")
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        data = sys.stdin.read()
        print(f"The text contains {len(data)} characters:")
        print(f"{count_characters(data)[0]} upper letters")
        print(f"{count_characters(data)[1]} lower letters")
        print(f"{count_characters(data)[2]} punctuation marks")
        print(f"{count_characters(data)[3]} spaces")
        print(f"{count_characters(data)[4]} digits")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
