'''Zaimplementuj wyszukiwanie najmniejszego i największego elementu w: tablicy posortowanej, 
tablicy nieposortowanej oraz BST - 
 dodaj licznik kroków, określ złożoność czasową i pamięciową.'''

def min_max_posortowana (tablica):
    kroki = 0
    min = tablica[0]
    kroki +=1
    max = tablica[-1]
    kroki +=1
    return min, max, kroki

#złożoność czasowa O(1)
#złoożoność pamięciowa O(1)


tab_posortowana = [0,1,2,3,4,5,6,7,8,9]
print(min_max_posortowana(tab_posortowana))


def min_max_nieposortowana (tablica):
    kroki = 0
    min = max = tablica[0]
    kroki +=1
    for i in tablica:
        kroki +=1
        if min < i:
           min = i
           kroki +=1
        elif max > i:
            max = i
            kroki +=1
    return max, min,kroki

tab_nieposortowana = [3,4,5,1,2,7,8,0,8,6,9]
print(min_max_nieposortowana(tab_nieposortowana))

#złożoność czasowa O(n)
#złożoność pamięciowa O(1)

class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewa = None
        self.prawa = None
def znajdz_min(node):
    kroki = 0
    while node.lewa:
        kroki +=1
        node = node.lewa
    return node.wartosc, kroki

def znajdz_max(node):
    kroki = 0
    while node.prawa:
        kroki +=1
        node = node.prawa
    return node.wartosc, kroki

root = Node(5)
root.lewa = Node(3)
root.prawa = Node(8)
root.lewa.lewa = Node(1)
root.lewa.prawa = Node(4)
root.prawa.lewa = Node(6)
root.prawa.prawa = Node(9)

print (znajdz_min(root))
print (znajdz_max(root))
        
#złożoność czasowa O(n), n wysokość drzewa
#złożoność pamięciowa O(1)