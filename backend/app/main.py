from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.Suggestion_Agent import router as suggestions_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(suggestions_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
