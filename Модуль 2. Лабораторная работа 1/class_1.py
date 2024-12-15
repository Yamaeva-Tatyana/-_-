import doctest


class Smartphone:
    def __init__(self, model: str, memory_capacity: int, battery_charge: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param model: Модель смартфона
        :param memory_capacity: Объем памяти (ГБ)
        :param battery_charge: Заряд батареи (%)

        Примеры:
        >>> smartphone = Smartphone("iPhone 14 Pro Max", 256, 80)
        """

        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть типа str")
        self.model = model

        if not isinstance(memory_capacity, int):
            raise TypeError("Объем памяти должен быть типа int")
        if memory_capacity <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory_capacity = memory_capacity

        if not isinstance(battery_charge, int):
            raise TypeError("Заряд батареи должен быть типа int")
        if battery_charge < 0:
            raise ValueError("Заряд батареи не может быть отрицательным числом")
        self.battery_charge = battery_charge

    def is_smartphone_discharged(self) -> bool:
        """
        Функция, которая проверяет разряжен ли смартфон

        :return: Является ли смартфон разряженным

        Примеры:
        >>> smartphone = Smartphone("iPhone 14 Pro Max", 256, 80)
        >>> smartphone.is_smartphone_discharged()
        """
        ...

    def charging_smartphone(self, added_charge: int) -> int:
        """
        Зарядка смартфона

        :param added_charge: Число добавленных процентов к заряду батареи
        :raise ValueError: Если заряд батареи после добавленных процентов превышает 100%, то вызываем ошибку
        :return: Заряд батареи после добавления процентов

        Примеры:
        >>> smartphone = Smartphone("iPhone 14 Pro Max", 256, 80)
        >>> smartphone.charging_smartphone(10)
        """
        if not isinstance(added_charge, int):
            raise TypeError("Количество добавленных процентов должно быть типа int")
        if added_charge < 0:
            raise ValueError("Добавленные проценты должны быть положительным числом")
        ...

    def discharging_smartphone(self, reduced_charge: int) -> int:
        """
        Разрядка смартфона

        :param reduced_charge: Число убавленных процентов
        :raise ValueError: Если число убавленных процентов превышает заряд батареи, то вызываем ошибку
        :return: Заряд батареи после убавления процентов

        Примеры:
        >>> smartphone = Smartphone("iPhone 14 Pro Max", 256, 80)
        >>> smartphone.discharging_smartphone(20)
        """
        if not isinstance(reduced_charge, int):
            raise TypeError("Количество убавленных процентов должно быть типа int")
        if reduced_charge < 0:
            raise ValueError("Убавленные проценты должны быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации