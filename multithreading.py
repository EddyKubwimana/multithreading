import time
import threading

start = time.perf_counter()

def do_sleep():
   print("I am sleeping for a two second")
   time.sleep(2)
   print("finished sleeping", end = "\n")

t1 = threading.Thread(target = do_sleep)
t2 = threading.Thread(target = do_sleep)
t1.start()
t2.start()
t1.join()
t2.join()


finish = time.perf_counter()
print(finish-start)
