from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import your routers
from routes.Suggestion_Agent import router as suggestions_router
from routes.trancribe import router as transcribe_router  # small typo corrected (optional)
from routes.testbackend import router as test_router

app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(test_router, tags=["Testing"])
app.include_router(suggestions_router,  tags=["Suggestions"])
app.include_router(transcribe_router,tags=["Transcription"]) 

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
