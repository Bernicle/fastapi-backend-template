from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from helper.security import decode_access_token
import os

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/login')

async def get_current_user(token: str = Depends(oauth_scheme)):
    setting = {
        "SECRET_KEY":os.getenv("SECRET_KEY"),
        "ALGORITHM": os.getenv("ALGORITHM")
    }
    
    user_detail = decode_access_token(token, setting)
    
    print(token)
    print(user_detail)
    # {
    #     "id": 'user id here', 
    #     "exp": 'expiration here in unix',
    # }

    #Place Logic here to get the details of User,
    #Place Logic here to also get the Permission Tag to that User.

    pass

