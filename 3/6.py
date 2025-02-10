import threading

n = 8
count = 0

barrier = threading.Semaphore(value = 0)
mutex = threading.Semaphore(value = 1)



def f_safe(i):
  global count
  global n
  mutex.acquire()
  count += 1
  mutex.release()
  print(f"{i}1")
  
  if count == n:
    barrier.release()
  barrier.acquire()
  barrier.release()

  print(f"{i}2")
  

def f_unsafe(i):
  print(f"{i}1")
  print(f"{i}2")


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
