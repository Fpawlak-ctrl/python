def odczytaj_dane():
    plik = open("dane.txt", "r", encoding="utf-8")
    dane = plik.readlines()
    plik.close()

    dane = [element.strip() for element in dane]

    return dane


def wyswietl_dane(dane):
    print("\nDane w pliku:")
    
    for element in dane:
        print(element)


def sortuj_dane(dane):
    dane.sort()

    plik = open("dane_posortowane.txt", "w", encoding="utf-8")

    for element in dane:
        plik.write(element + "\n")

    plik.close()

    print("\nDane zostały posortowane.")
    print("Zapisano je w pliku dane_posortowane.txt")

def usun_ucznia(dane):
    if len(dane) == 0:
        print("Lista jest pusta.")
        return

    wyswietl_dane(dane)

    try:
        numer = int(input("Podaj numer ucznia do usunięcia: "))

        if numer >= 1 and numer <= len(dane):
            usuniety = dane.pop(numer - 1)
            print("Usunięto ucznia:", usuniety)

            with open("dane_posortowane.txt", "w", encoding="utf-8") as plik:
                for uczen in dane:
                    plik.write(uczen + "\n")
        else:
            print("Nie ma ucznia o takim numerze.")

    except ValueError:
        print("Podaj poprawny numer.")

def menu():
    dane = odczytaj_dane()

    while True:
        print("\n===== MENU =====")
        print("1. Wyświetl uczniów")
        print("2. Posortuj uczniów")
        print("3. Usuń ucznia")
        print("4. Zakończ program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            wyswietl_dane(dane)

        elif wybor == "2":
            sortuj_dane(dane)

        elif wybor == "3":
            usun_ucznia(dane)

        elif wybor == "4":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")


menu()