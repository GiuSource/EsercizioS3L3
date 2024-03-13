import FunzioniS3L3

print("Benvenuto in questo programma di calcolo del perimetro \n\n ")
figura = int(input("Di quale forma geometrica vuoi calcolare il perimetro? \n1) Quadrato 2) Cerchio 3) Rettangolo "))

if figura == 1:
    lato = int(input("Inserisci la misura del lato del quadrato in cm \n"))
    perimetro = FunzioniS3L3.area_quadrato(lato)
    print("Il perimetro del quadrato è di " + str(perimetro) + "cm \n")

elif figura == 2:
    raggio = int(input("Inserisci la lunghezza del raggio del cerchio in cm \n "))
    circonferenza = FunzioniS3L3.area_cerchio(raggio)
    print("La circonferenza del cerchio è di " + str(circonferenza) + "cm \n")

elif figura == 3:
    base = int(input("Inserisci la lunghezza della base del rettangolo in cm \n "))
    altezza = int(input("Inserisci la lunghezza dell'altezza del rettangolo in cm \n "))
    perimetro = FunzioniS3L3.area_rettangolo(base, altezza)
    print("Il perimetro del rettangolo è di " + str(perimetro) + "cm \n")

else:
    print("Digita un input valido! \n")

