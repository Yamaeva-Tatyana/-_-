import doctest


class Car:
    def __init__(self, brand: str, colour: str, engine_power: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param colour: Цвет кузова
        :param engine_power: Мощность двигателя (в лошадиных силах)

        Примеры:
        >>> car = Car("Lada", "синий", 150)  # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.brand = brand

        if not isinstance(colour, str):
            raise TypeError("Цвет кузова должен быть типа str")
        self.colour = colour

        if not isinstance(engine_power, int):
            raise TypeError("Мощность двигателя должна быть типа int")
        if engine_power <= 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self.engine_power = engine_power

    def colour_change(self, new_colour: str) -> None:
        """
        Перекраска кузова автомобиля

        :param new_colour: Новый цвет кузова

        Примеры:
        >>> car = Car("Lada", "синий", 150)
        >>> car.colour_change("красный")
        """
        if not isinstance(new_colour, str):
            raise TypeError("Новый цвет кузова должен быть типа str")
        ...

    def engine_power_increase(self, added_power: int) -> None:
        """
        Увеличение мощности двигателя

        :param added_power: Количество лошадиных сил, на которое увеличилась мощность двигателя

        Примеры:
        >>> car = Car("Lada", "синий", 150)
        >>> car.engine_power_increase(25)
        """
        if not isinstance(added_power, int):
            raise TypeError("Количество лошадиных сил, на которое увеличилась мощность двигателя, должно быть типа int")
        if added_power <= 0:
            raise ValueError("Количество лошадиных сил, на которое увеличилась мощность двигателя, должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации