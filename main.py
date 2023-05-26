from fastapi import FastAPI

app = FastAPI()


@app.get("/rate")
async def btc_rate():
    return {"message": "Under development..."}


@app.post("/subscribe")
async def subscribe_email(email: str):
    return {"message": "Under development..."}


@app.post("/sendEmail")
async def mailing():
    return {"message": "Under development..."}
