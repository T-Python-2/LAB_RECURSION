def vowels(word:str):
    if len(word) == 0:
        return 0
    if word[0] in "aAeEiIoOuU":
        return 1 + vowels(word[1:])
    else:
        return 0 + vowels(word[1:])

print(vowels(input("Enter the word to count how many vowels in the word: ")))