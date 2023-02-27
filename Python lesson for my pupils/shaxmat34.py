# sps=['ati','familya','jili','jumis orni','staji']
# spisok={
# }
# for i in sps:
#     spisok[i]=input(f"{i}-->")
# print(spisok)
import asyncio
async def main():
    await asyncio.sleep(1)
    print('1999')
    await asyncio.sleep(2)
    print('Dawletyar')
    await asyncio.sleep(3)
    print('Awesbaev')
with asyncio.Runner() as runner:
    runner.run(main())