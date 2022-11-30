#Napisz funkcję która bierze sekwencje s="GTACAGTA" i przeprowadza ją na (A na T| C na G| T na A| G na C) i odrwaca kolejność
import re
def DNA(x):
	klucz = {"A":"T", "C": "G", "T":"A","G":"C"}
	for i in range(0,len(x)):
		if (x[i] in klucz) :
			for i in range(0,len(x)):
				c[len(x)-i]=klucz[x[i]]
			"".join(c)
		else:
			print("Wrong")
			c=[]
			return c
			
	return c
    
DNA("AACTG")
DNA("RRATAS")
