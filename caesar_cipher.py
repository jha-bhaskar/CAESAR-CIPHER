alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n','o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]


def encryption(plane_text,shift_key):
    cipher_text =""
    for char in plane_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position = (position + shift_key)%52
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The text after encryption : {cipher_text}")


def decryption(cipher_text,shift_key):
    plain_text =""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position = (position - shift_key)%52
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The text after decryption : {plain_text}")
    

exit=False
while not exit:
    work=input("Type 'encrypt' for encryption , type 'decrypt' for decryption : \n")
   
    if work == "encrypt":
        text=input("Type your message :\n")
        shift=int(input("Enter shift key : \n"))
        encryption(plane_text =text , shift_key =shift)

    elif work == "decrypt":
        text=input("Type your message :\n")
        shift=int(input("Enter shift key : \n"))
        decryption(cipher_text=text , shift_key=shift)
        
    print("Do you want to continue ?")
    begin = input("Type 'yes' or 'no'  \n")
    if begin == "no":
        exit=True
        print("exit ....")
    


    