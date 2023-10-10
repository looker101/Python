import pandas as pd
try:

    alexander_mcqueen = pd.read_excel("amq.xlsx")

    def mcqueen(x):
        return round(x * 0.70)

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Price"].astype("float64")

    alexander_mcqueen[["Variant Price", "Variant Compare At Price"]] = alexander_mcqueen[["Variant Price", "Variant Compare At Price"]].fillna(0)

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Compare At Price"].apply(mcqueen)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    alexander_mcqueen["Variant Price"] = alexander_mcqueen["Variant Price"].apply(arrotondamento)

    alexander_mcqueen["Template Suffix"] = alexander_mcqueen["Template Suffix"].fillna("Default product")

    directory = r"C:\Users\miche\Desktop\py\Progetti\BrandScraping\test_brand2\ok\\"

    salva = directory + 'amq_ok.xlsx'

    file = alexander_mcqueen.to_excel(salva, index=False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito amq.xlsx (Alexander McQueen)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")