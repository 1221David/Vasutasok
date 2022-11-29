"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""

bb=[]
bd=[]
bsz=[]

h=[]
k=[]
sze=[]
cs=[]
pentek=[]
szo=[]
v=[]


def jegyfoglalas():
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat+")
        return False
    
    foglalas=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    if foglalas>0:
        for i in range(foglalas):
            if vonat=="bb":
                bb.append(1)
            elif vonat=="bd":
                bd.append(1)
            else: 
                bsz.append(1) 
    nap=input("Adja meg melyik napon szeretne utazni: (h, k, sze, cs, p, szo, v):")    
    if nap not in ["h", "k", "sze", "cs", "p", "szo", "v"]:
        print("Nincs ilyen nap")
        return False             
    if foglalas>0:
        if nap=="h":
            h.append(1)
        elif nap=="k":
            k.append(1)
        elif nap=="sze":
            sze.append(1)
        elif nap=="cs":
            cs.append(1)
        elif nap=="p":
            p.append(1)
        elif nap=="szo":
            szo.append(1)
        else:
            v.append(1)
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



