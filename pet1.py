class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        print(self.name + "goes zzzzzzzzzzzzzz...")

    def play(self):
        print(self.name + "goes Yippee!")
        
    def read(self):
        print(self.name + "says hmmm interesting...")
        
    def sing(self):
        print(self.name + " sings la la la la laaaaaaaa")
        
    def dance(self):
        print(self.name + "says yaaaaasssss")
        
    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Jaz")
pet2 = Pet("Dai")
pet3 = Pet("oof")

