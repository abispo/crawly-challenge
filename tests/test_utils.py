from app.utils.token import transform_token

import pytest


@pytest.mark.asyncio
async def test_transform_token():
    token = "uu920z349z545v3607x6u4yx16uww383"
    expected = "ff079a650a454e6392c3f5bc83fdd616"

    assert expected == await transform_token(token)
