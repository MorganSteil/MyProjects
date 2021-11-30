import random


LOW_ALPHA = "abcdefghijklmnopqrstuvwxyz"
UP_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+?><"


ALL_CHARACTERS = LOW_ALPHA + UP_ALPHA + NUMBERS + SYMBOLS
length = len(ALL_CHARACTERS)



charCount = int(input("Enter password length: "))



def passwordGenerate(charNum):
  for i in range(charNum):
    ranChar = random.randint(1, length) - 1
    print(ALL_CHARACTERS[ranChar], end = "")



passwordGenerate(charCount)
