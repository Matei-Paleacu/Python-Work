# Midterm 2
# Question 1


class Pet:
    name = None   # name of pet (str)
    age = None    # age of pet in years (int)
    kind = None   # kind of pet (str)   
    def __repr__(self):
        return f'<{self.name}|age={self.age}|kind={self.kind}>'



def createListOfPets(n):
    # returns a list of n Pets (each with diferent ages)
    pets = [None]*n
    for i in range(n):
        pets[i] = Pet()
        pets[i].name = f'pet{i}'
        pets[i].age = i+2
        pets[i].kind = str(i%3)
        if i%3 == 0:
            pets[i].kind = "dog"
        if i%3 == 1:
            pets[i].kind = "cat"
        if i%3 == 2:
            pets[i].kind = "fish"
    return pets
    
pets = createListOfPets(9)
print(pets)

def oldestPet(petList,petKind):
    oldest_pet = 0
    pet_age = 0
    oldest_pet_name = "empty string"
    for pet in petList:                 #goes throught every pet
        if pet.kind == petKind:
            pet_age = pet.age
        if pet_age > oldest_pet:        #only stores age if it is the highest
            oldest_pet = pet_age
            oldest_pet_name = pet.name
    return oldest_pet_name              # once programe is over returns the pet name that was associated with the highest age

print(oldestPet(pets,"tt"))
