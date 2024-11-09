import time
import httpx

url = "https://www.baidu.com"

def main():
    with httpx.Client() as client:
        for i in range(50):
            res = client.get(url)
            print(f'第{i + 1}次请求，status_code = {res.status_code}')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'同步发送300次请求，耗时：{end - start}')
