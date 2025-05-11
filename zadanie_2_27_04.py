import re

def count_words_by_letter(text: str) -> dict:
    """
    Funkcja zlicza liczbę słów zaczynających się na daną literę.
    
    Krok 1: Tekst zostaje zamieniony na małe litery.
    Krok 2: Usuwamy interpunkcję (wszystko, co nie jest literą, cyfrą lub białym znakiem).
    Krok 3: Dzielimy tekst na słowa.
    Krok 4: Tworzymy hashmapę (słownik), która dla każdej litery (pierwszy znak słowa) inkrementuje licznik.
    Krok 5: Sortujemy wyniki malejąco wg liczby słów.
    """
    # Konwersja na małe litery
    text = text.lower()
    # Usuwanie interpunkcji – usuwamy wszystko co nie jest alfanumeryczne lub białym znakiem
    text = re.sub(r"[^\w\s]", "", text)
    # Dzielenie tekstu na słowa
    words = text.split()
    
    counts = {}
    # Liczymy słowa zaczynające się na literę (pomijamy te, które zaczynają się np. cyfrą)
    for word in words:
        if word:  # zabezpieczenie przed pustymi ciągami
            first_letter = word[0]
            if first_letter.isalpha():
                counts[first_letter] = counts.get(first_letter, 0) + 1
    
    # Sortujemy słownik wg liczby wystąpień malejąco
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

# Wygenerowany tekst o długości około 634 słów:
text = """
Tu w sercu malowniczego regionu, gdzie zielone łąki rozciągają się niczym bajkowa opowieść, stanęła niewielka osada, której mieszkańcy znani byli z serdeczności i niezwykłego gościnności. Pewnego słonecznego poranka, gdy mgła jeszcze leniwie unosiła się nad dolinami, zebrali się ludzie, aby rozpocząć dzień pełen nadziei i nowych wyzwań. Każdy z nich miał swoją historię, którą opowiadali z pasją przy ognisku, gdy ciepło ognia łączyło ich w jedną wielką rodzinę.

Dzień zaczynał się od dźwięku dzwonów, które budziły mieszkańców, zwiastując początek pracy na polach. Farmaceuci, kowale i nauczyciele – wszyscy znajdowali swoje miejsce w tej harmonijnej społeczności. Zarówno młodzi, jak i starzy wiedzieli, że każdy dzień niesie ze sobą nowe możliwości i przygody. Pracowite dusze stawiały czoła trudom życia, wierząc, że wszelkie przeszkody można przezwyciężyć, jeśli tylko człowiek z odwagą i determinacją podąża za swoim marzeniem.

Przygoda w tej osadzie nie ograniczała się tylko do codziennej pracy – wieczory były czasem, gdy opowiadano historie o dawnych czasach, legendach przekazywanych z pokolenia na pokolenie. W opowieściach tych pojawiały się mityczne postacie, czyli bohaterowie i bohaterki, które swoim przykładem uczyły, jak być prawdziwymi ludźmi honoru i wartości. Legenda o dzielnym rycerzu, który w obronie słabszych walczył z niesprawiedliwością, umacniała ducha całej wspólnoty. Każda opowieść motywowała do działania i dawała nadzieję na lepszą przyszłość.

Nad brzegiem rzeki, gdzie woda szepcze swoje sekrety, znajdował się stary dąb, który świadczył o przemijających czasach. Niezliczone wieki minęły, od kiedy ten dąb po raz pierwszy zakorzenił się w bogatej glebie, a on sam stał się świadkiem ludzkich losów. Przez tygodnie i miesiące, podobnie jak życie, dąb widział radość i smutek, śmiech i łzy, a też ciepło letnich wieczorów i chłód mroźnych nocy. Cisza tego miejsca przyciągała poszukiwaczy spokoju, którzy znaleźli w nim ukojenie i zadumę.

W małej, przytulnej kawiarence, gdzie zapach świeżo parzonej kawy unosił się w powietrzu, spotykali się mieszkańcy, aby dzielić się swoimi doświadczeniami, anegdotami i marzeniami. Barista zawsze pamiętał o ulubionych napojach swoich gości i serwował je z uśmiechem, który rozświetlał nawet najciemniejsze dni. Każdy, kto przekraczał próg tego miejsca, czuł, że jest częścią czegoś większego, że wspólnota jest siłą, która potrafi połączyć różnorodne losy.

Z dala od zgiełku wielkich miast, ta osada była oazą dla zmęczonych dusz, które szukały wytchnienia i autentycznego kontaktu z naturą. Piękne krajobrazy, w których łąki przeplatały się z głębokimi lasami, tworzyły scenerię równie niezwykłą, jak opowieści snute przez starych mędrców. Pokochać to miejsce potrafił każdy, kto choć raz tutaj zawitał, a wspomnienia z tych dni pozostawały na zawsze w pamięci, niezależnie od upływu czasu.

Podczas zimowych dni mieszkańcy osady organizowali liczne festyny i jarmarki, gdzie tradycje i rękodzieło były celebrowane z dumą oraz radością. Kramy wypełnione były świeżymi owocami, ręcznie robionymi wyrobami oraz opowieściami, które zdawały się przenosić uczestników w zupełnie inny wymiar, pełen magii i stworzonej z serca sztuki. Kolejne pokolenia uczyły się od starszych, słuchając z zapartym tchem każdej historii i czerpiąc inspirację z mądrości przekazywanej przez czas.

Pomiędzy pracą a odpoczynkiem, życie płynęło tu niczym spokojna rzeka, której bieg odzwierciedlał rytm serc mieszkańców. Codziennie wschodziło słońce, przynosząc nową energię i przypominając, że każdy dzień jest wyjątkowy. Z pokorą i radością witano każdy poranek, wiedząc, że świat pełen jest cudów, a miłość i dobroć są wartościami, które nigdy nie wyjdą z mody. Takie podejście do życia sprawiało, że nawet najmniejsze wyzwania stawały się okazją do nauki i osobistego rozwoju.

Między fragmentami tej opowieści można odnaleźć głębsze przesłanie; każdy, kto był częścią tej wspólnoty, wiedział, że życie jest piękne i pełne niespodzianek. Odwaga, pracowitość oraz wzajemny szacunek były fundamentem, na którym budowano codzienność. Mieszkańcy osady wierzyli w siłę jedności, wiedząc, że razem potrafią przezwyciężyć wszelkie przeciwności, a każda przygoda stawała się kolejnym rozdziałem w ich wspólnym życiu. Dzięki temu każdy dzień miał swój unikalny charakter, a historia tej małej społeczności zapisywała się złotymi literami, pozostawiając niezatarty ślad w sercach wszystkich, którzy ją odwiedzili.
"""

# Wywołanie funkcji i wyświetlenie wyników
stats = count_words_by_letter(text)
print("Liczba słów zaczynających się na daną literę (posortowane od najwięcej do najmniej):")
print(stats)
