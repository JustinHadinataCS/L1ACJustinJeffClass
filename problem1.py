def find_subword(word1, word2):
    for i in range(len(word1)):
        if word2.startswith(word1[i:]):
            return word1[i:]
    return ''

def word_linking_game():
    word1_length = int(input("Length of the first word: "))
    word1 = input("First word: ").lower()
    
    word2_length = int(input("Length of the second word: "))
    word2 = input("Second word: ").lower()

    subword = find_subword(word1, word2)

    if subword:
        print(f"Both words can be linked with the subword '{subword}'.")
    else:
        print("Both words cannot be linked.")

word_linking_game()

