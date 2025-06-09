import random

def generuj_graf_losowy(n):
    """Generuje losowy graf spójny w postaci listy krawędzi."""
    krawedzie = set()
    
    # Tworzenie podstawowej struktury grafu spójnego - połączenie wszystkich wierzchołków
    wierzcholki = list(range(n))
    random.shuffle(wierzcholki)
    
    for i in range(n - 1):
        krawedzie.add((wierzcholki[i], wierzcholki[i + 1]))

    # Dodanie dodatkowych krawędzi
    maks_krawedzi = random.randint(n - 1, n * (n - 1) // 2)
    while len(krawedzie) < maks_krawedzi:
        u, v = random.sample(range(n), 2)
        if u != v and (u, v) not in krawedzie and (v, u) not in krawedzie:
            krawedzie.add((u, v))
    
    return list(krawedzie)

def krawedzie_do_listy(krawedzie, n):
    """Konwertuje listę krawędzi na listę sąsiedztwa."""
    lista_sasiedztwa = [[] for _ in range(n)]
    for u, v in krawedzie:
        lista_sasiedztwa[u].append(v)
        lista_sasiedztwa[v].append(u)
    return lista_sasiedztwa

def krawedzie_do_macierzy(krawedzie, n):
    """Konwertuje listę krawędzi na macierz sąsiedztwa."""
    macierz = [[0] * n for _ in range(n)]
    for u, v in krawedzie:
        macierz[u][v] = 1
        macierz[v][u] = 1
    return macierz

# Przykładowe użycie:
n = 5  # Liczba wierzchołków
graf_krawedzie = generuj_graf_losowy(n)

print("Lista krawędzi:", graf_krawedzie)
print("Lista sąsiedztwa:", krawedzie_do_listy(graf_krawedzie, n))
print("Macierz sąsiedztwa:")
for wiersz in krawedzie_do_macierzy(graf_krawedzie, n):
    print(wiersz)

