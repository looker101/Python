import pandas as pd

# leggo il file delle vendite e dei resi
mg = pd.read_excel("margini_MESE.xlsx")
rim = pd.read_excel("rimborsi_MESE.xlsx")
tot = pd.read_excel("tot-margini.xlsx")

# calcolo somma colonna "G" ("TOT ORDINE (-card fee)")
g = mg["TOT ORDINE (-card fee)"].sum()

# calcolo somma colonna "M" ("Comm. PayPal")
m = mg["Comm. PayPal"].sum()

# calcolo i ricavi
ricavi = g - m

# calcolo la media della "% margine profitto"
media = mg["% margine"].mean()

# calcolo la perdita facendo la somma della colonna "Tot. aggiunto al ns conto - Tot. rimborso"
perdita = mg["Margine TOT"].sum() + rim["TOT. pERDITA"].sum()
tot_perdita = perdita.sum()

# setto come indici la colonna dei mesi
tot.set_index("Unnamed: 0", inplace = True)

# inserisco nelle rispettive righe
tot.loc["MESE", "Ricavi"] = ricavi
tot.loc["MESE", "Guadagno"] = tot_perdita
tot.loc["MESE", "% Margine Profitto"] = media

#tot
