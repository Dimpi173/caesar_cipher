def encrypt(msg, key):
    encrypted_msg = ""
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_msg += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            encrypted_msg += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted_msg += char
    print(f"Here's the encrypted result : {encrypted_msg}")


def decrypt(msg, key):
    decrypted_msg = ""
    for i in msg:
        if i.isupper():
            decrypted_msg += chr((ord(i) - key - 65) % 26 + 65)
        elif i.islower():
            decrypted_msg += chr((ord(i) - key - 97) % 26 + 97)
        else:
            decrypted_msg += i
    print(f"Here's the decrypted message : {decrypted_msg}")


stop_loop = False
while not stop_loop:
    option = input("Type 'encrypt' for encryption, Type 'decrypt' for decryption : \n")
    message = input("Type your message : \n")
    shift = int(input("Type the shift key / number : \n"))
    if option == "encrypt":
        encrypt(msg=message, key=shift)
    elif option == "decrypt":
        decrypt(msg=message, key=shift)
    else:
        print("Invalid Input")
        stop_loop = True
    user = input("type 'yes' if you want to do again, else type 'no' : \n")
    if user == "yes":
        continue
    elif user == "no":
        stop_loop = True
    else:
        print("You Entre Somthing Else")
        stop_loop = True

print("Goodbye............")
