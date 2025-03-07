#simon parker

'''
Readers/Writers problem: Reader and writer threads are accessing a data structure, reading from it or writing to it. Any number
of readers can access a data structure at the same time, but writers must have exclusive access to it.

Constraints: 
  -Any number of readers can access the structure at the same time
  -Writers must have exclusive access to the structure
  -No deadlocks


Solution:

int readers = 0
mutex = Semaphore(1)
clear = Semaphore(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Readers:
mutex.wait()
if readers == 1:
  clear.wait() #there is now at least 1 reader working on the data, stops readers from reading until the writer is done
readers += 1
mutex.signal()

read()

mutex.wait()
readers -= 1
if readers == 0:
  clear.signal() #there are no readers working on the data
mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Writers:
clear.wait() #if the writer grabs this then they know there are no readers. only 1 writer can grab this at a time

write()

clear.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

potential issues:
- what if readers keep on coming, and the new threads grab the mutex before old threads leave? all threads would be trapped.
- what if writers keep on coming, blocking the first read and all subsequent reads? no read threads would finish

in terms of the Lightswitch class in the book, you can't lock and unlock at the same time. So endless locks would block all unlocks




what about starvation? what if readers keep coming, a writer would be stuck forever

adjust the previous solution to address starvation, specifically: when a writer arrives, no new readers may enter


Solution:

room = Lightswitch()
writers = 0
mutex = Semaphore(1)
clear = Semaphore(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Readers:

#second lightswitch? for the writers?
switch.lock(clear)

read()

switch.unlock(clear)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Writers:

mutex.wait()
writers += 1
mutex.signal()

clear.wait() 

write()

clear.signal()

mutex.wait()
writers -= 1
mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
