class comp:
    def __init__(self):
        self.name="Shwe"
        self.age=23

    def update(self):
        self.age=27

    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=comp()
c2=comp()

c1.update()

if c1.compare(c2):
    print("They are same")
else:
    print("they are diff")



print(c1.name)
print(c2.name)
