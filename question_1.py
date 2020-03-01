class Car():
    def __init__(self,max_speed, door = 4,wheel = 5, seat = 4):
        self.door = door
        self.wheel = wheel
        self.seat = seat
        self.max_speed = max_speed

    def run(self):
        for i in range (0,10):
            print(self.max_speed)
        return True

    def info(self):
        print('wheel = ' + str(self.wheel))
        print('door = ' + str(self.seat))
        print('seat = ' + str(self.seat))
        return True

class Toyota(Car):
    def __init__(self,max_speed = 100):
        Car.__init__(self,max_speed)

class BMW(Car):
    def __init__(self,max_speed = 200):
        Car.__init__(self,max_speed)

toyota = Toyota()
toyota.run()
bmw = BMW()
bmw.run()




