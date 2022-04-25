

def vowels_in_sentence(sentence):
    vowels = {"a", "A", "e","E", "i","I", "o", "O", "u", "U"}
    
    if not sentence:
        return 0
    
    if sentence[0] in vowels:
        return 1 + vowels_in_sentence(sentence[1:])
    else:
        return 0 + vowels_in_sentence(sentence[1:])


input_sentence = input("Give a word/phrase to count how many vowels")
print(vowels_in_sentence(input_sentence))


