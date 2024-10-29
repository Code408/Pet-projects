# Небольшие проекты по аналитике и прочее

### kubik 🎲
Скрипт позволяет строить гистограмму для случайного подбрасывания кубика
____
**Также определяется**:
+ Дисперсия
+ Среднее значение
+ Среднеквадратическое отклонение
+ Мода

![фото](python_5mW3v4FWWU-1.png)
____

### game 👾
Простейшая игра, суть которой заключается в угадывании поля без мин
____
**Использующиеся навыки**:
+ импортирование модулей
+ принцип работы список
+ принципы работы функций
+ условные операторы
+ принцип работы циклов
+ f-строки
  
```python
  import random

Player_balance = 100
stavka = int(input("Введите вашу ставку: "))
count = 0
multiply = 1

N = 5
P = [[0] * N for _ in range(N)]
result = (P, Player_balance, multiply, stavka, count)


def game(P, Player_balance, multiply, stavka, count):
    c = random.randint(0, 4)
    vvod = int(input("Введите номер клетки от одного до пяти: "))

    P[count][c] = "*"

    if P[count][vvod - 1] == "*":
        Player_balance -= stavka
        multiply = 1
        if Player_balance == 0:
            print("--------------------------------------------------------")
            print(*P[:count + 1], sep="\n")
            print("--------------------------------------------------------")
            result = (P, Player_balance, multiply, stavka, count)
            return result
        print(f"Ты проиграл, твой баланс: {Player_balance} ")
        print("--------------------------------------------------------")
        print(*P[:count + 1], sep="\n")
        print("--------------------------------------------------------")
        P = [[0] * N for _ in range(N)]
        count = 0
        stavka = int(input("Введите вашу ставку: "))
        result = (P, Player_balance, multiply, stavka, count)
        return result

    if count == len(P) - 1:
        Player_balance += stavka * multiply
        print(f"Поздравляем, ты выиграл {stavka * multiply}, твой баланс составляет: {Player_balance} ")
        multiply = 1
        P = [[0] * N for _ in range(N)]
        count = 0
        stavka = int(input("Введите вашу ставку: "))
        result = (P, Player_balance, multiply, stavka, count)
        return result

    else:
        multiply = multiply * 1.5
        count = count + 1
        print("--------------------------------------------------------")
        print(*P[:count - 1], sep="\n")
        print(P[count - 1], "<----")
        print("--------------------------------------------------------")
        zb_flag = input((f"Ты выиграл, заберёшь: {stavka * multiply}  ?\n Ваш ответ:"))

        if zb_flag.lower() == 'yes':
            Player_balance += stavka * multiply
            multiply = 1
            P = [[0] * N for _ in range(N)]
            count = 0
            print("--------------------------------------------------------")
            print(f"Теперь ваш баланс составляет: {Player_balance}")
            print("--------------------------------------------------------")
            stavka = int(input("Введите вашу ставку: "))
            result = (P, Player_balance, multiply, stavka, count)
            return result

        else:
            result = (P, Player_balance, multiply, stavka, count)
            return result


while True:
    if result[1] == 0:
        print("ВЫ ПРОИГРАЛИ \nДЕНЕГ БОЛЬШЕ НЕТ")
        break
    result = game(*result)
  ```

____

### Небольшой проект и теория по курсу от T-банка
*Файлы с расширением 'ipynb'*.

**Представлены основные моменты построения диаграмм, использование библиотеки pandas и работы в JupiterNotebook**
___

+ Мой [профиль](https://stepik.org/users/930493503/profile) в Stepik
___


  > ***"Длительность минуты зависит от того, с какой стороны двери уборной вы находитесь"***
