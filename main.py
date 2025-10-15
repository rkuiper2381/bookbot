from stats import count_words
from stats import count_chars
from stats import chars_sorted
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    chars = chars_sorted(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    for i in chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
