def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    words = get_num_words(file_contents)
    char = get_num_char(file_contents)
    char_sorted = sort_char(char)
    create_report(path, words, char_sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_char(file_contents):
    lower_file_contents = file_contents.lower()
    char_count = {}
    for char in lower_file_contents:
        if char in char_count and char.isalpha():
            char_count[char] += 1
        elif char.isalpha(): 
            char_count[char] = 1
    return char_count

def sort_char(char_list):
    sorted_list = []
    for char in char_list:
        char_dict = {"name": char, "amount": char_list[char]}
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=lambda char: char["amount"])
    return sorted_list

def create_report(path, words, char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    for char in char_count:
        print(f"the '{char["name"]}' character was found {char["amount"]} times")
    print("\n--- End report ---")

main()