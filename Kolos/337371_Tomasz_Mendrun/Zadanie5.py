def f(string):
	samo=["a","e","i","o","u","y","ą","ę"]
	suma=0
	ilosc=0
	for x in range(len(string)):
		if string[x].lower() in samo:
			ilosc=ilosc+1
	if ilosc%2==0:
		suma=suma+2
	elif ilosc%2==1:
		suma=suma+1
	return suma
def fun(string):
	sumasuma=0
	lastx=0
	for x in range(len(string)):
		if string[x]==" ":
			sumasuma=sumasuma+f(string[lastx:x])
			lastx=x+1
		if x==len(string)-1:
			f(string[lastx:x])
			sumasuma=sumasuma+f(string[lastx:x])
	return sumasuma










string=str(input("Podaj zdanie/słowo: "))
print("To zdanie/słowo ma ",fun(string)," punkt/y/ów")
