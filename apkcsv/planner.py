import datetime

import moduly
import validacje

wybor_opcji_menu = -1


moduly.tworzenie_pliku()


while wybor_opcji_menu != 5:
    print("\t", "\U0001F4C5", "Program Planner", "\U0001F4C5")
    print("Wybierz opcję:")
    print("1.", "[\U0001F4BB]", "Wyświetl wydarzenie(a)")
    print("2.", "[\u2795]", "Dodaj wydarzenie")
    print("3.", "[\u2716\uFE0F]", "Usuń wydarzenie")
    print("4.", "[\U0001f527]", "Operacje")
    print("5.", "[↳]", "Wyjście z programu")

    wybor_opcji_menu = input()

    try:
        wybor_opcji_menu = int(wybor_opcji_menu)
        if wybor_opcji_menu not in range(1, 6):
            print("Niepoprawna wartość" + '\n')
        else:
            if wybor_opcji_menu == 1:
                moduly.wyswietl_wydarzenie()

            if wybor_opcji_menu == 2:
                print('podaj informację o nowym zadaniu (* - dane obowiązkowe):')

                data = input("podaj datę wydarzenia YYYY-MM-DD*: ")
                czy_data_poprawna = validacje.sprawdz_date(data);

                if czy_data_poprawna:

                    godzina = input("Podaj godzinę wydearzenia HH:MM*: ")
                    czy_godzina_poprawna = validacje.sprawdz_czas(godzina)
                    if czy_godzina_poprawna:

                            nazwa = input("Podaj nazwę wydarzenia*: ").upper()
                            czy_nazwa_poprawna = validacje.sprawdz_nazwe(nazwa)
                            if czy_nazwa_poprawna:

                                opis = input('podaj opis wydarzenia (opcjonalne): ').upper()
                                wstepny_df = moduly.wczytanie_df()
                                nowy_df = moduly.dodaj_wydarzenie(wstepny_df,data,godzina,nazwa,opis)
                                moduly.zapis_df(nowy_df);
                            else:
                                print('Pole obowiazkowe' + '\n')

                    else:
                        print('Podano nieprawidłowy format czasu, podaj HH:MM' + '\n')

                else:
                    print('Podano nieprawidłowy format daty' + '\n')



            if wybor_opcji_menu == 3:

                try:
                    data = input("podaj datę wydarzenia YYYY-MM-DD: ")
                    datetime.datetime.strptime(data, "%Y-%m-%d")
                    if len(data) != 10:
                        print('Podano nieprawidłowy format daty, podaj YYYY-MM-DD' + '\n')

                    else:
                        try:
                            godzina = input("Podaj godzinę wydearzenia HH:MM: ")
                            datetime.datetime.strptime(godzina, '%H:%M')
                            if len(godzina) != 5:
                                print('Podano nieprawidłowy format godziny, podaj HH:MM' + '\n')
                            else:
                                nazwa = input("Podaj nazwę wydarzenia: ").upper()
                                if nazwa == "":
                                    print("nie podano nazwy (dane obowiązkowe)" + '\n')
                                else:
                                    wstepny_df = moduly.wczytanie_df()
                                    usuniety_df = moduly.usun_wydarzenie(wstepny_df,data,godzina,nazwa)
                                    moduly.zapis_df(usuniety_df)
                        except ValueError:
                            print('Podano nieprawidłowy format czasu, podaj HH:MM' + '\n')

                except ValueError:
                    print('Podano nieprawidłowy format daty, podaj YYYY-MM-DD' + '\n')

            if wybor_opcji_menu == 4:
                moduly.operacje()

            if wybor_opcji_menu == 5:
                print("Zakończono program.")

    except Exception as e:
        print(e)

        print("Niepoprawny typ danych" + '\n')
