import pandas as pd
import chromadb, ollama, json
from tqdm import tqdm
from datetime import datetime
from langchain_community.llms import Ollama
from typing import Dict
from cnu_embedding_model import CnuEmbeddingModel

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

USER_INPUT = "소프트웨어 사업단 articles "
embedding_model = CnuEmbeddingModel()
embedded_query = embedding_model.get_embbedding_data(USER_INPUT)

for idx, content in enumerate(embedded_query):
    print(idx, len(content))
    for ix, c in enumerate(content):
        print(ix, len(c))    

query_result = collection.query(
    query_embeddings=embedded_query,
    n_results=3
)

print(query_result)
# print("[debug]",query_result)
# bot_response = llama2.get_result(f"Question: {USER_INPUT}, Please refer to this result : {query_result}")
# print(bot_response)
