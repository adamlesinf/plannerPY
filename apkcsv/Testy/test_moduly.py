from unittest import TestCase
import pandas as pd
from apkcsv import moduly,validacje

from pandas.testing import assert_frame_equal

class Validace(TestCase):
    def test_sprawdz_date(self):
        #arrange
        data_wejsciowa = '2022-02-02'
        oczekiwany_rezultat = True
        #act
        rezultat = validacje.sprawdz_date(data_wejsciowa)
        #assert
        self.assertEqual(oczekiwany_rezultat,rezultat)



class Test(TestCase):
    def test_dodaj_wydarzenie_poprawne_dodanie(self):
        TEST_INPUT_DIR = 'test_pliki/'
        ocz_rez_nazwa_pliku = 'testinput.csv'
        dane_wej_nazwa_pliku = 'testinputEmpty.csv'
        ocz_rez_df = pd.read_csv(TEST_INPUT_DIR + ocz_rez_nazwa_pliku)
        dane_wej_df = pd.read_csv(TEST_INPUT_DIR + dane_wej_nazwa_pliku)
        rezultat_df = moduly.dodaj_wydarzenie(dane_wej_df,'2000-12-13','12:13',13,13.0)
        assert_frame_equal(ocz_rez_df,rezultat_df,check_dtype=False);

    def test_usun_wydarzenie_poprawne_dodanie(self):
        TEST_INPUT_DIR = 'test_pliki/'
        dane_wej_nazwa_pliku = 'testinput.csv'
        ocz_rez_nazwa_pliku = 'testinputEmpty.csv'
        ocz_rez_df = pd.read_csv(TEST_INPUT_DIR + ocz_rez_nazwa_pliku)
        dane_wej_df = pd.read_csv(TEST_INPUT_DIR + dane_wej_nazwa_pliku)
        rezultat_df = moduly.usun_wydarzenie(dane_wej_df, '2000-12-13', '12:13', '13')
        assert_frame_equal(ocz_rez_df, rezultat_df, check_dtype=False, check_index_type=False);