from fastapi.security.api_key import APIKeyHeader
from fastapi import HTTPException, status, Depends

from config import Config

api_key_header_auth = APIKeyHeader(name='api-key')


def check_authentication_header(api_key: str = Depends(api_key_header_auth)):
    if api_key != Config.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API KEY")
