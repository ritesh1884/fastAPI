from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# handling errors
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded. Please try again later."},
    )
# rate limiter api
@app.get("/data")
@limiter.limit("5/minute")  # Limit to 5 requests per minute
def get_data(request: Request):
    return {"message": "This is some data."}
