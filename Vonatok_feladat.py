"""Van 3 vonat, mindegyik vonaton naponta 3x közlekedik.
Mindegyik vonaton van 12 darab 4 személyes asztal.
Egy darab vonatjegy 4000 Forint
1. feladat, lehessen foglalni és ezt kiíratni
2. feladat, mennyi volt a napi bevétel, (vonatonként)
szempontok: függvényekben dolgozni, fájlból olvasson be, fájlba írjon ki
"""
    #listak
#vonatok
bb=[]
bd=[]
bsz=[]
#napszakok
de=[]
d=[]
du=[]
#delelotti vonatok
debb=[]
debd=[]
debsz=[]
#delii vonatok
dbb=[]
dbd=[]
dbsz=[]
#delutani vonatok
dubb=[]
dubd=[]
dubsz=[]

#jegyfoglalas fuggveny
def jegyfoglalas():
    #vonat lekerdezes
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat")
        return False
    #napszak lekerdezes
    napszak=input("Adja meg melyik napon szeretne utazni: (de, d, du):")    
    if napszak not in ["de", "d", "du"]:
        print("Nincs ilyen napszak")
        return False     
    #jegy mennyiseg lekerdezes
    foglalas=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    if foglalas>0:
        for i in range(foglalas):
#budapest-becsi vonatok de-du
            if vonat=="bb" and napszak=="de":
                if (foglalas+len(debb))<=48:
                    bb.append(1)
                    debb.append(1)
                    de.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and napszak=="d":
                if (foglalas+len(dbb))<=48:
                    bb.append(1)
                    dbb.append(1)
                    d.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and napszak=="du":
                if (foglalas+len(dubb))<=48:
                    bb.append(1)
                    dubb.append(1)
                    du.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            
#budapest-debreceni de-du
            elif vonat=="bd" and napszak=="de":
                if (foglalas+len(debd))<=48:
                    bd.append(1)
                    debd.append(1)
                    de.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and napszak=="d":
                if (foglalas+len(dbd))<=48:
                    bd.append(1)
                    dbd.append(1)
                    d.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and napszak=="du":
                if (foglalas+len(dubd))<=48:
                    bd.append(1)
                    dubd.append(1)
                    du.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
#budapest-szegedi vonatok de-du
            elif vonat=="bsz" and napszak=="de":
                if (foglalas+len(debsz))<=48:
                    bsz.append(1)
                    debsz.append(1)
                    de.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and napszak=="d":
                if (foglalas+len(dbsz))<=48:
                    bsz.append(1)
                    dbsz.append(1)
                    d.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and napszak=="du":
                if (foglalas+len(dubsz))<=48:
                    bsz.append(1)
                    dubsz.append(1)
                    du.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
    else:
        print("Ervenytelen jegy mennyiseg!")
        return False

    print("Köszönjük a foglalást")
    return True    

        
#bevetel szamito fuggveny
def bevetel():
    elemszam=len(bb)+len(bd)+len(bsz)
    print(elemszam*4000)

def beveteldelelott():
    delelott=len(de)
    print(delelott*4000)

def beveteldel():
    delben=len(d)
    print(delben*4000)

def beveteldelutan():
    delutan=len(de)
    print(delutan*4000)

def bevetelbecsi():
    becsi=len(bb)
    print(becsi*4000)

def beveteldebreceni():
    debreceni=len(bd)
    print(debreceni*4000)

def bevetelszegedi():
    szegedi=len(bsz)
    print(szegedi*4000)

#MENU
opcio=None
while opcio!="kilepes":
    print ("jegyfoglalas","bevetel","kilepes")
    opcio=input("adja meg a menupontot!")

    if opcio=="jegyfoglalas":
        jegyfoglalas()
    elif opcio=="bevetel":
        print("napszak", "vonat")
        opcio=input("adja meg hogy napszak vagy vonat")
        if opcio=="napszak":
            print("de", "d", "du")
            opcio=input("adja meg a napszakot!")
            if opcio==("ossz"):
                bevetel()
            elif opcio==("de"):
                beveteldelelott()
            elif opcio==("d"):
                beveteldel()
            else:
                beveteldelutan()
        else:
            print("bb", "bd", "bsz")
            opcio=input("Adja meg a vonatot")
            if opcio==("bb"):
                bevetelbecsi()
            elif opcio==("bd"):
                beveteldebreceni()
            else:
                bevetelszegedi()

            


