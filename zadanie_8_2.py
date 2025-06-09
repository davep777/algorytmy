import random

def generuj_graf_losowy(n):
    """Generuje losowy graf spójny w postaci listy krawędzi."""
    krawedzie = set()
    wierzcholki = list(range(n))
    random.shuffle(wierzcholki)

    for i in range(n - 1):
        krawedzie.add((wierzcholki[i], wierzcholki[i + 1]))

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

def znajdz_cykle_dfs(graf):
    """Wykrywa wszystkie cykle w grafie nieskierowanym za pomocą DFS, deduplikując cykle."""
    
    def dfs(v, parent):
        sciezka.append(v)
        odwiedzone.add(v)

        for sasiad in graf[v]:
            if sasiad == parent:
                continue
            if sasiad in sciezka:
                cykl = sciezka[sciezka.index(sasiad):]  # Znaleziony cykl
                zbior_cykli.add(tuple(sorted(cykl)))  # Deduplikacja poprzez sortowanie
            elif sasiad not in odwiedzone:
                dfs(sasiad, v)

        sciezka.pop()  # Cofanie się po zakończeniu eksploracji

    odwiedzone = set()
    zbior_cykli = set()
    
    for v in range(len(graf)):
        if v not in odwiedzone:
            sciezka = []
            dfs(v, -1)

    return [list(cykl) for cykl in zbior_cykli]



n = 6  # Liczba wierzchołków w grafie
graf_krawedzie = generuj_graf_losowy(n)
graf_lista = krawedzie_do_listy(graf_krawedzie, n)

print("Lista krawędzi:", graf_krawedzie)
print("Lista sąsiedztwa:", graf_lista)
print("Wykryte cykle:", znajdz_cykle_dfs(graf_lista))

