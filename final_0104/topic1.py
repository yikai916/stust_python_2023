class FriedChicken:
    def __init__(self, flavor, amount, spices, part, size):
        self.flavor = flavor
        self.amount = amount
        self.spices = spices
        self.part = part
        self.size = size

    def add_amount(self):
        add = int(input('增加數量:')) #輸入欲增加數量
        self.amount += add #加上輸入之數量

    def choose_flavor(self):
        print(f'口味:{self.flavor}') #列印口味

    def calculate_price(self):
        unit_price = 100 #炸機每份100
        total_price = unit_price * self.amount #炸機數量*金額
        print(f'金額:{total_price}') #列印金額


obj1 = FriedChicken('Original', 2, 'Salt', 'Thigh', 'large')
obj2 = FriedChicken('Spicy', 1, 'Cajun', 'Leg', 'medium')
obj3 = FriedChicken('BBQ', 3, 'Barbecue', 'Breast', 'small')
obj4 = FriedChicken('Garlic Parmesan', 4, 'Garlic', 'Wing', 'large')

obj1.add_amount()
obj1.choose_flavor()
obj1.calculate_price()

obj2.add_amount()
obj2.choose_flavor()
obj2.calculate_price()

obj3.add_amount()
obj3.choose_flavor()
obj3.calculate_price()

obj4.add_amount()
obj4.choose_flavor()
obj4.calculate_price()
