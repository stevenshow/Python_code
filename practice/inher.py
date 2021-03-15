class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def whoAmI(self):
        print('I am ' + self.name + ' and I am ' + str(self.age) + ' years old!')

class Gamer(Person):
    def __init__(self, name, age, system, numGames):
        super().__init__(name, age)
        self.system = system
        self.numGames = numGames
    
    def printGames(self):
        print('My name is ' + self.name + ' and I own ' + str(self.numGames) + ' games!  Oh, and I play on the ' + self.system + '.')

def main():
    p1 = Person('Bob', 20)
    g1 = Gamer('Steven', 24, 'PC', 30)
    g1.printGames()
    p1.whoAmI()
    print(g1.age)

if __name__ == '__main__':
    main()