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

idea: each version of the agent has a semaphore indicating which ingredient it's missing. each smoker waits on that semaphore
before grabbing the ingredients from the agent
  - problem: this would require changing the agent's code, which i cannot do

the issue here is that the smoker threads are trying to grab the same ingredients. We need to make it so that only 1 of them
reaches for the ingredients at any given time. This means we need them to all be blocking and get signalled one at a time.
We can't change the agent's code to let it signal which smoker should unblock, and it can't be the smokers b/c they are all blocked.
Therefore we need a different thread to wake the smokers. This should wake when it sees the ingredient being put down, and signal
the appropriate smoker depending on what the ingredient is and what else was given
  - keep track of the 2 ingredients provided by agent?
  - tobacco aid waits on tobacco. it can't wait on paper and matches both, so it needs to, without semaphores, know if paper or 
    matches are placed, and then signal the appropriate smoker. 
  - aid sees the first ingredient, marks it as active. if another ingredient is marked active by another aid, signal the smoker
    and reset the active statuses. if no other ingredient is active then one of the other aids will signal the smoker when the 
    second ingredient becomes active.

~~~~~~~~~~~
has_paper = has_matches = has_tobacco = 0
mutex = semaphore(1)
need_paper = semaphore(0)
need_matches = semaphore(0)
need_tobacco = semaphore(0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tobacco Aid:
  tobacco.wait()
  mutex.wait()
  has_tobacco = 1
  if has_paper == 1:
    need_matches.signal()
    has_paper = 0
    has_tobacco = 0
  else if has_matches == 1:
    need_paper.signal()
    has_matches = 0
    has_tobacco = 0
  mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Matches Aid:
  matches.wait()
  mutex.wait()
  has_matches = 1
  if has_paper == 1:
    need_tobacco.signal()
    has_paper = 0
    has_matches = 0
  else if has_tobacco == 1:
    need_paper.signal()
    has_matches = 0
    has_tobacco = 0
  mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Paper Aid:
  paper.wait()
  mutex.wait()
  has_paper = 1
  if has_matches == 1:
    need_tobacco.signal()
    has_paper = 0
    has_matches = 0
  else if has_tobacco == 1:
    need_matches.signal()
    has_paper = 0
    has_tobacco = 0
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tobacco Smoker:

need_tobacco.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Matches Smoker:

need_matches.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Paper Smoker:

need_paper.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Generalized version: write this where the agent doesn't wait for the smoker to finish before putting more ingredients on the table


Now the aids need to keep track of how many of each ingredient is on the table. Instead of just saying there is 0 or 1 of each,
keep track of the exact number. If there is at least 1 of each, send the appropriate smoker


~~~~~~~~~~~
paper_count = matches_count = tobacco_count = 0
mutex = semaphore(1)
need_paper = semaphore(0)
need_matches = semaphore(0)
need_tobacco = semaphore(0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tobacco Aid:
  tobacco.wait()
  mutex.wait()
  tobacco_count += 1
  if paper_count >= 1:
    need_matches.signal()
    paper_count -= 1
    tobacco_count -= 1
  else if matches_count >= 1: 
    need_paper.signal()
    matches_count -= 1
    tobacco_count -= 1
  mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Matches Aid:
  matches.wait()
  mutex.wait()
  matches_count += 1
  if paper_count >= 1:
    need_tobacco.signal()
    paper_count -= 1
    matches_count -= 1
  else if tobacco_count >= 1:
    need_paper.signal()
    matches_count -= 1
    tobacco_count -= 1
  mutex.signal()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Paper Aid:
  paper.wait()
  mutex.wait()
  paper_count += 1
  if matches_count >= 1:
    need_tobacco.signal()
    paper_count -= 1
    matches_count -= 1
  if tobacco_count >= 1: 
    need_matches.signal()
    paper_count -= 1
    tobacco_count -= 1
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tobacco Smoker: #no difference in smoker code

need_tobacco.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Matches Smoker:

need_matches.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Paper Smoker:

need_paper.wait()
make_cigarette()
agentSem.signal()
smoke()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

