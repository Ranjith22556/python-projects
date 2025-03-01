import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#Encryption
print(chars)
print(key)
plain_text=input("Enter the text to encrypt : ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"Encrypted Message : {cipher_text}")
#Decryption
cipher_text=input("Enter the text to decrypt : ")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"Decrypted Message : {plain_text}")