from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from pydantic import EmailStr

from btc_rate import fetch_btc_rate
from subscribe import subscribe
from utils import setup_db

app = FastAPI()
setup_db()


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exception: HTTPException,
) -> Response:
    return Response(
        status_code=exception.status_code,
        content=exception.detail,
    )


@app.get("/rate", tags=["rate"])
async def btc_rate() -> float:
    return fetch_btc_rate()


@app.post("/subscribe", tags=["subscription"])
async def subscribe_email(email: EmailStr) -> Response:
    return Response(None, 200)


@app.post("/sendEmail", tags=["subscription"])
async def mailing() -> Response:
    return Response(None, 200)
