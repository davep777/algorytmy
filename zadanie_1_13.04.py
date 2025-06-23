#algorytm TimSort
#timsort dzieli tablicę na fragmenty, czyli runy, sortuje, a następnie je scala

#funkcja sortowania
def insertion_sort(tablica):
    porownania = 0
    for i in range(1, len(tablica)):
        klucz = tablica[i] #aktualna sprawdzana wartość
        j = i -1 #wartość wcześniejsza
        while j >= 0 and tablica[j] > klucz:
            porownania += 1
            tablica[j + 1] = tablica[j] #przesuwanie w prawo
            j = j - 1 #cofamy się w lewo
        tablica[j + 1] = klucz
    return porownania

#test działania insertion sort
#tab = [1,3,2]
#insertion_sort(tab)
#print(tab)

#funkcja scalania
def merge_sort(lewa, prawa):
    i = j = 0
    porownania = 0
    tablica = []
    while i < len(lewa) and j < len(prawa): #dopóki elementy iterowane są mniejsze
        porownania += 1
        if lewa[i] <= prawa[j]:
            tablica.append(lewa[i])
            i += 1
        else:
            tablica.append(prawa[j])
            j += 1

    tablica.extend(lewa[i:]) #extend dodaje elementy, append listę
    tablica.extend(prawa[j:])
    return tablica, porownania

#funkcja timsort
def timsort(tablica, rozmiar_runs):
    runs = [tablica[i:i + rozmiar_runs] for i in range(0, len(tablica), rozmiar_runs)] #dzielenie na runy, podtablice
    liczba_porownan = 0

    for i in runs: #sortowanie runów
        #insertion_sort(i)
        liczba_porownan += insertion_sort(i)
    

    while len(runs) > 1: #scalanie
        poloczone_runs = []
        for i in range(0, len(runs) - 1, 2):
            #poloczone_runs.append(merge_sort(runs[i], runs[i+1]))
            merged, porownania = merge_sort(runs[i], runs[i+1])
            poloczone_runs.append(merged)
            liczba_porownan +=porownania

        if len(runs) % 2 == 1:
            poloczone_runs.append(runs[-1])

        runs = poloczone_runs

    return runs[0] if len(runs) > 0 else [], liczba_porownan

testy = {
    "posortowana" : [1,2,3,4,5],
    "wstepnie_posortowana" : [1,2,4,3,5],
    "przypadkowa_kolejnosc" : [1,5,2,4,3],
    "odwrotna" : [5,4,3,2,1]
}

rozmiary_runs = [2,3]

for nazwa, tablica in testy.items():
    for rozmiar in rozmiary_runs:
        posortowana, porownania = timsort(tablica.copy(), rozmiar)
        print(f"Test: {nazwa}, Wielkość runy: {rozmiar}, Porównania: {porownania}")

#tablica = timsort(wstepnie_posortowana, 2)
#print(tablica)


