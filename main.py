def main():
    
    with open('books/frankenstein.txt', 'r') as f:
     
        file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)
    char_count = {}

    for word in words:
        lowered_word = word.lower()
        for lowered in lowered_word:   
            if lowered in char_count:
                char_count[lowered] += 1
            else:
                char_count[lowered] = 1
    

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")


    for char, count in char_count.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
main()
