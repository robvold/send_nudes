import math

def closest_number(n, m):
    q = math.ceil(n / m) 
    number = m * q
    return number
    