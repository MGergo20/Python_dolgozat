nev:str=str(input("Kérlek add meg a teljes neved:"))
email_cim:str=str(input("Kérlek add meg a teljes email címed:"))
jelszo:str=str(input("Kérlek add meg a helyes jelszavad:"))

def kiiratás():
    print("I/A, B:")
    print(f"    Név:{nev}")
    print(f"    Email cím:{email_cim}")
    print(f"    Jelszó:{jelszo}")
   

def eredmeny():
    print("I/C:")
    if len(jelszo) >= 6:
        print(f"Sikeres regisztráció {nev}, {email_cim}!")
    elif len(jelszo) == 0:
        print("Sikertelen regisztráció (üres jelszó).")
    else:
        print("Sikertelen regisztráció (kevés karakter).")

        