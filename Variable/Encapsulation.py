class car:
    def __init__(self,make,model,year):
        self.__make = make
        self.__model = model
        self.year = year
    def get_details(self):
        return (f"{self.__make} {self.__model} (self.__year)")
    def update_year(self,year):
        if year > 1885:
            self.year = year
        else:
            print("Invalid year please provide a valid year")
my_car = car("Toyota","Fortuner", "2022")
print(my_car.get_details())
my_car.update_year(2022)
print(my_car.get_details())
