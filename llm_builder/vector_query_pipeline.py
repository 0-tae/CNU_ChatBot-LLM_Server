import pandas as pd
import chromadb, ollama, json
from tqdm import tqdm
from datetime import datetime
from langchain_community.llms import Ollama
from typing import Dict

class LLMObject():
    def __init__(self):
        # Model Initialize
        self.instance = Ollama(model="llama2")

    def get_result(self, user_input):
        # LLM으로 질의 후 응답받기
        bot_response = self.instance(user_input)
        print("Llama2_response:",bot_response)
        return bot_response

llama2 = LLMObject()


# load Chroma DB
COLLECTION_NAME = "cnu_article_data" # cnu_article

print(f"[debug] Get Vector DB Client name : {COLLECTION_NAME}..", end=" ") # progress
client = chromadb.PersistentClient()
collection = client.get_or_create_collection(name=COLLECTION_NAME)
print("Complete") # progress


### TEST CODE

USER_INPUT = "소프트웨어 사업단 제목을 가진 게시물을 찾아줘"

embedded_query = ollama.embeddings(model="mxbai-embed-large", prompt=USER_INPUT)

query_result = collection.query(
    query_embeddings=embedded_query["embedding"],
    n_results=3
)


print("[debug]",query_result)
bot_response = llama2.get_result(f"Question: {USER_INPUT}, Please refer to this result : {query_result}")
print(bot_response)
