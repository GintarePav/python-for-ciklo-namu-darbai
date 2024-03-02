# 7. Architektas suprojektavo salę, kurioje bus n eilių. Pirmoje eilėje stovės k kėdžių, o kiekvienoje kitoje – 2 kėdėmis daugiau, negu prieš tai buvusioje. Parašykite programą, kuri apskaičiuotų, kiek iš viso kėdžių s reikia užsakyti, kad architekto sumanymas būtų įgyvendintas. Pasitikrinkite. Kai n = 3, o k = 8, turi būti išvesta: Reikia užsakyti s = 30 kėdžių.

def validuoti(txt):
    skaicius = int(input(txt))
    if skaicius <=0:
        print("Netinkamas skaičius, bandykite dar karta")
        return validuoti(txt)
    else:
        return skaicius

eiliuSkaiciusN = validuoti("Kiek kėdžių eilių bus salėje? ")
kedesPirmojeK = validuoti("Kiek kėdžių bus pirmoje eilėje? ")
kedesKitose = kedesPirmojeK
visosKedes = kedesPirmojeK

for i in range(1, eiliuSkaiciusN):
    kedesKitose += 2
    visosKedes += kedesKitose
    print(f'{i+1} eileje yra {kedesKitose} kedziu')

print(f'Iš viso reikia {visosKedes} kėdžių.')
