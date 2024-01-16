l1=[2,9,6]
l2=[9,5,8]
l=(l1==l2)
print(l)


l1=[2,9,6]
l2=[2,9,6]
l=(l1!=l2)
print(id(l1),id(l2))
print(l)
#id is diff, so output is false


t=23
p=67
q=t>p
print(q)


t=23
p=67
q=t<p
print(q)

a=786
b=237
c=(a>=b)
print(c)


a=7.86
b=2.37
c=(a<=b)
print(c)
