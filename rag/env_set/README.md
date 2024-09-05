# rag/env_set directory

현재 디렉토리에서는 CNU ChatBot에서 RAG(Retrievial-Argumented-Generation) 구현 시, 필요한 데이터를 구성합니다. 다음의 ipynb 파일을 순서대로 실행하여 초기 데이터를 구성합니다.

데이터는 _충남대학교 내 학교/학과 게시물_ 이며 정보화본부의 API, Vector DB(Chroma)에 Embedding하여 저장합니다.

### 1. data_init.ipynb

충남대학교 게시물 데이터를 .csv 파일로 저장하는 작업을 수행합니다.
.csv 파일은 환경에 구애받지 않고 학과 데이터를 이용하기 위해 생성합니다.

### 2. rag_database_init

충남대학교 게시물 데이터 .csv 파일을 MySQL DB에 저장하는 작업을 수행합니다.
.csv 파일에서 필요한 컬럼의 데이터만 저장하고, 조회하기 위해 사용합니다.

### 3. rag_vectordb_init

MySQL DB에 저장된 데이터를 Vector DB에 Embedding하여 저장하는 작업을 수행합니다.
RAG에서 사용자 입력으로 데이터를 조회하기 위해 사용됩니다.
