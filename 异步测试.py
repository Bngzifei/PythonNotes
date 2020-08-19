# coding:utf-8
import asyncio
import aiohttp

host = "https://access.redhat.com/ecosystem/hardware/"
urls_todo = {"1117473", "1117623", "1122183"}

loop = asyncio.get_event_loop()


async def fetch(url):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            response = await response.read()
            return response


if __name__ == '__main__':
    import time
    start = time.time()
    tasks = [fetch(host + url) for url in urls_todo]
    res = loop.run_until_complete(asyncio.gather(*tasks))
    import pdb;pdb.set_trace()
    print(time.time() - start)
