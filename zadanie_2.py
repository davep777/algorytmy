# a)Masz daną tablicę liczb całkowitych, 
# przesuń wszystkie liczby ujemne na początek, zachowując kolejność liczb dodatnich i ujemnych.


def przesuwanie(tablica):
    ujemne = 0
    for i in range(len(tablica)):
        if tablica[i] < 0:
            ujemne +=1
    
    nowa_tablica = [0] * len(tablica)
    index_ujemne = 0
    index_dodatnie = ujemne
    for i in range(len(tablica)):
        if tablica[i] < 0:
            nowa_tablica[index_ujemne] = tablica[i]
            index_ujemne +=1
        else:
            nowa_tablica[index_dodatnie] = tablica[i]
            index_dodatnie += 1
    return nowa_tablica
   
tablica = [1,-2,-3,4,5,6,7,8,-9]
print(przesuwanie(tablica))

print("\n")

#b) Masz daną tablicę o rozmiarze n-1, zawierającą unikalne liczby w zakresie od 1 do n. 
# Jedna z liczb jest brakująca.
#  Znajdź brakującą liczbę.

def znajdz_liczbe(tab, n):
    suma_liczb = 0
    for i in range(1,n+1):
        suma_liczb += i

    suma_tablicy = 0
    for i in range(len(tablica)):
        suma_tablicy += tablica[i]

    brakujaca = suma_liczb - suma_tablicy
    return brakujaca

tab = [1,2,3,5,6]
n = 6
print("Brakująca liczba to: ", znajdz_liczbe(tab, n))

print("\n")

# c)Mając daną tablicę liczb całkowitych,
#  znajdź i zwróć duplikaty w tej tablicy.


def szuka_duplikat(tabb):
    duplikaty = [0] *len(tabb)
    index_duplikaty = 0

    for i in range(len(tabb)):
        for j in range(i+1, len(tabb)):
            if tabb[i] == tabb[j]:
                czy_dodano = False
                for k in range(index_duplikaty):
                    if duplikaty[k] == tabb[i]:
                        czy_dodano = True
                        break
                if not czy_dodano:
                    duplikaty[index_duplikaty] = tabb[i]
                    index_duplikaty +=1

    wynik = [0] * index_duplikaty
    for i in range(index_duplikaty):
         wynik[i] = duplikaty[i]
    return wynik
    
      
zbior = [1,1,2,3,3,5,2,6,8]
print("Znalezione duplikaty: ", szuka_duplikat(zbior))

print("\n")

# d) Obróć tablicę o rozmiarze n.

def obracanie(table):
    i = 0
    j = len(table) -1

    while i < j:
        zapasowa = table[i]
        table[i] = table[j]
        table[j] = zapasowa

        i += 1
        j -= 1
    return table

table = [1,2,3,4,5,6,7]
print(f"Odwrócona tablica : {obracanie(table)}")



