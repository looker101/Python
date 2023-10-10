# SENZA BARRA
import pandas as pd
try:
    # leggi il file
    arnette = pd.read_excel("arnette.xlsx")

    # definisco la funzione per lo sconto
    def originals(x):
        return round(x * 0.7)

    #conversione interi in flot
    arnette["Variant Price"] = arnette["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    arnette[["Variant Price" ,"Variant Compare At Price"]] = arnette[["Variant Price" ,"Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    arnette["Variant Price"] = arnette["Variant Compare At Price"].apply(originals)

    # tutte le celle della colonna "Compare at price" saranno vuote (in modo da non mostrare la barra)
    arnette["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    arnette["Variant Price"] = arnette["Variant Price"].apply(arrotondamento)

    # compilo tutte le celle vuote della colonna "template suffix" con "Default product"
    arnette["Template Suffix"] = arnette["Template Suffix"].fillna("Default product")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + 'arnette_ok.xlsx'

    file = arnette.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito arnette.xlsx (Arnette)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")