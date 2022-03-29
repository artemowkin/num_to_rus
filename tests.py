from unittest import TestCase

from num_to_rus import Converter


class ConverterTestCase(TestCase):
    """Тесты для конвертера чисел в слова на русском языке"""

    def setUp(self):
        self.conv = Converter()

    def test_zero(self):
        """Тест с числом 0"""
        text = self.conv.convert(0)
        self.assertEqual(text, 'ноль')

    def test_zero_with_return_zero_arg_to_false(self):
        """Тест с числом 0 и аргументом return_zero=False"""
        text = self.conv.convert(0, return_zero=False)
        self.assertEqual(text, '')

    def test_one(self):
        """Тест с числом 1"""
        text = self.conv.convert(1)
        self.assertEqual(text, 'один')

    def test_five(self):
        """Тест с числом 5"""
        text = self.conv.convert(5)
        self.assertEqual(text, 'пять')

    def test_nine(self):
        """Тест с числом 9"""
        text = self.conv.convert(9)
        self.assertEqual(text, 'девять')

    def test_ten(self):
        """Тест с числом 10"""
        text = self.conv.convert(10)
        self.assertEqual(text, 'десять')

    def test_twelve(self):
        """Тест с числом 12"""
        text = self.conv.convert(12)
        self.assertEqual(text, 'двенадцать')

    def test_sixteen(self):
        """Тест с числом 16"""
        text = self.conv.convert(16)
        self.assertEqual(text, 'шестнадцать')

    def test_nineteen(self):
        """Тест с числом 19"""
        text = self.conv.convert(19)
        self.assertEqual(text, 'девятнадцать')

    def test_twenty(self):
        """Тест с числом 20"""
        text = self.conv.convert(20)
        self.assertEqual(text, 'двадцать')

    def test_23(self):
        """Тест с числом 23"""
        text = self.conv.convert(23)
        self.assertEqual(text, 'двадцать три')

    def test_74(self):
        """Тест с числом 74"""
        text = self.conv.convert(74)
        self.assertEqual(text, 'семьдесят четыре')

    def test_99(self):
        """Тест с числом 99"""
        text = self.conv.convert(99)
        self.assertEqual(text, 'девяносто девять')

    def test_100(self):
        """Тест с числом 100"""
        text = self.conv.convert(100)
        self.assertEqual(text, 'сто')

    def test_847(self):
        """Тест с числом 847"""
        text = self.conv.convert(847)
        self.assertEqual(text, 'восемьсот сорок семь')

    def test_503(self):
        """Тест с числом 503"""
        text = self.conv.convert(503)
        self.assertEqual(text, 'пятьсот три')

    def test_999(self):
        """Тест с числом 999"""
        text = self.conv.convert(999)
        self.assertEqual(text, 'девятьсот девяносто девять')

    def test_1000(self):
        """Тест с числом 1000"""
        text = self.conv.convert(1000)
        self.assertEqual(text, 'одна тысяча')

    def test_2000(self):
        """Тест с числом 2000"""
        text = self.conv.convert(2000)
        self.assertEqual(text, 'две тысячи')

    def test_2002(self):
        """Тест с числом 2002"""
        text = self.conv.convert(2002)
        self.assertEqual(text, 'две тысячи два')

    def test_2022(self):
        """Тест с числом 2022 :)"""
        text = self.conv.convert(2022)
        self.assertEqual(text, 'две тысячи двадцать два')

    def test_3020(self):
        """Тест с числом 3020"""
        text = self.conv.convert(3020)
        self.assertEqual(text, 'три тысячи двадцать')

    def test_5400(self):
        """Тест с числом 5400"""
        text = self.conv.convert(5400)
        self.assertEqual(text, 'пять тысяч четыреста')

    def test_8703(self):
        """Тест с числом 8703"""
        text = self.conv.convert(8703)
        self.assertEqual(text, 'восемь тысяч семьсот три')

    def test_9412(self):
        """Тест с числом 9412"""
        text = self.conv.convert(9412)
        self.assertEqual(text, 'девять тысяч четыреста двенадцать')

    def test_50000(self):
        """Тест с числом 50000"""
        text = self.conv.convert(50000)
        self.assertEqual(text, 'пятьдесят тысяч')

    def test_81234(self):
        """Тест с числом 81234"""
        text = self.conv.convert(81234)
        self.assertEqual(text, 'восемьдесят одна тысяча двести тридцать четыре')

    def test_500000(self):
        """Тест с числом 100000"""
        text = self.conv.convert(500000)
        self.assertEqual(text, 'пятьсот тысяч')

    def test_800020(self):
        """Тест с числом 800020"""
        text = self.conv.convert(800020)
        self.assertEqual(text, 'восемьсот тысяч двадцать')

    def test_4000000(self):
        """Тест с числом 4000000"""
        text = self.conv.convert(4000000)
        self.assertEqual(text, 'четыре миллиона')

    def test_3006100(self):
        """Тест с числом 3006100"""
        text = self.conv.convert(3006100)
        self.assertEqual(text, 'три миллиона шесть тысяч сто')

    def test_15000000(self):
        """Тест с числом 15000000"""
        text = self.conv.convert(15000000)
        self.assertEqual(text, 'пятнадцать миллионов')

    def test_123000000(self):
        """Тест с числом 123000000"""
        text = self.conv.convert(123000000)
        self.assertEqual(text, 'сто двадцать три миллиона')

    def test_7000000000(self):
        """Тест с числом 7000000000"""
        text = self.conv.convert(7000000000)
        self.assertEqual(text, 'семь миллиардов')

    def test_2003020800(self):
        """Тест с числом 2003020800"""
        text = self.conv.convert(2003020800)
        self.assertEqual(text, 'два миллиарда три миллиона двадцать тысяч восемьсот')

    def test_25000000000(self):
        """Тест с числом 25000000000"""
        text = self.conv.convert(25000000000)
        self.assertEqual(text, 'двадцать пять миллиардов')

    def test_999000000000(self):
        """Тест с числом 999000000000"""
        text = self.conv.convert(999000000000)
        self.assertEqual(text, 'девятьсот девяносто девять миллиардов')

    def test_1000000000000(self):
        """Тест с числом 1000000000000"""
        text = self.conv.convert(1000000000000)
        self.assertEqual(text, 'слишком много')

    def test_101000000(self):
        """Тест с числом 101000000"""
        text = self.conv.convert(101000000)
        self.assertEqual(text, 'сто один миллион')

    def test_101000000000(self):
        """Тест с числом 101000000000"""
        text = self.conv.convert(101000000000)
        self.assertEqual(text, 'сто один миллиард')

    def test_minus_532(self):
        """Тест с отрицательным числом: 532"""
        text = self.conv.convert(-532)
        self.assertEqual(text, 'минус пятьсот тридцать два')
