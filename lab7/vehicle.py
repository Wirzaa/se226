class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"Vehicle ID is: {self.vid} | Vehicle model is: {self.model} | Vehicle is from: {self.year}"
    
    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        
        return other.vid == self.vid
        
    def is_new(self, n):
        if 2026-int(n) <= int(self.year):
            return True
        else:
            return False
    
class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors
    def __str__(self):
        mainO = super().__str__()
        return f"{mainO} | Fuel: {self.fuel_type} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles
    def __str__(self):
        mainO = super().__str__()
        return f"{mainO} | Load: {self.max_load} | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type
    def __str__(self):
        mainO = super().__str__()
        return f"{mainO} | Engine: {self.engine_cc} | Type: {self.type}"
    
def save_fleet_to_file(vehicles, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for v in vehicles:
                line = f"{type(v).__name__}, {v.vid}, {v.model}, {v.year}"

                if isinstance(v, Car):
                    line += f", {v.fuel_type}, {v.doors}"
                elif isinstance(v, Truck):
                    line += f", {v.max_load}, {v.axles}"
                elif isinstance(v, Motorcycle):
                    line+= f", {v.engine_cc}, {v.type}"
            
                f.write(line +"\n")
    except Exception as e:
        print(f"An error occured while saving: {e}")

def load_from_file(filename):
    recon_fleet = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split(", ")
                if not data or len(data) < 4:
                    continue
                v_type = data[0]
                vid = data[1]
                model = data[2]
                year = int(data[3])

                if v_type == "Car":
                    obj = Car(vid, model, year, data[4], int(data[5]))
                elif v_type == "Truck":
                    obj = Truck(vid, model, year, int(data[4]), int(data[5]))
                elif v_type == "Motorcycle":
                    obj = Motorcycle(vid, model, year, int(data[4]), data[5])
                else:
                    print("Unknown vehicle type skipped.")
                    print(v_type)
                    continue
                recon_fleet.append(obj)
        return recon_fleet
    except FileNotFoundError:
        print(f"Error: {filename} can not be found!")
        return[]
    except Exception as e:
        print(f"Unexpected error has occured: {e}")
        return[]
    
if __name__ == "__main__":

    my_vehicles = [
        Car("C001", "Skoda Superb", 2024, "Gasoline", 4),
        Car("C002", "Toyota Corolla", 2018, "Hybrid", 4),
        Truck("T001", "Mercedes Actros", 2021, 19000, 2),
        Truck("T002", "Ford F-150", 2024, 1500, 2),
        Motorcycle("M001", "Kawasaki Ninja400", 2021, 399, "Sport"),
        Motorcycle("M002", "Harley Davidson Iron833", 2019, 833, "Cruiser")
    ]

    print(f"---Fleet is being saved to file---")
    save_fleet_to_file(my_vehicles, "fleet.txt")

    print(f"---Fleet is being loaded from the file---")
    loaded_fleet = load_from_file("fleet.txt")
    
    print("---All Vehicles---")
    for v in loaded_fleet:
        print(v)
    print("\n--- Recent Vehicles (Last 4 years) ---")
    for v in loaded_fleet:
        if v.is_new(4):
            print(v)
    print("\n---Electric Cars Only---")
    for v in loaded_fleet:
        if isinstance(v, Car) and v.fuel_type == "Electric":
            print(v)
        

