
s="Its a february month"
a=s.split()
print(a)
# output will be in list type i.e; ['Its', 'a', 'february', 'momth']

for i in a:
    print(i, end=" ")
    #Its a february month 

s="Its a february month"
a=s.split("r")
print(a)
#['Its a feb', 'ua', 'y month']

s="Its a february-month"
a=s.split("-")
print(a)
#['Its a february', 'month']