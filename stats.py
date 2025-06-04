def get_num_words(word_split):
    word_count = len(word_split)
    print(f"Found {word_count} total words") 
##
def get_letter_count(word_split):
    letter_count = {}
    for word in word_split:
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
    sorted_letters = sorted(letter_count.items(), key=lambda item: (-item[1], item[0]))
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")