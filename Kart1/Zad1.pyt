#wygeneruj liczby od 3 do 100 co 3 (3,6,...,99), 
#oblicz sumę tych liczb,
#Oblicz średnią tych liczb,
#funkcjje: sum, range, print
import math
print("Liczby od 3 do 100 co 3")
print([a for a in range(3,100, 3)])
print("Suma")
print(sum([a for a in range(0,100, 3)]))
print("Średnia arytmetyczna")
print(sum([a for a in range(0,100, 3)])/33)
