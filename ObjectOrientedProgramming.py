
class Animal(object):
    name = 'Undefined'
    noise = 'Undefined'
    species = 'Undefined'
    color = 'Undefined'
    origin = 'Unknown'

    def whatColor(self):
        print(self.color)

    def whatName(self):
        print(self.name)

    def makeOld(self):
        self.color = "white"
        print("{} is OLD! and has {} hair".format(self.name,self.color))

    def takeOnAWalk(self):
        print("Going on a walk!\n")
        for _ in range(1,5):
            print("{} says {}".format(self.name, self.noise))
        print("\n")

    def pet(self):
        print("Petting good {}".format(self.species))
        print("{} says {}".format(self.name, self.noise))
        print("\n")

    def printAttributes(self):
        print(self.color)
        print(self.species)
        print(self.name)
        print(self.noise)
        print(self.origin)
        print("\n")


class Dog(Animal):
    species = 'Dog'
    noise = '*Bark*'

    def __init__(self, NewName, MyColor):
        self.name = NewName
        self.color = MyColor

class Cat(Animal):
    species = "Cat"
    noise = "*meow*"

    def __init__(self, NewName, MyColor):
        self.name = NewName
        self.color = MyColor

    def takeOnAWalk(self):
        print("Cats don't go on a walk, silly!")


def adopt(type, NewName, MyColor):
    newAnimal = None
    if type == "dog":
        newAnimal = Dog(NewName,MyColor)
    elif type == "cat":
        newAnimal = Cat(NewName, MyColor)
    else:
        print("No animals available")

    return newAnimal


kiwi = Dog("kiwi","spotted")
lido = Dog("lido","brown")
print(lido.name)
print(lido.color)
print(lido.species)
lido.name = "Joe"
print(lido.name)


panion = adopt("dog", "panion", "black")

kiwi.takeOnAWalk()
lido.pet()
print(panion.color)
panion.makeOld()
print(panion.color)


kiwi.printAttributes()

george = adopt("cat", "george", "albino")
george.takeOnAWalk()
george.printAttributes()
george.pet()
