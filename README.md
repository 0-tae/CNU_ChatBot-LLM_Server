# 충남대학교 챗봇 프로젝트

이 프로젝트는 충남대학교 학생들을 위한 챗봇 서비스를 구현한 내용입니다. LLM(Large Language Model)과 RAG(Retrieval-Augmented Generation) 기술을 Naive하게 활용하여 교내 게시물 데이터를 기반으로 사용자에게 정보를 제공합니다.

추후 학칙 pdf파일, 크롤링 등의 Retrieve 기능 추가로 보다 많고 정확한 정보를 제공할 예정입니다.

## 프로젝트 개요

**LLM**을 기반으로 충남대학교의 다양한 정보를 제공하는 **챗봇 서비스**를 개발하고자 프로젝트를 진행하였습니다. **RAG** 기술을 적용하여 검색된 정보를 기반으로 챗봇이 더욱 정확한 답변을 할 수 있도록 합니다.

## 주요 기술

- **LLM**: 한국어로 학습된 모델(**MLP-KTLim/llama-3-Korean-Bllossom-8B**)을 사용하여 사용자 질문에 한국어 답변을 생성합니다.
- **RAG**: 검색 증강 생성 기술을 통해 사용자 질문과 관련된 문서를 검색하고, 그 정보를 기반으로 챗봇이 답변을 생성합니다.
- **Vector DB**: 문서 데이터를 임베딩하여 저장하고, 유사도 검색을 수행할 수 있도록 **Chroma DB**를 활용합니다.

## 시스템 아키텍처
<img width="591" alt="image" src="https://github.com/user-attachments/assets/c31be880-aed2-4289-8356-1b564fefac74">

- **Frontend**: Vanila JS로 구현됨(repository:)
- **Backend**: Java/SpringBoot로 구현됨(repository:)
- **LLM Interface**: LangChain 및 transformers 라이브러리를 사용하여 LLM 연결
- **Database**: MySQL 이용
- **Embedding Model**: KoSimCSE-roberta 모델 활용

**시스템 흐름**:
<img width="596" alt="image" src="https://github.com/user-attachments/assets/70935789-0884-4f8b-ab36-5392fcbef0be">

1. 사용자가 질문을 입력하면 웹 서버가 이를 처리하여 서버로 전달합니다.
2. 서버는 질문과 관련된 문서를 **Vector DB**에서 검색합니다.
3. 검색된 문서를 LLM에 전달하여 최종 답변을 생성합니다.
4. 생성된 답변이 사용자에게 웹 UI를 통해 제공됩니다.

## 데이터 수집 및 처리

- **데이터 수집**: 충남대학교 정보화본부 API를 통해 약 8,490개의 게시물 데이터를 수집하여 지식 베이스로 활용하였습니다.
- **데이터 처리**: 수집된 데이터를 **Vector DB**에 임베딩 처리 하였습니다. 데이터는 다음과 같이 구성됩니다.

  <img width="420" alt="image" src="https://github.com/user-attachments/assets/05f15997-ba6d-4194-9913-b18fee478a17">


## 테스트 및 평가

본 프로젝트에서는 챗봇의 성능을 평가하기 위해 20개의 질문에 대한 **Golden Dataset**을 구축하여 테스트를 진행했습니다.
<img width="582" alt="image" src="https://github.com/user-attachments/assets/0de590c0-edc7-4930-89a1-5d3c2032071e">

<img width="586" alt="image" src="https://github.com/user-attachments/assets/f84a1f7c-f7bd-49d1-90c2-1f6dd9589958">

- **평가 기준**: 정확도, 일관성, 적합성을 기준으로 LLM의 답변을 평가하였으며, 검색 결과의 추론 가능성 및 질문 연관성도 함께 평가하였습니다.

   <img width="606" alt="image" src="https://github.com/user-attachments/assets/757b9dd3-9784-479e-a0d7-183e130e453e">

- **프롬프트**: 프롬프트는 다음과 같이 작성하였습니다.

  <img width="565" alt="image" src="https://github.com/user-attachments/assets/200fce56-cd6b-4dc8-930b-f8c262d936e5">


## 개선 방향

**결과 분석**: 일부 질문에 대해 낮은 정밀도 및 재현율을 확인하였으며, 데이터 부족과 청크 분할로 인한 정보 누락 문제를 분석하였습니다.

1. **데이터 보완**: 현재 수집된 데이터 외에도 추가적인 데이터를 확보하여 검색 정확도를 높입니다.
2. **키워드 기반 검색**: 임베딩 벡터 계산에 의존하지 않고, 핵심 키워드를 기반으로 한 검색 방식을 도입합니다.
3. **Reranking**: 검색된 결과를 순위별로 다시 평가하여 검색 정확도를 높이는 **reranking** 기법을 적용합니다.

## 결과

<img width="405" alt="image" src="https://github.com/user-attachments/assets/0537b47e-8740-450b-b952-5a486e0dbe5c">

<img width="499" alt="image" src="https://github.com/user-attachments/assets/54db4ec5-b400-4d85-a359-345e22791bdc">

<img width="446" alt="image" src="https://github.com/user-attachments/assets/bd4b6b24-b6c1-4d93-9cdd-5cc24949f78f">

## 실행 방법
현재 레포지토리는 LLM Server이며, 이에 대한 실행 방법을 명시합니다.

다른 구현부에 대해서는 추후 링크 업데이트 예정입니다.
**Backend**:
**Web Server(Front)**:
**Infra**: 

1. rag/env_set에 환경 설정을 마쳐주세요

2. 프로젝트를 로컬 환경에 클론합니다.

   ```bash
   git clone https://github.com/username/CNU-ChatBot.git
   cd CNU-ChatBot
   ```

3. 필요한 패키지를 설치합니다.

   ```bash
   pip install -r requirements.txt
   ```

4. FastAPI 서버를 uvicorn으로 실행합니다.

   ```bash
   uvicorn router:app --reload
   ```

5. API_Doc.md를 읽고 LLM Server의 API를 이용하여 모델을 서버에 통합할 수 있습니다.
