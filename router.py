from fastapi import FastAPI, Request
from typing import Union
from schemas import HttpResponse
from exception.http_exception_handler import handler, HttpErrorResponse
from rag.llama_object import llm_obejct
from schemas import QueryDTO, ResponseQueryDTO


app = FastAPI()

prefix = "/llm/api/v1"

@app.post(
    f"{prefix}/query",
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
    answer = execute_func_with_exception_handler(llm_obejct.old_rag,query_dto.content)
    
    return ResponseQueryDTO(content=answer, sessionId=query_dto.sessionId)


@app.post(f"{prefix}//test")
async def test(request:Request, query_dto: QueryDTO):
    body = await request.body()
    headers = request.headers
    print(body)
    print(headers)

    return ResponseQueryDTO(ans_message="LLM http test OK")


@handler.http_error_handle
def execute_func_with_exception_handler(func, *args, **kwargs):
    return func(*args, **kwargs)