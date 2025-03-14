#algorytm O(1)

def suma(x):
    liczba_krokow = 0
    wynik = x + 10
    liczba_krokow = liczba_krokow + 1
    return wynik, liczba_krokow

print(suma(1))

for x in [100,1000,10000]:
   wynik, liczba_krokow = suma(x)
   print(f"Wynik wynosi: {wynik}, Liczba kroków wynosi: {liczba_krokow}")

print("\n")

# algorytm O(n)

def suma_tablicy(tablica):
    suma = 0
    kroki = 0
    for i in tablica:
        suma+=i
        kroki+=1
    return suma, kroki

tablice = [list(range(100)),list(range(1000)),list(range(1000000))]

for tablica in tablice:
    suma, kroki = suma_tablicy(tablica)
    print(f"Suma wynosi: {suma}, liczba kroków wynosi: {kroki}")

print("\n")

# algorytm O(n^2)

def porownanie(n):
    krok = 0
    tab = list(range(n))
    for i in range(n):
        for j in range(n):
            if i != j:
                krok+=1
    return krok


for n in [10,100,1000]:
    krok = porownanie(n)
    print(f"n = {n}, liczba kroków wynosi: {krok}")

print("\n")

# algorytm O(a^n)

def fib(f):
    ile_krokow = 0
    if f <= 1:
        ile_krokow +=1
        return f, ile_krokow
    else:
        ile_krokow +=1
        a, ile_krokow_a = fib(f-1)
        b, ile_krokow_b = fib(f-2)
        ile_krokow = ile_krokow + ile_krokow_a + ile_krokow_b
    return a+b, ile_krokow

dane = [1,10,20]
for f in dane:
    wyniki, ile_krokow = fib(f)
    print(f"f wynosi: {f}, wynik: {wyniki}, liczba kroków wynosi: {ile_krokow} ")




