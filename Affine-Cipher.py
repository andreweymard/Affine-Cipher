from string import ascii_lowercase
from math import gcd

alphabet = ascii_lowercase

def encode(plainText, multi, shift):
    cipherText = ""
    for char in plainText:
        cipher = ((multi * alphabet.index(char) + shift) % len(alphabet))
        cipherText += alphabet[cipher]
    return cipherText

def decode(cipherText, multi, shift):
    plainText = ""
    result = 1
    for i in range(1, len(alphabet)):
        if (multi * i) % len(alphabet) == 1:
            result = i

    for char in cipherText:
        plain = ((result * (alphabet.index(char) - shift)) % len(alphabet))
        plainText += alphabet[plain]
    return plainText

plainText = input("Welcome to my multiffine Cipher Script.\nPlease enter your plain text (Enter only alphabets and spaces):\n")

while True:
    multi = int(input("Please enter a multiplicative integer:\n"))
    if gcd(multi, len(alphabet)) == 1:
        break
    print("ValueError: This integer is not a coprime of ", len(alphabet), ".\n")

shift = int(input("Please enter the magnitude of the shift:\n"))

print("This is your cipher text: ", encode(plainText, multi, shift), "\n")
    
cipherText = encode(plainText, multi, shift)

print("This is your plain text: ", decode(cipherText, multi, shift))