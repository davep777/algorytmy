from collections import deque
from datetime import datetime

class Powiadomienie:
    def __init__(self, tresc, typ, priorytet):
        """
        :param tresc: Treść powiadomienia (np. "Masz nowe zadanie!")
        :param typ: Typ powiadomienia (np. "info", "warning", "error")
        :param priorytet: Priorytet powiadomienia – przyjmujemy:
                          "pilne" - wysoki priorytet, ma być wyświetlone jako pierwsze,
                          dowolna inna wartość (np. "niski") – powiadomienie standardowe.
        """
        self.tresc = tresc
        self.typ = typ
        self.priorytet = priorytet.lower()
        self.znacznik_czasu = datetime.now()

    def __str__(self):
        return f"[{self.znacznik_czasu:%Y-%m-%d %H:%M:%S}] ({self.typ}) {self.tresc} - priorytet: {self.priorytet}"


class SystemPowiadomien:
    def __init__(self, limit_niskich=5):
        """
        :param limit_niskich: Maksymalna liczba powiadomień o najniższym priorytecie,
                              przechowywanych w kolejce. Gdy limit zostanie przekroczony,
                              usuwane są najstarsze spośród tych powiadomień.
        """
        self.urgent_queue = deque()      # Kolejka dla powiadomień o priorytecie "pilne"
        self.low_priority_queue = deque()  # Kolejka dla pozostałych powiadomień
        self.limit_niskich = limit_niskich

    def dodaj_powiadomienie(self, powiadomienie):
        """
        Dodaje nowe powiadomienie do systemu – jeśli jest pilne, trafia do kolejki priorytetowej,
        w przeciwnym razie do kolejki standardowej (niski priorytet).
        Po dodaniu sprawdzany jest limit powiadomień niskiego priorytetu.
        """
        if powiadomienie.priorytet == "pilne":
            # Powiadomienia pilne dodajemy do kolejki, zachowując FIFO (newest wraca z tyłu)
            self.urgent_queue.append(powiadomienie)
        else:
            # Powiadomienia o niższym priorytecie dodajemy na koniec swojej kolejki
            self.low_priority_queue.append(powiadomienie)
            # Jeśli liczba powiadomień niskiego priorytetu przekracza limit, usuwamy najstarsze
            if len(self.low_priority_queue) > self.limit_niskich:
                usuniete = self.low_priority_queue.popleft()
                print(f"Limit powiadomień niskiego priorytetu przekroczony – usunięto najstarsze powiadomienie:\n  {usuniete}")

        self.wyswietl_ilosc_oczekujacych()

    def pobierz_nastepne_powiadomienie(self):
        """
        Pobiera (i usuwa) następne powiadomienie w kolejce zgodnie z zasadą FIFO:
         - Najpierw zwracane są powiadomienia pilne,
         - Następnie te o niższym priorytecie.
        Jeśli żadnych powiadomień nie ma, zwraca None.
        """
        if self.urgent_queue:
            return self.urgent_queue.popleft()
        elif self.low_priority_queue:
            return self.low_priority_queue.popleft()
        else:
            return None

    def wyswietl_ilosc_oczekujacych(self):
        """
        Wyświetla i zwraca łączną liczbę powiadomień, które oczekują na wyświetlenie.
        """
        l_urgent = len(self.urgent_queue)
        l_low = len(self.low_priority_queue)
        total = l_urgent + l_low
        print(f"Liczba oczekujących powiadomień: {total}  (Pilne: {l_urgent}, Niski: {l_low})")
        return total

    def wyswietl_kolejke(self):
        """
        Pomocnicza metoda: wyświetla wszystkie powiadomienia w kolejce według kolejności ich wyświetlenia.
        """
        print("Obecna kolejka powiadomień:")
        for powiadomienie in list(self.urgent_queue) + list(self.low_priority_queue):
            print(f"  {powiadomienie}")


# Przykładowe użycie systemu powiadomień
if __name__ == '__main__':
    system = SystemPowiadomien(limit_niskich=3)  # Ustawiamy limit dla powiadomień niskiego priorytetu

    # Dodajemy kilka powiadomień – zarówno pilnych, jak i standardowych
    system.dodaj_powiadomienie(Powiadomienie("Masz nowe zadanie!", "info", "niski"))
    system.dodaj_powiadomienie(Powiadomienie("Ostrzeżenie: Niski poziom baterii", "warning", "niski"))
    system.dodaj_powiadomienie(Powiadomienie("Błąd połączenia", "error", "pilne"))
    system.dodaj_powiadomienie(Powiadomienie("Nowa wiadomość", "info", "niski"))
    system.dodaj_powiadomienie(Powiadomienie("Alert systemowy", "error", "pilne"))
    # Dodanie kolejnego powiadomienia niskiego priorytetu spowoduje przekroczenie limitu,
    # więc najstarsze powiadomienie niskiego priorytetu zostanie usunięte.
    system.dodaj_powiadomienie(Powiadomienie("Aktualizacja systemu", "info", "niski"))

    system.wyswietl_kolejke()

    print("\nWyświetlanie powiadomień:")
    while system.wyswietl_ilosc_oczekujacych() > 0:
        powiad = system.pobierz_nastepne_powiadomienie()
        if powiad:
            print(f"Wyświetlono: {powiad}")
