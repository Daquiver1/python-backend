from threading import Thread, Lock
from queue import Queue
import os
import time

DATABASE_VALUE = 0;

def increase(lock):
	# Lock prevents a thread from modifing another resource being used by
	# another thread. Since threads share the same memory space, this is an
	# essential function. 
	global DATABASE_VALUE

	lock.acquire() # Locks the state
	local_copy = DATABASE_VALUE

	# processing
	local_copy += 1
	time.sleep(.1)
	DATABASE_VALUE = local_copy
	# Always release a thread after use. Always, or other threads won't be able to use the memory resource.
	lock.release() 

	"""
	# locks can be used as context managers
	with lock:
		local_copy = DATABASE_VALUE
		local_copy += 1
		time.sleep(.1)
		DATABASE_VALUE = local_copy
	"""


if __name__ == "__main__":
	
	lock = Lock()
	print(f'Start Value: {DATABASE_VALUE}')

	thread1 = Thread(target=increase, args=(lock,))
	thread2 = Thread(target=increase, args=(lock,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print(f'End Value: {DATABASE_VALUE}')

	print("End main")