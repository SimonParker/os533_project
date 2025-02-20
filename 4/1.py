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

buffer = Semaphore(1)
lock = Semaphore(0)

~~~~~~~~~~~~~~~~~~~~~~~
PRODUCER:
  event = waitForEvent()
  buffer.wait()
  buffer.add(event)
  lock.signal()
  buffer.signal()

~~~~~~~~~~~~~~~~~~~~~~~
CONSUMER:
  lock.wait()
  buffer.wait()
  event = buffer.get()
  buffer.signal()
  event.process()

~~~~~~~~~~~~~~~~~~~~~~~






Updated to enforce finite buffer constraint: a producer must block if the buffer is full

buffer_slots = Semaphore(n) #n is the size of the buffer
buffer = Semaphore(1)
lock = Semaphore(0)

~~~~~~~~~~~~~~~~~~~~~~~
PRODUCER:
  event = waitForEvent()
  buffer_slots.wait()
  buffer.wait()
  buffer.add(event)
  lock.signal()
  buffer.signal()

~~~~~~~~~~~~~~~~~~~~~~~
CONSUMER:
  lock.wait()
  buffer.wait()
  event = buffer.get()
  buffer.signal()
  buffer_slots.signal()
  event.process()

~~~~~~~~~~~~~~~~~~~~~~~
'''
