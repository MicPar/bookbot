def main():
    file_path = "books/frankenstein.txt"
    file_text = get_text(file_path)
    number_of_words = get_number_of_words(file_text)
    character_inventory = get_character_inventory(file_text)
    
    print_report(file_path, number_of_words, character_inventory)


def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_number_of_words(file_text):
    words = file_text.split()
    return len(words)

def get_character_inventory(file_text):
    character_inventory = {}
    for char in file_text.lower():
        character_inventory[char] = character_inventory.get(char, 0) + 1
    return character_inventory

def print_report(file_path, number_of_words, character_inventory):
    print(f"--- Begin report of {file_path} ---")
    print(f"{number_of_words} words in the document")
    print()
    for char in dict(sorted(character_inventory.items())):
        if char.isalpha() == True:
            print(f"The '{char}' character was found {character_inventory[char]} times")
    print("--- End report ---")


main()