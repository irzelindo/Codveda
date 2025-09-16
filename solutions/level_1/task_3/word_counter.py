def word_counter(filename):
    """
    Returns the number of words in a given file.

    If the file does not exist, returns "Error: File not found."
    """
    try:
        with open(filename, "r") as f:
            words = f.read().split()
            return len(words)
    except FileNotFoundError:
        return "Error: File not found."

if __name__ == "__main__":
    print(word_counter("sample.txt"))

