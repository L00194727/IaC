# function divisible return True if there is no remainder
def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

# call function with numerator = 30 and denominator = 4
print(divisible(30,4))

