def main():
    path_to_books = "books/frankenstein.txt"
    text = book_text(path_to_books)
    count = word_counter(text)
    letter = letter_count(text)
    print(count, letter)

def word_counter(text):
    word_list = text.split()
    return  len(word_list)

def book_text(path):
    with open(path) as f:
        return f.read()
    
def letter_count(text):
    letters = list(text.lower())
    l_list = {}
    for letter in letters:
        if letter not in l_list:
            l_list[letter] = letters.count(letter)
    return l_list

main()