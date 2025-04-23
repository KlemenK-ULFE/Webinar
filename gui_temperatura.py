import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def generiraj_meritve(n=50):
    podatki = []
    zacetni_cas = datetime.now()
    for i in range(n):
        temperatura = round(random.uniform(20.0, 30.0), 2)
        cas = zacetni_cas + timedelta(seconds=i * 10)
        podatki.append({'cas': cas, 'temperatura': temperatura})
    return pd.DataFrame(podatki)

def zaženi():
    df = generiraj_meritve()
    df.to_csv("meritve.csv", index=False)
    povp = df['temperatura'].mean()
    mini = df['temperatura'].min()
    maksi = df['temperatura'].max()
    
    msg = f"Povprečna: {povp:.2f} °C\nMin: {mini:.2f} °C\nMax: {maksi:.2f} °C"
    messagebox.showinfo("Analiza podatkov", msg)

    df['drseče povp'] = df['temperatura'].rolling(window=5).mean()
    df.plot(x='cas', y=['temperatura', 'drseče povp'], title="Temperaturni profil")
    plt.xlabel("Čas")
    plt.ylabel("Temperatura (°C)")
    plt.tight_layout()
    plt.savefig("graf_gui.png")
    plt.show()

okno = tk.Tk()
okno.title("Simulacija temperature")
gumb = tk.Button(okno, text="Zaženi simulacijo", command=zaženi)
gumb.pack(padx=20, pady=20)
okno.mainloop()