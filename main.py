from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from pydantic import EmailStr

from core.btc_rate import fetch_btc_rate
from core.subscribe import subscribe

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


@app.post(
    "/subscribe",
    tags=["subscription"],
    responses={
        200: {"description": "E-mail successfully added to db"},
        409: {"description": "E-mail is already in db"},
        422: {"description": "E-mail is invalid"},

    }
)
async def subscribe_email(email: EmailStr) -> Response:
    try:
        subscribe(email)
        return Response(None, 200)
    except ValueError as exception:
        raise HTTPException(409, str(exception)) from exception


@app.post("/sendEmail", tags=["subscription"])
async def mailing() -> Response:
    return Response(None, 200)
