
import random
import datetime

# Funkcja zapisująca wizytę użytkownika
def zapisz_wizyte(historia, lokalizacja, czas=None):
    historia[lokalizacja] = czas or datetime.datetime.now()

# Lista przykładowych lokalizacji
lokalizacje = []
for _ in range(10):
    x = round(random.uniform(10, 50), 2)
    y = round(random.uniform(10, 50), 2)
    lokalizacje.append((x, y))

historia_wizyt = {}

# Dodawanie wizyt w losowych lokalizacjach
for i in range(25):
    lok = random.choice(lokalizacje)
    przesunięcie_czasu = datetime.timedelta(days=i // 5, hours=(i % 3) * 8)
    czas = datetime.datetime.now() + przesunięcie_czasu
    zapisz_wizyte(historia_wizyt, lok, czas)

# Funkcja wyszukująca wizyty w danym dniu
def znajdz_wizyty_w_dniu(historia, data):
    wynik = []
    for lokalizacja, czas in historia.items():
        if czas.date() == data:
            wynik.append(lokalizacja)
    return wynik

# Wybór losowego dnia i wyświetlenie wyników
losowy_dzien = datetime.datetime.now().date() + datetime.timedelta(days=random.randint(0, 4))
wizyty_w_dniu = znajdz_wizyty_w_dniu(historia_wizyt, losowy_dzien)

print(f"Lokalizacje odwiedzone dnia {losowy_dzien}: {wizyty_w_dniu}")
