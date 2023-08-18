plainText = input("Enter the plain text: ")
#print(plainText)

key = int(input("Enter the key: "))
#print(key)

cipherText = ""

"""
The values 65 and 97 are being added and subtracted to convert the 
ASCII value of the character to its alphabetical index. In ASCII, 
the uppercase letters start at 65 and the lowercase letters start at 97. 
By subtracting 65 or 97 from the ASCII value of the character, we get its 
alphabetical index, which we can then use to perform the Caesar cipher 
shift. After the shift, we add 65 or 97 back to the alphabetical index to 
get the ASCII value of the shifted character.
"""

# implement caesar cipher
for c in plainText:
    if c.isalpha():
        if c.isupper():
            cipherText += chr((ord(c) + key - 65) % 26 + 65)
        else:
            cipherText += chr((ord(c) + key - 97) % 26 + 97)

    if c.isnumeric():
        cipherText += str(int(c) + key)

print(cipherText)