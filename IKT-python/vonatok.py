"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""

def kilepes():
    with open('bbHelyek.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()  
    with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()
    with open('bdHelyek.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()  
    with open('bdHelyekMasolat.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()
    with open('bszHelyek.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()  
    with open('bszHelyekMasolat.txt', 'w', encoding='utf-8') as torlofajl:
                        for i in range(12):
                            for j in range(5):
                                if(j == 4):
                                    print(i+1, end="", file = torlofajl)
                                else:
                                    print('0', end =";", file = torlofajl)
                            print('', file = torlofajl)
                        torlofajl.close()
        
def jegyfoglalas():
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat+")
        return False
    jegyekSzama=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    ulesSzama=int(input("Adja meg a foglalni kívánt ülés számát(1-4):"))
    sorSzama=int(input("Adja meg a foglalni kívánt üléssor számát:"))
    if jegyekSzama > 0 and sorSzama > 0:
        for i in range(1):
            if vonat=="bb":
                sor = sorSzama
                helySzukseg = jegyekSzama
                uloszam = ulesSzama
                helySzama = 1
                foglalthelySor = 0
                foglalthelyOszlop = 0
                print("A jegyfoglalás előtti helyek: ")
                with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                bblista = []
                with open('bbHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
                    for sorok in forrasfajl:
                        adatok = sorok.strip().split(";")
                        bblista.append(adatok)
                    with open('bbHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
                        for i in range(12):
                            for j in range(5):
                                if(helySzukseg > 1 and  helySzukseg < 5 and i == (sor-1) and j == (uloszam-1)):
                                    while(helySzukseg > 0):
                                            helySzukseg-=1
                                            print('X', end = ';', file = kifajl)
                                elif(i == (sor-1) and j == (uloszam-1) and bblista[i][j] != "1"):
                                    print('X', end=";", file = kifajl)
                                elif(j == 4):
                                    print(i+1, end ="", file = kifajl)
                                elif(bblista[i][j] == "1" and j !=4):
                                    print('X', end=";", file = kifajl)
                                else:
                                    print('0', end = ';', file = kifajl)
                            print('', file = kifajl)
                        kifajl.close()    
                with open('bbHelyekMasolat.txt','r') as elsofajl, open('bbHelyek.txt','w') as masodikfajl:
                    for elem in elsofajl:
                        masodikfajl.write(elem)
                print("A jegyfoglalás utáni helyek: ")
                with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                print()
            elif vonat=="bd":
                sor = sorSzama
                helySzukseg = jegyekSzama
                uloszam = ulesSzama
                helySzama = 1
                foglalthelySor = 0
                foglalthelyOszlop = 0
                print("A jegyfoglalás előtti helyek: ")
                with open('bbHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                bdlista = []
                with open('bdHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
                    for sorok in forrasfajl:
                        adatok = sorok.strip().split(";")
                        bdlista.append(adatok)
                    with open('bdHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
                        for i in range(12):
                            for j in range(5):
                                if(helySzukseg > 1 and  helySzukseg < 5 and i == (sor-1) and j == (uloszam-1)):
                                    while(helySzukseg > 0):
                                            helySzukseg-=1
                                            print('X', end = ';', file = kifajl)
                                elif(i == (sor-1) and j == (uloszam-1) and bdlista[i][j] != "1"):
                                    print('X', end=";", file = kifajl)
                                elif(j == 4):
                                    print(i+1, end ="", file = kifajl)
                                elif(bdlista[i][j] == "1" and j !=4):
                                    print('X', end=";", file = kifajl)
                                else:
                                    print('0', end = ';', file = kifajl)
                            print('', file = kifajl)
                        kifajl.close()    
                with open('bdHelyekMasolat.txt','r') as elsofajl, open('bbHelyek.txt','w') as masodikfajl:
                    for elem in elsofajl:
                        masodikfajl.write(elem)
                print("A jegyfoglalás utáni helyek: ")
                with open('bdHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                print()

            else: 
                sor = sorSzama
                helySzukseg = jegyekSzama
                uloszam = ulesSzama
                helySzama = 1
                foglalthelySor = 0
                foglalthelyOszlop = 0
                print("A jegyfoglalás előtti helyek: ")
                with open('bszHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                bszlista = []
                with open('bszHelyek.txt', 'r', encoding='utf-8') as forrasfajl:
                    for sorok in forrasfajl:
                        adatok = sorok.strip().split(";")
                        bszlista.append(adatok)
                    with open('bszHelyekMasolat.txt', 'w', encoding='utf-8') as kifajl:
                        for i in range(12):
                            for j in range(5):
                                if(helySzukseg > 1 and  helySzukseg < 5 and i == (sor-1) and j == (uloszam-1)):
                                    while(helySzukseg > 0):
                                            helySzukseg-=1
                                            print('X', end = ';', file = kifajl)
                                elif(i == (sor-1) and j == (uloszam-1) and bszlista[i][j] != "1"):
                                    print('X', end=";", file = kifajl)
                                elif(j == 4):
                                    print(i+1, end ="", file = kifajl)
                                elif(bszlista[i][j] == "1" and j !=4):
                                    print('X', end=";", file = kifajl)
                                else:
                                    print('0', end = ';', file = kifajl)
                            print('', file = kifajl)
                        kifajl.close()    
                with open('bszHelyekMasolat.txt','r') as elsofajl, open('bbHelyek.txt','w') as masodikfajl:
                    for elem in elsofajl:
                        masodikfajl.write(elem)
                print("A jegyfoglalás utáni helyek: ")
                with open('bszHelyekMasolat.txt', 'r', encoding='utf-8') as forrasfajl:
                    for elem in forrasfajl:
                        print(elem)                            
                print()

                print()
       
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

if opcio =="kilepes":
    kilepes()
