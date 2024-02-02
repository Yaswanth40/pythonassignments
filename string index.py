s="today is a thrusday"
#len(s)=19
a=s.index("is")
print(a)
#6


s="today is a thrusday"
#len(s)=19
a=s.index("today")
print(a)
#0


s="today is a thrusday"
#len(s)=19
a=s.index("a")
print(a)
#3

s="today is a thrusday"
#len(s)=19
a=s.index("t",5,19)
print(a)
#11

s="today is a thrusday"
#len(s)=19
a=s.rindex("a")
print(a)
#17

s="today is a thrusday"
#len(s)=19
a=s.index("monday")
print(a)
#error