from pydantic import BaseModel
from typing import Dict
from datetime import datetime


# 응답 데이터를 정의하는 Pydantic 모델

class HttpBaseResponse(BaseModel):
    ok: bool
    status_code: int
    message: str
    
class HttpResponse(HttpBaseResponse):
    ok: bool
    body: Dict[str, str]
    status_code: int
    message: str

class HttpErrorResponse(HttpBaseResponse):
    ok: bool = False
    message: str = "unexpected error"

class QueryDTO(BaseModel):
    query_message: str

class ResponseQueryDTO(BaseModel):
    ans_message: str