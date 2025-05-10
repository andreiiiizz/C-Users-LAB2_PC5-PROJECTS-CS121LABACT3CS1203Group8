# CS 121 - ADVANCE COMPUTER PROGRAMMING
This is our Labaratory Activity 3 in *CS 121*

**Category Assignment**
Develop a Python program that demonstrates the use of classes and core Object-Oriented Programming (OOP) principles.

**Given Abstract Base Class:**
```‧₊˚❀༉‧₊˚PLANTS‧₊˚❀༉‧₊˚```



# Members
| Name | GitHub Profile |
|------|----------------|
|Aldred|[Laurenzedc](https://github.com/Laurenzedc)|
|Jeily|[]()|
|Marylein|[RyOrquinaza](https://github.com/Orquinaza)|
|Kurt|[andreiiiizz](https://github.com/andreiiiizz)|

# Code Description
A plant management simulation that allows users to create, monitor, and maintain various plant types with features like growth tracking, health status, environmental effects, and data persistence.

Users can choose among **Tree, Flower, Cactus, and Fern** to manage and maintain;
```python
class Tree(Plant):
    """A Tree plant that thrives with both water and sunlight."""

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
    """A Flower that blossoms under proper care."""

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
    """A resilient Cactus that survives in dry, sunny conditions."""

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
    """A Fern that enjoys shaded, moist environments."""

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

    def fertilize(self):
        self.health = min(100, self.health + 10)
        print(f"{self.name} has been fertilized! Health is now {self.health}.")

    def describe(self):
        print(f"Fern: {self.name} | Height: {self.height} cm | Age: {self.age} years")





# Class Diagram
![Diagram](<https://raw.githubusercontent.com/andreiiiizz/C-Users-LAB2_PC5-PROJECTS-CS121LABACT3CS1203Group8/master/Diagram.png>)

# OOP Principles Demonstrated

*Encapsulation*  
The ```Plant``` class encapsulates attributes like ```name```, ```age```, ```height```, and ```health```, along with methods such as ```water()``` and ```get_status()``` to interact safely with the plant’s data.  
Specific plant types like ```Fern```, ```Flower```, and ```AirPlant``` maintain internal state changes (e.g., ```growth``` or ```health```) through these methods, preventing direct access to sensitive attributes.


*Abstraction*  
The ```Plant``` class serves as a base abstraction defining essential behaviors like ```grow()``` or ```wilt()``` that are shared among all plant types.  
Subclasses such as ```Fern```, ```Flower```, and ```AirPlant``` implement ```grow()``` differently, hiding complex internal logic while exposing a simple interface to users.


*Inheritance*  
All plant types inherit from the base ```Plant``` class, reusing core properties and behavior like ```name```, ```health```, and ```status tracking```.  
Specialized behavior (e.g., ```grow()``` in ```AirPlant``` depending on air and water) extends and customizes the inherited methods.


*Polymorphism*  
The ```grow()``` method behaves differently depending on the plant type. A ```Fern``` grows gradually, a ```Flower``` might bloom, and an ```AirPlant``` flourishes in unique conditions—all via the same method call.  
Other parts of the system (like a ```GardenManager``` or ```CareRoutine```) can treat all plant objects the same while letting each respond according to its type.


# Acknowledgement  
This laboratory activity would not have been possible without proper guidance. We sincerely thank *Ms. Fatima Agdon* for her support and assistance throughout the process—we truly hope to learn more from her in the future. We also extend our appreciation to each of our groupmates for the teamwork and effort in helping one another complete this project.
