import pandas as pd
import chromadb, ollama, json
from tqdm import tqdm
from datetime import datetime

def getSecondsDiff(start,end):
    time_dif = end - start
    return 0.2 if time_dif.seconds ==0 else time_dif.seconds

def getTimeDiffString(time_dif_seconds) : 
    seconds = time_dif_seconds

    # 시간
    hours = seconds // 3600
    seconds %= 3600

    # 분
    minutes = seconds // 60
    seconds %= 60

    return f"[{int(hours)}h-{int(minutes)}m-{int(seconds)}s] left"

# 게시글 CSV 파일 불러오기

CSV_FILE_NAME = "./cnu_article_data.csv"

print(f"[debug] Get {CSV_FILE_NAME} file data from current Directory..", end=" ") # progress
csv_data = pd.read_csv(CSV_FILE_NAME,encoding='utf-8')
print("Complete") # progress

entire_size, num_cols = csv_data.shape

# 디스크 모드로 이용, 이외에도 인메모리, HttpClient 방식 등이 존재

COLLECTION_NAME = "cnu_article_data"

print(f"[debug] Get Vector DB Client name : {COLLECTION_NAME}..", end=" ") # progress
client = chromadb.PersistentClient()
collection = client.get_or_create_collection(name=COLLECTION_NAME)
print("Complete") # progress

# site_name,article_number,article_title,article_text,writer_name,click_count,update_date
ids = []
metadatas = []
embeddings = []

# CSV 데이터 순회 후 vector DB에 저장
for idx, row in enumerate(csv_data.iterrows()):
  start_time = datetime.now()
  ######## TASK 1 ########
  metadata = {
    "site_name" : row[1]["site_name"],
    "board_name" : row[1]["board_name"],
    "article_number" : row[1]["article_number"],
    "article_text" : row[1]["article_text"],
    "article_title" : row[1]["article_title"],
    "writer_name" : row[1]["writer_name"],
    "click_count" : row[1]["click_count"],
    "update_date" : row[1]["update_date"]
  }

  metadatas.append(metadata)
  ids.append(str(idx))
  
  response = ollama.embeddings(model="mxbai-embed-large", prompt=json.dumps(metadata))
  embedding = response["embedding"]
  embeddings.append(embedding)
  #########################

  end_time = datetime.now()

  prediction_seconds = getSecondsDiff(start_time,end_time)*entire_size
  print(f"[debug] ({idx} / {entire_size})")
  
  if idx % 100 == 0 :
    # Collection ADD
    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas
    )

    ids = []
    metadatas = []
    embeddings = []

    print("[debug] data added",end_time.strftime("%Y-%m-%d %H:%M:%S"),getTimeDiffString(prediction_seconds))

# Collection ADD
collection.add(
    ids=ids,
    embeddings=embeddings,
    metadatas=metadatas
)


### TEST CODE
TARGET_IDX = 3
print("[debug] Test Query execute")
print(f"[debug] target idx {TARGET_IDX}")

query_result = collection.query(
    query_embeddings=embeddings[3],
    n_results=5
)

IS_CORRECT = query_result['ids'][0] == TARGET_IDX
print(query_result)
print(f"[debug] test result is {IS_CORRECT}")
print("[debug] Vecter db add complete")