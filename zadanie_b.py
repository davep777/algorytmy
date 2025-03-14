#Count Odd Numbers below n

n = int(input("Podaj liczbe n: "))
licznik = 0

for i in range(n):
    if i > 0 and i % 2 == 1:
        licznik = licznik + 1

print(f"Ilosc liczb dodatnich nieparzystych ponizej n: {licznik}")

#Polish alphabet

def bez_polskich_znakow(imie):
    imie = imie.replace('ą', 'a')
    imie = imie.replace('ć', 'c')
    imie = imie.replace('ę', 'e')
    imie = imie.replace('ł', 'l')
    imie = imie.replace('ń', 'n')
    imie = imie.replace('ó', 'o')
    imie = imie.replace('ś', 's')
    imie = imie.replace('ź', 'z')
    imie = imie.replace('ż', 'z')
    return imie
     
print(bez_polskich_znakow("Jędżej Błądziński"))

#Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

def zamiana():
    zdanie = input("Wprowdz zdanie z samogloska: ")
    samogloski = "aeiouAEIOU"
    rezultat = ''
    for char in zdanie:
        if char in samogloski:
            rezultat = rezultat + '!'
        else:
            rezultat = rezultat + char
    return rezultat

print(zamiana())

#Surface Area and Volume of a Box

def surface_volume_box(width, height, depth):
    surface = 2 * (width * height + width * depth + height * depth)
    volume = width * height * depth
    return(surface, volume)

print(surface_volume_box(1,2,3))

#Return the day

def week():
    day = int(input("Wprowadz numer dnia: "))
    if day == 1:
        return 'Sunday'
    elif day == 2:
        return 'Monday'
    elif day == 3:
        return 'Tuesday'
    elif day == 4 :
        return 'Wednesday'
    elif day == 5:
        return "Thurday"
    elif day == 6:
        return 'Friday'
    elif day == 7:
        return 'Saturday'
    else:
        return "Wrong, please enter a number between 1 and 7"
    
print(week())

    




    
        


