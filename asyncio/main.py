import asyncio


"""
The asynctio.create_task creates a task. The task is run when the CPU
is not being used. If the CPU is idle for 5 seconds,it'll dedicate
5 seconds to the task being created. After 5 seconds, control is passed
back to the main task. That's how the asyncio works in Python. 

A function is said to be coroutine when it has the attribute? async. This
means it's able to relinquish and get back CPU control.

Await means wait for the task to finish before going to the next line.

Asyncio.run(coroutine function) is more of telling python that it's going
to be an async function.
"""
async def main():
	print('daquiver')
	task  = asyncio.create_task(foo("Text")) 
	await asyncio.sleep(1)
	print('finished')

async def foo(text):
	print(text)
	await asyncio.sleep(9)
	print("Temporary")


asyncio.run(main())