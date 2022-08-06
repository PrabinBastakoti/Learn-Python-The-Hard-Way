
class Other(object):

    def override(self):
        print("Other Override()")
    
    def implicit(self):
        print("Other implicit()")
    
    def altered(self):
        print("Other altered()")

class child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        print("Child implicit()")

    def override(self):
        print("Child Override()")
    
    def altered(self):
        print("Child, before Other altered()")
        self.other.altered() # takes altered() function from Other class since we initiate self.other as Other()
        print("Child, after Other altered()")

son = child()

son.implicit()
son.override()
son.altered()


    