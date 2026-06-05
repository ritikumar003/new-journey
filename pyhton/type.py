class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed


        pass
    def bark(self):
        print("woof woof")


dog1 = dog("hell","street")
dog1.bark()
print(dog1.name)
print(dog1.breed)



dog2 = dog("nah","pug")
dog2.bark()
print(dog2.name)
print(dog2.breed)