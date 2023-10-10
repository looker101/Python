import pandas as pd
try:
    bv = pd.read_excel("bvlgari.xlsx")

    def bulgari(x):
        return round(x * 0.65)

    # colonna Variant Price == float64

    bv["Variant Price"] = bv["Variant Price"].astype("float64")

    bv[["Variant Price", "Variant Compare At Price"]] = bv[["Variant Price", "Variant Compare At Price"]].fillna(0)

    bv["Variant Price"] = bv["Variant Compare At Price"].apply(bulgari)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    bv["Variant Price"] = bv["Variant Price"].apply(arrotondamento)


    # default price
    bv["Template Suffix"] = bv["Template Suffix"].fillna("Default product")

    # salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + "bvlgari_ok.xlsx"

    file = bv.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito bvlgari.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")



