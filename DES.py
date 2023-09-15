def xor_encrypt(plain_text):
    # Ensure the plaintext is 64 bits (8 characters)
    if len(plain_text) != 8:
        raise ValueError("Input plaintext must be 8 characters (64 bits).")

    # Split the 64-bit plain text into two 32-bit blocks
    block1 = plain_text[:4]
    block2 = plain_text[4:]

    # Convert the blocks to binary representation
    block1_binary = ''.join(format(ord(char), '08b') for char in block1)
    block2_binary = ''.join(format(ord(char), '08b') for char in block2)

    # Perform XOR operation between the two blocks
    encrypted_block2_binary = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(block1_binary, block2_binary))

    # Convert the encrypted binary block back to characters
    encrypted_block2 = ''.join(chr(int(encrypted_block2_binary[i:i+8], 2)) for i in range(0, len(encrypted_block2_binary), 8))

    # The encrypted 64-bit cipher text is formed by combining the original second block and the encrypted second block
    cipher_text = block2 + encrypted_block2

    return cipher_text

if __name__ == "__main__":
    plain_text = input("Enter 64-bit plain text: ")
    if len(plain_text) != 8:
        print("Input plaintext must be 8 characters (64 bits).")
    else:
        cipher_text = xor_encrypt(plain_text)
        print("Encrypted Cipher Text: {} {}".format(cipher_text, len(cipher_text)))