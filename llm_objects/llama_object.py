import pandas as pd
import chromadb, ollama, json
from tqdm import tqdm
from datetime import datetime
from langchain_community.llms import Ollama
from typing import Dict
import utils.util as util

class LLMObject():
    def __init__(self):
        # Model Initialize
        util.debug_message("Waiting for Llama-2 instance..")
        self.instance = Ollama(model="llama2")
        util.debug_message("complete")
        
        # load Chroma DB
        COLLECTION_NAME = "cnu_article_data"
        util.debug_message(f"[debug] Get Vector DB Client name : {COLLECTION_NAME}..") # progress
        self.client = chromadb.PersistentClient()
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)
        util.debug_message("Complete") # progress

        TEST_INPUT = "공지사항"
        embedded_query = ollama.embeddings(model="mxbai-embed-large", prompt="TEST_INPUT")

        query_result = self.collection.query(
            query_embeddings=embedded_query["embedding"],
            n_results=3
        )

        print(query_result)


    def get_result(self, user_input):
        # LLM으로 질의 후 응답받기
        bot_response = self.instance(user_input)
        print(user_input,"Llama2: ",bot_response)
        return bot_response

    def get_post_result(self, user_input):
        USER_INPUT = user_input

        embedded_query = ollama.embeddings(model="mxbai-embed-large", prompt=USER_INPUT)

        query_result = self.collection.query(
            query_embeddings=embedded_query["embedding"],
            n_results=3
        )


        print("[debug]",query_result)
        bot_response = self.get_result(f"Question: {USER_INPUT}, Please refer to this result: {query_result}")
        return bot_response

llm_obejct = LLMObject()

