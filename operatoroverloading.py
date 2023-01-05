from asyncore import compact_traceback


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2


    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)

        return s3


    def __mul__(self,other):
        m1= self.m1*other.m1
        m2= self.m2*other.m2
        s4=student(m1,m2)
        return s4
    
    def __gt__(self,other):
        a=self.m1+self.m2
        b=other.m1+other.m2
        if a>b:
            return True
        else:
            return False

    def __str__(self) -> str:
        return '{} {}'.format(self.m1,self.m2)
        #retunr self.m1, self.m2


s1=student(15,14)
s2=student(13,18)


#print(s2.__str__())
print(s2)


s3=s1+s2  # student.__add__(s1,s2) // operator overloading
s4=s1*s2
print(s3.m1) 
print(s4.m1) 




if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")