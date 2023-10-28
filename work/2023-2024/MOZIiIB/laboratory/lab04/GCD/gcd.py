
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    return gcd(b % a, a)


def gcdExtended(a, b):
 
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
 
def gcdBinary(a, b):
    if (a == 0): return b
    if (b == 0): return a
    if(a == b): return a

    if(a % 2 ==0):
        if(b % 2 == 0):
            return 2 * gcdBinary(a / 2, b / 2)
        else: return gcdBinary(a / 2, b)
    else:
        if(b % 2 ==0): return gcdBinary(a, b / 2)

        else:
            return gcdBinary(abs(a - b), min(a, b))

def gcdExtendedBinary(A, B):
    k = 1
    x, xx, y, yy = 1, 0, 0, 1
 
    while (A != 0) and (B != 0):
        if A > B:
            q = a // b
        else:
            q = b // a
 
        while (A % 2 == 0) and (B % 2 == 0):
            A /= 2
            B /= 2
            k *= 2
 
        while A % 2 == 0:
            A /= 2
        while B % 2 == 0:
            B /= 2
 
        if A >= B:
            A -= B
        else:
            B -= A
 
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
 
    return B * k, x, y


# Driver code
a, b = 35, 15

print("\n")
gcd = gcd(a, b)
print("Euclidean Algorithm GCD: ", gcd)
print("\n")

gcdextended, x, y = gcdExtended(a, b)
print("Extended Euclidean Algorithm GCD: ", gcdextended, " ", x, " ", y)
print("\n")

gBinary = gcdBinary(a, b)
print("Binary GCD: ", gBinary)
print("\n")

gcdExBinary, x, y = gcdExtendedBinary(a, b)
print("GCD EXTENDED BINARY: ", gcdExBinary)
