from fastapi import FastAPI
import uvicorn

from apps.posts import router
from apps.comments import crouter

app = FastAPI()

app.include_router(router)
app.include_router(crouter)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)