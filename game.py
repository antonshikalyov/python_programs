import random
chislo=input("Please enter the number ot 1-5!")
chislo=int(chislo)
vybor=random.randint(1, 5)
if  vybor >  chislo:
	print(vybor)
	print("Game over")
if  vybor ==  chislo:
	print("You vinner")
if  vybor <  chislo:
	print(vybor)
	print("Game over")
