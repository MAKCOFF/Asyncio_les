# Shift+F6 - переименовать переменню во всех точка
#
import asyncio
import values_flags

global count_wr

# flag = False

async def gener_1():
    count = 1

    while True:

        print("gen1", count)
        await asyncio.sleep(0.5)
        count +=1
        if count==10:
            values_flags.flag = True
            break


async def gener_2(count_wr):

    if count_wr < 2:
        return
    count = 0
    while True:

        if count %3 == 0:
            print("{} секунд прошло".format(count))
        count += 1
        await asyncio.sleep(0.5)
        if count == 100:
            break

async def gener_3():
    count = 0

    while values_flags.flag:
        print("gen3", count)
        await asyncio.sleep(0.5)
        count += 1
        if count == 10:
            break

async def main():

    task_1 = asyncio.create_task(gener_1())
    task_2 = asyncio.create_task(gener_2(3))


    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':

    asyncio.run(main(), debug=True)
