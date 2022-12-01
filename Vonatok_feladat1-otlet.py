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
#napok
h=[]
k=[]
sze=[]
cs=[]
p=[]
szo=[]
v=[]
#napszakok
de=[]
d=[]
du=[]
    #hetfoi vonatok
#bb
hbb=[]
hbbde=[]
hbbd=[]
hbbdu=[]
#bd
hbd=[]
hbdde=[]
hbdd=[]
hbddu=[]
#bsz
hbsz=[]
hbszde=[]
hbszd=[]
hbszdu=[]
    #keddi vonatok
#bb
kbb=[]
kbbde=[]
kbbd=[]
kbbdu=[]
#bd
kbd=[]
kbdde=[]
kbdd=[]
kbddu=[]
#bsz
kbsz=[]
kbszde=[]
kbszd=[]
kbszdu=[]
    #szerdai vonatok
#bb
szebb=[]
szebbde=[]
szebbd=[]
szebbdu=[]
#bd
szebd=[]
szebdde=[]
szebdd=[]
szebddu=[]
#bsz
szebsz=[]
szebszde=[]
szebszd=[]
szebszdu=[]
    #csutortoki vonatok
#bb
csbb=[]
csbbde=[]
csbbd=[]
csbbdu=[]
#bd
csbd=[]
csbdde=[]
csbdd=[]
csbddu=[]
#bsz
csbsz=[]
csbszde=[]
csbszd=[]
csbszdu=[]
    #penteki vonatok
#bb
pbb=[]
pbbde=[]
pbbd=[]
pbbdu=[]
#bd
pbd=[]
pbdde=[]
pbdd=[]
pbddu=[]
#bsz
pbsz=[]
pbszde=[]
pbszd=[]
pbszdu=[]
    #szombati vonatok
#bb
szobb=[]
szobbde=[]
szobbd=[]
szobbdu=[]
#bd
szobd=[]
szobdde=[]
szobdd=[]
szobddu=[]
#bsz
szobsz=[]
szobszde=[]
szobszd=[]
szobszdu=[]
    #vasarnapi vonatok
#bb
vbb=[]
vbbde=[]
vbbd=[]
vbbdu=[]
#bd
vbd=[]
vbdde=[]
vbdd=[]
vbddu=[]
#bsz
vbsz=[]
vbszde=[]
vbszd=[]
vbszdu=[]
#jegyfoglalas fuggveny
def jegyfoglalas():
    #vonat lekerdezes
    vonat=input("Adja meg a vonatot (bb, bd, bsz):")
    if vonat not in ["bb","bd","bsz"]:
        print("Nincs ilyen vonat+")
        return False
    #nap lekerdezes
    nap=input("Adja meg melyik napon szeretne utazni: (h, k, sze, cs, p, szo, v):")    
    if nap not in ["h", "k", "sze", "cs", "p", "szo", "v"]:
        print("Nincs ilyen nap")
        return False
    napszak=input("Adja meg a napszakot (de, d, du):")
    if napszak not in ("de", "d", "du"):
        print ("Nincs ilyen napszak")
        return
    #jegy mennyiseg lekerdezes
    foglalas=int(input("Adja meg a foglalni kívánt jegyek számát:"))
    if foglalas>0:
        for i in range(foglalas):
            #budapest-becsi vonatok
