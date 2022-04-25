
def vowelCounter(i):
    if not i:
        return 0
    counter = 'aeiou'.count(i[0])
    return counter + vowelCounter(i[1:])

print(vowelCounter("i love python"))