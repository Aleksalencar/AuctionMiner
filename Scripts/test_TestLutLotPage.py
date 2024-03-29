import unittest
from typing import Union

from PageObject.Pages import LutLotPage
from PageObject.TestBase.logger_setup import LoggingConfig

logging = LoggingConfig()
logging = logging.get_logging()


class TestLutLotPage(unittest.TestCase):

    def setUp(self) -> None:
        url = "https://www.lut.com.br/lote/veiculo-peugeot-hb/87589"
        self.lut_page = LutLotPage.LotPage(url)

    def test_get_lot_info_(self):
        url = "https://www.lut.com.br/lote/veiculo-peugeot-hb/87589"
        self.lut_page = LutLotPage.LotPage(url)
        expected_result = {
            'url': "https://www.lut.com.br/lote/veiculo-peugeot-hb/87589",
            'site_lot_id': 87589,
            'actual_bid': "R$ 10.000,00",
            'opening_date': "25/10/2021",
            'ending_date': "28/10/2021 10:00:00",
            'minimal_increment': 'R$ 1.000,00',
            'lot_status': "Fechado"

        }

        logging.info("running test_get_lot_info_")

        result = self.lut_page.get_lot_info()
        self.assertEqual(result, expected_result)

    def test_get_car_info_(self):
        test_case = {
            'brand': "Peugeot",
            'model': "207 HB",
            'year': "2010/2011",
            'appraisal_value': "R$ 10.000,00",
            'location': "SERTÃOZINHO/SP"
        }

        logging.info("running test_get_lot_info_")
        result = self.lut_page.get_car_info()
        self.assertEqual(result, test_case)

    def test_compare_car_brand(self):
        logging.info("running test_get_brand")
        result = self.lut_page.compare_car_brand("PEUGEOT 207 HB")
        expected_result = "Peugeot"

        self.assertEqual(result, expected_result)

    def test_get_appraisal_value(self):
        logging.info("running test_get_appraisal_value")
        result = self.lut_page.get_appraisal_value()
        expected_result = "R$ 10.000,00"

        self.assertEqual(result, expected_result)

    def test_get_year(self):
        test_cases = [
            {
                'url': "https://www.lut.com.br/lote/motocicleta-honda-biz/88273",
                'year': "2009"
            },
            {
                'url': "https://www.lut.com.br/lote/veiculo-ford-fiesta/88571",
                'year': "2003"
            },
            {
                'url': "https://www.lut.com.br/lote/veiculo-peugeot-sw/88573",
                'year': "2007"
            },
            {
                'url': "https://www.lut.com.br/lote/veiculo-fiat-idea-elx/88697",
                'year': "Not found"
            },

        ]
        for case in test_cases:
            self.lut_page = LutLotPage.LotPage(case['url'])
            result = self.lut_page.get_year()
            self.assertEqual(result, case['year'])



    def test_get_location(self):
        logging.info("running test_get_location")
        result = self.lut_page.get_location()
        expected_result = "SERTÃOZINHO/SP"

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
