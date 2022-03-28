from .data_dicts import DIGITS, THOUSAND_DIGITS, TENS, TEENS, HUNDREDS


class Converter:
    """Конвертер чисел в слова на русском языке"""

    def convert(self, number: int, digit_class: int = 1,
            return_zero: bool = True) -> str:
        """
        Рекурсивная функция, конвертирующая числа в слова русского
        языка.

        Arguments
        ---------

        number -- само число, которое нужно сконвертировать

        digit_class -- класс числа при рекурсивном вызове. Это
        определяет, какого класса (сотни, тысячи, миллионы и т.д.)
        передается число при рекурсивном вызове (1, 2, 3, ...)
        соответственно. Этот аргумент используется для изменения формы
        числа в классе тысяч ('сто один' для сотен и 'сто одна' для тысяч)

        return_zero -- булево значение, определяющее возвращать ли
        для числа 0 слово 'ноль'. Это используется при рекурсивных
        вызовах, чтобы, например, для числа 100000 не возвращалось 'ноль'
        в конце ('сто тысяч ноль')

        Returns
        -------
        Возвращается переведенное в слова на русском языке числа. Если
        число больше 999999999999, то вернется 'слишком много'

        """
        if len(str(number)) < 4:
            if number == 0 and return_zero: return 'ноль'
            hundreds_text = self._convert_hundreds(number, digit_class)
            return hundreds_text
        elif len(str(number)) < 7:
            return self._get_thousands(number)
        elif len(str(number)) < 10:
            return self._get_millions(number)
        elif len(str(number)) < 13:
            return self._get_billions(number)
        else:
            return 'слишком много'

    def _convert_hundreds(self, number: int, digit_class: int) -> str:
        """
        Конвертирует тройку конкретного разряда, который указывается в
        digit_class, в слова на русском языке
        """
        if len(str(number)) == 2 and number // 10 == 1:
            return TEENS[number]
        elif len(str(number)) == 2:
            tens, dig = divmod(number, 10)
            if dig == 0: return TENS[tens]
            digits = THOUSAND_DIGITS if digit_class == 2 else DIGITS
            digits_text = digits[dig]
            return TENS[tens] + ' ' + digits_text
        elif len(str(number)) == 3:
            hundreds, tens = divmod(number, 100)
            if tens == 0: return HUNDREDS[hundreds]
            tens_text = self._convert_hundreds(tens, digit_class)
            return HUNDREDS[hundreds] + ' ' + tens_text
        else:
            digits = THOUSAND_DIGITS if digit_class == 2 else DIGITS
            return digits[number]

    def _get_thousands(self, number: int) -> str:
        """Переводит число больше 999 в слова на русском языке"""
        thousands, another = divmod(number, 1000)
        thousands_text = self.convert(thousands, 2, return_zero=False)
        thousand_word = ' ' + self._get_thousand_word(thousands)
        if another == 0:
            return thousands_text + thousand_word

        hundreds_text = ' ' + self.convert(another, 1, return_zero=False)
        return thousands_text + thousand_word + hundreds_text

    def _get_millions(self, number: int) -> str:
        """Переводит число больше 999999 в слова на русском языке"""
        millions, thousands = divmod(number, 1000000)
        millions_text = self.convert(millions, 3, return_zero=False)
        million_word = ' ' + self._get_million_word(millions)
        if thousands == 0:
            return millions_text + million_word

        thousands_text = ' ' + self.convert(thousands, 2, return_zero=False)
        return millions_text + million_word + thousands_text

    def _get_billions(self, number: int) -> str:
        """Переводит число больше 999999999 в слова на русском языке"""
        billions, millions = divmod(number, 1000000000)
        billions_text = self.convert(billions, 4, return_zero=False)
        billion_word = ' ' + self._get_billion_word(billions)
        if millions == 0:
            return billions_text + billion_word

        millions_text = ' ' + self.convert(millions, 3, return_zero=False)
        return billions_text + billion_word + millions_text

    def _get_thousand_word(self, number: int) -> str:
        """
        Возвращает слово 'тысяча' в правильном склонении по последней
        цифре числа
        """
        if str(number)[-1] == '1':
            return 'тысяча'
        elif str(number)[-1] in ('2', '3', '4'):
            return 'тысячи'
        else:
            return 'тысяч'

    def _get_million_word(self, number: int) -> str:
        """
        Возвращает слово 'миллион' в правильном склонении по последней
        цифре числа
        """
        if str(number)[-1] == '1':
            return 'миллион'
        elif str(number)[-1] in ('2', '3', '4'):
            return 'миллиона'
        else:
            return 'миллионов'

    def _get_billion_word(self, number: int) -> str:
        """
        Возвращает слово 'миллиард' в правильном склонении по последней
        цифре числа
        """
        if str(number)[-1] == '1':
            return 'миллиард'
        elif str(number)[-1] in ('2', '3', '4'):
            return 'миллиарда'
        else:
            return 'миллиардов'
