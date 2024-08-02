class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}\nДеньги: {self.__money}\nДом: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}\nВозраст по умолчанию: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Заработал {amount} денег')


    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f'Дом Куплен, поздравляю!')
        else:
            print('Недостаточно денег, иди работай!')


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Стоимость дома сейчас: {final_price}')
        return final_price

class SmollHouse(House):

    default_area = 40
    def __init__(self, price):
        super().__init__(SmollHouse.default_area, price)

Human.default_info()
print()
alex = Human('Alex', 43)
alex.info()
print()
shouse = SmollHouse(5000)
alex.buy_house(shouse, 20)
print()
alex.earn_money(10000)
alex.buy_house(shouse, 20)

