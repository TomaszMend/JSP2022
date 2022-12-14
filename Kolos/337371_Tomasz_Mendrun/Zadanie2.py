A=(1,2,{"jeden":"1","dwa":"2"})
A[2]["jeden"]=1
for x in range(1,98):
	A[2]["jeden"]=1+(A[2]["jeden"]*10)
	print(x)
print(A[2]["jeden"])
