from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


def aloita_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly(Tekoaly())
    if tyyppi == 'c':
        return KPSParempiTekoaly(TekoalyParannettu(10))

    return None
