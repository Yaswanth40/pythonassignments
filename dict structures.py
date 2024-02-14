d={}
print(type(d))

d=dict()
print(type(d))

d={}
d[31]="Jan"
d[28]="Feb"
d[31]="Mar"
print(d)

print(d[31])
print(d[28])
print(d[31])

d1=((31,"Jan"),(28,"Feb"),(31,"Mar"))
d=dict(d1)
print(d)

d2=([31,"Jan"], [28,"Feb"], [31,"Mar"])
d=dict(d2)
print(d)

d3=[{31,"Jan"}, {28,"Feb"}, {31,"Mar"}]
d=dict(d3)
print(d)
