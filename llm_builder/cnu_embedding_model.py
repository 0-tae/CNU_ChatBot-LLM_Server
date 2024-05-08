from transformers import AutoModel, AutoTokenizer


class CnuEmbeddingModel:
    def __init__(self):
        self.model = AutoModel.from_pretrained('BM-K/KoSimCSE-roberta')
        self.tokenizer = AutoTokenizer.from_pretrained('BM-K/KoSimCSE-roberta')

    def get_embbedding_data(self, input):
        sentences = [input]
        inputs = self.tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
        embeddings, _ = self.model(**inputs, return_dict=False)

        return embeddings.tolist()

