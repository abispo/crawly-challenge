from starlette.testclient import TestClient
from asynctest import patch

import pytest

from app.main import app

from tests.fixtures import getpage_content, postpage_content

client = TestClient(app)


@pytest.mark.freeze_time('2019-11-02')
@patch('aiohttp.ClientSession.get')
@patch('aiohttp.ClientSession.post')
def test_main(mock_post, mock_get):
    mock_post.return_value.__aenter__.return_value.text = postpage_content()
    mock_get.return_value.__aenter__.return_value.text = getpage_content()

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'answer': '11', 'elapsed_time': 0}
