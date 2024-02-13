t=(20,30,40,50,60,20,30,10,30)
a=t.index(30)
print(a)
#1

t=(20,30,40,50,60,20,30,10,30)
a=t.index(300)
print(a)
#0

t=("Jan", "Feb", "Mar", "Apr", "Jan", "Jan",)
a=t.index("Jun")
print(a)
#0


t=("Jan", "Feb", "Mar", "Apr", "Jan", "Jan",)
a=t.index("Jan")
print(a)
#3

