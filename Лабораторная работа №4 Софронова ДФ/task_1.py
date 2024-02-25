class Automobile:
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        """
        Конструктор базового класса Automobile.
        :param brand: Наименование производителя автомобиля.
        :param model: Модель автомобиля.
        :param max_speed: Максимальная скорость автомобиля.
        """
        self.brand: str = brand
        self._model: str = model
        self._max_speed: int = max_speed

    def start_automobile(self) -> None:
        """
        Метод, запускающий двигатель автомобиля.
        """
        pass

    def fill_automobile(self, volume: float) -> None:
        """
        Метод заправляющий автомобиль.
        """
        pass

    def __str__(self) -> str:
        """
        Метод для представления объекта в виде строки.
        """
        return f"{self.brand} {self._model} {self._max_speed}"

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде строки при отладке.
        """
        return f"{self.__class__.__name__}({self.brand}, {self._model}, {self._max_speed})"


class ElectricCar(Automobile):
    def __init__(self, brand: str, model: str, max_speed: int, battary_capacity: float) -> None:
        """
        Конструктор дочернего класса ElectricCar.
        :param battary_capacity: Объем аккумулятора электрокара
        """
        super().__init__(brand, model, max_speed)
        self.battary_capacity: float = battary_capacity

    def start_automobile(self) -> None:
        """
        Перегруженный метод запуска двигателя для электрокара.
        Обоснование: Запуск двигателя у электрокара отличается.
        """
        pass

    def charging_automobile(self, current: float) -> None:
        """
        Метод для зарядки электрокара.
        """
        pass


class Minivan(Automobile):
    def __init__(self, brand: str, model: str, max_speed: int, seats_number: int) -> None:
        """
        Конструктор дочернего класса Minivan.
        :param seats_number: Количество мест в автомобиле.
        """
        super().__init__(brand, model, max_speed)
        self.seats_number: float = seats_number

    def fill_automobile(self, volume: float) -> None:
        """
        Перегруженный метод заправляющий автомобиль.
        Обоснование: Необходимо учесть дополниельную канистру для дальних путешествий в минивене.
        """
        pass

    def seats_fold(self, number: int) -> None:
        """
        Метод для складывания сидений в минивене
        """
        pass


if __name__ == "__main__":
    porsche_taycan = ElectricCar("Porsche", "Taycan", 250, 93.4)
    grand_starex = Minivan("Hyundai", "Grand starex", 180, 8)

    print(porsche_taycan)
    print(porsche_taycan.brand)
    porsche_taycan.charging_automobile(21.0)

    print(grand_starex)
