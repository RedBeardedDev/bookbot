from sys import argv
from stats import get_num_words
from stats import get_letter_count
## Main script to read a file and count words and letters
if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

file_path = argv[1]
with open(file_path) as f:
    file_contents = f.read()
    word_split = file_contents.split()
## Output the results
print("============ BOOKBOT ============")
print(f"Analyzing book found at {argv[1]}...")
print("----------- Word Count ----------")
get_num_words(word_split)
print("--------- Character Count -------")
get_letter_count(word_split)
print("============= END ===============")