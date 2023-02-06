def fastModulo(x,y,z):
    #base case
    if y == 1:
        return x % z
    #if y is odd
    elif y % 2 == 1:
        return (fastModulo(x,y>>1,z)**2 * x) % z
    #if y is even
    else:
        return (fastModulo(x,y>>1,z)**2) % z

if __name__ == "__main__":
    x = int(input("Enter base: "))
    y = int(input("Enter exponent: "))
    z = int(input("Enter modulus: "))
    print(fastModulo(x,y,z))
