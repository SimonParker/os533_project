#simon parker

'''
Problem: further evolving the barbershop we've been working on before. Now:
  - 3 barbers, 3 chairs
  - the waiting room has a couch that holds 4 and room for others standing
  - fire codes limit the number of customers in the shop to 20 (chairs + couch + standing)
  - customers don't enter if the building is full
  - when a barber is free, they serve the customer on the couch that has been waiting the longest (FIFO)
  - if there is space on the couch, the customer that's been standing the longest sits down
  - when the haircut is done, a barber must take payment from the customer. there is 1 cash register, so payment must be done
    one at a time


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
max_customers = 20
customer_count = 0
couch_queue = []
standing_queue = []
customer_standing = Semaphore(0)
couch = Semaphore(4)
customer_sitting = Semaphore(0)
chair = Semaphore(3)
customer_ready = Semaphore(0)
barber_ready = Semaphore(0)
pay = Semaphore(0)
accepted = Semaphore(0)
register = Semaphore(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#couch aid
while True:
  customer_standing.wait()
  couch.wait()
  mutex.wait()
  standing_queue[0].signal()
  couch_queue.append(standing_queue.pop(0))
  mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#chair aid
while True:
  customer_sitting.wait()
  chair.wait()
  mutex.wait()
  couch_queue[0].signal()
  couch_queue.pop(0)
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#customer code
ticket = Semaphore(0)
mutex.wait()
if customer_count == max_customers:
  mutex.signal()
  leave()
else:
  customer_count += 1
  standing_queue.append(ticket)
  mutex.signal()
  customer_standing.signal()
  ticket.wait()
  customer_sitting.signal()
  ticket.wait()
  couch.signal()
  customer_ready.signal()
  barber_ready.wait()
  haircut()
  chair.signal()
  pay.signal()
  accepted.wait()
  mutex.wait()
  customer_count -= 1
  mutex.signal()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#barber code

while True:
  barber_ready.signal()
  customer_ready.wait()
  haircut()
  register.wait()
  pay.wait()
  accepted.signal()
  register.signal()






~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
