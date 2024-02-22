"""
def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result
 
print(sum_all(1, 2, 3, 4, 5))
"""
def sum(*a):
    result=0
    for x in a:
        result=result+x
        print(result)
sum(10,20,30,40,50,60)