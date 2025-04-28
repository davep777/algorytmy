import random

# Zmienna globalna do zliczania porównań
comparisons = 0

def insertion_sort(arr, left, right):
    """
    Sortuje fragment tablicy arr[left:right] używając sortowania przez wstawianie.
    Zlicza porównania wykonane przy sprawdzaniu warunku (czy element po lewej jest większy od klucza).
    """
    global comparisons
    # Iterujemy od drugiego elementu w danym fragmencie
    for i in range(left + 1, right):
        key = arr[i]
        j = i - 1
        while j >= left:
            comparisons += 1  # liczymy każde porównanie: arr[j] > key
            if arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = key

def merge(arr, left, mid, right):
    """
    Scala dwie posortowane części tablicy: arr[left:mid] oraz arr[mid:right].
    Podczas scalania zlicza porównania między elementami obu podtablic.
    """
    global comparisons
    left_part = arr[left:mid]
    right_part = arr[mid:right]
    
    i = j = 0
    k = left
    # Dopóki oba fragmenty mają jeszcze elementy, wybieramy mniejszy
    while i < len(left_part) and j < len(right_part):
        comparisons += 1  # porównanie między left_part[i] i right_part[j]
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    # Przepisujemy pozostałe elementy – tu nie dokonujemy porównań
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort_runs(arr, run_size):
    """
    Funkcja sortuje tablicę 'arr' w dwóch etapach:
      1. Dzieli tablicę na fragmenty o długości 'run_size'. Każdy fragment sortuje przy użyciu insertion_sort.
      2. Następnie scala posortowane fragmenty metodą przypominającą merge sort. 
         W obu etapach zliczamy porównania.
    """
    n = len(arr)
    # Sortowanie poszczególnych fragmentów (runów) za pomocą insertion sort
    for start in range(0, n, run_size):
        end = min(start + run_size, n)
        insertion_sort(arr, start, end)
    
    # Skalowanie: zaczynamy łączyć posortowane runy o długości run_size, potem 2*run_size itd.
    current_run_size = run_size
    while current_run_size < n:
        for left in range(0, n, 2 * current_run_size):
            mid = min(left + current_run_size, n)
            right = min(left + 2 * current_run_size, n)
            if mid < right:
                merge(arr, left, mid, right)
        current_run_size *= 2

# Funkcje pomocnicze do generowania tablic o różnych strukturach

def generate_random_array(n):
    """Generuje tablicę losowych liczb całkowitych z przedziału 0-100 o rozmiarze n."""
    return [random.randint(0, 100) for _ in range(n)]

def generate_sorted_array(n):
    """Generuje już posortowaną tablicę od 0 do n-1."""
    return list(range(n))

def generate_reverse_array(n):
    """Generuje tablicę posortowaną w kolejności malejącej (od n do 1)."""
    return list(range(n, 0, -1))

def generate_partially_sorted_array(n, swap_count=5):
    """
    Generuje tablicę prawie posortowaną:
    - Zaczynamy od tablicy posortowanej.
    - Następnie wykonujemy kilka losowych zamian elementów (domyślnie 5 zamian),
      aby wprowadzić niewielkie zakłócenia.
    """
    arr = list(range(n))
    for _ in range(swap_count):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Funkcja do testowania algorytmu na różnych typach tablic i run_size

def test_sorting(array_generator, n, run_sizes, description):
    global comparisons
    print(f"\nTest: {description}, rozmiar tablicy: {n}")
    for run_size in run_sizes:
        arr = array_generator(n)  # generujemy tablicę wg danego wzorca
        comparisons = 0  # resetujemy licznik porównań
        merge_sort_runs(arr, run_size)
        print(f"  Run size = {run_size:3d} -> Porównań: {comparisons}")

# Główna część skryptu wykonawcza
if __name__ == "__main__":
    # Ustal rozmiar tablicy
    n = 50  # można zmieniać np. na 100, 200, etc.
    # Lista wybranych rozmiarów runów do eksperymentów
    run_sizes = [1, 5, 10, 20]

    # Testujemy algorytm na różnych strukturach danych:
    test_sorting(generate_sorted_array, n, run_sizes, "Tablica już posortowana")
    test_sorting(generate_partially_sorted_array, n, run_sizes, "Tablica częściowo posortowana")
    test_sorting(generate_random_array, n, run_sizes, "Tablica losowa")
    test_sorting(generate_reverse_array, n, run_sizes, "Tablica odwrotna")
