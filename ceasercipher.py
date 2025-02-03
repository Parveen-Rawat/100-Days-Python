alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(original_text, shift_amount):
    
    cipher_text = ""
    for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text +=  alphabet[shifted_position]
        
        
    print(f"Here is your encrpted text : {cipher_text}")
    
def decrypt(encrypted_text, shifted_ammount):
    decipher_text = ""
    for letter in encrypted_text:
        if letter not in alphabet:
            decipher_text += letter
        else: 
            original_position = alphabet.index(letter) - shifted_ammount
            original_position %= len(alphabet)
            decipher_text += alphabet[original_position]
            
    print(decipher_text)    

    
def caeser():
    if direction == "decode":
        decrypt(encrypted_text=data, shifted_ammount=shift)
    elif direction == "encode":
        encrypt(original_text= data, shift_amount=shift )               
    else:
        print("You have entered the wrong direction kindly correct it.\n")

core = True

while core:
    direction = input("Type 'encode' or 'decode' to encrypt or decrypt the data: ").lower()
    data = input("What's your message: ").lower()
    shift = int(input("Type the shift number: "))

    caeser()
    
    taken = input("Do you want to continue: [y/n]").lower()
    if taken == 'y':
        core = True
    else:
        core = False
        print("GOOD BYE PLAYER")