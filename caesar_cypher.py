import logo
print(logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_alphabet = []
new = reversed(alphabet)
for i in new:
    reverse_alphabet.append(i)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift%26 # Tackling index list out of range error
def encrypt(text,shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

def decrypt(text,shift):
    decypher_text = ""
    for letter in text:
        position = reverse_alphabet.index(letter)
        new_position = position + shift
        new_letter = reverse_alphabet[new_position]
        decypher_text += new_letter
    print(f"The decoded text is: {decypher_text}")

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Enter a valid response")

stop = True
while stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else:
        print("Enter a valid response")
    rerun = input('Do you want to rerun the program? Type "yes" or "No"')
    if rerun == "no":
        stop = False
        print("Thankyou")
    
    

