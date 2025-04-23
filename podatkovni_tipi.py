# === OSNOVNI PODATKOVNI TIPI ===

# Števila
celo_stevilo = 10              # int
decimalno_stevilo = 3.14       # float

# Nizi (str)
pozdrav = "Živjo, svet!"

# Logične vrednosti (bool)
je_aktivno = True

# Seznami (list)
sadje = ["jabolko", "banana", "češnja"]

# Nabor (tuple)
koordinate = (10.0, 20.5)

# Slovarji (dict)
uporabnik = {
    "ime": "Ana",
    "starost": 25
}

# Množice (set)
unikatne_stevilke = {1, 2, 3, 3, 2}  # samodejno odstrani dvojnike

# === ZANKE IN POGOJI ===

# Zanka for
for sadez in sadje:
    print("Sadež:", sadez)

# Zanka while
stevec = 0
while stevec < 3:
    print("Stevec je:", stevec)
    stevec += 1

# Pogojni stavek
if "banana" in sadje:
    print("Imamo banano!")
else:
    print("Ni banane.")

# === FUNKCIJE ===

def pozdravi(ime):
    """Vrne pozdravno sporočilo za podano ime."""
    return f"Pozdravljen, {ime}!"

print(pozdravi("Miha"))

# === RAZREDI (class) ===

class Oseba:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def predstavi_se(self):
        print(f"Sem {self.ime} in star sem {self.starost} let.")

# Ustvarimo objekt
oseba1 = Oseba("Klemen", 26)
oseba1.predstavi_se()
