import pandas as pd
try:
    oakley_snow = pd.read_excel("oakley_snow.xlsx")

    def oak_snow(x):
        return round(x * 0.80)

    oakley_snow["Variant Price"] = oakley_snow["Variant Price"].astype("float64")

    oakley_snow[["Variant Price", "Variant Compare At Price"]] = oakley_snow[["Variant Price", "Variant Compare At Price"]].fillna(0)

    oakley_snow["Variant Price"] = oakley_snow["Variant Compare At Price"].apply(oak_snow)

    oakley_snow["Variant Compare At Price"] = ' '

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    oakley_snow["Variant Price"] = oakley_snow["Variant Price"].apply(arrotondamento)

    # Template Suffix
    oakley_snow["Template Suffix"] = oakley_snow["Template Suffix"].fillna("Default product")


    # salvataggio

    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + "oakley_snow_ok.xlsx"

    file = oakley_snow.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito oakley_snow.xlsx")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")