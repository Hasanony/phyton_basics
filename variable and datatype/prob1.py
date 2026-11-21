# check type of variable assigned using input() function.

a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

def convert(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

a = convert(a)
b = convert(b)

print("The type of variable a is:", type(a))
print("The type of variable b is:", type(b))
c=int(b)
if a<c:
    print("a is greater than c")
else:
    print("c is greater than a")

print("the average of a and c is:", (a+c)/2)
print("square of a is:", a**2)

    



    