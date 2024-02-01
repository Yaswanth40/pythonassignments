str = "Today is a Thrusday"

for i in range(len(str)):
    print("Character at position", i, ":", str[i])


str = "Today is a Thrusday"

for i in range(-1, -len(str) -1, -1):
    print("Character at position", i, ":", str[i])
    

s="hello people"
a=len(s)
for i in range(a):
    print("the char present in the +ve index is ",i, "is",s[i], "and -ve index is ",i-a)

s="hello people"
a=0
for i in s:
    print("the char present in the +ve index is ",a, "is",i, "and -ve index is ",a-len(s))
    a+=1

    