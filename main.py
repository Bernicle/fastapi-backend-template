from fastapi import FastAPI
from .api.v1.routers.main_route import router as v1_router

app = FastAPI()

app.include_router(v1_router)
# Include routers from different API versions here (e.g., from api.v1.routers import router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
