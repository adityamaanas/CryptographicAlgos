import string

# Taking the key input from the user
k = []
n = int(input("Enter number of key elements: "))
k = list(map(int,input("\nEnter key elements separated by spaces: ").strip().split()))[:n]
if len(k) > n or len(k) < n:
    print("Number of key elements entered does not match previously mentioned value")
#print(k)

# Taking plain text input from the user
pt = ""
pt = input("Enter the plain text: ")
#print(pt)

# Appending characters to the plain text to match key length
if len(pt)%n != 0:
    l = 1
    while len(pt)%n != 0:
        pt += string.ascii_lowercase[-l]
        l += 1
#print(pt)

# Creating cipher text
ct= ""
for m in range(0, len(pt), 5):
    for i in k:
        #print(pt[i+m-1])
        ct += pt[i+m-1]
print("The cipher text is: " + ct)
