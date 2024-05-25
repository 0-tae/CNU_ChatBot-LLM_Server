import pandas as pd
import chromadb, ollama, json
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup
from chromadb.utils import embedding_functions

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


def convertHTML(html_code):
    soup = BeautifulSoup(html_code, 'html.parser') 
    content = soup.get_text("\n")
    
    return content.replace(u"\xa0", u"").replace(u"\n", " ")
        
# 게시글 CSV 파일 불러오기

CSV_FILE_NAME = "./cnu_article_data.csv"

print(f"[debug] Get {CSV_FILE_NAME} file data from current Directory..", end=" ") # progress
csv_data = pd.read_csv(CSV_FILE_NAME,encoding='utf-8')
print("Complete") # progress

entire_size, num_cols = csv_data.shape

# 디스크 모드로 이용, 이외에도 인메모리, HttpClient 방식 등이 존재
import chromadb.utils.embedding_functions as embedding_functions
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="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",
    model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS"
)

COLLECTION_NAME = "cnu_article_data"

print(f"[debug] Get Vector DB Client name : {COLLECTION_NAME}..", end=" ") # progress
client = chromadb.PersistentClient()
collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function = huggingface_ef)
print("Complete") # progress

# site_name,article_number,article_title,article_text,writer_name,click_count,update_date
ids = []
metadatas = []
documents = []

openai_ef = embedding_functions.SentenceTransformerEmbeddingFunction()

# CSV 데이터 순회 후 vector DB에 저장
for idx, row in enumerate(csv_data.iterrows()):
  start_time = datetime.now()

  # metadata / id
  metadata = {
    "site_name" : row[1]["site_name"],
    "board_name" : row[1]["board_name"],
    "article_number" : row[1]["article_number"],
    "writer_name" : row[1]["writer_name"],
    "click_count" : row[1]["click_count"],
    "update_date" : row[1]["update_date"]
  }
  metadatas.append(metadata)
  ids.append(str(idx))
  
  # document
  document=f"제목: {row[1]['article_title']}, 내용: {convertHTML(row[1]['article_text'])}"
  documents.append(document)

  # embedding
    #   response = ollama.embeddings(model="mxbai-embed-large", prompt=json.dumps(metadata))
    #   embedding = response["embedding"]
    # embeddings.append(embedding)

  # time set
  end_time = datetime.now()
  prediction_seconds = getSecondsDiff(start_time,end_time)*(entire_size-idx)
  print(f"[debug] ({idx} / {entire_size})")
  
  if idx % 100 == 0 :
    # Collection add
    collection.add(
        ids=ids,
        metadatas=metadatas,
        documents=documents
    )

    ids = []
    metadatas = [] 
    documents = []

    print("[debug] data added",end_time.strftime("%Y-%m-%d %H:%M:%S"),getTimeDiffString(prediction_seconds))

# Collection ADD
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("[debug] Vecter db add complete")