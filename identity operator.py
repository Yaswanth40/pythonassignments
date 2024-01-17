# is

a = ["January","February","March"]
b = ["January","February","March"]
c = b

print(a is c)
print(a is b)
print(a == c)
print(type(a),type(b))

a = ("January","February","March")
b = ("January","February","March")
c = b

print(a is c)
print(a is b)
print(a == c)
print(type(a),type(b))


# is not

a=78
b=9.8
c=98
d=a=c


print(a is not b)
print(c is not b)
print(c != b)

a=["JAN","FEB","MAR"]
b=["JAN","FEB","MAR"]
c=a

print(a != b)
print(c is not a)
