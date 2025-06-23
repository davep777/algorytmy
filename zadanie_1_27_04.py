#funkcja haszująca suma kodów ASCII
#list comprehansion
def hasz_ascii(string, rozmiar):
    return(sum(ord(char) for char in string) % rozmiar)

#tradycyjna wersja
def hasz_ascii_v2(string, rozmiar):
    wartość_hasz = 0
    for char in string:
        wartość_hasz += ord(char)
    return wartość_hasz % rozmiar 

#funkcja haszująca Hornera
#zmienia wynik w zależności od kolejności znaków, nie bedzie abc = bca, dzięki bazie 
def hasz_hornera(string, rozmiar, baza = 31):
    wartość_hasz = 0
    for char in string:
        wartość_hasz = wartość_hasz * baza + ord(char)
    return wartość_hasz


# funkcja haszująca fnv1a
#
def hasz_fnv1a(string, rozmiar, fnv_prime = 0x01000193, offset_basis = 0x811c9dc5):
    wartosc_hasz = offset_basis #początkowa wartość haszowania
    for char in string:
        wartosc_hasz ^= ord(char) #XOR znaków ASCII
        wartosc_hasz *= fnv_prime # * stałą do mieszania wartości, jesli są minimalnie różen zmienia się całkowicie, XOR jak są takie same daje 0, rózne 1
        wartosc_hasz &= 0xFFFFFFFF #ograniczenie do 32 bitów
    return wartosc_hasz % rozmiar

test = [f"string_{i}" for i in range(30)]
#print(test)

rozklad = 100

print(f"{'String':<14}{'Hasz ASCII':<14}{'Hasz Hornera':<14}{'Hasz Hornera':<14}")
print("*" *56)
for s in test:
    print(f"{s:<15}{hasz_ascii(s, rozklad):<14}{hasz_hornera(s, rozklad):<14}{hasz_fnv1a(s, rozklad):<14}")
