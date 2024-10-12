alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt():
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    for x in original_text:
        for y in alphabet:
            if x == y:
                x = alphabet[y + shift_amount]
    print(*encrypt)
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
encrypt()
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction == "encode":
    encrypt()