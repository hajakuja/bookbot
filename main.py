from stats import count_words, count_characters, sorted_count
from pprint import pprint
import sys

def get_book_text(book_path):
    file_contents = ""
    with open(book_path, "r", encoding="utf8") as book:
        file_contents = book.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(book))} total words\n--------- Character Count -------")
    
    count = count_characters(get_book_text(book))
    sorted = sorted_count(count)
    for i in sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()