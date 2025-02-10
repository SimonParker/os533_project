import threading

n = 10 
count = 0

barrier1 = threading.Semaphore(value = 0)
barrier2 = threading.Semaphore(value = 0)
mutex = threading.Semaphore(value = 1)



def f_safe(i):
  global count
  global n
  print(f"{i}1")
  
  mutex.acquire()
  count += 1
  mutex.release()
  if count == n:
    barrier1.release()
  barrier1.acquire()
  barrier1.release()

  print(f"{i}2")

  mutex.acquire()
  count -= 1
  mutex.release()
  
  if count == 0:
    barrier2.release()
  barrier2.acquire()
  barrier2.release()
  
  print(f"{i}3")

def f_unsafe(i):
  print(f"{i}1")
  print(f"{i}2")
  print(f"{i}3")


def safe(n):
  threads = []
  print("safe:")
  for i in range(n):
    t = threading.Thread(target = f_safe, args = (i,))
    threads.append(t)
  for i in range(n):
    threads[i].start()
  for i in range(n):
    threads[i].join()
    
def unsafe(n):
  threads = []
  print("unsafe:")
  for i in range(n):
    t = threading.Thread(target = f_unsafe, args = (i, ))
    threads.append(t)
  for i in range(n):
    threads[i].start()
  for i in range(n):
    threads[i].join()



safe(n)
print("_______________")
unsafe(n)
