import csv
import pandas as pd
import datetime

header = ['Data', 'Godzina', 'Nazwa', 'Opis']


def wczytanie_df():
    wczytany_df = pd.read_csv('wydarzenia.csv')
    return wczytany_df


def tworzenie_pliku():
    try:
        plik = open('wydarzenia.csv')
    except FileNotFoundError:
        with open('wydarzenia.csv', 'w', newline='', encoding='utf-8') as plik:
            writer = csv.DictWriter(plik, fieldnames=header)
            writer.writeheader()
        plik.close()
    finally:
        plik.close()


def zapis_df(df):

    df.to_csv('wydarzenia.csv', index=False)
    print('Zapisano pomyślnie.')


def wyswietl_wydarzenie():
    df = pd.read_csv('wydarzenia.csv')
    df.index += 1
    df = df.fillna('')
    if df.empty:
        print('Brak wydarzeń do wyświetlenia.\n')
    else:
        print(df.to_string())
        print('Wyświetlono.' + '\n')


def dodaj_wydarzenie(df,data,godzina,nazwa, opis ):

    dodawane = {"Data": data, 'Godzina': godzina, "Nazwa": nazwa, "Opis": opis}
    nowy_ele_df = pd.DataFrame([dodawane])
    rezultat_df = pd.concat([df,nowy_ele_df],ignore_index=True)
    return rezultat_df


def usun_wydarzenie(df, data, godzina, nazwa):

    odp = df.drop(df[(df['Data'] == data) & (df['Godzina'] == godzina) & (df['Nazwa'].apply(str) == nazwa)].index)
    return odp


def operacje():
    print('[1] - sortowanie alfabetyczne')
    print('[2] - sortowanie niealfabetyczne')
    print('[3] - sortowanie po dacie i godzienie rosnąco')
    print('[4] - sortowanie po dacie i godzienie malejąco')
    print('[5] - wyszukaj wartości w nazwie lub opisie')
    print('[6] - powróć do menu')

    sortowanie = input('wybierz opcję: ')
    try:
        sortowanie = int(sortowanie)
        if sortowanie not in range(1, 7):
            print('Niepoprawna warotść' + '\n')
        else:
            if sortowanie == 1:
                sortowanie_alfabetycznie()
            if sortowanie == 2:
                sortowanie_niealfabetycznie()
            if sortowanie == 3:
                sortowanie_czas_rosnaco()
            if sortowanie == 4:
                sortowanie_czas_malejaco()
            if sortowanie == 5:
                wyszukiwanie_nazwa_opis()
            if sortowanie == 6:
                print('Powrót do menu.' + '\n')
    except ValueError:
        print('Niepoprawny format.' + '\n')
        print(ValueError)


def sortowanie_alfabetycznie():
    odp = pd.read_csv('wydarzenia.csv')
    sortowanie_alf = odp.sort_values('Nazwa')

    with open('wydarzenia.csv', 'w', encoding='utf-8', newline='') as plik:
        sortowanie_alf.to_csv('wydarzenia.csv', index=False)
    plik.close()
    print('Posortowno.' + '\n')


def sortowanie_niealfabetycznie():
    odp = pd.read_csv('wydarzenia.csv')
    sortowanie_alf = odp.sort_values('Nazwa')
    with open('wydarzenia.csv', 'w', encoding='utf-8', newline='') as plik:

        sortowanie_nie_alf = sortowanie_alf[::-1]
        sortowanie_nie_alf.to_csv('wydarzenia.csv', index=False)

    plik.close()
    print('Posortowno.' + '\n')


def sortowanie_czas_rosnaco():
    odp = pd.read_csv('wydarzenia.csv')
    sortowanie_czas = odp.sort_values(['Data', 'Godzina'], ascending=[True, True])

    with open('wydarzenia.csv', 'w', encoding='utf-8', newline='') as plik:
        sortowanie_czas.to_csv('wydarzenia.csv', index=False)
    plik.close()
    print('Posortowno.' + '\n')


def sortowanie_czas_malejaco():
    odp = pd.read_csv('wydarzenia.csv')
    sortowanie_nie_czas = odp.sort_values(['Data', 'Godzina'], ascending=[True, True])

    with open('wydarzenia.csv', 'w', encoding='utf-8', newline='') as plik:
        sortowanie_nie_czas = sortowanie_nie_czas[::-1]
        sortowanie_nie_czas.to_csv('wydarzenia.csv', index=False)
    plik.close()
    print('Posortowno.' + '\n')


def wyszukiwanie_nazwa_opis():
    wyszukiwane = input("Podaj wartość szukaną w nazwie lub opisie: ").upper()
    print()
    odp = pd.read_csv('wydarzenia.csv')
    wynik_wyszukiwania = (odp[(odp.Nazwa.str.contains(wyszukiwane)) | (odp.Opis.str.contains(wyszukiwane))])
    if not wynik_wyszukiwania.empty:
        wynik_wyszukiwania.index += 1
        print(wynik_wyszukiwania)
        print('wyświetlono.' + '\n')
    else:
        print("Nie znaleziono wydarzenia o nazwie lub opisie:", wyszukiwane, '\n')
