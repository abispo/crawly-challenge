import os
import sys

import aiohttp
import asyncio
import asynctest

import pytest

from asynctest import CoroutineMock, patch


from app.utils.request import get_answer, get_token
from tests.fixtures import getpage_content, postpage_content


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_get_token(mock_get):   
    mock_get.return_value.__aenter__.return_value.text = getpage_content()
       

    async with aiohttp.ClientSession() as session:
        retorno = await get_token(session)

        assert retorno == '969w1v3u8yz313v4wuv0907712v6395u'

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.post')
async def test_get_answer(mock_post):   
    mock_post.return_value.__aenter__.return_value.text = postpage_content()

    async with aiohttp.ClientSession() as session:
        retorno = await get_answer(session, '969w1v3u8yz313v4wuv0907712v6395u')

        assert retorno == '11'
