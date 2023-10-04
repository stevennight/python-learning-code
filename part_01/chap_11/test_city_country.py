import unittest
from city_functions import format_city_country


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = format_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = format_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted, 'Santiago, Chile - population 5000000')



if __name__ == '__main__':
    unittest.main()