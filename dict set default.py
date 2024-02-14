d={10:"Ten",40:"Fourty",80:"Eighty"}
print(d.setdefault(20,"Twenty"))
print(d)


d={"Month":"Feb","Year":2024,"Day":"Tuesday"}
print(d.setdefault("month","March"))
print(d)
