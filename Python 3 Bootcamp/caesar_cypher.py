#Ceaser Cypher
'''Quick project to encrypt and decrypt a message using a Caesar cypher.'''
#Creating the alphabet cipher dictionaries
import string
ALPHABET = {'a':0}
R_ALPHABET = {0:'a'}
ENCRYPTED_STRING = ""
GAME_STATE = True
KEY = 0
X = 1
Y = 26
for letter in string.ascii_lowercase:
    ALPHABET[letter] = X
    X += 1
    R_ALPHABET[Y] = letter
    Y -= 1

#Defining a function to take in a string and encrypt it
def encryption(encrypted_string,key):
    '''Function to ask for a string to encrypt, and the key to use to do so.'''
    string_to_encrypt = input("What is the message you would like encrypted?").lower()
    KEY = int(input("What is the encryption/decryption key?"))
    for character in string_to_encrypt:
        try:
            encrypted_string += R_ALPHABET[((KEY+ALPHABET[character])%26)]
        except KeyError:
            encrypted_string += " "
    print(f"The encrypted message: {encrypted_string}")
    return encrypted_string,KEY

#Defining a function to request the decryption key 3 times.
def decryption(encrypted_string):
    '''Function to decrypt the string'''
    decrypted_string = ""
    for i in range(4):
        decryption_key = int(input("What is the decryption key?"))
        if decryption_key == KEY:

            print("Correct! Message will now be decrypted.")

            for character in encrypted_string:
                try:
                    decrypted_string += R_ALPHABET[((KEY+ALPHABET[character])%26)]
                except KeyError:
                    decrypted_string += " "
            print(f"The decrypted message: {decrypted_string}")
            break
        elif i == 3:
            print("No attempts left! Message destroyed.")
        else:
            print(f"Incorrect! You have {3-i} attempts remaining.")
    encrypted_string = ""
    return encrypted_string

#Loop to accept new keys to encrypt and go through the decryption process
while GAME_STATE is True:
    ENCRYPTED_STRING,KEY = encryption(ENCRYPTED_STRING,KEY)
    ENCRYPTED_STRING = decryption(ENCRYPTED_STRING)
