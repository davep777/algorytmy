class BPlusTreeNode:
    def __init__(self, order, is_leaf=False):
        self.order = order          # maksymalna liczba kluczy w węźle
        self.is_leaf = is_leaf
        self.keys = []              # lista kluczy (wyników)
        if self.is_leaf:
            self.values = []        # lista list graczy – dla każdego klucza przechowujemy listę graczy z takim wynikiem
            self.next = None        # wskaźnik do następnego liścia (przydatny przy zapytaniach zakresowych)
        else:
            self.children = []      # lista wskaźników do dzieci (węzły wewnętrzne)


class BPlusTree:
    def __init__(self, order=4):
        self.order = order          # maksymalna liczba kluczy w węźle; liczba dzieci w węźle wewnętrznym może wynosić max order+1
        self.root = BPlusTreeNode(order, is_leaf=True)
        self.comparisons = 0        # licznik porównań wykonywanych przy operacjach

    def _find_leaf(self, key, node=None):
        """Znajduje liść, w którym powinien znajdować się klucz 'key'.  
        Każde porównanie klucza z elementami w węźle zwiększa licznik."""
        if node is None:
            node = self.root
        while not node.is_leaf:
            i = 0
            while i < len(node.keys):
                self.comparisons += 1
                if key < node.keys[i]:
                    break
                i += 1
            node = node.children[i]
        return node

    def _get_first_leaf(self):
        """Zwraca lewy (najmniejszy) liść drzewa."""
        node = self.root
        while not node.is_leaf:
            node = node.children[0]
        return node

    def add_player(self, nick, score):
        """
        Dodaje gracza o unikalnym nicku i wyniku 'score'.  
        Jeśli dany wynik już występuje, dodaje gracza do listy powiązanej z tym kluczem.
        Na końcu wykonuje ewentualne podziały (split) węzłów, jeśli zachodzi przepełnienie.
        """
        # Resetujemy licznik porównań przed operacją
        self.comparisons = 0
        self._insert(score, nick)

    def _insert(self, score, nick):
        """Procedura wstawiania – wyszukuje liść dla podanego wyniku, a następnie:
           • jeśli klucz już występuje – dodaje gracza do istniejącej listy,
           • w przeciwnym wypadku – wstawia nowy klucz wraz z listą [nick].
           Jeśli węzeł przekroczy maksymalną liczbę kluczy, wykonuje split."""
        leaf = self._find_leaf(score)
        i = 0
        inserted = False
        while i < len(leaf.keys):
            self.comparisons += 1  # porównanie score z kluczem w liściu
            if score == leaf.keys[i]:
                leaf.values[i].append(nick)
                inserted = True
                break
            elif score < leaf.keys[i]:
                break
            i += 1
        if not inserted:
            leaf.keys.insert(i, score)
            leaf.values.insert(i, [nick])
        # Jeśli liczba kluczy w liściu przekracza 'order', wykonaj dzielenie węzła
        if len(leaf.keys) > self.order:
            self._split_leaf(leaf)

    def _split_leaf(self, leaf):
        """Dzieli przepełniony liść – tworzy nowy liść i przenosi do niego połowę kluczy oraz powiązanych list graczy.
           Nowy klucz (pierwszy klucz nowego liścia) trafia do rodzica."""
        new_leaf = BPlusTreeNode(self.order, is_leaf=True)
        mid = (len(leaf.keys) + 1) // 2
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.values = leaf.values[mid:]
        leaf.keys = leaf.keys[:mid]
        leaf.values = leaf.values[:mid]
        new_leaf.next = leaf.next
        leaf.next = new_leaf
        if leaf == self.root:
            # Jeśli dzielony liść to korzeń – tworzymy nowy korzeń
            new_root = BPlusTreeNode(self.order, is_leaf=False)
            new_root.keys = [new_leaf.keys[0]]
            new_root.children = [leaf, new_leaf]
            self.root = new_root
        else:
            self._insert_in_parent(leaf, new_leaf.keys[0], new_leaf)

    def _insert_in_parent(self, left, key, right):
        """Wstawia klucz do rodzica danego podziału.  
        Szuka rodzica (funkcja _find_parent) i wstawia 'key' oraz nowy wskaźnik 'right'.
        Jeśli rodzic przepełni się, wykonuje split węzła wewnętrznego."""
        parent = self._find_parent(self.root, left)
        if parent is None:
            # Jeśli nie znaleziono rodzica – tworzymy nowy korzeń
            new_root = BPlusTreeNode(self.order, is_leaf=False)
            new_root.keys = [key]
            new_root.children = [left, right]
            self.root = new_root
            return
        index = parent.children.index(left)
        parent.keys.insert(index, key)
        parent.children.insert(index + 1, right)
        if len(parent.keys) > self.order:
            self._split_internal(parent)

    def _split_internal(self, node):
        """Dzieli węzeł wewnętrzny przepełniony kluczami.  
        Klucz środkowy jest "podnoszony" do poziomu wyższego."""
        new_internal = BPlusTreeNode(self.order, is_leaf=False)
        mid_index = len(node.keys) // 2
        up_key = node.keys[mid_index]
        new_internal.keys = node.keys[mid_index + 1:]
        new_internal.children = node.children[mid_index + 1:]
        node.keys = node.keys[:mid_index]
        node.children = node.children[:mid_index + 1]
        if node == self.root:
            new_root = BPlusTreeNode(self.order, is_leaf=False)
            new_root.keys = [up_key]
            new_root.children = [node, new_internal]
            self.root = new_root
        else:
            self._insert_in_parent(node, up_key, new_internal)

    def _find_parent(self, current, child):
        """Pomocnicza funkcja rekurencyjna – szuka rodzica węzła 'child' zaczynając od 'current'.
           Jeśli current jest liściem lub jego dzieci są liśćmi, zwraca None."""
        if current.is_leaf or current.children[0].is_leaf:
            return None
        for c in current.children:
            if c == child:
                return current
            else:
                res = self._find_parent(c, child)
                if res is not None:
                    return res
        return None

    def update_player(self, nick, new_score):
        """
        Aktualizuje wynik gracza – wyszukuje gracza (wg przeszukiwania liści) i usuwa go z poprzedniego wyniku,
        a następnie wstawia gracza z nowym wynikiem.
        """
        old_score = self.delete_player(nick)
        if old_score is not None:
            self._insert(new_score, nick)
            return old_score
        else:
            print("Gracz nie został znaleziony!")
            return None

    def get_player_score(self, nick):
        """
        Wyszukuje gracza wg nicku, przeszukując liście drzewa (zliczając porównania przy sprawdzaniu równości).
        Zwraca przypisany wynik lub None, gdy gracza nie ma.
        """
        self.comparisons = 0
        leaf = self._get_first_leaf()
        while leaf:
            for i, key in enumerate(leaf.keys):
                for player in leaf.values[i]:
                    self.comparisons += 1  # każde sprawdzenie równości player == nick
                    if player == nick:
                        return key
            leaf = leaf.next
        return None

    def query_range(self, low, high):
        """
        Zwraca listę graczy, których wyniki mieszczą się w przedziale [low, high].  
        Wyszukiwanie odbywa się przez znalezienie pierwszego liścia zawierającego wynik >= low,
        a następnie przeglądanie kolejnych liści poprzez wskaźnik next.
        Każde porównanie klucza w liściu zwiększa licznik.
        """
        self.comparisons = 0
        results = []
        leaf = self._find_leaf(low)
        while leaf:
            for key, players in zip(leaf.keys, leaf.values):
                self.comparisons += 1  # porównanie klucza
                if key < low:
                    continue
                if key > high:
                    return results
                results.extend(players)
            leaf = leaf.next
        return results

    def get_best(self):
        """
        Zwraca najlepszy wynik (maksymalny klucz) wraz z odpowiadającą listą graczy.
        Przechodzi do prawego, ostatniego liścia, a następnie wybiera ostatni klucz.
        """
        self.comparisons = 0
        node = self.root
        while not node.is_leaf:
            self.comparisons += 1
            node = node.children[-1]
        if node.keys:
            return node.keys[-1], node.values[-1]
        return None, []

    def get_worst(self):
        """
        Zwraca najgorszy wynik (minimalny klucz) wraz z odpowiadającą listą graczy.
        """
        self.comparisons = 0
        node = self._get_first_leaf()
        if node.keys:
            return node.keys[0], node.values[0]
        return None, []

    def delete_player(self, nick):
        """
        Usuwa gracza (wg nicku) z drzewa – przeszukuje listę liści i przy pierwszym trafieniu:
          • usuwa nick z listy graczy powiązanej z danym kluczem,
          • jeśli lista graczy dla klucza staje się pusta, usuwa sam klucz (choć pełne rebalansowanie nie zostało tu zaimplementowane).
        Każde sprawdzenie równości zwiększa licznik porównań.
        Zwraca poprzedni wynik gracza lub None, jeśli nie znaleziono.
        """
        self.comparisons = 0
        leaf = self._get_first_leaf()
        while leaf:
            for i, key in enumerate(leaf.keys):
                for j, player in enumerate(leaf.values[i]):
                    self.comparisons += 1
                    if player == nick:
                        old_score = leaf.keys[i]
                        # Usuwamy gracza z listy
                        leaf.values[i].pop(j)
                        # Jeżeli lista graczy przy tym kluczu jest pusta – usuwamy klucz i wartość
                        if not leaf.values[i]:
                            leaf.keys.pop(i)
                            leaf.values.pop(i)
                            # (Uwaga: pełne rebalansowanie drzewa przy usuwaniu nie jest tutaj rozbudowane.)
                        return old_score
            leaf = leaf.next
        return None


