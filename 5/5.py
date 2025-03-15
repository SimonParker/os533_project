#simon parker


'''
Problem: Santa is sleeping at the north pole. He can be woken up when all 9 of his reindeer are back from vacation or when at least
3 elves have problems. If santa's woken by the elves he can help 3 before going back to sleep. If he's woken by the deer, he 
prepares his sleigh and then hitches all reindeer to it. The deer all go back on vacation when done flying. If santa wakes and there are 3 elves waiting and all 9 deer, he chooses to help the deer.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
deer = 0
elves = 0
mutex = Semaphore(1)
elf_barrier = Semaphore(1)
santa = Semaphore(0)
sleigh_ready = Semaphore(0)
deer_ready = Semaphore(0)
santa_ready = Semaphore(0)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#deer code

mutex.wait()
deer += 1
if deer == 9:
  santa.signal()
mutex.signal()
sleigh_ready.wait()
get_hitched()
mutex.wait()
deer -= 1
if deer == 0:
  deer_ready.signal()
mutex.signal()
santa_ready.wait()
fly()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#elf code

elf_barrier.wait()
mutex.wait()
elves += 1
if elves == 3:
  santa.signal()
else:
  elf_barrier.signal()
mutex.signal()

santa_ready.wait()
get_help()

mutex.wait()
elves -= 1
if elves == 0:
  elf_barrier.signal()
mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#santa code
while True:
  santa.wait()
  mutex.wait()
  if deer == 9:
    prepare_sleigh()
    sleigh_ready.signal(9)
    deer_ready.wait()
    santa_ready.signal(9)
    fly()
  else:
    santa_ready.signal(3)
    help_elves()
  mutex.signal()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
