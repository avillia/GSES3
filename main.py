from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/rate", tags=["rate"])
async def btc_rate() -> float:
    return 3.1415926


@app.post("/subscribe", tags=["subscription"])
async def subscribe_email(email: str) -> Response:
    return Response(None, 200)


@app.post("/sendEmail", tags=["subscription"])
async def mailing() -> Response:
    return Response(None, 200)
