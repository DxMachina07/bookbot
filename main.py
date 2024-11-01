def main():
    path_to_books = "books/frankenstein.txt"
    text = book_text(path_to_books)
    count = word_counter(text)
    letter = letter_count(text)
    letter_list = char_to_be_sorted(letter)

    print(f"--- Begin report of {path_to_books} ---")
    print(f"{count} words found in the document")
    print()

    for i in letter_list:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")

def word_counter(text):
    word_list = text.split()
    return  len(word_list)

def book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(d):
    return d["num"]

def char_to_be_sorted(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char":char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def letter_count(text):
    letters = list(text.lower())
    l_list = {}
    for letter in letters:
        if letter.isalpha() == True:
            if letter not in l_list:
                l_list[letter] = letters.count(letter)
    return l_list


main()