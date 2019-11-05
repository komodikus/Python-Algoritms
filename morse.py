from typing import List

MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

MORSE_TABLE = dict(zip(ALPHABET, MORSE))


def words_to_morse(words: List):
    for word in words:
        morse_word = ""
        for letter in word:
            morse_word += (MORSE_TABLE[letter])
        yield morse_word


if __name__ == '__main__':
    _words = ["gin", "zen", "gig", "msg"]
    print(len(set(words_to_morse(_words)))) # unique morse words in list