#budapest-becsi vonatok hetfo
            if vonat=="bb" and nap=="h" and napszak=="de":
                if (foglalas+len(hbbde))<=48:
                    bb.append(1)
                    hbb.append(1)
                    h.append(1)
                    de.append(1)
                    hbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="h" and napszak=="d":
                if (foglalas+len(hbbd))<=48:
                    bb.append(1)
                    hbb.append(1)
                    h.append(1)
                    d.append(1)
                    hbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="h" and napszak=="du":
                if (foglalas+len(hbbdu))<=48:
                    bb.append(1)
                    hbb.append(1)
                    h.append(1)
                    du.append(1)
                    hbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok kedd
            elif vonat=="bb" and nap=="k" and napszak=="de":
                if (foglalas+len(kbbde))<=48:
                    bb.append(1)
                    kbb.append(1)
                    k.append(1)
                    de.append(1)
                    kbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="k" and napszak=="d":
                if (foglalas+len(kbbd))<=48:
                    bb.append(1)
                    kbb.append(1)
                    k.append(1)
                    d.append(1)
                    kbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="k" and napszak=="du":
                if (foglalas+len(kbbdu))<=48:
                    bb.append(1)
                    kbb.append(1)
                    k.append(1)
                    du.append(1)
                    kbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok szerda                
            elif vonat=="bb" and nap=="sze" and napszak=="de":
                if (foglalas+len(szebbde))<=48:
                    bb.append(1)
                    szebb.append(1)
                    sze.append(1)
                    de.append(1)
                    szebbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="sze" and napszak=="d":
                if (foglalas+len(szebbd))<=48:
                    bb.append(1)
                    szebb.append(1)
                    sze.append(1)
                    d.append(1)
                    szebbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="sze" and napszak=="du":
                if (foglalas+len(szebbdu))<=48:
                    bb.append(1)
                    szebb.append(1)
                    sze.append(1)
                    du.append(1)
                    szebbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok csutortok
            elif vonat=="bb" and nap=="cs" and napszak=="de":
                if (foglalas+len(csbbde))<=48:
                    bb.append(1)
                    csbb.append(1)
                    cs.append(1)
                    de.append(1)
                    csbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="cs" and napszak=="d":
                if (foglalas+len(csbbd))<=48:
                    bb.append(1)
                    csbb.append(1)
                    cs.append(1)
                    d.append(1)
                    csbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="cs" and napszak=="du":
                if (foglalas+len(csbbdu))<=48:
                    bb.append(1)
                    csbb.append(1)
                    cs.append(1)
                    du.append(1)
                    csbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok pentek
            elif vonat=="bb" and nap=="p" and napszak=="de":
                if (foglalas+len(pbbde))<=48:
                    bb.append(1)
                    pbb.append(1)
                    p.append(1)
                    de.append(1)
                    pbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="p" and napszak=="d":
                if (foglalas+len(pbbd))<=48:
                    bb.append(1)
                    pbb.append(1)
                    p.append(1)
                    d.append(1)
                    pbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="p" and napszak=="du":
                if (foglalas+len(pbbdu))<=48:
                    bb.append(1)
                    pbb.append(1)
                    p.append(1)
                    du.append(1)
                    pbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok szombat
            elif vonat=="bb" and nap=="szo" and napszak=="de":
                if (foglalas+len(szobbde))<=48:
                    bb.append(1)
                    szobb.append(1)
                    szo.append(1)
                    de.append(1)
                    szobbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="szo" and napszak=="d":
                if (foglalas+len(szobbd))<=48:
                    bb.append(1)
                    szobb.append(1)
                    szo.append(1)
                    d.append(1)
                    szobbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bb" and nap=="szo" and napszak=="du":
                if (foglalas+len(szobbdu))<=48:
                    bb.append(1)
                    szobb.append(1)
                    szo.append(1)
                    du.append(1)
                    szobbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-becsi vonatok vasarnap
            elif vonat=="bb" and nap=="v" and napszak =="de":
                if (foglalas+len(vbbde))<=48:
                    bb.append(1)
                    vbb.append(1)
                    v.append(1)
                    de.append(1)
                    vbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False       
            elif vonat=="bb" and nap=="v" and napszak =="d":
                if (foglalas+len(vbbd))<=48:
                    bb.append(1)
                    vbb.append(1)
                    v.append(1)
                    d.append(1)
                    vbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False       
            elif vonat=="bb" and nap=="v" and napszak =="du":
                if (foglalas+len(vbbdu))<=48:
                    bb.append(1)
                    vbb.append(1)
                    v.append(1)
                    du.append(1)
                    vbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False       
        #budapest-debreceni vonatok h-v
#budapest-debreceni vonatok hetfo
            elif vonat=="bd" and nap=="h" and napszak=="de":
                if (foglalas+len(hbdde))<=48:
                    bd.append(1)
                    hbd.append(1)
                    h.append(1)
                    de.append(1)
                    hbbde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bd" and nap=="h" and napszak=="d":
                if (foglalas+len(hbdd))<=48:
                    bd.append(1)
                    hbd.append(1)
                    h.append(1)
                    d.append(1)
                    hbbd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bd" and nap=="h" and napszak=="du":
                if (foglalas+len(hbddu))<=48:
                    bd.append(1)
                    hbd.append(1)
                    h.append(1)
                    du.append(1)
                    hbbdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest-debreceni vonatok kedd
            elif vonat=="bd" and nap=="k" and napszak=="de":
                if (foglalas+len(kbdde))<=48:
                    bd.append(1)
                    kbd.append(1)
                    k.append(1)
                    de.append(1)
                    kbdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="k" and napszak=="d":
                if (foglalas+len(kbdd))<=48:
                    bd.append(1)
                    kbd.append(1)
                    k.append(1)
                    d.append(1)
                    kbdd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="k" and napszak=="du":
                if (foglalas+len(kbddu))<=48:
                    bd.append(1)
                    kbd.append(1)
                    k.append(1)
                    du.append(1)
                    kbddu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
#budapest debreceni vonatok szerda
            elif vonat=="bd" and nap=="sze" and napszak=="de":
                if (foglalas+len(szebdde))<=48:
                    bd.append(1)
                    szebd.append(1)
                    sze.append(1)
                    de.append(1)
                    szebdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
