j = [1,2,3,4,5,6,7,8,9,10]
x = []
for i in range(1,11):
	print("Podaj liczbę całkowitą do tabliczki mnożenia poraz " , i , " maksymalnie do 10 :")
	x[i] = int(input(""))
print("\t",j)
for i in range(1,11):
	print(x[i], end = '')
	for k in range(10) :
		print("\t", x[i]*j[k], end = '')
	print("")
