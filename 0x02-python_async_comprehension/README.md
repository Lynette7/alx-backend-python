# Asynchronous Comprehension

- 0-async_generator.py: Python script that contains an asynchronous coroutine called async_generator that takes no arguments where the coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.
- 1-async_comprehension.py: Python script that imports async_generator from 0-async_generator.py and then writes a coroutine called async_comprehension that takes no arguments. The coroutine collects 10 random numbers using an async comprehensing over async_generator, then returns the 10 random numbers.
- 2-measure_runtime.py: Python script that imports async_comprehension from 1-async_comprehension.py and writes a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.measure_runtime measures the total runtime and returns it.
