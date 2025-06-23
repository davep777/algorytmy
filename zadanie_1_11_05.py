
#permutacje

def permutacje(string, wynik=""):
    if not string: #jeśli jest pusty i można wypisać
        print(wynik)
        return
    for i in range(len(string)):
        permutacje(string[:i] + string[i+1:], wynik + string[i])

permutacje("abc")

#bc, a -> c, ab -> abc itd.

#konwersja liczby całkowitej na zapis binarny

def binarne(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binarne(n // 2) + str(n % 2)

print(binarne(10))

#labirynt

def znajdz_sciezke(labirynt, x, y, sciezka=[]):
    if x < 0 or y < 0 or x >=len(labirynt) or y >= len(labirynt[0]) or labirynt[x][y] == 1: #wyjście poza granicę albo ściana
        return None

    if (x, y) in sciezka:
        return None #jeśli już byliśmy

    sciezka.append((x,y)) #dodajemy współrzędne

    if(x,y) == (len(labirynt)-1, len(labirynt[0])-1):
        return sciezka #jesli dotarliśmy, wiersz, kolumna

    # prawo, dół, lewo, góra, x wiersze(kierunek pion) y kolumny(kierunek poziom)
    for dx, dy in [(0,1), (1,0), (0, -1), (-1, 0)]:
        wynik = znajdz_sciezke(labirynt, x + dx, y + dy, sciezka.copy()) #nowe współrzędne
        if wynik:
            return wynik

    return None

maze = [[0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]]

print(znajdz_sciezke(maze, 0, 0))  # Przykładowe wywołanie
