import math #used for calculating the square root of the discriminants
from fractions import Fraction #used to convert my answers from decimals to fractions

# Getting values from user 
valueOfa = input("Enter the value of a(x squared) : ")
valueOfb = input("Enter the value of b : ")
valueOfc = input("Enter the value of c : ")

print(f'The value of a is {valueOfa} and b is {valueOfb} and c is {valueOfc}')

# converting user input to int 
valueOfa_int = int(valueOfa)
valueOfb_int = int(valueOfb)
valueOfc_int = int(valueOfc)

# Calculating discriminant
valueOfbSquared = valueOfb_int * valueOfb_int
valueOf4ac = (4 * valueOfa_int * valueOfc_int)
discriminant = valueOfbSquared - valueOf4ac

print(f"the value of b squared is {valueOfbSquared}")
print(f"the value of the valueof4ac is {valueOf4ac}")
print(f"the value of the discrimant is {discriminant}")
# Calculating roots

if discriminant > 0:
    squareRootOfDiscriminant = math.sqrt(discriminant)
    print(f"the square of the discrimant is {squareRootOfDiscriminant}")
    root1 = Fraction(((-valueOfb_int + squareRootOfDiscriminant) / (2 * valueOfa_int))).limit_denominator() #Returning the value as a fraction
    print(f"the value of the first root using {valueOfb_int} + the square root of {squareRootOfDiscriminant} is {root1} ")

    root2 = Fraction(((-valueOfb_int - squareRootOfDiscriminant) / (2 * valueOfa_int))).limit_denominator() #Returning the value as a fraction
    print(f"the value of the first root using {valueOfb_int} + the square root of {squareRootOfDiscriminant} is {root2} ")
elif discriminant == 0 :
    root = -valueOfb_int / (2 * valueOfa_int)
    print(f"the value of the root is {root}")
else:
    print(f"Invalid values from users")