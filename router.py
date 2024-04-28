from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from typing import Union
from schemas import HttpResponse
from exception.http_exception_handler import handler, HttpErrorResponse
from llm_objects.llama_object import llm_obejct
from schemas import QueryDTO, ResponseQueryDTO
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(    
    CORSMiddleware,
    allow_origins=["*"],  # 모든 origin을 허용하려면 ["*"]로 설정합니다.
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],)

@app.post(
    "/api/v1/llm/query",
    response_model=Union[HttpResponse, HttpErrorResponse, ResponseQueryDTO],
    response_model_exclude_defaults=True,
    
)
async def result_for_query(request:Request, query_dto: QueryDTO):
    '''
        :param user_input: 유저가 인터페이스에 입력한 질의
        :return: LLM으로 부터 받은 질의 결과
    '''
    body = await request.body()
    headers = request.headers
    print(body)
    print(headers)
    #  TODO: Header 확인하여 접근권한을 가진 요청인지 확인하기

    # 질의를 통해 LLM에서 결과 얻어오기
    answer = execute_func_with_exception_handler(llm_obejct.get_post_result,query_dto.query_message)
    
    return ResponseQueryDTO(ans_message=answer)

@handler.http_error_handle
def execute_func_with_exception_handler(func, *args, **kwargs):
    return func(*args, **kwargs)