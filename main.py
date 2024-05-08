def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print_report(book_path, num_words, num_letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_num_letters(book_text):
    letters = {}
    for letter in book_text:
        if letter.isalpha():
            if letter.lower() not in letters:
                letters.update({letter.lower() : 1})
            else:
                letters[letter.lower()] += 1
    return letters


def sort_on(dict):
    return dict[1]


def print_report(book_path, num_words, num_letters):
    num_letters_list = num_letters.items()

    sorted_letters_list = sorted(num_letters_list, reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book.")
    print()
    for char in sorted_letters_list:
        print(f"The '{char[0]}' character was found {char[1]} times.")
    print()
    print("--- End report ---")


main()