import random
import sys
chislo=input("Please enter the number ot 1-5!")
if chislo in ['1','2','3','4','5']:
	pass
else:
    print("not numbers")
    sys.exit()
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
