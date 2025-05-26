# 1. Rekurencyjne DFS (głębokie przeszukiwanie)
def flood_fill_dfs(obraz, x, y, nowy_kolor, stary_kolor):
    # Sprawdzenie, czy współrzędne są w granicach obrazu
    if x < 0 or y < 0 or x >= len(obraz) or y >= len(obraz[0]):  
        return
    
    # Jeśli piksel ma inny kolor niż startowy, nie zmieniamy go
    if obraz[x][y] != stary_kolor:
        return

    # Zmiana koloru pikselu
    obraz[x][y] = nowy_kolor  

    # Rekurencyjne przejście w czterech kierunkach: prawo, lewo, dół, góra
    flood_fill_dfs(obraz, x+1, y, nowy_kolor, stary_kolor)  
    flood_fill_dfs(obraz, x-1, y, nowy_kolor, stary_kolor)  
    flood_fill_dfs(obraz, x, y+1, nowy_kolor, stary_kolor)  
    flood_fill_dfs(obraz, x, y-1, nowy_kolor, stary_kolor)  


# 2. Iteracyjny BFS (szerokie przeszukiwanie)
def flood_fill_bfs(obraz, x, y, nowy_kolor):
    from collections import deque  # Importowanie kolejki

    stary_kolor = obraz[x][y]  # Pobranie koloru startowego
    if stary_kolor == nowy_kolor:  # Jeśli kolor jest już zmieniony, nic nie robimy
        return

    kolejka = deque()  # Tworzenie pustej kolejki
    kolejka.append((x, y))  # Dodanie współrzędnych startowych

    while kolejka:  # Dopóki są elementy w kolejce
        px, py = kolejka.popleft()  # Pobranie pierwszego elementu z kolejki

        # Sprawdzenie, czy współrzędne są w granicach obrazu
        if px < 0 or py < 0 or px >= len(obraz) or py >= len(obraz[0]):
            continue
        # Jeśli piksel ma inny kolor niż startowy, pomijamy go
        if obraz[px][py] != stary_kolor:
            continue

        # Zmiana koloru pikselu
        obraz[px][py] = nowy_kolor  

        # Dodanie sąsiadujących pikseli do kolejki (prawo, lewo, dół, góra)
        kolejka.append((px+1, py))  
        kolejka.append((px-1, py))  
        kolejka.append((px, py+1))  
        kolejka.append((px, py-1))  


# Przykładowy obraz (macierz pikseli)
obraz = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 0]
]

# Testowanie algorytmu DFS
flood_fill_dfs(obraz, 0, 0, 2, obraz[0][0])
print("Po zastosowaniu DFS:", obraz)

# Testowanie algorytmu BFS
obraz = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 0]
]

flood_fill_bfs(obraz, 0, 0, 2)
print("Po zastosowaniu BFS:", obraz)

