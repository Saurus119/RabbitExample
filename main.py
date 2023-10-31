import uvicorn
import asyncio
from fastapi import BackgroundTasks
from contextlib import asynccontextmanager

from Api.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)