

import asyncio
import json

import aiohttp

from understat import Understat

matchid = input("Please enter the matchID you wish to pull grouped data for:  ")
filename = input ("Please enter the name of the file you wish to output to: ")


async def main():
    async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            players = await understat.get_match_players(match)
            print(json.dumps(players))

            with open(filename, 'a') as outfile:
                json.dump(players, outfile)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
