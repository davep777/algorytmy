import re

# HashMapa
class HashMapa:
    def __init__(self, rozmiar=26):  # 26 liter alfabetu
        self.rozmiar = rozmiar
        self.tablica = [0] * rozmiar  # tablica dla liter
    
    def hash(self, klucz):
        return sum(ord(znak) for znak in klucz) % self.rozmiar  # służy za index

    def dodaj(self, klucz):
        indeks = self.hash(klucz)  # oblicza indeks
        self.tablica[indeks] += 1  # zwieksza licznik dla litery

    def posortowane(self):
        litery = [chr(i + ord('a')) for i in range(self.rozmiar)]  # lista liter a-z 0+97, 0+98 itd.
        liczby = list(zip(litery, self.tablica))  # laczmy litery z liczba wystapien
        return sorted(liczby, key=lambda x: x[1], reverse=True)  # sortujemy

# Funkcja liczaca slowa w tekscie
def licz_slowa_po_literze(tekst):
    hash_mapa = HashMapa()
    slowa = re.findall(r'\b\w+\b', tekst.lower())  # usuwa interpunkcje i tworzy małe litery
    
    for slowo in slowa:
        pierwsza_litera = slowo[0]  # pobiera pierwszą literę
        hash_mapa.dodaj(pierwsza_litera)
    
    return hash_mapa.posortowane()  # sortowanie

# Test z przykladowym tekstem
tekst = """Lorem ipsum dolor sit amet. Ad alias odio ea rerum porro At modi quisquam. Quo neque dolorem ut quaerat dicta a Quis autem eum necessitatibus facere 33 quasi fuga aut ullam commodi. Et quia modi qui sequi magni eum unde iste cum accusantium pariatur! Ut quae cumque aut numquam ipsum aut incidunt autem. Aut culpa voluptas 33 deleniti temporibus et officiis galisum est aperiam aperiam est quasi vitae. Aut adipisci odit ab deserunt nulla qui quibusdam sunt aut nemo commodi aut maiores suscipit. Aut earum facere eum optio vero et beatae voluptatem. Ut eaque voluptas est nostrum voluptates ut omnis eaque id molestiae internos.
Sed rerum debitis ab velit porro ea voluptatem reiciendis a consequatur tenetur id galisum atque ut culpa perferendis? Eos voluptatum velit vel maiores rerum non sequi beatae sed quaerat laudantium non optio suscipit. Non porro galisum ut modi delectus et rerum quibusdam et mollitia praesentium et quas corrupti ut error soluta. Est velit nihil sed rerum deserunt aut dolores ipsa qui velit voluptatem. A exercitationem possimus non dolorem magnam et minus voluptatum nam aliquam nemo sit nisi omnis id necessitatibus voluptatum. Est illum fugiat ut magnam ipsa id ducimus dolores eos dolores tenetur vel consectetur accusamus aut modi dolor. Hic quia perspiciatis 33 mollitia saepe id exercitationem fugiat nam labore minima qui veniam autem est tempora cupiditate! Et libero dolorem a accusantium possimus id reprehenderit omnis ea dignissimos dolor et provident maxime et nemo dolor. Est aliquid debitis ex amet Quis ut quibusdam dolorem. Sit eius eaque ut consequuntur beatae sed voluptatem sunt cum tempore iste id temporibus nobis est nihil dolorum. Ut eveniet quia id quod neque hic quasi maxime aut animi voluptatibus ad eveniet minima sed illo ipsam. Aut magni facere ut culpa omnis sed tenetur impedit est totam enim et voluptatem delectus. Sed enim culpa ab consectetur expedita aut nostrum dicta aut incidunt voluptas ab rerum assumenda et consequatur dignissimos. In ducimus porro sed consequatur perspiciatis ad architecto accusamus! """
liczba_slow = licz_slowa_po_literze(tekst)
print(liczba_slow)

