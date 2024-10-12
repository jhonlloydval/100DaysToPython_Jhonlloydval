alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt():
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    encrypted_text = []
    for x in range(len(original_text)):
        for y in range(len(alphabet)):
            if original_text[x] == alphabet[y]:
                if y + shift_amount >= len(alphabet):
                    text_mod = (y + shift_amount) % len(alphabet)
                    encrypted_text.append(alphabet[text_mod])  
                else:
                    encrypted_text.append(alphabet[y + shift_amount])
                continue


                
    print("Here is the encoded result: " + "".join(encrypted_text))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def decrypt():
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    decrypted_text = []

    for x in range(len(original_text)):
        for y in range(len(alphabet)):
            if original_text[x] == alphabet[y]:
                if y - shift_amount < 0:
                    text_mod = (y - shift_amount) % len(alphabet)
                    decrypted_text.append(alphabet[text_mod])
                else:
                    decrypted_text.append(alphabet[y - shift_amount])
    print("Here is the decoded result: " + "".join(decrypted_text))

if direction == "encode":
    encrypt()

elif direction == "decode":
    decrypt()


