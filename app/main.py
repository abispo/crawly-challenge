from bs4 import BeautifulSoup
from decouple import config
from fastapi import FastAPI

import aiohttp

app = FastAPI()
URL = config('CRAWLY_APP_URL')

headers = {
    'Host': 'applicant-test.us-east-1.elasticbeanstalk.com',
    'User-Agent': 'Crawly Challenge Browser',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://applicant-test.us-east-1.elasticbeanstalk.com',
    'Referer': 'http://applicant-test.us-east-1.elasticbeanstalk.com/',
}


async def transform_token(token: str) -> str:
    replacements = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
        'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
        'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
        's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a', '0': '9', '1': '8', '2': '7', '3': '6',
        '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0'
    }

    return ''.join([replacements.get(char) for char in token])


async def get_token(session: aiohttp.ClientSession) -> str:
    try:
        async with session.get(URL) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'html.parser')

            return soup.find('input', {'id': 'token'})['value']
    except Exception as e:
        raise aiohttp.ClientError(str(e))

async def get_answer(session: aiohttp.ClientSession, token: str) -> str:
    data = {'token': token}

    try:
        async with session.post(URL, data=data, headers=headers) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')

            return soup.find('span', {'id': 'answer'}).text
    except Exception as e:
        raise aiohttp.ClientError(str(e))


@app.get("/")
async def index():
    async with aiohttp.ClientSession() as session:

        token = await get_token(session)
        answer = await get_answer(session, await transform_token(token))

        response = {
            'answer': answer
        }

        return response
