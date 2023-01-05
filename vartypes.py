class dog:

    legs=4

    def __init__(self):
        self.breed = 'German'
        self.age = 10
    

a=dog()
dog.legs=5
a.breed="Indian"

print(a.breed,a.age, dog.legs)
