from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import v1_router

app = FastAPI(
    title="scrap videos_via_youtube",
    version = "1.0",
)
# Set up CORS middleware
# The `origins` list in the FastAPI code snippet is specifying the allowed origins for Cross-Origin
# Resource Sharing (CORS) requests. CORS is a security feature implemented by web browsers to restrict
# web pages from making requests to a different domain than the one that served the original page.
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
