import pandas
from matplotlib import pyplot as plt
import random
import numpy as np
from scipy. stats import norm

lst = []
key = [1,2,3,4,5,6]
disp = []


for _ in range(100):
    lst.append(random.randint(1,6))

sred = sum(lst) / len(lst)

print('sred:', sred)

for i in lst:
    disp.append((i-sred)**2)

disp1 = sum(disp)

disp = disp1 / len(disp) - 1

print('disp:',disp)

st_otkl = disp ** 0.5

print('st_otkl:',st_otkl)

# Создание DataFrame
df = pandas.DataFrame({
    'zn_kubik':lst,
    'nomer': range(len(lst))
})

# Определение моды (наиболее часто встречающегося значения)
moda = df['zn_kubik'].mode()[0]
print(f"moda: {moda}")
print("---------")
grouped = df.groupby('zn_kubik').count()
print(grouped)

# Построение гистограммы бросков кубика
plt.hist(df['zn_kubik'], bins=np.arange(1, 8) - 0.5, edgecolor='black', density=True)
# Диапазон для x значений
x = np.arange(1, 7 ,0.1)
# Построение нормальной кривой
plt.plot(x, norm. pdf(x, sred, st_otkl), color='red', label='Нормальное распределение')
# Добавление вертикальной линии для среднего значения
plt.axvline(sred, color='green', linestyle='--', label=f'Среднее: {sred:.2f}')
# Добавление вертикальной линии для моды
plt.axvline(moda, color='blue', linestyle='--', label=f'Мода: {moda}')
# Настройка графика
plt.xlabel('Значение кубика')
plt.ylabel('Плотность')
plt.title('Распределение значений бросков кубика')
plt.show()
plt.legend()
plt.show()