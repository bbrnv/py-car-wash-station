class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(self, 
                 distance_from_city_center: float, 
                 clean_power: int,
                 average_rating: float, 
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    
    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class 
                     *(self.clean_power - car.clean_mark) 
                     * self.average_rating 
                     / self.distance_from_city_center, 1)


    def wash_single_car(self, car: Car) -> float:
        single_income = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return single_income


    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)
        return income
    

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
    

bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

print(income)
print(bmw.clean_mark)
print(audi.clean_mark)
print(mercedes.clean_mark)  

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford) 

print(wash_cost)
print(ford.clean_mark)
ws.rate_service(5)
print(ws.count_of_ratings)
print(ws.average_rating)