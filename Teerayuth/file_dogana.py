import pandas as pd

# creo la classe madre con il metodo costruttore
class Teerayuth:
    def __init__(self, tot_ordini, spedizione):
        self.tot_ordini = tot_ordini
        self.spedizione = spedizione
        self.df1 = None
        self.df2 = None
        
    # leggo il file con tutti gli ordini di Teerayuth e lascio solo le colonne che mi interessano
    # tolgo eventuali spazi dalla colonna SKU
    # rinomino la colonna del prezzo
    def file_ordini(self):
        self.df1 = pd.read_csv(self.tot_ordini, usecols=["Name", "Vendor", "Lineitem sku", "Lineitem quantity", "Lineitem price", "Currency"])
        self.df1["Lineitem sku"] = self.df1["Lineitem sku"].str.strip()
        self.df1 = self.df1[["Name", "Vendor", "Lineitem sku", "Lineitem quantity","Lineitem price", "Currency"]]
        self.df1.rename(columns = {"Lineitem price" : "Price Before Discount"}, inplace = True)
        return self.df1
    
    # leggo il file degli articoli inseriti nella spedizione odierna
    # anche qui rinomino la colonna del prezzo
    def file_spediti(self):
        self.df2 = pd.read_csv(self.spedizione, usecols=["Name", "Lineitem sku", "Lineitem quantity", "Lineitem price"])
        self.df2.rename(columns={"Lineitem price": "Price Before Discount"}, inplace=True)
        return self.df2
    
    # effettuo il confronto tra i due file
    def confronto(self):
        df3 = self.df1.merge(self.df2, how="right", on=["Name", "Lineitem sku", "Price Before Discount","Lineitem quantity"])
        return df3

# i due attributi tot_ordini e spedizione  vengono assegnati ai rispettivi percorsi per l'apertura dei file
tot_ordini = r"C:\Users\miche\Desktop\py\Progetti\Teerayuth\Dogana\Ordini.csv"
spedizione = r"C:\Users\miche\Desktop\py\Progetti\Teerayuth\Dogana\spediti.csv"

file = Teerayuth(tot_ordini, spedizione) # istanza

file.file_ordini() # richiamo le funzione relativa al file degli ordini
file.file_spediti() # richiamo la funzione relativa al file degli occhiali spediti

results = file.confronto() # effettuo il confronto con la funzione "confronto"

# creo la funzione per scontare il prezzo del 5%
def getAfterDiscount(price):
    price = price * 0.95
    return round(price, 2)

# assegno la funzione "getAfterDiscount" alla colonna "Price Before Discount" e creo una nuova colonna
results["Price After Discount"] = results["Price Before Discount"].apply(getAfterDiscount)

# compilo tutti i valori vuoti della colonna "Currency"
results["Currency"] = results["Currency"].fillna("EUR")

# ordino le colonne
results = results[["Name", "Vendor", "Lineitem sku", "Lineitem quantity", "Currency", "Price Before Discount", "Price After Discount"]]
results.set_index("Name", inplace = True)
results.to_excel("Shipment_No_.xlsx")