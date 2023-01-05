class A:
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')
    

    def __init__(self) -> None:
        print('Init A method check')

class B(A):
    def __init__(self) -> None:
        print("B method check")
        super().__init__()

    def feature3(self):
        print('Feature 3 is working')
    
    def feature4(self):
        print('Feature 4 is working')

a1=A()
b1=B()

