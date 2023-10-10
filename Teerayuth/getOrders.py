import pandas as pd

tezuia = pd.read_excel("Da_Spedire.xlsx")
new = pd.read_csv("orders_export.csv", usecols=["Name" ,"Lineitem sku", "Lineitem quantity","Lineitem price"])

new_file = pd.concat([tezuia, new])

new_file.to_excel("Da_Spedire.xlsx", index=False)

if new_file is not None:
    print("Tutto ok!")
else:
    print("Errore!! C'è qualcosa che non va")