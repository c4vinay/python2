from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, fuel_capacity, fuel_efficiency):
        self.__brand = brand
        self.__fuel_capacity = fuel_capacity  # max fuel in L
        self.__fuel_efficiency = fuel_efficiency  # km per litre
        self.__fuel_level = 0  # current fuel
        self.__km_run = 0

    # Encapsulation: Getters
    def get_brand(self):
        return self.__brand

    def get_fuel_level(self):
        return self.__fuel_level

    def get_km_run(self):
        return self.__km_run

    def get_fuel_capacity(self):
        return self.__fuel_capacity

    def get_fuel_efficiency(self):
        return self.__fuel_efficiency

    # Abstraction: Refuel and travel methods
    def refuel(self, liters):
        if liters + self.__fuel_level <= self.__fuel_capacity:
            self.__fuel_level += liters
            print(f"{self.__brand}: Refueled {liters}L. Current fuel: {self.__fuel_level}L")
        else:
            print(f"{self.__brand}: Cannot refuel beyond fuel capacity.")

    def travel(self, km):
        fuel_needed = km / self.__fuel_efficiency
        if fuel_needed <= self.__fuel_level:
            self.__fuel_level -= fuel_needed
            self.__km_run += km
            print(f"{self.__brand}: Trip of {km} km completed.")
        else:
            print(f"{self.__brand}: Not enough fuel for the trip.")

    # Abstract methods for polymorphism
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def summary(self):
        pass

    # Service check (if km_run > 10000, needs service)
    def needs_service(self):
        return self.__km_run > 10000

# === Subclasses with Polymorphism ===
class Car(Vehicle):
    def start(self):
        print(f"{self.get_brand()} Car is starting...")

    def stop(self):
        print(f"{self.get_brand()} Car is stopping...")

    def summary(self):
        print(f"Car - Brand: {self.get_brand()}, Fuel: {self.get_fuel_level()}L, KM Run: {self.get_km_run()}")

class Bike(Vehicle):
    def start(self):
        print(f"{self.get_brand()} Bike is starting...")

    def stop(self):
        print(f"{self.get_brand()} Bike is stopping...")

    def summary(self):
        print(f"Bike - Brand: {self.get_brand()}, Fuel: {self.get_fuel_level()}L, KM Run: {self.get_km_run()}")

class Truck(Vehicle):
    def start(self):
        print(f"{self.get_brand()} Truck is starting...")

    def stop(self):
        print(f"{self.get_brand()} Truck is stopping...")

    def summary(self):
        print(f"Truck - Brand: {self.get_brand()}, Fuel: {self.get_fuel_level()}L, KM Run: {self.get_km_run()}")

# === Fleet Manager ===
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def fleet_summary(self):
        print("\n=== Fleet Summary ===")
        for v in self.vehicles:
            v.summary()
            print(f"{v.get_brand()} is a {v.__class__.__name__}")
            print("Needs Service" if v.needs_service() else "Does Not Need Service")
            print()

def main():
    # Creating vehicle objects
    car = Car("Toyota", fuel_capacity=50, fuel_efficiency=15)
    bike = Bike("Yamaha", fuel_capacity=15, fuel_efficiency=40)
    truck = Truck("Volvo", fuel_capacity=100, fuel_efficiency=5)

    # Car actions
    car.start()
    car.refuel(30)
    car.travel(200)
    car.summary()
    car.stop()

    # Simulate wear
    car._Vehicle__km_run += 10000  # forcefully increase for service check

    # Bike actions
    bike.start()
    bike.refuel(30)  # over capacity
    bike.summary()
    bike.stop()

    # Truck actions
    truck.start()
    truck.refuel(30)
    truck.travel(200)
    truck.summary()
    truck.stop()

    # Add to fleet and print summary
    fleet = Fleet()
    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(truck)

    fleet.fleet_summary()

if __name__ == "__main__":
    main()
