# CS 121 - ADVANCE COMPUTER PROGRAMMING
This is our Labaratory Activity 3 in *CS 121*

*Category Assignment*
Develop a Python program that demonstrates the use of classes and core Object-Oriented Programming (OOP) principles.

*Given Abstract Base Class:* 
‧₊˚❀༉‧₊˚PLANTS‧₊˚❀༉‧₊˚```



# Members
| Name | GitHub Profile |
|------|----------------|
|Aldred|[Aldred De Castro Laurenzedc](https://github.com/Laurenzedc)|
|Jeily|[jeilyannnmerhan](https://github.com/jeilyannnmerhan)|
|Marylein|[RyOrquinaza](https://github.com/Orquinaza)|
|Kurt|[andreiiiizz](https://github.com/andreiiiizz)|

# Code Description
A plant management simulation that allows users to create, monitor, and maintain various plant types with features like growth tracking, health status, environmental effects, and data persistence.

Users can choose among Tree, Flower, Cactus, and Fern to manage and maintain:
```python
class Tree(Plant):
    def grow(self):
        if self.has_water and self.has_sunlight:
            self.height += 10
            self.age += 1
            self.health = min(100, self.health + 5)
            print(f"The tree {self.name} grew taller! Now it's {self.height} cm tall.")
        else:
            self.health -= 10
            print(f"The tree {self.name} needs both water and sunlight to grow.")


perhaps through *Cactus*, which thrives even in tough conditions:
class Cactus(Plant):
    def grow(self):
        if self.has_sunlight:
            self.height += 5
            self.age += 1
            self.health = min(100, self.health + 3)
            print(f"The cactus {self.name} grew slightly. Height: {self.height} cm.")
        else:
            self.health -= 5
            print(f"The cactus {self.name} needs sunlight to grow.")





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
