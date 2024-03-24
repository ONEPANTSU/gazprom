import uvicorn
from app import App

app = App()

if __name__ == "__main__":

    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
