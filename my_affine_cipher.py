from string import ascii_letters
from math import gcd

alphabet = ascii_letters + " "

def encode(plaintxt, A, B):
    ciphertxt = ""
    for char in plaintxt:
        cipher = ((A * alphabet.index(char)+ B) % len(alphabet))
        ciphertxt += alphabet[cipher]
    return ciphertxt

def decode(ciphertxt, A, B):
    plaintxt = ""
    result = 1
    for i in range(1, len(alphabet)):
        if (A * i) % len(alphabet) == 1:
            result = i
    
    for char in ciphertxt:
        plain = ((result * (alphabet.index(char)- B)) % len(alphabet))
        plaintxt += alphabet[plain]
    return plaintxt

plaintxt = input("Welcome to my Affine Cipher Script.\nPlease enter your plain text (Enter only alphabets and spaces):\n")

while True:
    A = int(input("Please enter a multiplicative integer:\n"))
    if gcd(A, len(alphabet)) == 1:
        break
    print("ValueError: This integer is not a coprime of ",len(alphabet),".\n")

B = int(input("Please enter the magnitude of the shift:\n"))

print("This is your cipher text: ",encode(plaintxt, A, B),"\n")
ciphertxt = encode(plaintxt, A, B)
print("This is your plain text: ",decode(ciphertxt, A, B))
