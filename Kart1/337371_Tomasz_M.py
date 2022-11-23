#Napisz funkcje która w tekście zastąpi wszystkie nazwiska ich pierwszą literą i .
#nazwiska możliwe Nowak Kowalski Kowal
#Adam Kowal i Marek Nowak zostali skazani
zdanie="Adam Kowal i Marek Nowak zostali skazani"
print(zdanie)

lista=["Nowak","Kowalski","Kowal"]
Nowak=zdanie.replace("Nowak","N.")
Kowal=Nowak.replace("Kowal","K.")
Kowalski=Kowal.replace("Kowalski","K.")


print(Kowalski)
