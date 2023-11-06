import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastosta_ei_pysty_ottamaan_liikaa_tavaraa(self):
        self.varasto.ota_varastosta(self.varasto.saldo + 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_varastoon_ei_pysty_lisaamaan_liikaa_tavataa(self):
        varastonSaldoAluksi = self.varasto.saldo
        varastonTilaAluksi = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 5)
        self.assertEqual(self.varasto.saldo, varastonSaldoAluksi + varastonTilaAluksi)

    def test_negatiivisen_lisays_varastoon_ei_onnistu(self):
        varastonSaldoAluksi = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, varastonSaldoAluksi)

    def test_negatiivinen_otto_varastosta_ei_onnistu(self):
        varastonSaldoAluksi = self.varasto.saldo
        self.varasto.ota_varastosta(-5)
        self.assertEqual(self.varasto.saldo,varastonSaldoAluksi)