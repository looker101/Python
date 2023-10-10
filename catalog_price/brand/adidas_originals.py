# SENZA BARRA
import pandas as pd
try:
    # leggi il file
    adidas_originals = pd.read_excel("or.xlsx")

    # definisco la funzione per lo sconto
    def originals(x):
        return round(x * 0.7)

    #conversione interi in flot
    adidas_originals["Variant Price"] = adidas_originals["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    adidas_originals[["Variant Price" ,"Variant Compare At Price"]] = adidas_originals[["Variant Price" ,"Variant Compare At Price"]].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    adidas_originals["Variant Price"] = adidas_originals["Variant Compare At Price"].apply(originals)

    # tutte le celle della colonna "Compare at price" saranno vuote (in modo da non mostrare la barra)
    adidas_originals["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    adidas_originals["Variant Price"] = adidas_originals["Variant Price"].apply(arrotondamento)

    # compilo tutte le celle vuote della colonna "template suffix" con "Default product"
    adidas_originals["Template Suffix"] = adidas_originals["Template Suffix"].fillna("Default product")

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + 'adidas_originals_ok.xlsx'

    file = adidas_originals.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito or.xlsx (Adidas Originals)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")