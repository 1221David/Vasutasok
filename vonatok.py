"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""

def jegyfoglalas():
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat+")
        return False
    jegyekSzama=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    sorSzama=int(input("Adja meg a foglalni kívánt üléssor számát:"))
    if jegyekSzama > 0 and sorSzama > 0:
        for i in range(1):
            if vonat=="bb":
                sor = sorSzama
                helySzukseg = jegyekSzama
                sorokSzama = 0
                foglalthelySor = 0
                foglalthelyOszlop = 0
                print("A jegyfoglalas elotti helyek: ")
                with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)
                        sorokSzama+=1
                    for i in range(1, (sorokSzama+1)):
                        for j in range(1, 5):
                            if(j =="1"):
                                foglalthelySor = i
                                foglalthelyOszlop = j
                            
                print()
                with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
                    for i in range(1, (sorokSzama+1)):
                        for j in range(1, 5):
                                    if(i == sor and helySzukseg > 0):
                                            print('1', end = ';', file = kifajl)
                                            helySzukseg -=1
                                    elif(i==foglalthelySor and j==foglalthelyOszlop):
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
            elif vonat=="bd":
                bd.append(1)
            else: 
                bsz.append(1)        
    else:
        print("Ervenytelen jegy mennyiseg!")
        return False

    print("Köszönjük a foglalást")
    return True    



def bevetel():
    elemszam=len(bb)+len(bd)+len(bsz)
    print(elemszam*4000)

opcio=None

while opcio!="kilepes":
    print ("jegyfoglalas","bevetel","kilepes")
    opcio=input("adja meg a menupontot!")

    if opcio=="jegyfoglalas":
        jegyfoglalas()
    elif opcio=="bevetel":
        bevetel()
