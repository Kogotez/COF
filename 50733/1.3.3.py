s = 3.141592
ra = int(input())
a = round(2 * s * ra, 3)
b = round(s * (ra ** 2), 3)
c = round(4 / 3 * s * (ra ** 3), 3)
d = round(4 * s * (ra ** 2), 3)
print(f'Длина окружности радиуса {ra} равна {a}')
print(f'Площадь круга радиуса {ra} равна {b}')
print(f'Объем шара радиуса {ra} равен {c}')
print(f'Площадь поверхности шара радиуса {ra} равна {d}')
