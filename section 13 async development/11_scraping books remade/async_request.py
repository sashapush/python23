import aiohttp
import asyncio
import time


#first we create a coroutine - like a generator which suspends and resumes anytime by using wait
async def fetch_page(url):
    page_start = time.time()
    async with asyncio.timeout(10):
        #create a client session from aiohttp
        async with aiohttp.ClientSession() as session: #create a session; can be suspended here
            async with session.get(url) as response: #get url; can be suspended here
                print(f"Page took {time.time() - page_start}")
                return response.status #return response status

#we also need a task scheduler

#to run 1 task
#loop.run_until_complete(fetch_page("https://google.com")) #we don't get response status - but a coroutine object.
async def main():
    tasks = [fetch_page("http://google.com") for i in range(50)]#to run multiple requests:
    await asyncio.gather(*tasks)  #*tasks is argument unpacking, = tasks[0],tasks[1] etc. gather() collects every task and runs it


start_time = time.time()
asyncio.run(main())
print(f'All took {time.time() - start_time}')
