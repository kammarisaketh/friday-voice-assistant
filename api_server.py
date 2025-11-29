from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from friday.core.assistant import FridayAssistant

app = FastAPI()

# Allow the browser UI to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all origins (for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create one global FRIDAY assistant instance
assistant = FridayAssistant()


@app.get("/api/listen")
async def listen_once():
    print(">>> /api/listen called")   # debug
    result = assistant.handle_once()
    print(">>> handle_once result:", result)   # debug
    return result


@app.get("/")
async def root():
    return {"status": "FRIDAY API running"}


# ---- IMPORTANT: run uvicorn from inside this script ----
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=9000,
        reload=False,   # keep it simple (no extra worker process)
    )
