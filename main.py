from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .api.v1.routers.main_route import router as v1_router
from .config.database import get_db, Base

app = FastAPI()

app.include_router(v1_router, dependencies=[Depends(get_db)])
# Include routers from different API versions here (e.g., from api.v1.routers import router)

#@app.before_first_request
#def create_tables(db : Session = Depends(get_db)):
#    db.create_all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
