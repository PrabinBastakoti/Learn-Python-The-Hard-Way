 

class Parent(object):

    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")
    
class child(Parent):

    def override(self):
        print("Child override()")

    def implicit(self):
        print("Child implicit()")
    
    def altered(self):
        print("Child, Before Parent altered()")
        super(child,self).altered() # calls altered from parent(Super) class 
        print("Child, After Parent altered()")
    

dad = Parent()

son = child()

dad.implicit() #prints implicit from parent class
son.implicit() #prints implicit from child class

dad.override() #prints override from parent class
son.override() #prints override from child class

dad.altered() #prints altered from parent class
son.altered() #prints altered from child class