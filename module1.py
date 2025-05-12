def mult_el(num: list[int | float], ratio: int | float = 2) -> list[int | float]:
    return [n * ratio for n in num]


num1 = input("Введите список чисел через пробел: ")
try:
    num_v = [float(x) for x in num1.split()]
    # Проверка на целые числа
    num_v = [int(x) if x.is_integer() else x for x in num_v]
except ValueError:
    print("Ошибка: введите только числа, разделенные пробелами")
    exit()

# Получение множителя с обработкой значения по умолчанию
ratio1 = input("Введите множитель (по умолчанию 2): ")
try:
    ratio_v = float(ratio1) if ratio1 else 2
    # Проверка на целое число
    ratio_v = int(ratio_v) if ratio_v.is_integer() else ratio_v
except ValueError:
    print("Ошибка: множитель должен быть числом")
    exit()

# Вычисление результатов
f_ret = mult_el(num_v, ratio_v)
lambda_ret = list(map(lambda x: x * ratio_v, num_v))

# Вывод результатов
print("Результат (функция):", f_ret)
print("Результат (лямбда-функция):", lambda_ret)

