import random
from datetime import datetime, timedelta

# Funkcja zapisująca wizytę w danej lokalizacji.
def add_visit(visit_dict: dict, location: tuple, visit_time: datetime = None):
    """
    Dodaje czas wizyty do słownika.

    Parametry:
      - visit_dict: słownik, gdzie kluczem jest krotka reprezentująca lokalizację,
        a wartością lista wizyt (datetime).
      - location: krotka (lat, lon), np. (52.23, 21.01)
      - visit_time: obiekt datetime; jeśli None, przyjmujemy datetime.now()
    """
    if visit_time is None:
        visit_time = datetime.now()

    # Jeśli lokalizacja już występuje – dopisujemy nową wizytę
    if location in visit_dict:
        visit_dict[location].append(visit_time)
    else:
        visit_dict[location] = [visit_time]

# Funkcja przeszukująca słownik i zwracająca listę lokalizacji, w których
# użytkownik był w podany dzień.
def locations_on_day(visit_dict: dict, target_day: datetime.date) -> list:
    """
    Zwraca listę lokalizacji, w których zapisana jest chociaż jedna wizyta w danym dniu.
    
    Parametry:
      - visit_dict: słownik z wizytami (klucz: lokalizacja, wartość: lista datetime)
      - target_day: obiekt datetime.date określający dzień, którego szukamy.
    """
    result = []
    for location, times in visit_dict.items():
        # Jeśli choć jedna z wizyt dla danej lokalizacji przypada na target_day,
        # to dodajemy lokalizację do wyniku.
        for t in times:
            if t.date() == target_day:
                result.append(location)
                break
    return result

# Przygotowujemy listę 10 przykładowych lokalizacji (współrzędne z dwoma miejscami po przecinku)
locations = [
    (52.14, 21.00),
    (52.23, 21.01),
    (52.34, 21.10),
    (52.45, 21.20),
    (52.56, 21.30),
    (52.67, 21.40),
    (52.78, 21.50),
    (52.89, 21.60),
    (52.90, 21.70),
    (53.00, 21.80)
]

# Inicjalizujemy słownik, który będzie pełnił rolę hashmapy z wizytami.
location_visits = {}

# Ustalamy bazowy czas – np. startujemy od konkretnej daty.
current_time = datetime(2025, 5, 9, 20, 55)

# Symulacja ok. 25 wywołań funkcji add_visit:
# W każdej iteracji losujemy jedną lokalizację z listy.
# Po każdej wizycie aktualizujemy current_time – co 5 wizyt dodamy dzień,
# w pozostałych przypadkach zmieniamy czas o 8 bądź 12 godzin.
for i in range(25):
    loc = random.choice(locations)
    add_visit(location_visits, loc, current_time)
    
    # Aktualizujemy current_time. Aby uzyskać "zmieszany" przyrost czasu:
    if (i + 1) % 5 == 0:
        current_time += timedelta(days=1)  # co piąta wizyta – nowy dzień
    elif (i + 1) % 2 == 0:
        current_time += timedelta(hours=8)
    else:
        current_time += timedelta(hours=12)

# Dla celów demonstracyjnych: wyświetlamy zawartość całej hashmapy.
print("Hashmapa z wizytami (lokalizacja -> lista wizyt):")
for loc, times in location_visits.items():
    times_str = ", ".join(t.strftime("%Y-%m-%d %H:%M") for t in times)
    print(f"{loc}: [{times_str}]")

# Przykład przeszukania – wybieramy jeden z dni, w których mogły wystąpić wizyty.
# Wyświetlimy lokalizacje, w których użytkownik był np. 2025-05-10
target_date = datetime(2025, 5, 10).date()
visited_locs = locations_on_day(location_visits, target_date)
print("\nLokalizacje odwiedzone w dniu", target_date, ":", visited_locs)

# ---------------------------------------------------------------------
# Złożoność wyszukiwania:
#
# Aby znaleźć lokalizacje, w których użytkownik był w danym dniu,
# funkcja `locations_on_day` iteruje po każdym kluczu (lokalizacji) w hashmapie.
# Jeśli mamy N lokalizacji, a dla każdej lokalizacji średnio zapisano M wizyt,
# to w najgorszym przypadku wykonamy O(N * M) operacji.
#
# W typowej implementacji operacje klucz->wartość w hashmapie mają średnio O(1),
# ale ponieważ wyszukiwanie odbywa się przez przeszukanie wartości (listy wizyt),
# całkowity koszt jest liniowy względem łącznej liczby zapisanych wizyt.
# ---------------------------------------------------------------------
print("\nZłożoność obliczeniowa wyszukiwania po wartościach hashmapy wynosi O(n * m),")
print("gdzie n to liczba kluczy (lokalizacji), a m to średnia liczba wizyt przypadających na daną lokalizację.")
