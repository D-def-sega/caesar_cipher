import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter # to handle spaces and symbols
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet) # in case the number exceeds the length of the alphabet
            output_text += alphabet[shifted_position] # appends new letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


run = True
#caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    y_or_no = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

    if y_or_no == "yes":
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    elif y_or_no == "no":
        run = False
    else:
        print("Incorrect typo")

