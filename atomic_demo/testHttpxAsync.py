import asyncio
import time
import httpx

# proxy
# proxies = {
#     'http://': 'http://127.0.0.1:7890',
# }

url = "https://www.baidu.com"

async def req(client, i):
    res = await client.get(url)
    print(f'第{i + 1}次请求，status_code = {res.status_code}')
    return res


async def main():
    async with httpx.AsyncClient() as client:
        task_list = []  # 任务列表
        for i in range(50):
            res = req(client, i)
            task = asyncio.create_task(res)  # 创建任务
            task_list.append(task)
        await asyncio.gather(*task_list)  # 收集任务


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'异步发送300次请求，耗时：{end - start}')
