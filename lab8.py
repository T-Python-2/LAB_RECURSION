
def countVowels(phrase:str):
    vowels = 0
    for i in range(0,len(phrase)):
      if phrase[i] in "aAeEiIoOuU": 
       vowels += 1
     
    return print("Vowels = ", vowels)
   


countVowels("lama")