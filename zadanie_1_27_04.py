#!/usr/bin/env python3

# Funkcja haszująca - prosta metoda:
# Sumuje kody ASCII wszystkich znaków w ciągu,
# a następnie zwraca resztę z dzielenia przez rozmiar tablicy.
def simple_hash(key: str, table_size: int) -> int:
    ascii_sum = sum(ord(c) for c in key)
    return ascii_sum % table_size

# Funkcja haszująca oparta na metodzie Hornera:
# Traktuje ciąg znaków jako wielomian (przy podstawie 'a', tutaj 31).
# Dla ciągu "s0 s1 s2 ... sn" oblicza:
#    hash = (((s0 * a + s1) * a + s2) * a + ... + sn) mod table_size
def horner_hash(key: str, table_size: int) -> int:
    hash_value = 0
    a = 31  # stała – często wybierana jako liczba pierwsza
    for c in key:
        hash_value = (hash_value * a + ord(c)) % table_size
    return hash_value

# Funkcja haszująca DJB2:
# Inicjujemy hash wartością 5381, następnie dla każdego znaku
# wykonujemy: hash = ((hash << 5) + hash) + ord(c), czyli hash * 33 + ord(c).
# Na końcu stosujemy modulo, by uzyskać wartość w zakresie [0, table_size-1].
def djb2_hash(key: str, table_size: int) -> int:
    hash_value = 5381
    for c in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(c)  # równoważne: hash_value * 33 + ord(c)
    return hash_value % table_size

# Implementacja prostej HashMap wykorzystującej
# funkcję simple_hash do określenia indeksu.
# Używamy list jako "bucketów" do obsługi kolizji (łańcuchowanie).
class HashMap:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
    
    # Metoda put pozwala wstawić lub zaktualizować parę klucz-wartość.
    def put(self, key, value):
        index = simple_hash(key, self.capacity)
        bucket = self.buckets[index]
        # Jeśli klucz już istnieje, aktualizujemy wartość
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Jeśli klucza nie ma, dodajemy nową parę
        bucket.append((key, value))
    
    # Metoda get zwraca wartość dla danego klucza, lub None jeśli nie znaleziono.
    def get(self, key):
        index = simple_hash(key, self.capacity)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.buckets):
            result += f"Bucket {i}: {bucket}\n"
        return result

# Lista 25 podobnych stringów - przykładowe klucze (np. "klucz0", "klucz1", ..., "klucz24")
keys = [f"klucz{i}" for i in range(25)]

# Ustalony rozmiar tablicy dla funkcji haszujących (wybieramy 10 żeby pokazać kolizje)
table_size = 10

# Obliczamy hasze dla każdej funkcji z osobna,
# tworząc listę wyników
results = []
for key in keys:
    row = {
        "key": key,
        "simple": simple_hash(key, table_size),
        "horner": horner_hash(key, table_size),
        "djb2": djb2_hash(key, table_size)
    }
    results.append(row)

# Funkcja do ładnego wyświetlania wyników w formacie tabelarycznym
def print_table(rows):
    header = f"{'Klucz':>10} | {'Simple':>6} | {'Horner':>6} | {'DJB2':>6}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(f"{r['key']:>10} | {r['simple']:6} | {r['horner']:6} | {r['djb2']:6}")
    print()

print("Porównanie wyników funkcji haszujących:")
print_table(results)

# Obliczamy rozkład (liczebność w poszczególnych "bucketach")
def compute_distribution(hash_func):
    dist = {i: [] for i in range(table_size)}
    for key in keys:
        index = hash_func(key, table_size)
        dist[index].append(key)
    return dist

distrib_simple = compute_distribution(simple_hash)
distrib_horner = compute_distribution(horner_hash)
distrib_djb2   = compute_distribution(djb2_hash)

# Funkcja do wyświetlania rozkładu hashy
def print_distribution(name: str, dist: dict):
    print(f"Rozkład dla {name}:")
    print(f"{'Bucket':>6} | {'Liczba elementów':>17} | Klucze")
    print("-" * 50)
    for bucket, keys_list in dist.items():
        print(f"{bucket:>6} | {len(keys_list):>17} | {keys_list}")
    print()

print_distribution("Simple Hash", distrib_simple)
print_distribution("Horner Hash", distrib_horner)
print_distribution("DJB2 Hash", distrib_djb2)

# Przykład użycia HashMap opartej o simple_hash:
print("Przykład działania HashMap:")
hash_map = HashMap(capacity=table_size)
for key in keys:
    hash_map.put(key, f"Wartość dla {key}")

print(hash_map)
