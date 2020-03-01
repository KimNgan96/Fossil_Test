import threading

lock = threading.Lock()
class Car(threading.Thread):
    def __init__(self, max_speed, door=4,wheel=5, seat=4):
        threading.Thread.__init__(self)
        self.door = door
        self.wheel = wheel
        self.seat = seat
        self.max_speed = max_speed

    def run(self):
        lock.acquire()
        for i in range(0, 10):
            print(self.max_speed)
        lock.release()

    def info(self):
        print('wheel = ' + str(self.wheel))
        print('door = ' + str(self.seat))
        print('seat = ' + str(self.seat))
        return True

toyota = Car(100)
toyota.start()
bmw = Car(200)
bmw.start()

