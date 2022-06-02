from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
	while True:
		value = q.get() # Removes and reutrns an item. Think .pop

		# Processing
		with lock: # Context manager
			print(f"In {current_thread().name} got {value}")
		q.task_done() # Done processing on the item in queue



if __name__ == "__main__":

	lock = Lock()
	q = Queue()
	num_threads = 10

	for i in range(num_threads):
		thread = Thread(target=worker, args=(q,lock))
		# Daemon threads die when the main threads end.
		thread.daemon=True
		thread.start()

	for i in range(1, 21):
		print(f"Putting {i} in queue")
		q.put(i) # Put items. 
		print(f"Done putting {i} in queue")

	q.join() # Wait until all the items in the queue are processed. 


	print('end main')