import time
import threading
import concurrent.futures

start = time.perf_counter()

#creating function to test how thread works
def do_sleep():
   print("I am sleeping for a two second")
   time.sleep(2)
   print("finished sleeping", end = "\n")
#creating threads
t1 = threading.Thread(target = do_sleep)
t2 = threading.Thread(target = do_sleep)
t1.start()
t2.start()
#added join method for each thread to make sure the code after the thread doesn' t run before the threads end
t1.join()
t2.join()

#if we were to run the code without thread, this code would take 20 seconds
# However, it is going to take 2 seconds because of threading
threads = []
for i in range(10):
    t = threading.Thread(target = do_sleep)
    t.start()
    threads.append(t)
    

for thread in threads:
    thread.join



finish = time.perf_counter()
print(finish-start)
