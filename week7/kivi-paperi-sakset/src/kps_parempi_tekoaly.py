from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly
    
    def _tokan_siirto(self, ekan_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return siirto
