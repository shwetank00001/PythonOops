class A:
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')
    

class B(A):
    def feature3(self):
        print('Feature 3 is working')
    
    def feature4(self):
        print('Feature 4 is working')


class C(B):
    def feature5(self):
        print('Feature 5 is working')


s1=A()
b1=B()
c1=C()

s1.feature1()
b1.feature3()
b1.feature1()

c1.feature1()
c1.feature5()
