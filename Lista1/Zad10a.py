import cmath
z=int(input())
s=complex(cmath.sin(z))
c=complex(cmath.cos(z))

print(s)
print(c)

print("Dodaje sin^2(z) do cos^2(z)")
if (s**2 + c**2 == 1):
    print(s**2 + c**2)
    print("sin^2(z) do cos^2(z) wynosi 1")
else:
    print("Nope! It ain't working.")