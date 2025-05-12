def summ(a, b):
    """Сложение двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b

def sub(a, b):
    """Вычитание двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a - b

def mult(a, b):
    """Умножение двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a * b

def division_operation(a, b):
    """Деление двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

def int_div(a, b):
    """Целочисленное деление"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a // b

def expon(base, exponent):
    """Возведение в степень"""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return base ** exponent

def factr(n):
    """Вычисление факториала"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определен только для целых неотрицательных чисел")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def root2(number):
    """Извлечение квадратного корня"""
    if number < 0:
        raise ValueError("Корень из отрицательного числа не определен")
    return number ** 0.5

def ostd(a, b):
    """Остаток от деления"""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b

def srar(numbers):
    """Среднее арифметическое"""
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Все элементы должны быть числами")
    if not numbers:
        raise ValueError("Список чисел не может быть пустым")
    return sum(numbers) / len(numbers)

def run_calculator():
    """Основная функция калькулятора"""
    operations = {
        '1': ('Сложение', summ),
        '2': ('Вычитание', sub),
        '3': ('Умножение', mult),
        '4': ('Деление', division_operation),
        '5': ('Целочисленное деление', int_div),
        '6': ('Остаток от деления', ostd),
        '7': ('Возведение в степень', expon),
        '8': ('Факториал', factr),
        '9': ('Квадратный корень', root2),
        '10': ('Среднее арифметическое', srar)
    }

    while True:
        print("\nДоступные операции:")
        for key, (name, _) in sorted(operations.items(), key=lambda x: int(x[0])):
            print(f"{key}. {name}")
        
        choice = input("\nВыберите операцию (или 'выход' для завершения): ").lower()
        
        if choice in ('выход', 'exit', 'quit'):
            print("Работа калькулятора завершена.")
            break
        
        if choice not in operations:
            print("Неверный выбор операции! Пожалуйста, попробуйте снова.")
            continue
        
        try:
            if choice == '8':  # Факториал
                num = int(input("Введите целое число: "))
                result = operations[choice][1](num)
                print(f"Результат: {result}")
            elif choice == '9':  # Квадратный корень
                num = float(input("Введите число: "))
                result = operations[choice][1](num)
                print(f"Результат: {result}")
            elif choice == '10':  # Среднее арифметическое
                nums = input("Введите числа через пробел: ").split()
                numbers = [float(x) for x in nums]
                result = operations[choice][1](numbers)
                print(f"Результат: {result}")
            else:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = operations[choice][1](a, b)
                print(f"Результат: {result}")
        
        except ValueError as e:
            print(f"\nОшибка ввода: {e}")
        except ZeroDivisionError as e:
            print(f"\nМатематическая ошибка: {e}")
        except Exception as e:
            print(f"\nПроизошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    run_calculator()