# a=first_value if condition else second_value
a, b = 50, 100
z = a if a < b else b 
print(z) 

a = 6.7
b = 7.9
c = a if a > b else b
print (c)

l1 = [3,4,5,8,78]
l2 = [3,5,8,9,12]
l = l1 if l1 < l2 else l2
print(l)

t1 = (3,4,5,8,78)
t2 = (3,5,8,9,12)
t = t1 if t1 < t2 else t2
print(t)

s1 = {3,5,8,9,12}
s2 = {3,4,5,8,78}
s = s1 if s1 < s2 else s2
print(s)
