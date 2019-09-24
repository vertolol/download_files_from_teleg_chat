import asyncio
import datetime
import settings
from telethon import TelegramClient
import timeit


start_time = timeit.default_timer()
clients = []

client = TelegramClient(f'sessions/anon_test',
                        settings.api_id,
                        settings.api_hash,
                        proxy=settings.proxies[0])


async def download(start_date):
    tasks = []

    group = await client.get_entity(settings.dev_group_id)
    flag = True
    offset = 0
    limit = 20
    while flag:
        start_while_time = timeit.default_timer()
        print("start while")
        result = await client.get_messages(group,
                                           reverse=True,
                                           limit=limit,
                                           offset_date = start_date,
                                           add_offset = -offset
                                           )

        for message in result:

            if message.date.date() > start_date.date():
                flag = False
                break

            elif message.file and message.file.mime_type in settings.mime_types.values():
                print('create task for mes id: ', message.id, message.date)
                task = asyncio.create_task(message.download_media(settings.download_dir))
                tasks.append(task)

            else:
                print(message.file.mime_type)

        print('gathering 10')
        await asyncio.gather(*tasks)
        offset += limit

        print(timeit.default_timer() - start_while_time)


start_date = datetime.datetime(2019, 7, 20, 4, 0)

with client:
    print("with client")
    client.loop.run_until_complete(download(start_date))


end_time = timeit.default_timer()
print(end_time - start_time)