import doctest


class Human:
    def __init__(self, is_male: bool, height: float, weight: float):
        """
        Создание и подготовка к работе объекта "Человек"

        :param is_male: Человек мужского пола?
        :param height: Рост человека (см)
        :param weight: Вес человека (кг)

        Примеры:
        >>> human = Human(True, 184.6, 75)  # инициализация экземпляра класса
        """

        if not isinstance(is_male, bool):
            raise TypeError("Аргумент is_male должен быть типа bool")
        self.is_male = is_male

        if not isinstance(height, (int, float)):
            raise TypeError("Рост должен быть типа int или float")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self.height = height

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

    def BMI_calculation(self) -> float:
        """
        Функция, которая расчитывает ИМТ

        :return: значение ИМТ

        Примеры:
        >>> human = Human(True, 184.6, 75)
        >>> human.BMI_calculation()
        """
        ...

    def height_increase(self, added_height: float) -> float:
        """
        Увеличение роста человека

        :param added_height: Количество сантиметров, на которое вырос человек
        :return: Рост человека после увеличения

        Примеры:
        >>> human = Human(True, 184.6, 75)
        >>> human.height_increase(4)
        """
        if not isinstance(added_height, (int, float)):
            raise TypeError("Количество сантиметров, на которое вырос человек, должно быть типа int или float")
        if added_height <= 0:
            raise ValueError("Количество сантиметров, на которое вырос человек, должно быть положительным числом")
        ...

    def sex_change(self) -> bool:
        """
        Изменение пола человека #почему бы и нет

        :return: ответ на вопрос "Человек мужского пола?" после изменения

        Примеры:
        >>> human = Human(True, 184.6, 75)
        >>> human.sex_change()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации