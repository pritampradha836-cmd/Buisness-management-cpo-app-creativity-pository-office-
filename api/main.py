from fastapi import FastAPI

app = FastAPI()

# Middleware
@app.middleware("http")
def add_process_time_header(request: Request, call_next):
    response = call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start)
    return response

# Import routes
from .routes import example

app.include_router(example.router)