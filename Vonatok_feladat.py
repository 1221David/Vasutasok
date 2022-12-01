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
p=[]
szo=[]
v=[]

hbb=[]
hbd=[]
hbsz=[]

kbb=[]
kbd=[]
kbsz=[]

szebb=[]
szebd=[]
szebsz=[]

csbb=[]
csbd=[]
csbsz=[]

pbb=[]
pbd=[]
pbsz=[]

szobb=[]
szobd=[]
szobsz=[]

vbb=[]
vbd=[]
vbsz=[]

def jegyfoglalas():
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat+")
        return False
        
    nap=input("Adja meg melyik napon szeretne utazni: (h, k, sze, cs, p, szo, v):")    
    if nap not in ["h", "k", "sze", "cs", "p", "szo", "v"]:
        print("Nincs ilyen nap")
        return False     
    
    foglalas=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    if foglalas>0:
        for i in range(foglalas):
            if vonat=="bb" and nap=="h":
                if (foglalas+len(hbb))<=144:
                    bb.append(1)
                    hbb.append(1)
                    h.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="k":
                if (foglalas+len(kbb))<=144:
                    bb.append(1)
                    kbb.append(1)
                    k.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="sze":
                if (foglalas+len(szebb))<=144:
                    bb.append(1)
                    szebb.append(1)
                    sze.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="cs":
                if (foglalas+len(csbb))<=144:
                    bb.append(1)
                    csbb.append(1)
                    cs.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="p":
                if (foglalas+len(pbb))<=144:
                    bb.append(1)
                    pbb.append(1)
                    p.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="szo":
                if (foglalas+len(szobb))<=144:
                    bb.append(1)
                    szobb.append(1)
                    szo.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            if vonat=="bb" and nap=="v":
                if (foglalas+len(vbb))<=144:
                    bb.append(1)
                    vbb.append(1)
                    v.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False       

            elif vonat=="bd" and nap=="h":
                if (foglalas+len(hbd))<=144:
                    bd.append(1)
                    hbd.append(1)
                    h.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="k":
                if (foglalas+len(kbd))<=144:
                    bd.append(1)
                    kbd.append(1)
                    k.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="sze":
                if (foglalas+len(szebd))<=144:
                    bd.append(1)
                    szebd.append(1)
                    sze.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="cs":
                if (foglalas+len(csbd))<=144:
                    bd.append(1)
                    csbd.append(1)
                    cs.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="p":
                if (foglalas+len(pbd))<=144:
                    bd.append(1)
                    pbd.append(1)
                    p.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="szo":
                if (foglalas+len(szobd))<=144:
                    bd.append(1)
                    szobd.append(1)
                    szo.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="v":
                if (foglalas+len(vbd))<=144:
                    bd.append(1)
                    vbd.append(1)
                    v.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bsz" and nap=="h":
                if (foglalas+len(hbsz))<=144:
                    bsz.append(1)
                    hbsz.append(1)
                    h.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="k":
                if (foglalas+len(kbsz))<=144:
                    bsz.append(1)
                    kbsz.append(1)
                    k.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="sze":
                if (foglalas+len(szebsz))<=144:
                    bsz.append(1)
                    szebsz.append(1)
                    sze.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="cs":
                if (foglalas+len(csbsz))<=144:
                    bsz.append(1)
                    csbsz.append(1)
                    cs.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="p":
                if (foglalas+len(pbsz))<=144:
                    bsz.append(1)
                    pbsz.append(1)
                    p.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="szo":
                if (foglalas+len(szobsz))<=144:
                    bsz.append(1)
                    szobsz.append(1)
                    szo.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="v":
                if (foglalas+len(vbsz))<=144:
                    bsz.append(1)
                    vbsz.append(1)
                    v.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
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

