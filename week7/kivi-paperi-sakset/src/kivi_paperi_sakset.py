from tuomari import Tuomari


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ekan_siirto()
        tokan_siirto = self._tokan_siirto(ekan_siirto)

        while True:
            ekan_siirto = self._ekan_siirto()
            tokan_siirto = self._tokan_siirto(ekan_siirto)

            if self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            
            else:
                break

        print("Kiitos!")
        print(tuomari)

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _tokan_siirto(self, ekan_siirto):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
