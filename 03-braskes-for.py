# 8. Vasaros pradžioje prasideda braškių sezonas. Pirmąją dieną lysvėje prinoko b braškių. Kiekvieną kitą dieną prinoksta d braškių daugiau, negu prieš tai buvusią. Parašykite programą, skaičiuojančią, kiek prinokusių braškių k bus po n dienų. Pasitikrinkite: kai b =4, d = 5, n = 3, tuomet kompiuterio ekrane turi būti rodoma: Per 3 dienas prinoko 27 braškės.

def validuoti(txt):
    skaicius = int(input(txt))
    if skaicius < 0:
        print("Netinkamas skaičius, bandykite dar karta")
        return validuoti(txt)
    else:
        return skaicius

prinokeBraskes = validuoti("Kiek braskiu prinoko pirma diena? ")
papildomosBraskes = validuoti("Keliomis braskemis daugiau prinoko kita diena? ")
dienos = validuoti("Kiek dienų nurenkame braskes? ")
visoBraskiu = prinokeBraskes

for i in range(1, dienos):
    prinokeBraskes += papildomosBraskes
    visoBraskiu += prinokeBraskes

print(f'Per {dienos} d. surinkta {visoBraskiu} braskiu.')