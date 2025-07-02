import threading
import time
import requests
import asyncio
import aiohttp

def get_data_sync(urls):
    st = time.time()
    json_array = []
    
    for url in urls:
        json_array.append(requests.get(url).json())
    
    et = time.time()
    elapsed_time = et - st
    print(f"Elapsed time for synchronous requests: {elapsed_time:.2f} seconds")
    return json_array

 
class ThreadingDownloader(threading.Thread):
    json_array = []
    
    def __init__(self, url):
        super().__init__()
        self.url = url
        
    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array


def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        thread = ThreadingDownloader(url)
        thread.start() 
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        print(f"Thread {thread.name} finished execution.")
    
    et = time.time()
    elapsed_time = et - st
    print(f"Elapsed time for synchronous requests: {elapsed_time:.2f} seconds")
    


async def get_data_async_as_wrapper(urls):
    st = time.time()
    json_array = []
    
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())
    
    et = time.time()
    elapsed_time = et - st
    print(f"Elapsed time for synchronous requests: {elapsed_time:.2f} seconds")
    return json_array



async def get_data(session, url, json_array):
    async with session.get(url) as response:
        json_array.append(await response.json())
    

async def get_data_async(urls):
    st = time.time()
    json_array = []
    
    async with aiohttp.ClientSession() as session: 
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
    
        await asyncio.gather(*tasks)
    
    et = time.time()
    elapsed_time = et - st
    print(f"Elapsed time for synchronous requests: {elapsed_time:.2f} seconds")
    return json_array
    


urls = ["https://postman-echo.com/delay/3"] * 10

get_data_sync(urls)
get_data_threading(urls)
asyncio.run(get_data_async_as_wrapper(urls))
asyncio.run(get_data_async(urls))