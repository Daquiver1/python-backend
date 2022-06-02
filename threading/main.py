import threading
import time

def count(n):
	for i in range(1, n+1):
		print(i)
		time.sleep(0.01)

def count2(n):
	for i in range(1, n+1):
		print(i)
		time.sleep(0.02)

x = threading.Thread(target=count, args=(10,))
x.start()

y = threading.Thread(target=count2, args=(10,))
y.start()

print('Done')