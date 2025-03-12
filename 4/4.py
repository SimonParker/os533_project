#simon parker

'''
Dining Philosophers: You have 5 diners sitting at a table, with 5 forks between them. There is a bowl of pasta in the center of the table, and each diner needs 2 forks to eat the pasta. They want to do the following loop:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while true:
  think()
  get_forks()
  eat()
  drop_forks()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


We can assume left(i) and right(i) return the left and right fork for a given diner's index

Constraints:
  -Only 1 diner can hold a fork at once
  -No deadlocks
  -No starvation
  -Maximize the number of diners eating at the same time

create get_forks() and drop_forks() that satisfies the above


Starter: represent each fork as a mutex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
get_forks(i):
  right(i).wait()
  left(i).wait()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
drop_forks(i)
  right(i).signal()
  left(i).signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



The above solution fails because, if every diner reached for their right fork at the same time, all the forks would be grabbed.
They would all wait for their left fork to be dropped, but no forks will ever be dropped. This is a deadlock


Fix the deadlock:

We deadlock here because each person grabs for the right fork and then the left. What happens if some go the other way around?


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

get_forks(i):
  if i%2 == 0: #left handed
    left(i).wait()
    right(i).wait()
  else: #right handed
    right(i).wait()
    left(i).wait()

drop_forks(i): #order doesn't matter when releasing
  right(i).signal()
  left(i).signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's imagine the same scenario as before, each philosopher trying to get_forks() simultaneously. Where before each one would grab
the one on their left and wait for the one on their right, now even ones grab the left and odd the right. This gives us some 
contention:
  - 0 and 1 try to grab fork 1
    - one of them will grab it
  - 2 and 3 try to grab fork 3
    - one grabs it
  - 4 grabs fork 0

At this point we are still able to proceed.
  - It's possible for multiple philosophers to eat. Assuming 0 grabs f.1, 2 grabs f.3.
    - then philosopher 4 will grab fork 4 and eat and philosopher 2 will grab fork 2 and eat
  - I don't believe there's any deadlock here, as when philosophers are fighting over a fork, there will be a winner
  - What about starvation?
    - i don't think it can happen here. because the philosophers are fighting over forks, the instant one puts one down, the other
    will grab it. There is no opportunity for the philosopher to pick the fork back up before the other grabs it. FIFO ?
    - there is only ever 1 thread waiting for any given fork, so it will get that fork when it is put down.


'''
