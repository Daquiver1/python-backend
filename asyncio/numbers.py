import asyncio 


"""
A future is like a promise in js. 
It's a placeholder for a value that'll exist in the future.


Flow:
The main says there are two tasks. Task 1 and task 2. It starts with
task 1. We print fetching data, then sleep for 2 seconds. Now the processor
is idle, so we switch to task2. There we start print numbers from 0 to 9. 
But within the 2 seconds window. Since the second function sleeps for 0.5 seconds,
there's only time to print 4 numbers. Which is 0 to 3. Then control is given
back to fetch data. It prints done fetchint and returns a value. Then control is
returned to main, it prints value then terminate.
"""


async def fetch_data():
	print("Fetching data...")
	await asyncio.sleep(2)
	print("Done fetching")
	return {'data': 1}

async def print_numbers():
	for i in range(10):
		print(i)
		await asyncio.sleep(0.5)

async def main():
	task1 = asyncio.create_task(fetch_data())
	task2 = asyncio.create_task(print_numbers())

	value = await task1 # Wait for task1 to complete.
	print("value")
asyncio.run(main())