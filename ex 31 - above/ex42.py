## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):

    def __init__(self,name):
        ## A Dog has-a name
        self.name = name

## A cat is-an animal
class Cat(Animal):
    def __init__(self,name):
        ## A cat has-a name
        self.name = name


## A person is-an object
class Person(object):
    def __init__(self,name):
        ## A person has-a name
        self.name= name

        ##Person has-a pet of some kind
        self.pet = None
    
## A Employee is-an Person

class Employee(Person):
    def __init__(self,name, salary):
        ## An employee has-a name. hmm what is this strange music?
        super(Employee,self).__init__(name)
        ## A employee has-a salary
        self.salary = salary

## fish is-an object
class Fish(object):
    pass

## salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a dog 
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank(employee) has-a name and salary
frank = Employee("Frank" , 120000)

## frank has-a pet named rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


