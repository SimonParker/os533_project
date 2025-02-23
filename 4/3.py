#simon parker

'''
No-Starve Mutex: Find a way for 3 threads to access a mutex without starvation. You can only assume that you have access to weak
semaphores, meaning that if there are threads waiting for a semaphore, then one will awaken when signal() is called.


Starter:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while true:
  mutex.wait()
  #critical section
  mutex.signal()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem with above is thread A goes, signals, and then waits at the mutex again. B grabs the mutex, goes, signals, and waits 
at the mutex. A grabs the mutex, goes, signals, etc.. There is no guarentee that C will ever go, it 'starves'.

Fix this, assuming a finite number of threads







'''
