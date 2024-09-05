### README.md 작성 예시

````markdown
# CNU ChatBot

CNU ChatBot은 RAG(Retrieval-Augmented Generation)를 이용하여 충남대학교와 관련된 다양한 질의에 대한 답변을 제공하는 챗봇 프로젝트입니다. Python과 FastAPI를 사용하여 간단한 REST API 기반의 챗봇을 구현했습니다.

## 기술 스택

- **Python**: 프로젝트 전반에서 사용되는 프로그래밍 언어
- **FastAPI**: REST API 서버 프레임워크
- **Uvicorn**: ASGI 서버로 FastAPI 애플리케이션을 실행
- **RAG (Retrieval-Augmented Generation)**: 대규모 언어 모델(LLM)을 사용하여 문서에서 답변을 검색하고 생성

## 핵심 코드

아래는 `router.py`에 정의된 API 엔드포인트입니다.

```python
from fastapi import FastAPI, Request, APIRouter
from typing import Union

prefix = "/llm/api/v1"
app = FastAPI()
router = APIRouter()

@app.post(
    f"{prefix}/query",
    response_model=Union[HttpResponse, HttpErrorResponse, ResponseQueryDTO],
    response_model_exclude_defaults=True,
)
async def result_for_query(request: Request, query_dto: QueryDTO):
    '''
    :param user_input: 유저가 인터페이스에 입력한 질의
    :return: LLM으로부터 받은 질의 결과
    '''
    body = await request.body()
    headers = request.headers
    print(body)
    print(headers)
    # TODO: Header 확인하여 접근권한을 가진 요청인지 확인하기

    # 질의를 통해 LLM에서 결과 얻어오기
    answer = execute_func_with_exception_handler(llm_object.old_rag, query_dto.content)

    return ResponseQueryDTO(content=answer, sessionId=query_dto.sessionId)
```
````

## API 명세서

### POST /llm/api/v1/query

유저가 입력한 질의를 LLM에 전달하여 답변을 반환하는 API입니다.

#### Request Body

- **query_dto** (`QueryDTO`): 유저가 입력한 질문 및 세션 정보를 포함한 데이터
  - `content` (string): 유저의 질문
  - `sessionId` (string): 유저의 세션 ID

#### Response

- **ResponseQueryDTO**
  - `content` (string): LLM으로부터 받은 답변
  - `sessionId` (string): 유저의 세션 ID

#### Response Example

```json
{
  "content": "충남대학교는 대전광역시에 위치한 국립대학교입니다.",
  "sessionId": "1234567890"
}
```

## 실행 방법

1. 프로젝트를 로컬 환경에 클론합니다.

```bash
git clone https://github.com/username/CNU-ChatBot.git
cd CNU-ChatBot
```

2. 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

3. FastAPI 서버를 uvicorn으로 실행합니다.

```bash
uvicorn router:app --reload
```

4. 브라우저에서 `http://localhost:8000/docs`로 이동하여 API 명세서를 확인하고 테스트할 수 있습니다.

```
이 문서는 프로젝트 설명, API 명세서, 그리고 실행 방법을 포함합니다. `uvicorn`을 사용하여 FastAPI 서버를 실행하는 방법도 명시되어 있으며, 제공한 API 코드와 함께 어떻게 동작하는지 쉽게 이해할 수 있도록 작성되었습니다.
```
