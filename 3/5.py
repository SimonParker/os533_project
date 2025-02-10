import threading

multiplex = threading.Semaphore(value = 5) #set the value here to be whatever upper limit you want in the critical zone


