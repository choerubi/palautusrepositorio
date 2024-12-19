from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    # toteutetaan metodi pelityypin mukaisesti
    def _tokan_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
