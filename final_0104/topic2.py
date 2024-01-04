class Employer:
    def __init__(self, name, seniority, time):
        self.name = name
        self.seniority = seniority
        self.time = time

    def check_name(self):
        print(f"姓名: {self.name}") #列印姓名

    def check_seniority(self):
        print(f"年資: {self.seniority} 年") #列印年資

    def check_time(self):
        print(f"時數: {self.time} 小時") #列印時數

    def calculate_salary(self):
        hours_salary = 170 #時薪設定170
        total_salary = hours_salary * self.time * 30 #計算月薪_(時薪*時數*一個月30天)

        print(f"月薪: {total_salary}") #列印月薪

    def add_time(self, add_time):
        self.time += add_time #增加時數(self.time = self.time + add_time)
        print(f"增加工時: {add_time} 小時") #列印時數

    def add_seniority(self, add_years):
        self.seniority += add_years #增加年資
        print(f"增加年資: {add_years} 年") #列印年資

class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ColdDrinks(Drinks):
    def __init__(self, name, price, sweet, ice):
        super().__init__(name, price)  #繼承Drinks類別設定名稱及價格
        self.sweet = sweet
        self.ice = ice  

class HotDrinks(Drinks):
    def __init__(self, name, price, sweet):
        super().__init__(name, price)  #繼承Drinks類別設定名稱及價格
        self.sweet = sweet


employee1 = Employer("john", 5, 40)
employee2 = Employer("jane", 3, 35)
employee3 = Employer("kevinnn", 2, 45)

employee1.check_name()
employee1.check_seniority()
employee1.check_time()
employee1.calculate_salary()

employee1.add_time(5) #增加5小時
employee1.add_seniority(1) #增加1年年資

employee1.check_time()
employee1.check_seniority()
employee1.calculate_salary()

print("\n")

employee2.check_name()
employee2.check_seniority()
employee2.check_time()
employee2.calculate_salary()

employee2.add_time(3)
employee2.add_seniority(2)

employee2.check_time()
employee2.check_seniority()
employee2.calculate_salary()

print("\n")

employee3.check_name()
employee3.check_seniority()
employee3.check_time()
employee3.calculate_salary()

employee3.add_time(8)
employee3.add_seniority(3)

employee3.check_time()
employee3.check_seniority()
employee3.calculate_salary()

print("\n")

drink1 = ColdDrinks("Black Tea", 100, "Medium", "less ice")
drink2 = HotDrinks("Coffee", 50, "Less sweet")
drink3 = HotDrinks("Milk", 80, "No sweet")

print(f"冷飲: {drink1.name}, 價格: {drink1.price}, 甜度: {drink1.sweet}, 冰度: {drink1.ice}")
print("\n")
print(f"熱飲: {drink2.name}, 價格: {drink2.price}, 甜度: {drink2.sweet}")
print("\n")
print(f"熱飲: {drink3.name}, 價格: {drink3.price}, 甜度: {drink3.sweet}")
print("\n")