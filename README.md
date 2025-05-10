# CS 121 Laboratory 3
# CS 121 - ADVANCE COMPUTER PROGRAMMING
This is our Labaratory Activity 3 in *CS 121*

*Category Assignment*
Develop a Python program that demonstrates the use of classes and core Object-Oriented Programming (OOP) principles.

*Given Abstract Base Class:* 
‧₊˚❀༉‧₊˚PLANTS‧₊˚❀༉‧₊˚```



# Members
| Name | GitHub Profile |
|------|----------------|
|Aldred|[Laurenzedc](https://github.com/Laurenzedc)|
|Jeily|[]()|
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




