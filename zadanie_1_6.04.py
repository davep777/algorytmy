class HistoriaAkcji:
    def __init__(self):
        self.stos_undo = []  # Stos przechowujący wykonane akcje
        self.stos_redo = []  # Stos przechowujący cofnięte akcje

    def wykonaj_akcje(self, akcja):
        """
        Wykonuje nową akcję: dodaje ją do historii i czyści historię możliwych ponowień.
        """
        self.stos_undo.append(akcja)
        self.stos_redo.clear()  # Po wykonaniu nowej akcji nie można ponowić wcześniejszych cofnięć
        print(f"Wykonano akcję: {akcja}")

    def cofnij(self):
        """
        Cofnięcie ostatniej wykonanej akcji.
        Usuwa akcję ze stosu wykonanych działań i dodaje ją do stosu ponowień.
        """
        if not self.stos_undo:
            print("Brak akcji do cofnięcia!")
            return
        akcja = self.stos_undo.pop()
        self.stos_redo.append(akcja)
        print(f"Cofnięto akcję: {akcja}")

    def ponow(self):
        """
        Ponowne wykonanie ostatnio cofniętej akcji.
        Usuwa akcję ze stosu ponowień i przywraca ją do stosu wykonanych działań.
        """
        if not self.stos_redo:
            print("Brak akcji do ponowienia!")
            return
        akcja = self.stos_redo.pop()
        self.stos_undo.append(akcja)
        print(f"Ponownie wykonano akcję: {akcja}")

    def usun(self):
        """
        Usunięcie ostatniej wykonanej akcji z historii.
        Akcja jest usuwana bez możliwości cofnięcia lub ponowienia.
        """
        if not self.stos_undo:
            print("Brak akcji do usunięcia!")
            return
        akcja = self.stos_undo.pop()
        print(f"Usunięto akcję: {akcja}")


# Przykład użycia
if __name__ == '__main__':
    historia = HistoriaAkcji()

    # Symulujemy wykonanie kilku akcji w aplikacji
    historia.wykonaj_akcje("Dodano tekst")
    historia.wykonaj_akcje("Wstawiono obrazek")
    historia.wykonaj_akcje("Zmieniono rozmiar czcionki")
    
    # Cofamy ostatnią akcję
    historia.cofnij()         # Cofnięto: Zmieniono rozmiar czcionki

    # Ponawiamy cofniętą akcję
    historia.ponow()          # Ponownie wykonano: Zmieniono rozmiar czcionki

    # Usuwamy ostatnią akcję
    historia.usun()           # Usunięto: Zmieniono rozmiar czcionki

    # Cofamy kolejną akcję
    historia.cofnij()         # Cofnięto: Wstawiono obrazek
