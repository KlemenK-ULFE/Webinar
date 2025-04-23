import random
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def generiraj_meritve(n=50):
    podatki = []
    zacetni_cas = datetime.now()
    for i in range(n):
        temperatura = round(random.uniform(20.0, 30.0), 2)
        cas = zacetni_cas + timedelta(seconds=i * 10)
        podatki.append({'cas': cas, 'temperatura': temperatura})
    return pd.DataFrame(podatki)

# Shranjevanje in analiza
df = generiraj_meritve()
df.to_csv("meritve.csv", index=False)

print("Povprečje:", df['temperatura'].mean())
print("Maksimum:", df['temperatura'].max())
print("Minimum:", df['temperatura'].min())

# Vizualizacija
plt.plot(df['cas'], df['temperatura'])
plt.xlabel("Čas")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturni profil")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graf.png")
plt.show()