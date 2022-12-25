from aiohttp import BodyPartReader
from lcu_driver import Connector
from time import sleep

connector = Connector()
@connector.ready

async def connect(connection):
    print("Name Sniper is ready to work !")
    #Here is exemple of name you can try to snipe:
    names = ['Faker', 'Huni', 'Ssumday', 'Bang', 'CoreJJ', 'Zven', 'Rekkles', 'Caps', 'Perkz', 'Jankos']
    k = 0
    while True:
        for i in names:
            k += 1
            if k % 10 == 0:
                sleep(1)
            changename = await connection.request('get', "/lol-summoner/v1/check-name-availability/" + i)
            changename = await changename.json()
            print("try " + i,  changename)
            #if the name is found, you can change your name with this code:
            if changename == True:
                #response = await connection.request('post', '/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": i}), headers=headers)
                print("name found !!!!" + i)
                exit(0)

connector.start()