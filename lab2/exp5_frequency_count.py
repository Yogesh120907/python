def count_frequencies(text: str) -> tuple[dict[str, int], dict[str, int]]:
    words = text.lower().split()
    word_freq = {}
    for word in words:
        clean_word = "".join(char for char in word if char.isalnum())
        if clean_word:
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

    char_freq = {}
    for char in text.lower():
        if char.isalnum():
            char_freq[char] = char_freq.get(char, 0) + 1

    return word_freq, char_freq

if __name__ == "__main__":
    sample_text = "Data Science with Python. Python is powerful for Data Science!"
    w_freq, c_freq = count_frequencies(sample_text)
    print("Word Frequencies:", w_freq)
    print("Character Frequencies:", c_freq)
