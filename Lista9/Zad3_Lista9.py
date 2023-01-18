import math
import numpy
import matplotlib.pyplot as plt
v0=float(input("Podaj prędkość początkową obiektu: "))
a=int(input("Podaj kąt pod którym zostanie rzucony obiekt: "))
vy=v0*math.sin(a)
vx=v0*math.cos(a)
g=9.81
czaslotu=float((2*v0*math.sin(a))/g)
czas=numpy.arange(0,czaslotu,0.01)
poy = (vy*czas)-((g*(czas*czas))/2)
pox = vx*czas
czaswznoszenia=vy/g
hmax=(vy*czaswznoszenia)-((g*(czaswznoszenia*czaswznoszenia))/2)
zasieg=vx*czaslotu
vypr=(vy-g*czas)*(vy-g*czas)
vwt=numpy.sqrt(vypr+(vx*vx))
print("Odpowiedzi:","\n","Ciało wzniesie się do ",hmax," metrów nad ziemię","\n","Zasięg rzutu wynosi: ",zasieg," metrów","\n","Czas lotu wynosi: ",czaslotu," sekund","\n")
"""
plt.plot(czas,vwt)
plt.xlabel('t[s]')
plt.ylabel('v[m/s]')
plt.title("Wykres prędkości od czasu")
plt.show()

plt.plot(pox,poy)
plt.xlabel('s[m]')
plt.ylabel('h[m]')
plt.title("Trajektoria lotu obiektu")
plt.show()

plt.plot(czas,poy)
plt.xlabel('s[m]')
plt.ylabel('h[m]')
plt.title("Wykres wysokości od czasu")
plt.show()
"""

fig, (ax1,ax2,ax3) = plt.subplots(3)



fig, (ax1,ax2,ax3) = plt.subplots(3)
ax1.plot(czas,vwt)
ax1.set_title('Wykres prędkości od czasu')
ax2.plot(pox,poy)
ax2.set_title('Trajektoria lotu obiektu')
ax3.plot(czas,poy)
ax3.set_title('Wykres wysokości od czasu')

plt.show()
