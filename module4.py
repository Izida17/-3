class CosmeticProduct:
    """Представления косметического продукта."""
    
    product_type: str = "Декоративная косметика"  # Атрибут класса тип продукта
    default_origin: str = "Италия"                # Атрибут класса страна производства

    def __init__(self, product_name: str, manufacturer: str, color: str, 
                 cost: float, expiry: str) -> None:
        """Инициализирует экземпляр косметического продукта.
        
        Аргументы:
            product_name (str): Наименование продукта
            manufacturer (str): Производитель
            color (str): Оттенок
            cost (float): Стоимость в рублях
            expiry (str): Дата окончания срока годности (ГГГГ-ММ-ДД)
        """
        self.product_name = product_name
        self.manufacturer = manufacturer
        self.color = color
        self.cost = cost
        self.expiry = expiry
        self.is_used = False  # Флаг использования продукта

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return (f"Косметический продукт: {self.product_name}, {self.manufacturer}, "
                f"{self.color}, {self.cost}, {self.expiry}")

    def mark_as_used(self) -> None:
        """Помечает продукт как использованный."""
        self.is_used = True
        print(f"{self.product_name} теперь помечен как использованный.")

    def check_expiry_status(self, current_date: str) -> bool:
        """Проверяет, истек ли срок годности.
        
        Аргументы:
            current_date (str): Текущая дата для сравнения (ГГГГ-ММ-ДД)
        Возвращает:
            bool: True если срок годности истек, иначе False
        """
        return self.expiry < current_date

    def apply_discount(self, discount_percent: float) -> None:
        """Применяет скидку к стоимости продукта.
        
        Аргументы:
            discount_percent (float): Процент скидки (0%-100%)
        """
        if 0 <= discount_percent <= 100:
            self.cost *= (1 - discount_percent / 100)
            print(f"Применена скидка {discount_percent}%. Новая цена: {self.cost:.2f} руб.")
        else:
            print("Неверный процент скидки. Допустимый диапазон: 0%-100%.")

    def get_product_details(self) -> str:
        """Возвращает подробную информацию о продукте.
        
        Возвращает:
            str: Строка с полным описанием продукта
        """
        details = (f"Продукт: {self.product_name}\n"
                   f"Бренд: {self.manufacturer}\n"
                   f"Цвет: {self.color}\n"
                   f"Цена: {self.cost:.2f} руб.\n"
                   f"Годен до: {self.expiry}\n"
                   f"Статус: {'Использован' if self.is_used else 'Новый'}")
        return details


# Создаем экземпляры класса
lip_gloss = CosmeticProduct("Блеск для губ DEFENCE COLOR LIP PLUMP", "BioNike", 
                           "002 Rose Gold", 2950.00, "2025-08-22")
eye_shadow = CosmeticProduct("Тени для век Ombre 4 Couleurs", "Clarins", 
                            "05 Jade Gradation", 4889.50, "2024-10-01")
concealer = CosmeticProduct("Консилер Pure beauty fluid", "Astra Make-Up", "Vanilla", 1290.00, "2026-06-17")

# Демонстрация работы методов
print(lip_gloss)  # Используется __str__
print(eye_shadow.get_product_details())  # Вывод полной информации
concealer.apply_discount(15)  # Применяем скидку 15%
lip_gloss.mark_as_used()  # Помечаем как использованный

# Проверка срока годности
print("Срок годности истек:", eye_shadow.check_expiry_status("2025-04-06"))
