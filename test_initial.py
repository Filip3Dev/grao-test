import unittest

from initial import main


class TestSum(unittest.TestCase):
    def test_unit(self):
        """
        Test that it calculates good
        """
        semanas = 30
        valor = 200
        result = main(semanas, valor)
        self.assertEqual(result, '6.515,35')
    def test_unit_fail(self):
        """
        Test that it calculates and return 0
        """
        semanas = 0
        valor = 200
        result = main(semanas, valor)
        self.assertEqual(result, '0,00')


if __name__ == '__main__':
    unittest.main()
