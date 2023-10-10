# SENZA BARRA
import pandas as pd
try:
    rayban = pd.read_excel("rb.xlsx")

    def ray(x):
        return round(x * 0.80)

    rayban["Variant Price"] = rayban["Variant Price"].astype("float64")

    rayban[["Variant Price", "Variant Compare At Price"]] = rayban[["Variant Price", "Variant Compare At Price"]].fillna(0)

    rayban["Variant Price"] = rayban["Variant Compare At Price"].apply(ray)

    rayban["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    rayban["Variant Price"] = rayban["Variant Price"].apply(arrotondamento)

    # Template Suffix
    rayban["Template Suffix"] = rayban["Template Suffix"].fillna("Default product")

    #salvataggio
    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + "rayban_ok.xlsx"

    file = rayban.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito rb.xlsx (Ray-Ban)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")