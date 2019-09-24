import asyncio
from proxybroker import Broker
import socks


def get_proxy(limit=1):
    results = []

    async def show(proxies):
        while True:
            proxy = await proxies.get()
            if proxy is None: break
            results.append((socks.HTTP, proxy.host, proxy.port))

    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(types=['SOCKS5'], limit=limit),
        show(proxies))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    return results

# print(get_proxy(10))