import os
import sys

import aiohttp
import pytest

from app.main import get_token, get_answer, transform_token
from asynctest import CoroutineMock, patch


@pytest.mark.asyncio
async def test_transform_token():
    token = "uu920z349z545v3607x6u4yx16uww383"
    expected = "ff079a650a454e6392c3f5bc83fdd616"

    assert expected == await transform_token(token)


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


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.post')
async def test_get_answer(mock_post):
    mock_post.return_value.__aenter__.return_value.text = CoroutineMock(side_effect=[
        """
        RESPOSTA: <span id="answer">11</span><br /><a href="http://applicant-test.us-east-1.elasticbeanstalk.com/">Voltar</a>
        """
    ])
    async with aiohttp.ClientSession() as session:
        retorno = await get_answer(session, '969w1v3u8yz313v4wuv0907712v6395u')

        assert retorno == '11'
