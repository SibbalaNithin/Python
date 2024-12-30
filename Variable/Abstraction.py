from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return"BARK"
    def move(self):
        return"Run"
class Bird(Animal):
    def make_sound(self):
        return"Chirp"
    def move(self):
        return"fly"
dog = Dog()
dog.make_sound()
dog.move()
print(dog.make_sound())
print(dog.move())

bird = Bird()
bird.make_sound()
bird.move()
print(bird.make_sound())
print(bird.move())

