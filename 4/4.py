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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





'''
