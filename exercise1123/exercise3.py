class car:
    def __init__(self,brand,model,color,years):
        self.brand = brand
        self.model = model
        self.color = color
        self.years = years

    def carBrand(self):
        print("This car's brand is",self.brand)

    def carModel(self):
        print("This car's model is",self.model)

    def carColor(self):
        print("This car's color is",self.color)

    def carYears(self):
        print("This car's years is",self.years)

car1 = car('Honda','CRV','White',2023)
car1.carBrand()
car1.carModel()
car1.carColor()
car1.carYears()