import threading
lock = threading.Lock()
current_thread = ''
class Car(threading.Thread):
    def __init__(self, max_speed, thread_id, door=4,wheel=5, seat=4):
        threading.Thread.__init__(self)
        self.door = door
        self.wheel = wheel
        self.seat = seat
        self.max_speed = max_speed
        self.thread_id = thread_id

    def run(self):
        global current_thread
        loop = 0
        while loop < 1000:
            lock.acquire()
            if current_thread != self.thread_id:
                print(self.max_speed)
                current_thread = self.thread_id
                loop +=1
            lock.release()

    def info(self):
        print('wheel = ' + str(self.wheel))
        print('door = ' + str(self.seat))
        print('seat = ' + str(self.seat))
        return True
toyota = Car(100,'thread-1')
bmw = Car(200,'thread-2')
toyota.start()
bmw.start()

