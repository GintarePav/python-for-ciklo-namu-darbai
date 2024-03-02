# 1. Vienu smūgiu stalius įkala vinį į k cm gylį. Parašykite programą, kuri išspausdintu plaktuko dūžį "Tuk!" su kiekvienu smūgiu, šalia smūgio numerį ir kiek vinies ilgio dar liko neįkaltos. Kalamos vinies ilgis n cm. Baigus kalti vinį, pranešama "Vinis įkalta".
def validuoti(txt):
    centimetrai = int(input(txt))
    if centimetrai <=0:
        print("Netinkamas skaičius, bandykite dar karta")
        return validuoti(txt)
    else:
        return centimetrai
    
viniesIlgis = validuoti("Koks vinies ilgis centimetrais? ")
ikaltaCm = validuoti("Kiek centimetrų vinies stalius įkalė vienu smūgiu? ")
viniesLikutis = viniesIlgis

for i in range(1, 1000):
    viniesLikutis -= ikaltaCm
    print(f'"Tuk!" {i}-asis smūgis, vinies liko dar {viniesLikutis} cm.')
    if viniesLikutis <= 1:
        print ("Vinis įkalta.")
        break    