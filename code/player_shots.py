

import asyncio
import json

import aiohttp

from understat import Understat

playerid = input("Please enter the playerID you wish to pull grouped data for:  ")
filename = input ("Please enter the name of the file you wish to output to: ")

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        player_shots = await understat.get_player_shots(
        playerid,)
        print(json.dumps(player_shots))

        f = open(filename, "a")
        f.write(str(player_shots))
        f.close()



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
