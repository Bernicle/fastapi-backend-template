# Import all Builtin and Custom Exception that we want to map to each handler
from jwt.exceptions import ExpiredSignatureError

# Import all Handler Function that we create
from api.v1.exception.handler.expire_signature_handler import expire_signature_handler

# Include all Exception with it own Handler
handlers = [
    {"exception":ExpiredSignatureError , "handler":expire_signature_handler}
]