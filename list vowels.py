
vowels = ['a', 'e', 'i', 'o', 'u']

for i in vowels:
    print(i)


L = input("Enter any name : ")
vowels =['a','e','i','o','u']
list=[]
for x in L:
    if (x in vowels and x not in list):
        list.append(x)

print("Vowels present in given name : ",list)
#yaswanthyeshcallingyou
#Vowels present in given name :  ['a', 'e', 'i', 'o', 'u']
