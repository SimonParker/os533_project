'''
not quite sure about this one. this matches the solution given in the book, as far as i can tell. 
i'm expecting this to print out leader and follower pairs, in either order. leader follower or follower leader. im not getting that :(
think on this
'''
import threading

n = 10

leader_queue = threading.Semaphore(value = 0)
follower_queue = threading.Semaphore(value = 0)


def leader_safe():
  follower_queue.release()
  leader_queue.acquire()
  print(f"leader going")

def follower_safe():
  leader_queue.release()
  follower_queue.acquire()
  print(f"follower going")

def leader_unsafe():
  print(f"leader going")

def follower_unsafe():
  print(f"follower going")

def safe(n):
  leaders = []
  followers = []
  print("safe:")
  for i in range(n):
    t1 = threading.Thread(target = leader_safe)
    leaders.append(t1)
    t2 = threading.Thread(target = follower_safe)
    followers.append(t2)
  for i in range(n):
    leaders[i].start()
    followers[i].start()
  for i in range(n):
    leaders[i].join()
    followers[i].join()
  
def unsafe(n):
  leaders = []
  followers = []
  print("unsafe:")
  for i in range(n):
    t1 = threading.Thread(target = leader_unsafe)
    leaders.append(t1)
    t2 = threading.Thread(target = follower_unsafe)
    followers.append(t2)
  for i in range(n):
    leaders[i].start()
    followers[i].start()
  for i in range(n):
    leaders[i].join()
    followers[i].join()
  

safe(n)
print("______________________")
unsafe(n)
