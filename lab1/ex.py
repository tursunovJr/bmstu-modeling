class Parent(object):
    def __init__(self, param):
        self.v1 = param

class Child(Parent):
    def __init__(self, param):
        self.v2 = param

obj = Child(11)
print("%d %d" % (obj.v1, obj.v2))