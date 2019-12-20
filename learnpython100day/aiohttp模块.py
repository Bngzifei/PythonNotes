# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-05-13 20:26:44
# @Last Modified by:   Marte
# @Last Modified time: 2019-05-14 08:57:49


import asyncio
import aiohttp

# 简单示例
async def aiohttp_test01(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text('utf-8'))


loop = asyncio.get_event_loop()
tasks = [aiohttp_test01("https://api.github.com/events")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()