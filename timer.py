import time

class Timer:
    def __init__(self,timeout):
        self.timeout = timeout
        self.start_time = None

    def start(self):
        self.start_time = time.time()
    
    def elapsed_time(self):
        if self.start_time:
            return time.time() - self.start_time
        else:
            return 0
        
    def is_timeout(self):
        if self.elapsed_time() >= self.timeout:
            return True
        else:
            return False
t1 = time.time()
timer = Timer(10)
timer.start()
while not timer.is_timeout():
    t2 = time.time()
    print(t2-t1)
    time.sleep(0.5)

        