from fastapi import FastAPI, Response
from pydantic import EmailStr

from btc_rate import fetch_btc_rate


app = FastAPI()


@app.get("/rate", tags=["rate"])
async def btc_rate() -> float:
    return fetch_btc_rate()


@app.post("/subscribe", tags=["subscription"])
async def subscribe_email(email: EmailStr) -> Response:
    return Response(None, 200)


@app.post("/sendEmail", tags=["subscription"])
async def mailing() -> Response:
    return Response(None, 200)
