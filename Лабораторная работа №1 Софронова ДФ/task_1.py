# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class CookiesPackage:
    def __init__(self, name: str, quantity_of_cookies: int, price: float):
        """
        Создание и подготовка к работе объекта "Коробка печенья"

        :param name: Наименование бренда печенья
        :param quantity_of_cookies: Количество печенья в коробке
        :param price: Цена коробки печенья

        Примеры:
        >>> cookies_package = CookiesPackage("Milka", 20, 199.99)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Наименование бренда печенья должно быть типа str")
        if len(name) == 0:
            raise ValueError("Наименование бренда печенья должно содержать символы")
        self.name = name

        if not isinstance(quantity_of_cookies, int):
            raise TypeError("Количество печенья в коробке должно быть типа int")
        if quantity_of_cookies <= 0:
            raise ValueError("Количество печенья в коробке должо быть больше 0")
        self.quantity_of_cookies = quantity_of_cookies

        if not isinstance(price, float):
            raise TypeError("Цена печенья должна быть типа float")
        if price <= 0:
            raise ValueError("Цена печенья должна быть больше 0")
        self.price = price

    def price_change(self, percent: int) -> float:
        """
        Функция, которая изменяет цену на указанное число процентов
        :param percent: Значение в процентах, на которое изменяется цена
        :raise ValueError: Если значение изменения цены не целое число, то вызывает ошибку
        :return: Измененное значение цены коробки печенья

        Примеры:
        >>> cookies_package = CookiesPackage("Milka", 5, 349.99)
        >>> cookies_package.price_change(-15)
        """
        if not isinstance(percent, int):
            raise TypeError("Значение в процентах, на короторое изменяется цена, должно быть типа int")
        ...

    def eat_cookies(self, number_of_cookes: int) -> None:
        """
        Функция, которая съедает печенье из коробки
        :param number_of_cookes: количество печенья, которое будет съедено
        :raise ValueError: Если печенья в коробке меньше, чем планировалось съесть, вызывает ошибку

        Примеры:
        >>> cookies_package = CookiesPackage("Milka", 5, 349.99)
        >>> cookies_package.eat_cookies(2)
        """
        if not isinstance(number_of_cookes, int):
            raise TypeError("Количество печенья для поедания должно быть типа int")
        ...


class BankAccount:
    def __init__(self, number: int, currency_name: str, value: float):
        """
        Создание и подготовка к работе объекта "Банковский аккаунт"

        :param number: Номер банковского счета
        :param currency_name: Наименование валюты
        :param value: Количество денег на счете

        Примеры:
        >>> bank_account = BankAccount(80070060050040055555, "EUR", 5000.50)
        """

        if not isinstance(number, int):
            raise TypeError("Номер банковского счета должен быть типа int")
        if not len(str(number)) == 20:
            raise ValueError("Номер банковского счета должен состоять из 20 цифр")
        self.number = number

        if not isinstance(currency_name, str):
            raise TypeError("Наименование валюты должно быть типа str")
        if not len(currency_name) == 3:
            raise ValueError("Наименование валюты должно состоять из 3 символов")
        self.currency_name = currency_name

        if not isinstance(value, float):
            raise TypeError("Количество денег на счете должно быть типа float")
        self.value = value
        if value < 0:
            raise ValueError("Количество денег на счете должно быть больше 0")

    def add_money(self, income_value: float) -> None:
        """
        Функция, которая кладет деньги на счет
        :param income_value: Сумма зачисления

        Примеры:
        >>> bank_account = BankAccount(12012012012012012012, "USD", 65700.0)
        >>> bank_account.add_money(887.7)
        """
        if not isinstance(income_value, float):
            raise TypeError("Сумма зачисления должна быть типа float")
        if income_value <= 0:
            raise ValueError("Сумма зачисления должна быть больше 0")
        ...

    def get_money(self, outcome_value: float) -> None:
        """
        Функция, которая снимат деньги с счета
        :param outcome_value: Сумма списания
        :raise ValueError: Если запрашиваемая сумма превышает количество денег на счете, то возвращается ошибка

        Примеры:
        >>> bank_account = BankAccount(81181181181181181181, "RUB", 100100100.88)
        >>> bank_account.get_money(8940.0)
        """
        if not isinstance(outcome_value, float):
            raise TypeError("Сумма списания должна быть типа float")
        if outcome_value <= 0:
            raise ValueError("Сумма списания должна быть больше 0")
        ...


class Car:
    def __init__(self, gas_volume: float, colour: str):
        """
        Создание и подготовка к работе объекта "Машина"
        :param gas_volume: Количесвто бензина в машине
        :param colour: Цвет машины

        Примеры:
        >>> supra = Car(50.0, "Pink")
        """
        if not isinstance(gas_volume, float):
            raise TypeError("Количество бензина должно быть типа float")
        if gas_volume < 0:
            raise ValueError("Количество бензина быть не меньше 0")
        self.gas_volume = gas_volume

        if not isinstance(colour, str):
            raise TypeError("Цвет машины должен быть типа str")
        if len(colour) == 0:
            raise ValueError("Цвет машины должен содержать символы")
        self.colour = colour

    def is_this_car_blue(self) -> bool:
        """
        Функция проверяет синего ли цвета машина
        :return: Является ли машина синей

        Примеры:
        >>> red_car = Car(10.5, "Red")
        >>> red_car.is_this_car_blue()
        """
        ...

    def add_gas(self, income_value: float) -> None:
        """
        Функция, которая добавляет бензин в машину
        :param income_value: Количество бензина добавляемое в машину

        Примеры:
        >>> miata = Car(15.0, "Light green")
        >>> miata.add_gas(5.0)
        """
        if not isinstance(income_value, float):
            raise TypeError("Количество бензина должно быть типа float")
        if income_value <= 0:
            raise ValueError("Количество бензина должно быть больше 0")
        self.is_this_car_blue()
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    # pass
    doctest.testmod()
