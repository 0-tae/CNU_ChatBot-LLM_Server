
from transformers import AutoModel, AutoTokenizer
import chromadb

class VectorDBObject():
    def __init__(self):
        self.__client = chromadb.PersistentClient(path="./rag/chroma")
        self.__collection = self.__client.get_collection(name="cnu_post_data")
        self.__collection2 = self.__client.get_collection(name="cnu_post_content_data")

        self.__embedding_model = AutoModel.from_pretrained('BM-K/KoSimCSE-roberta')
        self.__embedding_tokenizer = AutoTokenizer.from_pretrained('BM-K/KoSimCSE-roberta')


    def __get_embeddings(self, input_str: str):
        documents = []
        documents.append(input_str)

        inputs = self.__embedding_tokenizer(documents, padding=True, truncation=True, return_tensors="pt")
        embeddings, _ = self.__embedding_model(**inputs, return_dict=False)
        doc_embeddings = []

        for embedded_doc in embeddings:
            doc_embedding = embedded_doc[0].detach().cpu().numpy().tolist()
            doc_embeddings.append(doc_embedding)

        return doc_embeddings

    def query_to_vector_db(self, user_input: str, filter:list = ["컴퓨터융합학부","인공지능학과"]):
        doc_embeddings = self.__get_embeddings(user_input)
        
        query_result = self.__collection2.query(
                query_embeddings=doc_embeddings,
                where={"학과명": {"$in": filter}},
                n_results=15
        )
        print("ids: ", query_result['ids'][0])
        return query_result['ids'][0],query_result["documents"][0]

vector_db_object = VectorDBObject()