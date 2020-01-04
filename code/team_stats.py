

import asyncio
import json

import aiohttp

from understat import Understat

year = input("Please enter the year you wish to pull data from (please note, currently this argument can only pass throguh one year at a time, the default behaviour of this script is to append to the filename provided so if you're looking to access match data from multiple years please run this script multiple times):  ")
club = input ("Please enter the name of the team you wish to pull the data for: ")
filename = input ("Please enter the name of the file you wish to output to: ")


async def main():
    async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            team_stats = await understat.get_team_stats(club, year)
            print(json.dumps(team_stats))

            with open(filename, 'a') as outfile:
                json.dump(team_stats, outfile)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
