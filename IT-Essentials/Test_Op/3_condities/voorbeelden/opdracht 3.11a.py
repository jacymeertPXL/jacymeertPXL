burgerlijke_staat = int(input("geef bs in (1= ongehuwd, 2 = gehuwd, 3= weduwe(naar) "))
leeftijd = int(input("geef de leeftijd in"))
# ongehuwd 25 gehuwd 20 weduwe(naar) 15

if burgerlijke_staat == 1:
    lidgeld = 25
elif burgerlijke_staat == 2:
    lidgeld = 20
else:
    lidgeld = 25
print("lidgeld = ", lidgeld)
