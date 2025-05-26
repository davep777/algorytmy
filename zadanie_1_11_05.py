# 1. Generowanie wszystkich permutacji ciągu znaków
def permutacje(s, wynik=""):
    if len(s) == 0:  # Jeśli ciąg jest pusty, wypisz permutację
        print(wynik)
    else:
        for i in range(len(s)):  
            nowy_ciag = s[:i] + s[i+1:]  # Tworzenie nowego ciągu bez bieżącego znaku
            permutacje(nowy_ciag, wynik + s[i])  # Wywołanie rekurencyjne

permutacje("abc") # Przykład 


# 2. Konwersja liczby na zapis binarny
def binarny(n):
    if n == 0:  # Podstawa rekurencji - jeśli liczba to 0, zwróć "0"
        return "0"
    if n == 1:  # Jeśli liczba to 1, zwróć "1"
        return "1"
    return binarny(n // 2) + str(n % 2)  # Podział liczby na mniejsze części i dodanie reszty z dzielenia

print(binarny(10))  # Przykład


# 3. Znajdowanie ścieżki w labiryncie
def znajdz_sciezke(labirynt, x, y, sciezka=[]):
    if x < 0 or y < 0 or x >= len(labirynt) or y >= len(labirynt[0]) or labirynt[x][y] == 1:
        return None  # Sprawdzenie, czy współrzędne są poza granicami lub trafiły na ścianę
    
    if (x, y) in sciezka:  # Sprawdzenie, czy już odwiedzono to miejsce
        return None

    sciezka.append((x, y))  # Dodanie aktualnej pozycji do ścieżki

    if (x, y) == end:  # Jeśli dotarliśmy do celu, zwróć ścieżkę
        return sciezka

    kierunki = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Możliwe ruchy: prawo, dół, lewo, góra
    for dx, dy in kierunki:
        wynik = znajdz_sciezke(labirynt, x + dx, y + dy, sciezka.copy())  # Sprawdzenie kolejnych ruchów
        if wynik:
            return wynik  # Jeśli znaleziono ścieżkę, zwróć ją

    return None  # Jeśli nie znaleziono ścieżki, zwróć None

maze = [[0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]]

start = (0, 0)
end = (3, 3)

print(znajdz_sciezke(maze, start[0], start[1]))  #Przykładowy labirynt

