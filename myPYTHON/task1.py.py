class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Create two car objects
car1 = Car("Lamborghini", "Huracan", 2014)
car2 = Car("Koenigsegg ", "Agera", 2010)

# Display their details
car1.display_info()
print()  # Add a newline for better readability
car2.display_info()