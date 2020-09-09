from tkinter import Tk,simpledialog,messagebox

root = Tk()
root.withdraw()

def get_task():
    task = simpledialog.askstring('choice','Do you want to encrypt or decrypt data?')
    return task
def get_message():
    message = simpledialog.askstring('message', 'Enter message here')
    return message
def is_even(number):
    return number % 2 == 0
def get_even_letter(message):
    even_letter = []
    for counter in range(0,len(message)):
        if is_even(counter):
            even_letter.append(message[counter])
    return even_letter
def get_odd_letter(message):
    odd_letter = []
    for counter in range(0,len(message)):
        if not is_even(counter):
            odd_letter.append(message[counter])
    return odd_letter
def swap_letter(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    odd_letter = get_odd_letter(message)
    even_letter = get_even_letter(message)
    for counter in range(0,int(len(message)/2)):
        letter_list.append(odd_letter[counter])
        letter_list.append(even_letter[counter])
        new_message = ''.join(letter_list)
    return new_message
def encrypt(message):
    swapped_message = swap_letter(message)
    encrypted_message = ''.join(reversed(swapped_message))
    return encrypted_message
def decrypt(message):
    reversed_letter = ''.join(reversed(message))
    decrypted_message = swap_letter(reversed_letter)
    return decrypted_message
def encrypt_message_box():
    message = get_message()
    if message:
        encrypt_message = encrypt(message)
        messagebox.showinfo('Encrypted message', encrypt_message)
    else:
        messagebox.showinfo('Empty', 'Message box is empty')
def decrypt_message_box():
    message = get_message()
    if message:
        decrypt_message = decrypt(message)
        messagebox.showinfo('decrypted message', decrypt_message)
    else:
        messagebox.showinfo('message is empty', 'Enter message correctly.')

while True:
    task = get_task()
    if task == 'encrypt':
       encrypt_message_box()
    elif task == 'decrypt':
       decrypt_message_box()
    else:
        break