#budapest debreceni vonatok csutortok
            elif vonat=="bd" and nap=="cs" and napszak=="de":
                if (foglalas+len(csbdde))<=48:
                    bd.append(1)
                    csbd.append(1)
                    cs.append(1)
                    de.append(1)
                    csbdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="cs" and napszak=="d":
                if (foglalas+len(csbdd))<=48:
                    bd.append(1)
                    csbd.append(1)
                    cs.append(1)
                    d.append(1)
                    csbdd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="cs" and napszak=="du":
                if (foglalas+len(csbddu))<=48:
                    bd.append(1)
                    csbd.append(1)
                    cs.append(1)
                    du.append(1)
                    csbddu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
#budapest-debreceni vonatok pentek
            elif vonat=="bd" and nap=="p" and napszak=="de":
                if (foglalas+len(pbdde))<=48:
                    bd.append(1)
                    pbd.append(1)
                    p.append(1)
                    de.append(1)
                    pbdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="p" and napszak=="d":
                if (foglalas+len(pbdd))<=48:
                    bd.append(1)
                    pbd.append(1)
                    p.append(1)
                    d.append(1)
                    pbdd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="p" and napszak=="du":
                if (foglalas+len(pbddu))<=48:
                    bd.append(1)
                    pbd.append(1)
                    p.append(1)
                    du.append(1)
                    pbddu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
#budapest-debreceni vonatok szombat
            elif vonat=="bd" and nap=="szo" and napszak=="de":
                if (foglalas+len(szobdde))<=48:
                    bd.append(1)
                    szobd.append(1)
                    szo.append(1)
                    de.append(1)
                    szobdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="szo" and napszak=="d":
                if (foglalas+len(szobdd))<=48:
                    bd.append(1)
                    szobd.append(1)
                    szo.append(1)
                    d.append(1)
                    szobdd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bd" and nap=="szo" and napszak=="du":
                if (foglalas+len(szobddu))<=48:
                    bd.append(1)
                    szobd.append(1)
                    szo.append(1)
                    du.append(1)
                    szobddu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
#budapest-debreceni vonatok vasarnap
            elif vonat=="bd" and nap=="v" and napszak=="de":
                if (foglalas+len(vbdde))<=48:
                    bd.append(1)
                    vbd.append(1)
                    v.append(1)
                    de.append(1)
                    vbdde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bd" and nap=="v" and napszak=="d":
                if (foglalas+len(vbdd))<=48:
                    bd.append(1)
                    vbd.append(1)
                    v.append(1)
                    d.append(1)
                    vbdd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
            elif vonat=="bd" and nap=="v" and napszak=="du":
                if (foglalas+len(vbddu))<=48:
                    bd.append(1)
                    vbd.append(1)
                    v.append(1)
                    du.append(1)
                    vbddu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False
        #budapest-szegedi vonatok h-v
#budapest szegedi vonatok hetfo
            elif vonat=="bsz" and nap=="h" and napszak=="de":
                if (foglalas+len(hbszde))<=48:
                    bsz.append(1)
                    hbsz.append(1)
                    h.append(1)
                    de.append(1)
                    hbszde.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="h" and napszak=="d":
                if (foglalas+len(hbszd))<=48:
                    bsz.append(1)
                    hbsz.append(1)
                    h.append(1)
                    d.append(1)
                    hbszd.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="h" and napszak=="du":
                if (foglalas+len(hbszdu))<=48:
                    bsz.append(1)
                    hbsz.append(1)
                    h.append(1)
                    du.append(1)
                    hbszdu.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 



#budapest-szegdi vonatok kedd
            elif vonat=="bsz" and nap=="k":
                if (foglalas+len(kbsz))<=58:
                    bsz.append(1)
                    kbsz.append(1)
                    k.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="sze":
                if (foglalas+len(szebsz))<=48:
                    bsz.append(1)
                    szebsz.append(1)
                    sze.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="cs":
                if (foglalas+len(csbsz))<=48:
                    bsz.append(1)
                    csbsz.append(1)
                    cs.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="p":
                if (foglalas+len(pbsz))<=48:
                    bsz.append(1)
                    pbsz.append(1)
                    p.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="szo":
                if (foglalas+len(szobsz))<=48:
                    bsz.append(1)
                    szobsz.append(1)
                    szo.append(1)
                else:
                    print("elfogyott a jegy erre a járatra")
                    return False 
            elif vonat=="bsz" and nap=="v":
                if (foglalas+len(vbsz))<=48:
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

        
#bevetel szamito fuggveny
def bevetel():
    elemszam=len(bb)+len(bd)+len(bsz)
    print(elemszam*4000)

#MENU
opcio=None
while opcio!="kilepes":
    print ("jegyfoglalas","bevetel","kilepes")
    opcio=input("adja meg a menupontot!")

    if opcio=="jegyfoglalas":
        jegyfoglalas()
    elif opcio=="bevetel":
        bevetel()

