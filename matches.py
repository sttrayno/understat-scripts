import asyncio
import json

import aiohttp

from understat import Understat

year = input("Please enter the year you wish to pull data from: ")
league = input("Please enter the league you wish to pull data from EPL/Bundesliga etc: ")
club = input ("Please enter the name of the team you wish to pull the data for: ")
filename = input ("Please enter the name of the file you wish to output to: ")
async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        teams = await understat.get_teams(
            league,
            year,
            title = club
        )
        print(json.dumps(teams))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
