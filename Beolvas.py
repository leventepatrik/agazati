from Filmek import osztaly

def feladat():
    f=open("film.txt","r",encoding="utf-8")
    f.readline()
    f_sorok_lista=f.readlines()
    f.close()
    osztaly_lista=[]
    for i in range(0,len(f_sorok_lista),1):
        aktelem=f_sorok_lista[i]
        sor_lista=aktelem.strip().split(";")
        cim=str(sor_lista[0])
        rendezo=str(sor_lista[1])
        foszereplo=str(sor_lista[2])
        ev=int(sor_lista[3])
        perc=int(sor_lista[4])
        osztalyom=osztaly(cim,rendezo,foszereplo,ev,perc)
        osztaly_lista.append(osztalyom)
        return osztaly_lista