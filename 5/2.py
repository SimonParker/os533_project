#simon parker


'''
Barbershop problem: You have a barber thread and a bunch of customer threads. There is 1 chair in the barbershop, and a waiting
room that can hold N customers. If there are no waiting customers the barber should go to sleep. When a customer enters the shop,
if the waiting room is full they should just leave, otherwise they should get in the waiting room. If the chair is empty, a 
customer in the waiting room whould fill it and get their hair cut.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
waiting_room = N
mutex = Semaphore(1)
customer_ready = Semaphore(0)
chair_empty = Semaphore(1)
haircut_over = Semaphore(0)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#customer code
mutex.wait()
if waiting_room == 0:
  mutex.signal()
  leave()
else:
  waiting_room -= 1
  mutex.signal()
  chair_empty.wait()
  mutex.wait()
  waiting_room += 1
  mutex.signal()
  customer_ready.signal()
  haircut()
  haircut_over.wait()
  chair_empty.signal()




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#barber code

while True:
  customer_ready.wait()
  haircut()
  haircut_over.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
