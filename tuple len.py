t=(20,30,40,50,60,20,30,10,30)
print(t,len(t),type(t))

t=(20,)
print(type(t),len(t))

t=()
print(type(t),len(t))

t=30,40,10,50
print(t,type(t))

t=30,40,10,50,90,
print(t,type(t))

t=(20,30,40,50,60,20,30,)
print(t,len(t),type(t))


t=("Jan", "Feb", "Mar",)
print(type(t),len(t),t)


t=("Jan", 31, "Feb", 28, "Mar", 31)
print(type(t),len(t),t)

t=tuple(["Jan", "Feb", "Mar"])
print(t,type(t),len(t))