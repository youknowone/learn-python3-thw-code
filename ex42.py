## Animal 은 object의 일종(is-a)이다 (네, 조금 헷갈리죠) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person은 어떤 종류의 pet을 갖고(has-a) 있다
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? 음 이 마법은 뭐죠?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

##??
class Halibut(Fish):
    pass


## rover 는 Dog 의 일종(is-a) 이다
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()