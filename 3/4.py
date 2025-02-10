import threading


mutex = threading.Semaphore(value = 1)
count = 0

def inc_safe():
  global count
  mutex.acquire()
  count += 1
  print(f"count = {count}")
  mutex.release()

def inc_unsafe():
  global count
  count += 1
  print(f"count = {count}")

def safe():
  global count
  count = 0
  print("safe:")
  for i in range(10):
    a = threading.Thread(target = inc_safe)
    b = threading.Thread(target = inc_safe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()

  
def unsafe():
  global count
  count = 0
  print("unsafe:")
  for i in range(10):
    a = threading.Thread(target = inc_unsafe)
    b = threading.Thread(target = inc_unsafe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()

t1 = threading.Thread(target = safe)
t2 = threading.Thread(target = unsafe)
t1.start()
t1.join()
print("____________________")
t2.start()
t2.join()
