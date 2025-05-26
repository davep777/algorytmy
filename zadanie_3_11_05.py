# 1. Zwykły blur (średnia wartość otaczających pikseli)
def blur(obraz):
    szerokosc = len(obraz)  # Pobranie szerokości obrazu
    wysokosc = len(obraz[0])  # Pobranie wysokości obrazu
    nowy_obraz = [[0] * wysokosc for _ in range(szerokosc)]  # Tworzenie nowego obrazu (macierz)

    for x in range(szerokosc):
        for y in range(wysokosc):
            suma = 0
            licznik = 0
            # Przechodzenie po sąsiadujących pikselach w macierzy 3x3
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < szerokosc and 0 <= ny < wysokosc:  # Sprawdzenie, czy piksel nie wychodzi poza obraz
                        suma += obraz[nx][ny]  # Dodanie wartości piksela do sumy
                        licznik += 1  # Liczenie ilości pikseli w okolicy
            
            nowy_obraz[x][y] = suma // licznik  # Obliczenie średniej wartości

    return nowy_obraz


# 2. Blur Gaussa (średnia ważona otaczających pikseli)
def blur_gauss(obraz):
    szerokosc = len(obraz)
    wysokosc = len(obraz[0])
    nowy_obraz = [[0] * wysokosc for _ in range(szerokosc)]
    
    # Macierz wag dla filtru Gaussa
    macierz_gaussa = [[1, 2, 1], 
                      [2, 4, 2], 
                      [1, 2, 1]]
    
    for x in range(szerokosc):
        for y in range(wysokosc):
            suma = 0
            suma_wag = 0
            # Przechodzenie po sąsiadujących pikselach z wagami
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < szerokosc and 0 <= ny < wysokosc:  # Sprawdzenie granic
                        waga = macierz_gaussa[dx + 1][dy + 1]  # Pobranie wagi z macierzy
                        suma += obraz[nx][ny] * waga  # Pomnożenie wartości piksela przez wagę
                        suma_wag += waga  # Sumowanie wag
            
            nowy_obraz[x][y] = suma // suma_wag  # Obliczenie średniej ważonej

    return nowy_obraz


# 3. Przekształcenie obrazu na obraz binarny (thresholding)
def thresholding(obraz, prog):
    szerokosc = len(obraz)
    wysokosc = len(obraz[0])
    nowy_obraz = [[0] * wysokosc for _ in range(szerokosc)]  # Tworzenie nowej macierzy obrazu

    for x in range(szerokosc):
        for y in range(wysokosc):
            # Jeśli wartość piksela jest większa lub równa progowi, ustaw na 1 (czarny)
            # Jeśli mniejsza, ustaw na 0 (biały)
            nowy_obraz[x][y] = 1 if obraz[x][y] >= prog else 0  

    return nowy_obraz


# Przykładowy obraz (odcienie szarości)
obraz = [
    [100, 120, 130, 150],
    [110, 140, 160, 170],
    [90, 100, 120, 130],
    [80, 90, 110, 120]
]

print("Zwykły blur:", blur(obraz))  # Testowanie funkcji blur
print("Blur Gaussa:", blur_gauss(obraz))  # Testowanie filtru Gaussa
print("Thresholding (próg = 120):", thresholding(obraz, 120))  # Testowanie binaryzacji obrazu

