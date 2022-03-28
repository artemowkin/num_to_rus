# num\_to\_rus

[![codecov](https://codecov.io/gh/artemowkin/num_to_rus/branch/main/graph/badge.svg?token=UO7R3HM5FH)](https://codecov.io/gh/artemowkin/num_to_rus)

Небольшая библиотека, позволяющая переводить числа в слова на русском
языке

## Установка

Чтобы установить библиотеку, нужно выполнить следующую команду:

```
pip install num_to_rus
```

## Использование

Для того, чтобы использовать библиотеку, нужно импортировать
`Converter` из `num_to_rus`, создать его экземпляр и вызвать
у него метод `convert`, которому передать число, которое нужно конвертировать

```python
from num_to_rus import Converter

conv = Converter()

print(conv.convert(512)) # 'пятьсот двенадцать'
```

## Тестирование

Чтобы запустить тесты, нужно выполнить следующую команду:

```
python -m unittest
```

## Лицензия

Проект находится под лицензией [GPL-3.0](LICENSE.txt)

