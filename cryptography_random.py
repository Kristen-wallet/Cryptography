from random import random,choice
import string

def is_even(number):
    return number % 2 == 0

def encrypt(message):
    letter_list = []
    for counter in range(len(message)):
        letter_list.append(message[counter])
        letter_list.append(choice(string.ascii_letters))

    cypher_data =''.join(reversed(letter_list))
    return cypher_data

def decrypt(message):
    letter_list = []
    plain_data = ''.join(reversed(message))
    for counter in range(len(message)):
        if is_even(counter):
         letter_list.append(plain_data[counter])
    plain_data = ''.join(letter_list)
    return plain_data

print("1)use for encryption")
print("2)Use for decryption")
while True:
    choose = input("Enter your choice: ")
    if choose == '1':
        message = input("Enter word or sentence to encrypt: ")
        encrypted_msg = encrypt(message)
        print("encrypted_msg: "+encrypted_msg)
    elif choose == '2':
        message = input("Enter word or sentence to decrypt: ")
        decrypted_msg = decrypt(message)
        print(decrypted_msg)
    else:
         print("Incorrect choice! Make sure that you are entered correct number.")