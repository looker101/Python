# CON BARRA
import pandas as pd

# leggo il file
swarovski = pd.read_excel("sk.xlsx")

# definisco la funzione per lo sconto
def swaro(x):
    return round(x * 0.65)

# tutti i valori della colonna "Variant Price" li trasfrormo in float64
swarovski["Variant Price"] = swarovski["Variant Price"].astype("float64")

# compilo con il valore 0 tutti i NaN della colonna del "Compare at Price"
swarovski[["Variant Price", "Variant Compare At Price"]] = swarovski[["Variant Price", "Variant Compare At Price"]].fillna(0)

# applico la funzione dello sconto alla colonna del "Compare Price" e compilo la colonna "Variant Price"
swarovski["Variant Price"] = swarovski["Variant Compare At Price"].apply(swaro)

# tolgo la barra eliminando i valori sotto la colonna "Variant compare at price"
swarovski["Variant Compare At Price"] = ' '

# Template Suffix
swarovski["Template Suffix"] = swarovski["Template Suffix"].fillna("Default product") 

#Salvataggio
directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

salva = directory + 'sk_ok.xlsx'

file = swarovski.to_excel(salva, index=False)