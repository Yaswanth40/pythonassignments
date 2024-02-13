t=(20,30,40,50,60,20,30,10,30)
a=t.count(30)
print(a)
#3

t=(20,30,40,50,60,20,30,10,30)
a=t.count(300)
print(a)
# 0 (300 value is not in my tuple but output will be get zero)

t=("Jan", "Feb", "Mar", "Apr", "Jan", "Jan",)
a=t.count("Jan")
print(a)
#3

t=("Jan", "Feb", "Mar", "Apr", "Jan", "Jan",)
a=t.count("Jun")
print(a)
#0