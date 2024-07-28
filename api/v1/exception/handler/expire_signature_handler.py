from fastapi import Request
from fastapi.responses import JSONResponse
from jwt.exceptions import ExpiredSignatureError

async def expire_signature_handler(request: Request, exc: ExpiredSignatureError):
    return JSONResponse(status_code=401, content={"detail":exc.args[0]})
