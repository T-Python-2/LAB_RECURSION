

def vowel_check(sen):

    if not sen:
        return 0
    return 'aeiouAEIOU'.count(sen[0]) + vowel_check(sen[1:])





print(vowel_check("I love python"))