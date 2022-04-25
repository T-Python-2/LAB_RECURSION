def vowelChar(char):
    char = char.lower()
    vowels = 'aeiou'
    if char in vowels :
        return 1
    else :
        return 0
def countVowels(word) :
    count = 0
    for i in range(len(word)):
        if vowelChar(word[i]) :
           count+=1    
    return count

print(countVowels("helloooo"))  