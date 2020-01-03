

import asyncio
import json

import aiohttp

from understat import Understat

playerid = input("Please enter the playerID you wish to pull grouped data for:  ")
assist = input("If you're looking shots which are assisted by a specific player please enter their name, otherwise just leave this blank:  ")
filename = input ("Please enter the name of the file you wish to output to: ")

async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)

        if assist == "":
            player_shots = await understat.get_player_shots(
            playerid)
        else:
            player_shots = await understat.get_player_shots(
            playerid,{"player_assisted": assist})


        print(json.dumps(player_shots))

        with open(filename, 'a') as outfile:
            json.dump(player_shots, outfile)




loop = asyncio.get_event_loop()
loop.run_until_complete(main())
