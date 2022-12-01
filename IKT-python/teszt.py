"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""
'''
sor = 1
oszlop = 2
'''
'''
print("A jelenlegi helyek: ")
with open('bbHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
    for elem in forrasfajl:
        print(elem)
        sorokSzama+=1
print()
with open('bbHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
    with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
            for i in range(1, (sorokSzama+1)):
                for j in range(1, 5):
                    if(i == sor and j == oszlop):
                        print('1', end = ';', file = kifajl)
                
                    else:
                        print('0', end = ';', file = kifajl)
                print('\t', file = kifajl)
            kifajl.close()

print("A szabadon maradt helyek: ")
with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
    for elem in forrasfajl:
        print(elem)
print()
'''
def fajlbairas(sor, oszlop):
    bblista = []
    with open('bbHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
        for sorok in forrasfajl:
            adatok = sorok.strip().split(";")
            bblista.append(adatok)
        with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
            for i in range(12):
                for j in range(5):
                    if(i == (sor-1) and j == (oszlop-1)):
                        print('1', end = ';', file = kifajl)
                    elif(j == 4):
                        print(i+1, end=" ", file = kifajl)
                    elif(bblista[i][j] == "1"):
                        print('1', end=";", file = kifajl)
                    else:
                        print('0', end = ';', file = kifajl)
                print('', file = kifajl)
            kifajl.close()    
    with open('bbHelyekMasolat.txt','r') as elsofajl, open('bbHelyek.txt','w') as masodikfajl:
        for elem in elsofajl:
            masodikfajl.write(elem)
fajlbairas(1, 2)
fajlbairas(1, 3)
fajlbairas(3,2)
