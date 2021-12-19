import asyncio

async def rxer():
    i=0
    while True:
        i+=1
        print ('Rxer ',i)
        await asyncio.sleep(0)

async def WsServe():
    count = 10
    while count != 0:
        print ('WsServe',count)
        count -=1
        await asyncio.sleep(0)

    print ('Finish')
    #loop.stop()
    #loop.close()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(rxer())
    loop.run_until_complete(WsServe())
    #loop.run_forever()


    #asyncio.run(main())