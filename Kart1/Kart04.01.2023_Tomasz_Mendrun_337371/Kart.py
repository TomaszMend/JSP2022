with open('payload_337371.txt', 'r',encoding='utf-8') as file:
    data = file.read()
def deszyfr(tekst):
	lista={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
	list={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
	for x in range(1,26):
    		tek=""
    		for i in range(0,len(tekst)):
    			if tekst[i] in "!@#$%^&*()_+-=[]{};':,./<>?1234567890ĄąŚśĆćĘęóÓŁłżŻźŹńŃ " or tekst[i] in "\n" or tekst[i] in "—":
    				tek=tek+tekst[i]
    			elif list[tekst[i].upper()]-x<0:
    				p=26+list[tekst[i].upper()]-x
    				if tekst[i].isupper():
    					tek=tek+lista[p].upper()
    				elif tekst[i].islower():
    					tek=tek+lista[p].lower()
    			else:
    				if tekst[i].isupper():
    					tek=tek+lista[list[tekst[i]]-x].upper()
    				elif tekst[i].islower():
    					tek=tek+lista[list[tekst[i].upper()]-x].lower()
    			if "Tomasz" in tek and "Mendruń" in tek and "337371" in tek:
    				tupl = str(x) , tek
    				return tupl;
	return tek;
with open('hacked_337371.txt', 'w') as f:
    f.write(deszyfr(data)[1])
    f.write("\n")
    f.write(deszyfr(data)[0])
    f.write(" to liczba przesunięcia szyfrująca")

