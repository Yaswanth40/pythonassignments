s="Today is a friday"
#len(s)=17
a=s.find("friday")
print(a)
#11

s="Today is a friday"
#len(s)=17
a=s.find("y",1,17)
print(a)
#4

s="Today is a friday"
#len(s)=17
a=s.find("d",2,16)
print(a)
#2

s="Today is a friday"
#len(s)=17
a=s.find("monday")
print(a)
#-1

s="Today is a friday"
#len(s)=17
a=s.rfind("a")
print(a)
#15 it shows latest position