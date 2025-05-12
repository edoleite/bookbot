from stats import count_words
from stats import count_chars
from stats import sort_dictionary

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = count_words(get_book_text('books/frankenstein.txt'))    

    num_chars = sort_dictionary(count_chars(get_book_text('books/frankenstein.txt')))
    
    print("=" * 28, "BOOKBOT", "=" * 28)
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("-" * 43)
    print(f"Found {num_words} total words")
    print("-" * 43)
    print("--------- Character Count -------")
    for entry in num_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
        else:
            continue
    print("=" * 28, "END", "=" * 28)


main()
