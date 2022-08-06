myapple = { 'apple': "I AM APPLES!" }
print(myapple['apple'])


import mystuff
mystuff.apple()
print(mystuff.tangerine)


class Mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = Mystuff()
thing.apple()
print(thing.tangerine)

#get things from things

#dict style
print(myapple['apple'])

#modeule style
mystuff.apple()
print(mystuff.tangerine)

#class style

thing = Mystuff()
thing.apple()
print(thing.tangerine)