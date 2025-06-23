

#dfs
def flood_fill_dfs(obraz, x_start,y_start, nowy_kolor):
    wysokosc = len(obraz) #wiersz
    szerokosc = len(obraz[0]) #kolumna
    kolor_poczatkowy = obraz[x_start][y_start]

    if kolor_poczatkowy == nowy_kolor: #zapobiega nieskończonej pętli
        return

    def dfs(wiersz, kolumna):
        if wiersz < 0 or wiersz >= wysokosc or kolumna < 0 or kolumna >= szerokosc: #granice obrazu, jeśli nie przerywa
            return

        if obraz[wiersz][kolumna] != kolor_poczatkowy: #jeśli ma inny piksel niż początkowy, nie interesuje nas
            return

        obraz[wiersz][kolumna] = nowy_kolor #ustawiamy nowy piksel

    #rekurencyjne dfs na sąsiednich
        dfs(wiersz -1, kolumna) #góra
        dfs(wiersz +1, kolumna) #dół
        dfs(wiersz, kolumna -1) #lewo
        dfs(wiersz, kolumna +1) #prawo

    dfs(x_start, y_start)

obraz = [
        [1,1,0],
        [1,0,0],
        [1,1,1]
 ]

flood_fill_dfs(obraz,0,0,2)

for wiersz in obraz:
    print(wiersz)


#bfs
from collections import deque

def flood_fill_bfs(obraz, x_start, y_start, nowy_kolor):
    wysokosc = len(obraz)
    szerokosc = len(obraz[0])
    kolor_poczatkowy = obraz[x_start][y_start]

    if kolor_poczatkowy == nowy_kolor:
        return

    kolejka = deque()
    kolejka.append((x_start, y_start)) #punkt startowy

    while kolejka:
        wiersz, kolumna = kolejka.popleft() #pobiera pierwszy element

        if wiersz < 0 or wiersz >= wysokosc or kolumna < 0 or kolumna >= szerokosc:
            continue

        if obraz[wiersz][kolumna]!= kolor_poczatkowy:
            continue

    #ustawiamy nowy kolor
        obraz[wiersz][kolumna] = nowy_kolor

    #dodajemy sąsiednie do kolejki
        kolejka.append((wiersz -1, kolumna)) #góra
        kolejka.append((wiersz +1, kolumna)) #dół
        kolejka.append((wiersz, kolumna -1)) #lewo
        kolejka.append((wiersz, kolumna +1)) #prawo



flood_fill_bfs(obraz,0,0,2)

print("-" *20)
for wiersz in obraz:
     print(wiersz)

