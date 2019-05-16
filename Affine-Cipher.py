from string import ascii_lowercase as alphabet 
from math import gcd

def encode(plainText, multi, shift):
    cipherText = ""
    for char in plainText:
        cipher = ((multi * alphabet.index(char) + shift) % len(alphabet))
        cipherText += alphabet[cipher]
    return cipherText

def decode(cipherText, multi, shift):
    plainText = ""
    for i in range(1, len(alphabet)):
        if (multi * i) % len(alphabet) == 1:
            inv = i

    for char in cipherText:
        plain = ((inv * (alphabet.index(char) - shift)) % len(alphabet))
        plainText += alphabet[plain]
    return plainText

plainText = input("Welcome to my Affine Cipher Script.\nPlease enter your plain text.\n"
                "(Enter only lowercase alphabets, no special characters or spaces.):\n")

while True:
    multi = int(input("Please enter a multiplicative integer:\n"))
    if gcd(multi, len(alphabet)) == 1:
        break
    print("ValueError: This integer is not a coprime of ", len(alphabet), ".\n")

shift = int(input("Please enter the magnitude of the shift:\n"))

print("This is your cipher text: ", encode(plainText, multi, shift), "\n")

cipherText = encode(plainText, multi, shift)

print("This is your plain text: ", decode(cipherText, multi, shift))
