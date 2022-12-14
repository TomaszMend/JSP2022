import math
def f(number, meter):
	if meter == "mm":
		number=number/1000
	elif meter == "cm":
		number=number/100
	elif meter == "m":
		number=number
	strret = str(math.pi*number*number)+" m^2"
	return strret
		
		
		
meter=input("podaj jednostkę (m dla metrów, cm dla centymetrów, mm dla milimetrów): ")
number=float(input("podaj liczbę: "))
print(f(number, meter))

