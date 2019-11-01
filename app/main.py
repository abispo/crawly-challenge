
from datetime import datetime

import aiohttp
import pydantic

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from aiohttp import ClientError

from app.utils.request import get_answer, get_token
from app.utils.token import transform_token

app = FastAPI()


@app.exception_handler(ClientError)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error_message": f"{exc}"},
    )


@app.get("/")
async def index():
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        start_time = datetime.now()

        token = await get_token(session)
        answer = await get_answer(session, await transform_token(token))

        end_time = datetime.now()

        delta = end_time - start_time

        response = {
            'answer': answer,
            'elapsed_time': int(delta.total_seconds() * 1000)
        }

        return response
