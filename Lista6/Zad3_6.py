n=int(input("Jak dużo razy powtórzyć 'look-and-say': "))
look="1"
print(look)
for i in range(0,n):
    x=""
    if look.count("9")>0:
        x=x+str(look.count("9"))+"9"
    if look.count("8")>0:
        x=x+str(look.count("8"))+"8"
    if look.count("7")>0:
        x=x+str(look.count("7"))+"7"
    if look.count("6")>0:
        x=x+str(look.count("6"))+"6"
    if look.count("5")>0:
        x=x+str(look.count("5"))+"5"
    if look.count("4")>0:
        x=x+str(look.count("4"))+"4"
    if look.count("3")>0:
        x=x+str(look.count("3"))+"3"
    if look.count("2")>0:
        x=x+str(look.count("2"))+"2"
    if look.count("1")>0:
        x=x+str(look.count("1"))+"1"
    print(x)
    look=x

