
#Drzewo BPlus

class Wezel:
    def __init__(self, czy_lisc=True):
        self.klucze = [] #wynik i nazwa gracza
        self.dzieci = []
        self.czy_lisc = czy_lisc
        self.nastepny : "Wezel | None" = None

class Drzewo: 
    def __init__(self):
        self.korzen = Wezel(czy_lisc=False)
        self.lisc1 = Wezel()
        self.lisc2 = Wezel()
        self.lisc1.nastepny = self.lisc2
        self.korzen.dzieci = [self.lisc1, self.lisc2]

    def dodaj(self, klucz, wartosc):
        docelowy_lisc = self.lisc1 if klucz < 50 else self.lisc2
        docelowy_lisc.klucze.append((klucz, wartosc))
        docelowy_lisc.klucze.sort()

    def wyszukaj(self, klucz):
        for lisc in [self.lisc1, self.lisc2]:
            for k, v in lisc.klucze:
                if k == klucz:
                    return v
        return None

    def usun(self, wartosc):
        for lisc in [self.lisc1, self.lisc2]:
            nowe_klucze = []
            for k, v in lisc.klucze:
                if v != wartosc: #jeśli to nie ten gracz, zapisuje
                    nowe_klucze.append((k,v))
            lisc.klucze = nowe_klucze

    def zakres_wyszukaj(self, min_klucz, max_klucz):
        wyniki = []
        lisc = self.lisc1
        while lisc:
            for k,v in lisc.klucze:
                if min_klucz <= k <= max_klucz:
                    wyniki.append((k,v))
            lisc = lisc.nastepny
        return wyniki

    def aktualizuj(self, wartosc, nowy_wynik):
        for lisc in [self.lisc1, self.lisc2]:
            for i in range(len(lisc.klucze)): #iterowanie indexów
                k, v = lisc.klucze[i] #pobranie k i v
                if v == wartosc:
                    lisc.klucze[i] = (nowy_wynik, v)
                    lisc.klucze.sort()
                    return


#dodanie graczy
drzewo = Drzewo()
drzewo.dodaj(10, "Gracz_A")
drzewo.dodaj(20, "Gracz_B")
drzewo.dodaj(60, "Gracz_C")

#wyszukiwanie po wyniki
print(drzewo.wyszukaj(10))

#wyszukiwanie po zakresie
print(drzewo.zakres_wyszukaj(5,70))

#usuwanie gracza
drzewo.usun("Gracz_C")
print(drzewo.wyszukaj(60))

#aktualizacja gracza
drzewo.aktualizuj("Gracz_B", 25)
#wynik po aktualizacji
print(drzewo.wyszukaj(25))
