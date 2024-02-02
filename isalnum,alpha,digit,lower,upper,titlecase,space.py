#isalnum()
s="the price of SAMSUNG galaxy s225G is 40000 rupees"
print(s.isalnum())# giving space- output is false.

s="thepriceofSAMSUNGgalaxys225Gis40000rupees"
print(s.isalnum())# without give any space - output is True.


#isalpha()
s="the price of SAMSUNG galaxy s225G is 40000 rupees"
print(s.isalpha())#False

s="thepriceofSAMSUNGgalaxyisfourtythousandrupees"
print(s.isalpha())#True

s="the price of SAMSUNG galaxy is fourty thousand rupees"
print(s.isalpha())#false because of giving space


#isdigit()
s="the price of SAMSUNG galaxy s225G is 40000 rupees"
print(s.isdigit())#False

s="2024"
print(s.isdigit())#True


#islower()
s="this is a february MONTH"
print(s.islower())#False

s="this is a february month"
print(s.islower())#True

#isupper()
s="this is a february MONTH"
print(s.isupper())#False

s="THIS IS A FEBRUARY MONTH"
print(s.isupper())


#istitle()
s="this is a february month"
print(s.istitle())#False

s="THIS IS A FEBRUARY MONTH"
print(s.istitle())# false

s="This Is A Februaury Month"
print(s.istitle())#True


#isspace()
s="ThisIsAFebruauryMonth"
print(s.isspace())#False

s="This Is A Februaury Month"
print(s.isspace())#False

s="In February 28 days"
print(s.isspace())#False

s="10 20"
print(s.isspace())#False

s=" monday "
print(s.isspace())#false

s = " "
print(s.isspace())#True
