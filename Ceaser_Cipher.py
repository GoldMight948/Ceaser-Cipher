import time
import sys

def flash_text(text, duration, interval):
    start_time = time.time()  
    while time.time() - start_time < duration:
        sys.stdout.write('\r' + text)
        sys.stdout.flush()  
        time.sleep(interval)
        sys.stdout.write('\r' + ' ' * len(text))
        sys.stdout.flush()
        time.sleep(interval)

def encrypt_message(text, shift):
    #Encrypts a message using a Caesar cipher with a given shift.
    encrypted = ""
    for char in text:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_char = char  # Leave non-alphabetic characters unchanged
        encrypted += new_char
    return encrypted

def decrypt_message(text, shift):
    #Decrypts a message that was encrypted using a Caesar cipher with a given shift.
    decrypted = ""
    for char in text:
        if char.islower():
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            new_char = char  # Leave non-alphabetic characters unchanged
        decrypted += new_char
    return decrypted

# Main program
print("Welcome to The Caesar Cipher")
choice = int(input("Would you like to 1.Encrypt or 2.Decrypt a message? "))

shift = int(input("Enter Shift: "))

if choice in range(1,3):
    message = input("Enter String: ")
    flash_text("---------------", duration=5, interval=0.5)
    print("")  # Blank line for spacing
    
    if choice == 1:
        encrypted_message = encrypt_message(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 2:
        decrypted_message = decrypt_message(message, shift)
        print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice.")
