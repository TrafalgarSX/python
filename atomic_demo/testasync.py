import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def another_count():
    print("Three")
    print("Four")
    await asyncio.sleep(1)
    print("Five")

async def main():
    await asyncio.gather(count(), another_count())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    
