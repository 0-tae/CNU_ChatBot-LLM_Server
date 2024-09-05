### API 명세서 v.1.0

이 API는 LLM(대형 언어 모델)에 질의를 전송하고 응답을 받기 위한 엔드포인트들을 제공합니다.

---

### **1. 질의 처리 API**

- **엔드포인트**: `/llm/api/v1/query`
- **HTTP 메소드**: `POST`
- **설명**: 사용자가 제공한 질의 내용을 LLM에 전달하고, 그 결과를 반환하는 API입니다.
- **요청 바디 예시**:

  ```json
  {
    "sessionId": "Qwe693KX",
    "content": "이번 학기 수강신청 언제야?"
  }
  ```

- **요청 헤더**:  
  필요한 경우 특정 헤더를 통해 접근 권한을 확인할 수 있습니다. (추후 구현 예정)

- **응답**:
  - **성공 응답** (`ResponseQueryDTO`):
    ```json
    {
      "sessionId": "Qwe693KX",
      "content": "${수강신청과 관련된 응답}"
    }
    ```
  - **에러 응답** (`HttpErrorResponse`):
    ```json
    {
      "ok": false,
      "status_code": 500,
      "message": "unexpected error"
    }
    ```

---

### **데이터 모델**

#### 1. **QueryDTO**

- **설명**: 사용자의 질의를 담고 있는 요청 데이터 모델.
- **필드**:
  - `sessionId`: `string` (세션 식별자)
  - `content`: `string` (사용자가 질의한 내용)

#### 2. **ResponseQueryDTO**

- **설명**: 질의에 대한 LLM의 응답을 담고 있는 데이터 모델.
- **필드**:
  - `sessionId`: `string` (세션 식별자)
  - `content`: `string` (LLM이 생성한 응답)

#### 3. **HttpResponse**

- **설명**: 일반적인 성공 응답을 담고 있는 데이터 모델.
- **필드**:
  - `ok`: `bool` (성공 여부)
  - `status_code`: `int` (HTTP 상태 코드)
  - `message`: `string` (응답 메시지)
  - `body`: `Dict[str, str]` (응답 본문)

#### 4. **HttpErrorResponse**

- **설명**: 에러 응답을 담고 있는 데이터 모델.
- **필드**:
  - `ok`: `bool` (기본값: `False`, 성공 여부)
  - `status_code`: `int` (HTTP 상태 코드)
  - `message`: `string` (에러 메시지)

---

### **예외 처리**

- API 호출 중 발생할 수 있는 예외는 `execute_func_with_exception_handler` 함수를 통해 처리됩니다.
- 예외 발생 시 `HttpErrorResponse` 형식으로 응답이 반환됩니다.

### **기타 사항**

- `handler.http_error_handle` 데코레이터를 사용하여 전역 예외 처리가 가능합니다.
- 헤더를 통해 요청의 적합성을 확인하는 기능은 추후 추가될 예정입니다.
