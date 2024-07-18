from bcrypt import hashpw, gensalt
from typing import Union
from datetime import datetime, timedelta, timezone
import jwt

def hash_password(password : str) -> str:
    if not isinstance(password, str):
        raise TypeError("Input must be a string.")
   
    password_bytes = password.encode('utf-8')
    generate_salt = gensalt()
    hashed_bytes = hashpw(password_bytes, generate_salt)
    return f"{hashed_bytes.decode('utf-8')}:{generate_salt.decode('utf-8')}"

def verify_password(password : str, hash_password : str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Input must be a string.")
    if not isinstance(hash_password, str):
        raise TypeError("Input must be a string.")
    hash_code, salt = hash_password.split(':')
    return (hash_code == hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8'))

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None, SECRET_SETTING : dict = {}):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=to_encode,key=SECRET_SETTING.get('SECRET_KEY'), algorithm=SECRET_SETTING.get('ALGORITHM'))
    return encoded_jwt


def decode_access_token(encoded_jwt: str, SECRET_SETTING : dict = {}) -> dict:
    
    decoded_jwt = jwt.decode(encoded_jwt, SECRET_SETTING.get('SECRET_KEY'), algorithms=SECRET_SETTING.get('ALGORITHM'))
    
    return decoded_jwt