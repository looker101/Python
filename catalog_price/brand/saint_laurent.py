# CON BARRA
import pandas as pd
try:
    # leggo il file
    saint_laurent = pd.read_excel("sl.xlsx")

    # definisco la funzione per lo sconto
    def saint(x):
        return round(x * 0.7)

    # tutti i valori della colonna "Variant Price" li trasfrormo in float64
    saint_laurent["Variant Price"] = saint_laurent["Variant Price"].astype("float64")

    # compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
    saint_laurent["Variant Price"] = saint_laurent["Variant Price"].fillna(0)

    # applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
    saint_laurent["Variant Price"] = saint_laurent["Variant Compare At Price"].apply(saint)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    saint_laurent["Variant Price"] = saint_laurent["Variant Price"].apply(arrotondamento)

    # Template Suffix
    saint_laurent["Template Suffix"] = saint_laurent["Template Suffix"].fillna("Default product") 

    #Salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + 'sl_ok.xlsx'

    file = saint_laurent.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito sl.xlsx (Saint Laurent)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")