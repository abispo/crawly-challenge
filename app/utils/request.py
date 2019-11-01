from bs4 import BeautifulSoup
from decouple import config

import aiohttp

URL = config('CRAWLY_APP_URL')

headers = {
    'Host': 'applicant-test.us-east-1.elasticbeanstalk.com',
    'User-Agent': 'Crawly Challenge Browser',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://applicant-test.us-east-1.elasticbeanstalk.com',
    'Referer': 'http://applicant-test.us-east-1.elasticbeanstalk.com/',
}


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
