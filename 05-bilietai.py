# 5. Autobusų parko administracija nusprendė keleiviams, kurių bilietų numeriai laimingi, dovanoti kelionę už pusę kainos. Autobuso bilietas laikomas laimingu, jei jo pirmųjų trijų skaitmenų trejetas sutampa su paskutinių trijų skaitmenų trejetu (pvz., laimingas bilietas, kurio numeris yra 234234). Autobusų parko administracija nutarė bilietus sunumeruoti nuo m-tojo iki n-tojo šešiaženklio skaičiaus. Parašykite programą, kuri apskaičiuotų, kiek keleivių įsigis laimingus bilietus. Pasitikrinkite. Kai m = 170849, o n = 189965, turi būti išvesta: Laimingus bilietus įsigijo 19 keleivių.

def validuoti(txt, num):
    skaicius = int(input(txt))
    if skaicius > num and 10 ** 5 <= skaicius < 10 ** 6:
        return skaicius
    else:
        print("Netinkamas skaičius, bandykite dar karta")
        return validuoti(txt, num)
    
        
mBilietas = validuoti("Koks m-tojo bilieto šešiaženklis skaičius? ", 0)
nBilietas = validuoti("Koks n-tojo bilieto šešiaženklis skaičius? ", mBilietas)
kiekLaimingu = 0

for i in range(mBilietas, nBilietas + 1):
    pradzia = i // 1000
    galas = i % 1000
    if pradzia == galas:
        kiekLaimingu += 1

print(f"Laimingus bilietus isigijo {kiekLaimingu} keleiviu.")
