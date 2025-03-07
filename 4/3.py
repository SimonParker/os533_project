#simon parker

'''
No-Starve Mutex: Find a way for 3 threads to access a mutex without starvation. You can only assume that you have access to weak
semaphores, meaning that if there are threads waiting for a semaphore, then one will awaken when signal() is called. 
- AKA you have to assume the worst case scheduler


Starter:

mutex = Semaphore(1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while true:
  mutex.wait()
  #critical section
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem with above is thread A goes, signals, and then waits at the mutex again. B grabs the mutex, goes, signals, and waits 
at the mutex. A grabs the mutex, goes, signals, etc.. There is no guarentee that C will ever go, it 'starves'.

Fix this, assuming a finite number of threads



Starter:

n = 3 #3 threads
c1 = 0 #count of incoming threads, stop new threads when this reaches the n (all threads are ready to go)
c2 = 0 #count of threads ready to work on the critical section
mutex = Semaphore(1)

gate1 = Semaphore(1) #ready to let people through initially
gate2 = Semaphore(0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while true:
  gate1.wait()
  gate1.signal()

  mutex.wait()
  c1 += 1
  if c1 == n:
    c1 = 0
    gate1.wait() #close the gate
    gate2.signal()
  mutex.signal()

  gate2.wait():
  #critical section
  gate2.signal()

  mutex.wait()
  c2 += 1
  if c2 == n:
    c2 = 0
    gate2.wait() 
    gate1.signal()
  mutex.signa()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, ABC line up and go through gate1 1 at a time, lining up at gate 2 after. The last one through closes gate 1 and opens gate 2.
Now each accesses the critical section 1 at a time, going back and waiting at gate 1. The last through closes gate 2 and opens gate 1,
restarting the process. Notably it is now impossible for a thread to access the critical section again before all others also have. :)


'''
