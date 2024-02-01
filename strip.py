#strip()

city=input("enter the city name ")
list=["Tirupathi", "Hyderabad", "Banglore","Chennai"]

if city.strip() in list:
    print("Yes it is available.")

else:
    print(city, "Not available.")



Mobile=input("enter the mobile name ")
Store=["Samsung", "Realme", "Vivo"," Redmi", "Oppo"]

if Mobile.strip() in Store:
    print("Yes it is available.")

else:
    print(Mobile, "Not available.")
