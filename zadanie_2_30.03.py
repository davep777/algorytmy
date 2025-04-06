'''Mamy zbiór słów i chcemy sprawnie wyszukiwać wszystkie słowa zaczynające się od danego prefiksu. 
Zaimplementuj rozwiązanie za pomocą tablicy (array) oraz drzewa trie. Zapisz w każdej strukturze min. 100 słów (po polsku lub angielsku) 
i przygotuj wyszukiwanie po zadanym prefiksie – dodaj licznik kroków, 
określ złożoność czasową i pamięciową.'''

from faker import Faker

def szukanie_prefiks(slowa, prefix):
    kroki = 0
    rezultat =[]

    for slowo in slowa:
        kroki +=1
        if slowo.startswith(prefix):
            rezultat.append(slowo)
            kroki +=1

    return rezultat, kroki
    
#złożoność czasowa O(n)
#złożoność pamięciowa O(k) k to liczba pasujących wyników

faker = Faker("pl_PL")
lista_slow = [faker.word() for i in range(100)]
print(lista_slow)
print(szukanie_prefiks(lista_slow,"z"))

class TrieNode:
    def __init__(self):
        self.dziecko = {}
        self.koniec_slowa = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, slowo):
        node = self.root
        for i in slowo:
            if i not in node.dziecko:
                node.dziecko[i] = TrieNode()
            node = node.dziecko[i]

        node.koniec_slowa = True
    
    def szukanie_pref(self, prefix):
        kroki = 0
        node = self.root
        for i in prefix:
            if i in node.dziecko:
                node = node.dziecko[i]
                kroki +=1
            else:
                return [], kroki
        return self.szukanie_slow(node, prefix, [], kroki)
    
    def szukanie_slow(self, node, prefix, slowa, kroki):
        if node.koniec_slowa:
            slowa.append(prefix)
            kroki +=1

        for char, kolejny_node in node.dziecko.items():
            self.szukanie_slow(kolejny_node, prefix + char, slowa, kroki)
        
        return slowa, kroki
    

trie = Trie()
for slowo in lista_slow:
 trie.insert(slowo)

print(trie.szukanie_pref("z"))

    #złożoność czasowa O(m) m jako długość prefiksu
    #złożoność pamięciowa  O(n * l) n liczba słów, l średnia dł słowa

