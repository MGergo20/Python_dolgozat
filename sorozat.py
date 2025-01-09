import random

global lista
lista=[]
i=0
while i<5:
    rszam=random.randint(1, 10)
lista.append(rszam)
i+=1
def fel2():
    i=0
    while i if i
        print(f"{lista[i]}", end="!")
    else:
        print(f"{lista[i]}",end=" ")
    i+=1

    return lista

def nagyobb():
    db=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            db+=1
        return db

def konzol_ir():
    kiir=nagyobb()
    print(f"Nagyobb számok száma: {kiir}")

def fajlba_ir():
    print("II/F:")
kiir=nagyobb()
t = open('vegeredmeny.txt', 'w', encoding="utf-8")
t.write("II/F:")
t.write(f"\nA tizzel osztahtóak száma {kiir}.")
t.close()

    