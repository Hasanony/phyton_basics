# check type of variable assigned using input() function.

a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
c=int(b)
if a.isdigit():
    a = int(a)
elif a.replace(".", "", 1).isdigit():
    a = float(a)

t = type(a)
print("The type of variable a is:", t)


if a<c:
    print("a is greater than c")
else:
    print("c is greater than a")

print("the average of a and c is:", (a+c)/2)
print("square of a is:", a**2)

    



    