def Vowel_Count(x):
    
    if len(x) == 0:
        return 0
    letter = x[0]
    if letter in 'aeiouAEIOU':
        return 1 + Vowel_Count(x[1:])
    return Vowel_Count(x[1:])
    print(Vowel_Count)
Vowel_Count(Ali)