#simon parker

'''
Dining Savages problem: You have a group of savages eating out of a pot. The pot holds M servings, after which a cook must refill the
pot. Create a protocol that enforces that savages cannot take a serving from the pot if it's empty, and the cook can only refill
the pot if it's empty

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
servings = M
mutex = Semaphore(1)
need_food = Semaphore(0)
pot_full = Semaphore(0)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Savages' code

while True:
  mutex.wait()
  if servings == 0
    need_food.signal()
    pot_full.wait()
    servings = M
  servings -= 1
  mutex.signal()
  get_food_from_pot()
  eat()



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cook's code

while True:
  need_food.wait()
  fill_pot()
  pot_full.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
