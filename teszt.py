"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""
sor = 1
oszlop = 2
sorokSzama = 0
print("A jelenlegi helyek: ")
with open('bbHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
    for elem in forrasfajl:
        print(elem)
        sorokSzama+=1
print()
with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
        for i in range(1, (sorokSzama+1)):
            for j in range(1, 5):
                if(i == sor and j == oszlop):
                    print('1', end = ';', file = kifajl)
                
                else:
                    print('0', end = ';', file = kifajl)
        kifajl.close()

print("A szabadon maradt helyek: ")
with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
    for elem in forrasfajl:
        print(elem)
print()
