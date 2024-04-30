def preprocess_pattern(pattern):
    # Preprocessing step to generate the bad character heuristic
    pattern_length = len(pattern)
    bad_character = {}
    for i in range(pattern_length - 1):
        bad_character[ord(pattern[i])] = pattern_length - i - 1
    return bad_character

def boyer_moore(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    bad_character = preprocess_pattern(pattern)
    shift = 0

    while shift <= text_length - pattern_length:
        mismatch_index = -1
        for i in range(pattern_length - 1, -1, -1):
            if pattern[i] != text[shift + i]:
                mismatch_index = i
                break

        if mismatch_index == -1:
            return shift  # Pattern found

        shift += max(1, mismatch_index - bad_character.get(ord(text[shift + mismatch_index]), -1))

    return -1  # Pattern not found

def wordle_solver(word_list, pattern):
    for word in word_list:
        if len(word) == len(pattern) and boyer_moore(word, pattern) != -1:
            return word
    return None

# Example usage:
word_list = ["apple", "banana", "cherry", "lemon", "mango"]
pattern = "pear"
result = wordle_solver(word_list, pattern)
if result:
    print(f"The word is: {result}")
else:
    print("No matching word found.")
