import rlcompleter
from unicodedata import name


class student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll 
        self.lap=self.laptop


    def show(self):
        print(self.name,self.roll)


    class laptop:
        def __init__(self) -> None:
            self.brand="HP"
            self.procs="i5"
            self.ram="16"



s1=student('Shwetank',1)
s2=student('Mishra',3)

s1.show()
s2.show()
s1.lap.brand()