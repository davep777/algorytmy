import random

def generuj_labirynt(n, m, start, meta):
    """Generuje labirynt o wymiarach n x m wykorzystując DFS."""
    
    # Tworzymy graf (siatkę komórek)
    labirynt = [[{"visited": False, "walls": {"N": True, "E": True, "S": True, "W": True}} for _ in range(m)] for _ in range(n)]
    kierunki = {"N": (-1, 0, "S"), "E": (0, 1, "W"), "S": (1, 0, "N"), "W": (0, -1, "E")}
    
    def dfs(x, y):
        labirynt[x][y]["visited"] = True
        kierunki_losowe = list(kierunki.keys())
        random.shuffle(kierunki_losowe)

        for kierunek in kierunki_losowe:
            dx, dy, przeciwna_sciana = kierunki[kierunek]
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not labirynt[nx][ny]["visited"]:
                # Usuwamy ściany, aby utworzyć przejście
                labirynt[x][y]["walls"][kierunek] = False
                labirynt[nx][ny]["walls"][przeciwna_sciana] = False
                dfs(nx, ny)
    
    # Startujemy DFS od punktu startowego
    dfs(start[0], start[1])

    # Oznaczamy ścieżkę rozwiązania do mety
    sciezka = []
    def znajdz_sciezke(x, y):
        if (x, y) == meta:
            sciezka.append((x, y))
            return True
        
        labirynt[x][y]["visited"] = False
        for kierunek, (dx, dy, _) in kierunki.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not labirynt[x][y]["walls"][kierunek] and labirynt[nx][ny]["visited"]:
                if znajdz_sciezke(nx, ny):
                    sciezka.append((x, y))
                    return True
        return False

    znajdz_sciezke(meta[0], meta[1])

    return labirynt, sciezka

# Parametry
n, m = 5, 5  # Rozmiar labiryntu
start = (0, 0)  # Punkt startowy
meta = (4, 4)  # Punkt końcowy

labirynt, sciezka = generuj_labirynt(n, m, start, meta)

# Wyświetlanie wyników
print("Ścieżka rozwiązania:", sciezka)
print("Labirynt (True = ściana, False = przejście):")
for x in range(n):
    for y in range(m):
        print(f"({x},{y}): {labirynt[x][y]['walls']}", end="  ")
    print()

