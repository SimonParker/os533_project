#simon parker

'''
Problem: Exactly the same as the barber shop problem in 5.2, but this time customers must be served in a FIFO scheme.

idea: use a list of semaphores, like a queue. the first customer in line gets the chair, and then each person in line behind them
moves up. When a new customer comes they go to the back on the line (if there are k customers then the k + 1th spot in line
is the last one). Shuffling and updating must all be done in the mutex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
queue = []
waiting_count = 0

mutex = Semaphore(1)
store_not_empty = Semaphore(0)
customer_ready = Semaphore(0)
haircut_done = Semaphore(0)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#customer code
ticket = Semaphore(0) #each thread has their own semaphore

mutex.wait()
if waiting_count == n:
  mutex.signal()
  leave()
else:
  queue.append(ticket)
  waiting_count += 1
  mutex.signal()
  store_not_empty.signal()
  ticket.wait()
  mutex.wait()
  waiting_count -= 1
  queue.pop(0)
  mutex.signal()
  customer_ready.signal()
  haircut()
  haircut_done.wait()
  


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#barber code
while True:
  store_not_empty.wait()
  queue[0].signal()
  customer_ready.wait()
  haircut()
  haircut_done.signal()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
