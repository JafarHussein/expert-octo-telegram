from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span_func():
    print("The server is booting up")
    yield
    print("The server is shutting down")
    
app=FastAPI()


