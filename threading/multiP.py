from multiprocessing import Process
import os
import time


def square_numbers():
	for i in range(100):
		i = i 
		time.sleep(0.1)

processes = []
num_processes = os.cpu_count() # counts number of cpus.

# Create processes
for i in range(num_processes):
	process = Process(target=square_numbers)
	processes.append(process)

# start
for process in processes:
	process.start()

# wait for all processes to finish
# block the main program until these processes are finished
for process in processes:
	process.join()

print("End main")