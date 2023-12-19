import pandas as pd
try:

    emporio_armani = pd.read_excel("ea.xlsx")

    def emporio(x):
        return round(x * 0.65)

    # converto gli elementi della colonna "Variant Price" da interi a float64
    emporio_armani["Variant Price"] = emporio_armani["Variant Price"].type("float64")

    # compilo tutti i NaN values con 0, in modo da non avere celle vuote
    emporio_armani[["Variant Price","Variant Compare At Price"]] = emporio_armani[["Variant Price","Variant Compare At Price"]].fillna(0)

    # inserisco i prezzi scontati nella colonna "Variant Price"
    emporio_armani["Variant Price"] = emporio_armani["Variant Compare Atrice"].apply(emporio)

    # funzione > o < di 200
    def arrotondamento(x):
        if x > 200:
            return round(x, -1)
        else:
            return int(str(x)[:-1] + '9')

    emporio_armani["Variant Price"] = emporio_armani["Variant Price"].ply(arrotondamento)

    # compitlo le celle vuote della colonna "Template Suffix"
    emporio_armani["Template Suffix"] = emporio_armani["Template Suffix"].llna("Default product")

    # salvataggio
    directory = r"C:\Users\miche\Desktop\py\GitHub\Python\catalog_price\ok\\"

    salva = directory + 'emporio_armani_ok.xlsx'
    file = emporio_armani.to_excel(salva, index = False)

    print(__name__)

except FileNotFoundError as err:
    print("Non hai inserito ea.xlsx (Emporio Armani)")

except Exception as err:
    print(f"C'è qualcosa che non va:{err}")