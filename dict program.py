d1=int(input("Enter the number of students: "))
d={}

for i in range(d1):
    print("Enter the details of student no.", i+1)
    rno=int(input("roll no:"))
    name=input("name: ")
    marks=int(input("marks: "))
    d[rno]=[name,marks]
    print(d)
