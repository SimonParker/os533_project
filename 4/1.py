#simon parker

'''
Producer-Consumer problem: producer threads wait for events and then add objects to a buffer, while consumer threads take items
from the buffer and process them.

Constraints:
  -Threads must have exclusive access to the buffer
  -Consumers should block until there is an event in the event buffer

Starter code:

~~~~~~~~~~~~~~~~~~~~~~~
PRODUCER:
  event = waitForEvent()
  buffer.add(event)

~~~~~~~~~~~~~~~~~~~~~~~
CONSUMER:
  event = buffer.get()
  event.process()

~~~~~~~~~~~~~~~~~~~~~~~





Updated to enforce constraints:

mutex = Semaphore(1)
not_empty = Semaphore(0)

~~~~~~~~~~~~~~~~~~~~~~~
PRODUCER:
  event = waitForEvent()
  mutex.wait()
  buffer.add(event)
  not_empty.signal()
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~
CONSUMER:
  not_empty.wait()
  mutex.wait()
  event = buffer.get()
  mutex.signal()
  event.process()

~~~~~~~~~~~~~~~~~~~~~~~






Updated to enforce finite buffer constraint: a producer must block if the buffer is full

buffer_slots = Semaphore(n) #n is the size of the buffer
mutex = Semaphore(1)
not_empty = Semaphore(0)

~~~~~~~~~~~~~~~~~~~~~~~
PRODUCER:
  event = waitForEvent()
  buffer_slots.wait() #reserve a slot
  mutex.wait()
  buffer.add(event)
  not_empty.signal()
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~
CONSUMER:
  not_empty.wait()
  mutex.wait()
  event = buffer.get()
  mutex.signal()
  buffer_slots.signal()
  event.process()

~~~~~~~~~~~~~~~~~~~~~~~
'''
