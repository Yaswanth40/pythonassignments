def my_function(name="Suresh"):
    print("hello",name," how are you")

my_function()

def my_function(name,age=25, city="Chennai"):
    print(f"{name} is {age} years old and belongs to {city}.")

my_function("Rajesh")
my_function("Suresh",35)
my_function("Raju", city="Hyderabad")

