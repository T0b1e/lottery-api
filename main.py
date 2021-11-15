from fastapi import FastAPI
from lottery import *

app = FastAPI()


@app.get("/")
async def root():
    return {"lottery": lottery}

@app.get("/{date}")
async def root():
    return {"lottery": lottery}

@app.get("/first_reward")
async def root():
    return {"first_reward": first_reward()['first_reward']}

@app.get("/front_three")
async def root():
    return {"front_three": first_reward()['front_three']}

@app.get("/last_three")
async def root():
    return {"last_three": first_reward()['last_three']}

@app.get("/last_two")
async def root():
    return {"last_two": first_reward()['last_two']}

@app.get("/close_reward")
async def root():
    return {"close_reward": first_reward()['close_reward']}

@app.get("/second_reward")
async def root():
    return {"second_reward": second_reward()}

@app.get("/third_reward")
async def root():
    return {"third_reward": third_reward()}

@app.get("/fourth_reward")
async def root():
    return {"fourth_reward": fourth_reward()}

@app.get("/fifth_reward")
async def root():
    return {"fifth_reward": fifth_reward()}