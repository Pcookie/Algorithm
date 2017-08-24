class Pet :
    __type = ""
    def __init__(self, type):
        self.__type = type
    def getPetType(self):
        return self.__type
class Dog(Pet):
    def __init__(self, type = "dog"):
        super(Dog, self).__init__(type)
class Cat(Pet):
    def __init__(self, type = "cat"):
        super(Cat, self).__init__(type)

class PetEnterQueue:
    __pet = Pet("")
    __count = 0

    def __init__(self, pet, count):
        self.__count = count
        self.__pet = pet
    def getPet(self):
        return self.__pet
    def getCount(self):
        return self.__count
    def getEnterPetType(self):
        return self.__pet.getPetType()
class DogCatQueue:
    __dogQ = []
    __catQ = []
    __count = 0

    def add(self, pet: Pet):
        self.__count += 1
        if(pet.getPetType() is "dog"):
            self.__dogQ.append(PetEnterQueue(pet, self.__count))
        elif(pet.getPetType() is "cat"):
            self.__catQ.append(PetEnterQueue(pet, self.__count))
        else:
            raise Exception("err, not dog or cat")
    def pollAll(self):
        if(len(self.__dogQ) != 0 and len(self.__catQ) != 0):
            if(self.__dogQ[0].getCount() < self.__catQ[0].getCount()):
                return self.__dogQ.pop(0).getPet()
            else:
                return self.__catQ.pop(0).getPet()
        elif(len(self.__dogQ) != 0):
            # print(DogCatQueue.__dogQ)
            print(self.__catQ)
            return self.__dogQ.pop(0).getPet()
        elif(len(self.__catQ) != 0):
            return self.__catQ.pop(0).getPet()
        else:
            raise Exception("err, queue is empty")
    def pollDog(self):
        if (self.isDogQueueEmpty() == False):
            return self.__dogQ.pop(0).getPet()
        else:
            raise Exception("Dog queue is empty")
    def pollCat(self):
        if(self.idCatQueueEmpty() == False):
            b = self.__catQ[0].getCount()
            return self.__catQ.pop(0).getPet()
        else:
            raise Exception("Cat queue is empty")
    def isEmpty(self):
        return len(self.__dogQ) == 0 and len(self.__catQ) == 0
    def isDogQueueEmpty(self):
        return len(self.__dogQ) == 0
    def idCatQueueEmpty(self):
        return len(self.__catQ) == 0

a = Cat()
b = Dog()
c = Cat()
d = Cat()
queue = DogCatQueue()
queue.add(a)
queue.add(b)
queue.add(c)
queue.add(d)
print(queue.pollAll())
print(queue.pollAll())
print(queue.pollAll())
print(queue.pollAll())
# print(queue.pollCat())
# print(queue.pollCat())
# print(queue.pollCat())
# print(queue.pollCat())
# print(queue.pollDog())
# print(queue.pollDog())