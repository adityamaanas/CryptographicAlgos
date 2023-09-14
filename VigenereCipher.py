ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_cipher(msg, key):
    msg = msg.upper()
    key = key.upper()
    encrypted_msg = ''

    # Loop through each character in the message
    for i in range(len(msg)):
        # Get the character at the current index
        char = msg[i]

        # Get the character at the current index of the key
        key_char = key[i % len(key)]

        # Get the index of the character in the alphabet
        char_index = ALPHABET.index(char)

        # Get the index of the character in the alphabet
        key_char_index = ALPHABET.index(key_char)

        # Get the index of the encrypted character
        encrypted_char_index = (char_index + key_char_index) % len(ALPHABET)

        # Get the encrypted character
        encrypted_char = ALPHABET[encrypted_char_index]

        # Add the encrypted character to the encrypted message
        encrypted_msg += encrypted_char

    # Return the encrypted message
    return encrypted_msg

if __name__ == '__main__':
    ans=vigenere_cipher("hai", "hello")
    print(ans)