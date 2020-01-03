

import asyncio
import json

import aiohttp

from understat import Understat

playerid = input("Please enter the playerID you wish to pull grouped data for:  ")
filename = input ("Please enter the name of the file you wish to output to: ")


async def main():
    async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            player = await understat.get_player_grouped_stats(playerid)
            print(json.dumps(player))

            with open(filename, 'a') as outfile:
                json.dump(player, outfile)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
