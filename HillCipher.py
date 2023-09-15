import numpy as np

pt = input("Enter the plain text: ")
key = input("Enter the key: ")

# format the plain text
pt = pt.replace(" ", "")
pt = pt.lower()

# format the key
key = key.replace(" ", "")
key = key.lower()

alpha = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}

n = len(pt)
keylist = []

for i in key: 
    keylist.append(alpha[i])

# reshape keylist to nxn
keylist = np.array(keylist)
keylist = keylist.reshape(n, n)

print(keylist)

ptvector = []

for i in pt:
    ptvector.append(alpha[i])

ciphervector = []
ciphervector = np.dot(keylist, ptvector)

for i in range(len(ciphervector)):
    ciphervector[i] = ciphervector[i] % 26

cipher = ""

for i in ciphervector:
    for key, value in alpha.items():
        if value == i:
            cipher += key

print(cipher)

# key = GYBNQKURP