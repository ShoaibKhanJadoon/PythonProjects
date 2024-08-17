import time
import asyncio

async def function1():
  await asyncio.sleep(3)
  print("function1")


async def function2():
  await asyncio.sleep(2)
  print("function2")


async def function3():
  await asyncio.sleep(1)
  print("function3")

async def main():
  await asyncio.gather(function1(),function2(),function3())
asyncio.run(main())