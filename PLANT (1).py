import random
import json
from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.has_sunlight = False
        self.has_water = False
        self.health = 100
        self.times_grown = 0

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def photosynthesize(self):
        pass

    @abstractmethod
    def absorb_water(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    def provide_sunlight(self):
        self.has_sunlight = True
        print(f"{self.name} has received sunlight.")

    def check_health(self):
        print(f"{self.name}'s current health is {self.health}.")
        if self.health <= 0:
            print(f"Oh no! {self.name} has withered away. 💀")

class Tree(Plant):
    def grow(self):
        if self.has_water and self.has_sunlight:
            self.height += 10
            self.age += 1
            self.health = min(100, self.health + 5)
            self.times_grown += 1
            print(f"The tree {self.name} grew taller! Now it's {self.height} cm tall and {self.age} years old.")
            if self.height >= 50:
                print("🎉 Achievement unlocked: Tall Tree!")
        else:
            self.health -= 10
            print(f"The tree {self.name} needs both water and sunlight to grow. Health is now {self.health}.")

    def photosynthesize(self):
        if self.has_sunlight:
            print(f"The tree {self.name} is photosynthesizing.")
        else:
            print("Provide sunlight first.")

    def absorb_water(self):
        self.has_water = True
        print(f"The tree {self.name} has absorbed water.")

    def describe(self):
        print(f"Tree: {self.name} | Height: {self.height} cm | Age: {self.age} years")

class Flower(Plant):
    def grow(self):
        if self.has_water and self.has_sunlight:
            self.height += 5
            self.age += 0.5
            self.health = min(100, self.health + 5)
            self.times_grown += 1
            print(f"The flower {self.name} has grown! It's now {self.height} cm tall and {self.age:.1f} years old.")
            if self.height >= 30:
                print("🌸 Achievement unlocked: Blooming Beauty!")
        else:
            self.health -= 10
            print("Water and sunlight are required for growth. Health is now", self.health)

    def photosynthesize(self):
        if self.has_sunlight:
            print(f"The flower {self.name} is making food through photosynthesis.")
        else:
            print("Sunlight is missing.")

    def absorb_water(self):
        self.has_water = True
        print(f"{self.name} has been watered.")

    def describe(self):
        print(f"Flower: {self.name} | Height: {self.height} cm | Age: {self.age} years")

class Cactus(Plant):
    def grow(self):
        if self.has_sunlight:
            self.height += 2
            self.age += 0.2
            self.health = min(100, self.health + 3)
            self.times_grown += 1
            print(f"Cactus {self.name} grew a little. Height: {self.height} cm, Age: {self.age:.1f} years.")
            if self.height >= 20:
                print("🌵 Achievement unlocked: Desert Survivor!")
        else:
            self.health -= 5
            print("Cactus needs sunlight to grow. Health is now", self.health)

    def photosynthesize(self):
        if self.has_sunlight:
            print(f"Cactus {self.name} is photosynthesizing through its stem.")
        else:
            print("Sunlight required.")

    def absorb_water(self):
        self.has_water = True
        print(f"{self.name} has stored water.")

    def describe(self):
        print(f"Cactus: {self.name} | Height: {self.height} cm | Age: {self.age} years")

class Fern(Plant):
    def grow(self):
        if self.has_water and self.has_sunlight:
            self.height += 4
            self.age += 0.3
            self.health = min(100, self.health + 4)
            self.times_grown += 1
            print(f"The fern {self.name} has grown. New height: {self.height} cm.")
            if self.height >= 25:
                print("🌿 Achievement unlocked: Lush Leaves!")
        else:
            self.health -= 7
            print("The fern needs more care. Health is now", self.health)

    def photosynthesize(self):
        if self.has_sunlight:
            print(f"Fern {self.name} is photosynthesizing.")
        else:
            print("No photosynthesis without sunlight.")

    def absorb_water(self):
        self.has_water = True
        print(f"{self.name} absorbed water from the soil.")

    def describe(self):
        print(f"Fern: {self.name} | Height: {self.height} cm | Age: {self.age} years")

    def fertilize(self):
        self.health = min(100, self.health + 10)
        print(f"{self.name} has been fertilized! Health is now {self.health}.")


def save_plants(plants):
    def plant_to_dict(plant):
        return {
            "type": plant.__class__.__name__,
            "name": plant.name,
            "height": plant.height,
            "age": plant.age,
            "has_sunlight": plant.has_sunlight,
            "has_water": plant.has_water,
            "health": plant.health,
            "times_grown": plant.times_grown
        }
    with open("plants_data.json", "w") as file:
        json.dump([plant_to_dict(plant) for plant in plants], file)


def load_plants():
    try:
        with open("plants_data.json", "r") as file:
            data = json.load(file)
            plants = []
            for plant_data in data:
                plant_type = plant_data.pop("type")
                name = plant_data.pop("name")
                height = plant_data.pop("height")
                age = plant_data.pop("age")
                if plant_type == "Tree":
                    plant = Tree(name, height, age)
                elif plant_type == "Flower":
                    plant = Flower(name, height, age)
                elif plant_type == "Cactus":
                    plant = Cactus(name, height, age)
                elif plant_type == "Fern":
                    plant = Fern(name, height, age)
                else:
                    continue
                plant.has_sunlight = plant_data.get("has_sunlight", False)
                plant.has_water = plant_data.get("has_water", False)
                plant.health = plant_data.get("health", 100)
                plant.times_grown = plant_data.get("times_grown", 0)
                plants.append(plant)
            return plants
    except FileNotFoundError:
        return []


def view_all_plants(plants):
    if plants:
        for i, plant in enumerate(plants, 1):
            print(f"[{i}] ", end="")
            plant.describe()
            print("="*40)
    else:
        print("No plants to display.")


def remove_plant(plants):
    if plants:
        view_all_plants(plants)
        index = int(input("Enter the number of the plant you want to remove: ")) - 1
        if 0 <= index < len(plants):
            print(f"Removing {plants[index].name}...")
            plants.pop(index)
        else:
            print("Invalid choice.")
    else:
        print("No plants to remove.")


def display_menu():
    print("\n" + "="*80)
    print(f"{'‧₊˚❀༉‧₊˚Welcome to the PLANTASY‧₊˚❀༉‧₊˚':^80}")
    print("="*80)
    print("Main Menu:")
    print("[1] Add Plant")
    print("[2] Manage Plants")
    print("[3] View All Plants")
    print("[4] Remove Plant")
    print("[5] Save Plants")
    print("[6] Load Plants")
    print("[7] Exit")


def add_plant_menu():
    print("\nChoose a plant type to add:")
    print("[1] Tree")
    print("[2] Flower")
    print("[3] Cactus")
    print("[4] Fern")
    print("[5] Back to Main Menu")


def plant_actions_menu():
    print("\nWhat would you like to do with your plant?")
    print("[1] Water the plant")
    print("[2] Give sunlight")
    print("[3] Grow")
    print("[4] Photosynthesize")
    print("[5] Describe plant")
    print("[6] Check plant health")
    print("[7] Random weather event")
    print("[8] Fertilize (Fern only)")
    print("[9] Go back to plant selection")
    print("[10] Exit")


def random_weather_event(plant):
    event = random.choice(["sunny", "storm", "drought", "rainy"])
    if event == "sunny":
        plant.provide_sunlight()
        print(f"☀️ A sunny day! {plant.name} is happy with the sunlight!")
    elif event == "storm":
        plant.health -= 20
        print(f"🌩️ A storm has hit! {plant.name}'s health decreased by 20.")
    elif event == "drought":
        plant.has_water = False
        plant.health -= 15
        print(f"🌵 A drought has occurred! {plant.name} is thirsty and its health decreased by 15.")
    elif event == "rainy":
        plant.absorb_water()
        print(f"🌧️ It's raining! {plant.name} has been watered.")

plants = load_plants()
if plants:
    print("🌱 Previously saved plants have been loaded.")
else:
    print("🪴 Starting a new garden.")

while True:
    display_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        while True:
            add_plant_menu()
            plant_type = input("Enter your choice (1-5): ")

            if plant_type == "1":
                print("\nChoose a type of Tree:")
                print("[1] Mango Tree")
                print("[2] Acacia Tree")
                print("[3] Narra Tree")
                print("[4] Other")
                subtype = input("Enter your choice (1-4): ")
                if subtype == "1":
                    name = "Mango Tree"
                elif subtype == "2":
                    name = "Acacia Tree"
                elif subtype == "3":
                    name = "Narra Tree"
                elif subtype == "4":
                    name = input("Enter your custom tree name: ")
                else:
                    name = "Unknown Tree"
                height = int(input("Enter initial height (cm): "))
                age = float(input("Enter initial age (years): "))
                plants.append(Tree(name, height, age))
                print(f"Added {name} to your garden!")
                break

            elif plant_type == "2":
                print("\nChoose a type of Flower:")
                print("[1] Sampaguita")
                print("[2] Roses")
                print("[3] Waling-Waling")
                print("[4] Other")
                subtype = input("Enter your choice (1-4): ")
                if subtype == "1":
                    name = "Sampaguita"
                elif subtype == "2":
                    name = "Roses"
                elif subtype == "3":
                    name = "Waling-Waling"
                elif subtype == "4":
                    name = input("Enter your custom flower name: ")
                else:
                    name = "Unknown Flower"
                height = int(input("Enter initial height (cm): "))
                age = float(input("Enter initial age (years): "))
                plants.append(Flower(name, height, age))
                print(f"Added {name} to your garden!")
                break

            elif plant_type == "3":
                print("\nChoose a type of Cactus:")
                print("[1] Prickly Pear")
                print("[2] Saguaro")
                print("[3] Schlumbergera")
                print("[4] Other")
                subtype = input("Enter your choice (1-4): ")
                if subtype == "1":
                    name = "Prickly Pear"
                elif subtype == "2":
                    name = "Saguaro"
                elif subtype == "3":
                    name = "Schlumbergera"
                elif subtype == "4":
                    name = input("Enter your custom cactus name: ")
                else:
                    name = "Unknown Cactus"
                height = int(input("Enter initial height (cm): "))
                age = float(input("Enter initial age (years): "))
                plants.append(Cactus(name, height, age))
                print(f"Added {name} to your garden!")
                break

            elif plant_type == "4":
                print("\nChoose a type of Fern:")
                print("[1] Ostrich Fern")
                print("[2] Maidenhair Fern")
                print("[3] Makahiya")
                print("[4] Other")
                subtype = input("Enter your choice (1-4): ")
                if subtype == "1":
                    name = "Ostrich Fern"
                elif subtype == "2":
                    name = "Maidenhair Fern"
                elif subtype == "3":
                    name = "Makahiya"
                elif subtype == "4":
                    name = input("Enter your custom fern name: ")
                else:
                    name = "Unknown Fern"
                height = int(input("Enter initial height (cm): "))
                age = float(input("Enter initial age (years): "))
                plants.append(Fern(name, height, age))
                print(f"Added {name} to your garden!")
                break

            elif plant_type == "5":
                break
            else:
                print("Invalid choice. Try again.\n")

    elif choice == "2":
        if not plants:
            print("No plants available to manage. Please add plants first.")
            continue

        view_all_plants(plants)
        plant_index = int(input("Enter the number of the plant you want to manage: ")) - 1
        if 0 <= plant_index < len(plants):
            selected_plant = plants[plant_index]
            while True:
                plant_actions_menu()
                action = input("Enter your choice (1-10): ")
                if action == "1":
                    selected_plant.absorb_water()
                elif action == "2":
                    selected_plant.provide_sunlight()
                elif action == "3":
                    selected_plant.grow()
                elif action == "4":
                    selected_plant.photosynthesize()
                elif action == "5":
                    selected_plant.describe()
                elif action == "6":
                    selected_plant.check_health()
                elif action == "7":
                    random_weather_event(selected_plant)
                elif action == "8":
                    if isinstance(selected_plant, Fern):
                        selected_plant.fertilize()
                    else:
                        print("This action is only available for Ferns.")
                elif action == "9":
                    break
                elif action == "10":
                    save_plants(plants)
                    print("\nPlants saved successfully!")
                    print("Thank you for using the PLANTASY! Goodbye.")
                    exit()
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid plant selection.")

    elif choice == "3":
        view_all_plants(plants)

    elif choice == "4":
        remove_plant(plants)

    elif choice == "5":
        save_plants(plants)
        print("Plants saved successfully!")

    elif choice == "6":
        plants = load_plants()
        print("Plants loaded successfully!")

    elif choice == "7":
        save_plants(plants)
        print("\nPlants saved successfully!")
        print("Thank you for using the PLANTASY! Goodbye.")
        break

    else:
        print("Invalid choice. Try again.\n")