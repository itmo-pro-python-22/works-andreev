# Система управления рестораном

> Все великие умы перед тем, как совершить открытие,
> плотно обедали. © Андреев Н.В.

## Описание системы

Небольшая ~~система~~ ***управления*** рестораном.

*Система* предназначена **для учёта товаров** в ресторане.

Пример ![GitHub Logo](https://github.githubassets.com/favicons/favicon.svg) работающей системы можно посмотреть [тут](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

![Описание картинки](https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif)

## Возможности системы

* Хранение информации о товарах
* Разделение товаров на еду и напитки
* Работа с персоналом

+ Ещё один список

- И ещё один список

1. Это нумерованный список
   * Вложенный маркированный список
2. А это его второй пункт
   1. Вложенный список
   2. Второй пункт вложенного списка
   3. Три
   4. Четыре
   5. Пять

## Примеры использования

Можете импортировать классы `Food` и `Drink` и самостоятельно их изучить.

```python
cake = Food('Тортик', 150, 5)
sushi = Food('Суши', 220, 3)
latte = Drink('Латте', 'Кофе', 190, 10)
kvass = Drink('Хлебный', 'Квас', 70, 5)
switch = Item('Nintendo Switch', 23990, 1)

for item in cake, sushi, latte, kvass, switch:
    print(item)

print(Food.get_report())
print(Drink.get_report())

exporter = FileItemsExporter('items.txt')
exporter.export([cake, sushi, latte, kvass, switch])

table_exporter = CSVFileExporter('items.csv')
table_exporter.export([cake, sushi, latte, kvass, switch])
```

## Пример экспорта

| Товар           | Стоимость | Количество |
|-----------------|:---------:|:----------:|
| Тортик          |    150    |     5      |
| Суши            |    220    |     3      |
| Латте           |    190    |     10     |
| Квас            |    70     |     5      |
| Nintendo Switch |   23990   |     1      |

## Формула расчёта зарплаты

$$
Salary(Evtushenko) = 130000 \cdot \log_2{1}
$$

$$
Ограничения:
\begin{equation}
    \begin{cases}
    x_1 + x_3 = 230\\
    x_2 + x_4 = 68\\
    \frac{x_1}{10} + \frac{x_2}{12} \leq 24\\
    \frac{x_3}{13} + \frac{x_4}{13} \leq 24\\
    \frac{x_1}{10} + \frac{x_3}{13} \leq 24\\
    \frac{x_2}{12} + \frac{x_4}{13} \leq 24\\
    \end{cases}
\end{equation}
$$
