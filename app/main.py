from bs4 import BeautifulSoup
from decouple import config
from fastapi import FastAPI

import aiohttp

app = FastAPI()
URL = config('CRAWLY_APP_URL')


async def get_token(session: aiohttp.ClientSession) -> str:
    try:
        async with session.get(URL) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'html.parser')

            return soup.find('input', {'id': 'token'})['value']
    except Exception as e:
        raise aiohttp.ClientError(str(e))


@app.get("/")
async def index():
    async with aiohttp.ClientSession() as session:

        token = await get_token(session)

        return {"token": token}
