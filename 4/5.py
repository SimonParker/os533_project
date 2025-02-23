#simon parker

'''
Cigarette Smoker's problem: You've got an agent and 3 smokers. Each smoker waits around until it has the 3 ingredients to smoke, then
it crafts a cigarette and smokes it. The ingredient are tobacco, paper, and matches. Each smoker has 1 of the three ingredients, a
different one per smoker. The agent has all 3 ingredients, and randomly grabs 2 of them and offers them to the smokers. The smoker that
has the complementary ingredient to the agent's 2 should grab the ingredients and smoke.

Let the agent be made up of 3 versions, with a mutex that controls which is active

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mutex = semaphore(1)
paper = semaphore(0)
matches = semaphore(0)
tobacco = semaphore(0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Agent A:

mutex.wait()
paper.signal()
matches.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Agent B:

mutex.wait()
matches.signal()
tobacco.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Agent C:

mutex.wait()
tobacco.signal()
paper.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Come up with code for the 3 smokers that doesn't deadlock



'''
