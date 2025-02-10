import threading

t1_done = threading.Semaphore(value=0)

def t1_safe():
  print("t1 does stuff")
  t1_done.release()


def t2_safe():
  t1_done.acquire()
  print("then t2 does stuff")

def t1_unsafe():
  print("t1 does stuff")


def t2_unsafe():
  print("then t2 does stuff")


def safe():
  print("these should be in order:")
  print()
  for i in range(10):
    a = threading.Thread(target=t1_safe)
    b = threading.Thread(target=t2_safe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()


def unsafe():
  print("these might not be in order:")
  print()
  for i in range(10):
    a = threading.Thread(target=t1_unsafe)
    b = threading.Thread(target=t2_unsafe)
    a.start()
    b.start()
    a.join()
    b.join()
    print()


safe()
unsafe()
