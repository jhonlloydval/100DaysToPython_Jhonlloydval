# CAESAR CYPHER [SOLUTION 1: OWN SOLUTION]
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


encrypted_text = []
def encrypt(original_text, shift_amount):
    for letter in original_text:
        if letter in alphabet:
            y = alphabet.index(letter)
            encrypted_text.append(alphabet[(y + shift_amount) % len(alphabet)])
        else:
            encrypted_text.append(original_text[original_text.index(letter)])
    print("Here is the encoded result: " + "".join(encrypted_text))


decrypted_text = []
def decrypt(original_text, shift_amount):
    for letter in original_text:
        if letter in alphabet:
            y = alphabet.index(letter)
            decrypted_text.append(alphabet[(y - shift_amount) % len(alphabet)])
        else:
            decrypted_text.append(original_text[original_text.index(letter)])
    print("Here is the decoded result: " + "".join(decrypted_text))


if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)

elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
'''

# CAESAR CIPHER [SOLUTION 2: Based on bootcamp]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            encrypted_text += alphabet[shifted_position]
        else:
            encrypted_text += letter
    print("Here is the encoded result: " + "".join(encrypted_text))

def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter
    
    print("Here is the decoded result: " + "".join(decrypted_text))
    
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)

if direction == "decode":
    decrypt(original_text=text, shift_amount=shift)