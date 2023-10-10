# SENZA BARRA
import pandas as pd
try:
    rudy_project = pd.read_excel("rudy.xlsx")

    def rp(x):
        return round(x * 0.84)

    rudy_project["Variant Price"] = rudy_project["Variant Price"].astype("float64")

    rudy_project[["Variant Price", "Variant Compare At Price"]] = rudy_project[["Variant Price", "Variant Compare At Price"]]

    rudy_project["Variant Price"] = rudy_project["Variant Compare At Price"].apply(rp)

    rudy_project["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    rudy_project["Variant Price"] = rudy_project["Variant Price"].apply(arrotondamento)

    # Template Suffix
    rudy_project["Template Suffix"] = rudy_project["Template Suffix"].fillna("Default product")


    #salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + "rudy_project_ok.xlsx"

    file = rudy_project.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito rudy.xlsx (Rudy Project)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")