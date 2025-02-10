import threading

a1_done = threading.Semaphore(value = 0)
b1_done = threading.Semaphore(value = 0)


def a_safe():
  print("a1")
  a1_done.release()
  b1_done.acquire()
  print("a2")

def a_unsafe():
  print("a1")
  print("a2")

def b_safe():
  print("b1")
  b1_done.release()
  a1_done.acquire()
  print("b2")

def b_unsafe():
  print("b1")
  print("b2")


def safe():
  print("safe:")
  for i in range(10):
    a = threading.Thread(target = a_safe)
    b = threading.Thread(target = b_safe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()

def unsafe():
  print("unsafe:")
  for i in range(10):
    a = threading.Thread(target = a_unsafe)
    b = threading.Thread(target = b_unsafe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()



safe()
print("_____________________")
unsafe()
  
