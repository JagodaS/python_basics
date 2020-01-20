import random
from abc import ABCMeta,abstractmethod

'''
Dowolny, nieegzotyczny jezyk programowania obiektowego (sugerowane: C++, Java, C#, TypeScript). W programie maja wystapic:

    Klasy z polami prywatnymi, akcesorami (setter, getter), konstruktory (domyslny, ogolny=parametrowy).
    Dziedziczenie i zwiazki calosc-czesc (kompozycja i/lub agregacja), prosze zwrocic uwage na aktywowanie konstruktorow klas bazowych oraz obiektow czesciowych.
    Klasa abstrakcyjna (interfejs), polimorfizm.
'''

class Address(object):
    def __init__(self,street,city):
        print "Address constructor"
        self.street = street
        self.city = city
    
    def __str__(self):
        return '\n'.join([self.street, self.city])

class religions():
    Christianity = "Christianity"
    Islam = "Islam"
    Hinduism = "Hinduism"
    Buddhism = "Buddhism"
    Folk = "Folk religions"


class Human(object):
    __metaclass__ = ABCMeta

    def __init__(self, name="", age=0):
        super(Human, self).__init__()
        print "Human constructor"
        # public 
        self.name = name
        self.age = age
        # private
        self.__address = None
        self.__religion = religions.Christianity

    @abstractmethod
    def say_hobby(self):
        raise NotImplementedError

    def make_older(self):
        self.age+=1
        print self.name, "is", self.age, "now."
    
    def get_religion(self):
        return self.__religion

    def set_religion(self, new_religion):
        self.__religion = new_religion

    def get_address(self):
        print self.name, "address is:\n", self.__address 
        return self.__address
    
    def set_address(self, street, city):
        if not isinstance(self.__address, Address):
            self.__address = Address(street, city)
        else:
            self.__address.street = street
            self.__address.city = city

class Girl(Human):
    def __init__(self):
        super(Girl, self).__init__()
        print "Girl constructor"
        self.__lucky_number = 0
        self.set_address("Main Street", "New York")

    def say_hobby(self):
        print "My name is", self.name, "and I like boys"

    def get_lucky_number(self):
        self.__lucky_number = random.randint(0,10)
        print self.name, "lucky number is:", self.__lucky_number
        return self.__lucky_number

class Boy(Human):
    def __init__(self, name, age):
        super(Boy, self).__init__(name=name, age=age)
        print "Boy constructor"
        self.set_address("Bazzinga Street", "Texas")

    def say_hobby(self):
        print "My name is", self.name, "and I like girls"

if __name__ =="__main__":
    Jack = Boy("Jack Harrison", 25)
    print Jack.name
    #print Jack.__religion
    print Jack.get_religion()

    Stephanie = Girl()
    Stephanie.name = "Stephanie"
    Stephanie.age = 18
    Stephanie.set_religion(religions.Folk)

    print Stephanie.name, "is", Stephanie.age, "old"
    Stephanie.get_lucky_number()
    Stephanie.get_address()

    # polimorfism
    people = [Stephanie, Jack]
    for person in people:
        person.make_older()

    for person in people:
        person.say_hobby()


