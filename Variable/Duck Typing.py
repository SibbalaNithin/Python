class Bird:
    def fly(self):
        print("Bird is flying")
class Airplane:
    def fly(self):
        print("Airplane is flying")
def let_it_fly(flying_object):
    flying_object.fly()
bird = Bird()
airplane = Airplane()
let_it_fly(bird)
let_it_fly(airplane)