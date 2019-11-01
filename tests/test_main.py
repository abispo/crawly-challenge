import os
import sys

import aiohttp

import pytest

from asynctest import CoroutineMock, patch
from app.main import get_token


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_get_token(mock_get):   
    mock_get.return_value.__aenter__.return_value.text = CoroutineMock(side_effect=[
    """
    <html>
    <head>
        <script src="adpagespeed.js"></script>
    </head>
    <body>
    <form action="/" method="post" id="form">
        <input type="hidden" name="token" id="token" value="969w1v3u8yz313v4wuv0907712v6395u" />
        <input type="button" value="Descobrir resposta" onClick="findAnswer()">
    </form>
    </body>
    </html>
    """
    ])
       

    async with aiohttp.ClientSession() as session:
        retorno = await get_token(session)

        assert retorno == '969w1v3u8yz313v4wuv0907712v6395u'
