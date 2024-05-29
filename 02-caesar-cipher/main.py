import ceasar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    """
    This function performs a Caesar cipher shift on the input text.
    
    Parameters:
    text (str): The message to be encrypted or decrypted.
    shift (int): The number of positions to shift the letters.
    direction (str): 'encode' to encrypt, 'decode' to decrypt.
    
    Returns:
    str: The resulting text after the shift.
    """
        
    shifted_text = ""
    if direction == "decode":
        shift = -shift
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            shifted_text += alphabet[new_position]
        else:
            shifted_text += char
    return shifted_text

def main():
    """
    The main function to run the Caesar cipher program.
    It repeatedly asks the user for input and processes it until the user decides to stop.
    """
    print(ceasar_art.logo)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction in ["encode", "decode"]:
            result = caesar_cipher(text, shift, direction)
            print(f"The {direction}d text is {result}")
        else:
            print("Invalid input. Please type 'encode' to encrypt or 'decode' to decrypt.")

        # TODO-4: Ask if the user wants to restart the cipher program
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart != 'yes':
            print("Goodbye!")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
