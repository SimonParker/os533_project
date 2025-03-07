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
  - fixed by First in, First out scheduling of threads
- what if writers keep on coming, blocking the first read and all subsequent reads? no read threads would finish
  - fixed by First in, First out scheduling of threads

in terms of the Lightswitch class in the book, you can't lock and unlock at the same time. So endless locks would block all unlocks




what about starvation? what if readers keep coming, a writer would be stuck forever

adjust the previous solution to address starvation, specifically: when a writer arrives, no new readers may enter


Solution:

room = Lightswitch()
gate = Semaphore(1)
clear = Semaphore(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Readers:

gate.wait() #turnstile barrier
gate.signal()

room.lock(clear)

read()

room.unlock(clear)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Writers:

gate.wait() #this will eventually run b/c there are a finite # of readers waiting at the gate before the writer, FIFO scheduling :)
clear.wait() 

write()

clear.signal()
gate.signal() #this oks another writer to go, or the reader queue to start going



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Writer priority version: when a writer arrives, no readers enter until all writers have left

- now we have 2 requirements
  - when a writer arrives, no readers enter until all writers have left
  - when a reader arrives, no writers enter until all readers have left
- 2 lightswitches?

Solution:

r = Lightswitch()
w = Lightswitch()
no_readers = Semaphore(1) #indicating there are no readers
no_writers = Semaphore(1) #indicating there are no writers

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Readers:


no_writers.wait() #waits for the last writer to leave
r.lock(no_readers) #indicates at least 1 reader, queueing writers
no_writers.signal() #allows writers to queue future readers

read()

r.unlock(no_readers) #last reader out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Writers:

w.lock(no_writers) #indicates theres at least 1 writer, queueing readers
no_readers.wait() #waits for there to be no readers

write()

no_readers.signal() #if there is another writer, it will grab this with priority over waiting readers, which can't lock until 
                    #writer leaves
                    
w.unlock(no_writers) #last writer out


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Note that this solution gives writers priority, but now can starve a reader.
'''
