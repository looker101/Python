import pandas as pd

tezuia = pd.read_excel("Da_Spedire.xlsx")
new = pd.read_csv("orders_export.csv", usecols=["Name" ,"Lineitem sku", "Lineitem quantity","Lineitem price"])

new_file = pd.concat([tezuia, new])

new_file = new_file.sort_values(by = "Name")

new_file.to_excel("Da_Spedire.xlsx", index=False)

if new_file is not None:
    print("File sostituito correttamente!")
else:
    print("Il file non è stato sostiuito. Ci dev'essere un errore!")