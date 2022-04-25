


def vowCount(string:str) -> int:
    count=0
    for char in string:
        if char in "aeiouAEIOU":
           count +=1 
    return count

print(vowCount("I love python") )
