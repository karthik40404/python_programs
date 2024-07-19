from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(s):
        print('sound')
class bird (animal):
    def fly (self):
        print('fly')
    def make_sound(s):
        print('bird sound')
class cat (animal):
    def run(self):
        print('run')
    def make_sound(s):
        print('cat sound')

b1=bird()
b1.fly()
b1.make_sound()

print('cat')
c=cat()
c.run()