# Przykładowe użycie
if __name__ == "__main__":
    tree = BPlusTree(order=4)

    # Dodajemy kilku graczy (uwaga: nicki są unikalne)
    tree.add_player("Alice", 50)
    tree.add_player("Bob", 70)
    tree.add_player("Charlie", 60)
    tree.add_player("Dave", 70)       # ten sam wynik co Bob – lista graczy przy kluczu 70
    tree.add_player("Eve", 40)

    best_score, best_players = tree.get_best()
    print("Najlepszy wynik:", best_score, "Gracze:", best_players)
    worst_score, worst_players = tree.get_worst()
    print("Najgorszy wynik:", worst_score, "Gracze:", worst_players)

    score = tree.get_player_score("Charlie")
    print("Wynik gracza Charlie:", score, "Liczba porównań:", tree.comparisons)

    players_in_range = tree.query_range(50, 70)
    print("Gracze z wynikami z przedziału [50,70]:", players_in_range, "Liczba porównań:", tree.comparisons)

    # Aktualizacja wyniku – zmieniamy wynik gracza Alice
    old_score = tree.update_player("Alice", 80)
    print("Aktualizacja wyniku Alice (poprzedni wynik:", old_score, ") -> nowy najlepszy wynik:", tree.get_best(), "Liczba porównań:", tree.comparisons)

    # Usuwamy gracza
    deleted_score = tree.delete_player("Bob")
    print("Usunięto gracza Bob o wyniku:", deleted_score)
    players_in_range = tree.query_range(40, 80)
    print("Gracze z wynikami [40,80] po usunięciu Boba:", players_in_range, "Liczba porównań:", tree.comparisons)
