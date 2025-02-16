class Glasses:
    """ Базовый класс, описывающий модель очков """
    def __init__(self, brand: str, colour: str, material: str, quantity: int):
        """
        Инициализация базового класса "Очки"

        :param brand: Бренд очков
        :param colour: Цвет оправы
        :param material: Материал оправы
        :param quantity: Кол-во в наличии
        """

        self._brand = brand #Непубличный атрибут, только для чтения
        self._colour = colour #Непубличный атрибут, только для чтения
        self._material = material #Непубличный атрибут, только для чтения
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Очки. Бренд: {self._brand}. Цвет оправы: {self._colour}. Материал оправы: {self._material}. Кол-во в наличии: {self.quantity}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, colour={self._colour!r}, material={self._material!r}, quantity={self.quantity!r})"

    def is_quantity_in_stock(self, necessary_quantity: int) -> bool:
        """
        Функция, которая проверяет, есть ли в наличии необходимое кол-во очков. Наследуется в дочерние классы.

        :return: Есть ли в наличии
        """
        return necessary_quantity <= self.quantity

    def get_info(self) -> str:
        """
        Получение информации об очках.

        :return: Строка с информацией об очках.
        """
        return f"Очки бренда {self._brand}. Оправа выполнена из материала - {self._material}, цвет - {self._colour}."

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def colour(self) -> str:
        return self._colour

    @property
    def material(self) -> str:
        return self._material

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if not isinstance(new_quantity, int):
            raise TypeError
        if new_quantity < 0:
            raise ValueError
        self._quantity = new_quantity


class Sunglasses(Glasses):
    """ Дочерний класс, описывающий модель солнцезащитных очков """
    def __init__(self, brand: str, colour: str, material: str, quantity: int, UV: int, filter_cat: int):
        """
        Инициализация дочернего класса "Солнцезащитные очки"

        :param UV: Степень защиты от ультрафиолета в диапазоне от 10 до 400 нм
        :param filter_cat: Категория затемненности в диапазоне от 0 до 4
        """

        super().__init__(brand=brand, colour=colour, material=material, quantity=quantity)
        self.UV = UV
        self.filter_cat = filter_cat

    def __str__(self) -> str:
        return f"Солнцезащитные очки. Бренд: {self._brand}. Цвет оправы: {self._colour}. Материал оправы: {self._material}. Степень защиты: UV{self.UV}. Категория затемненности: {self.filter_cat}. Кол-во в наличии: {self.quantity}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, colour={self._colour!r}, material={self._material!r}, quantity={self.quantity!r}, UV={self.UV!r}, filter_cat={self.filter_cat!r})"

    def get_info(self) -> str:
        """
        Получение информации о солнцезащитных очках.

        Переопределяем метод, чтобы добавить информацию о защите от УФ и категории затемненности.

        :return: Строка с информацией о солнцезащитных очках.
        """
        return f"{super().get_info()} С ультрафиолетовой защитой до {self.UV} нм и {self.filter_cat}-ой степенью затемненности."

    @property
    def UV(self) -> int:
        return self._UV

    @UV.setter
    def UV(self, new_UV: int) -> None:
        if not isinstance(new_UV, int):
            raise TypeError
        if not 10 <= new_UV <= 400:
            raise ValueError
        self._UV = new_UV

    @property
    def filter_cat(self) -> int:
        return self._filter_cat

    @filter_cat.setter
    def filter_cat(self, new_filter_cat: int) -> None:
        if not isinstance(new_filter_cat, int):
            raise TypeError
        if not 0 <= new_filter_cat <= 4:
            raise ValueError
        self._filter_cat = new_filter_cat


class Eyeglasses(Glasses):
    """ Дочерний класс, описывающий модель очков для зрения """
    def __init__(self, brand: str, colour: str, material: str, quantity: int, diopter: float):
        """
        Инициализация дочернего класса "Очки для зрения"

        :param diopter: Диоптрии линз (положительное или отрицательное число с шагом 0,25)
        """

        super().__init__(brand=brand, colour=colour, material=material, quantity=quantity)
        self.diopter = diopter

    def __str__(self) -> str:
        return f"Очки для зрения. Бренд: {self._brand}. Цвет оправы: {self._colour}. Материал оправы: {self._material}. Диоптрии линз: {self.diopter}. Кол-во в наличии: {self.quantity}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, colour={self._colour!r}, material={self._material!r}, quantity={self.quantity!r}, diopter={self.diopter!r})"

    def get_info(self) -> str:
        """
        Получение информации об очках для зрения.

        Переопределяем метод, чтобы добавить информацию о диоптриях.

        :return: Строка с информацией об очках для зрения.
        """
        return f"{super().get_info()} Линзы с диоптриями {self.diopter}."

    @property
    def diopter(self) -> float:
        return self._diopter

    @diopter.setter
    def diopter(self, new_diopter: float) -> None:
        if not isinstance(new_diopter, float):
            raise TypeError
        if not new_diopter % 0.25 == 0:
            raise ValueError
        self._diopter = new_diopter


if __name__ == "__main__":
    glasses = Glasses("Ray-Ban", "чёрный", "пластик", 12)
    sunglasses = Sunglasses("Gucci", "коричневый", "метал", 21, 400, 3)
    eyeglasses = Eyeglasses("Mango", "красный", "пластик", 0, -2.25)

    print(glasses, sunglasses, eyeglasses, sep='\n')
    print(glasses.is_quantity_in_stock(2), eyeglasses.is_quantity_in_stock(2))
    print(sunglasses.get_info())

    eyeglasses.quantity = 10
    eyeglasses.diopter = -3.50

    print(eyeglasses.is_quantity_in_stock(2))
    print(eyeglasses.__repr__())

    pass