# 9. Paskutinis knygos puslapis pažymėtas skaičiumi 710. Kiek reikia skaitmenų knygos puslapiams sunumeruoti (numeracija pradedama nuo vieneto)?

def validuoti(txt):
    skaicius = int(input(txt))
    if skaicius < 0:
        print("Netinkamas skaičius, bandykite dar karta")
        return validuoti(txt)
    else:
        return skaicius
    
paskutinisPuslapis = validuoti("Kokiu skaiciumi pazymetas paskutinis knygos puslapis? ")
skaitmenuSkaicius = 0

for i in range(1, paskutinisPuslapis + 1):
    skaitmenuSkaicius += len(str(i))

print(f'Knygai sunumeruoti reikia {skaitmenuSkaicius} skaitmenų.')