# Load model directly
import os
os.environ["TRANSFORMERS_CACHE"] = "./cache/"
os.environ["HF_HOME"] = "./cache/"

from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import torch

gpu_llm = HuggingFacePipeline.from_model_id(
    model_id="beomi/llama-2-ko-7b",  # 사용할 모델의 ID를 지정합니다.
    task="text-generation",  # 수행할 작업을 설정합니다. 여기서는 텍스트 생성입니다.
    # 사용할 GPU 디바이스 번호를 지정합니다. "auto"로 설정하면 accelerate 라이브러리를 사용합니다.
    device_map="auto",
    # 파이프라인에 전달할 추가 인자를 설정합니다. 여기서는 생성할 최대 토큰 수를 10으로 제한합니다.
    pipeline_kwargs={"max_new_tokens": 64},
)


template = """Answer the following question in Korean.
    #Question: 
    {question}

#Answer: """  # 질문과 답변 형식을 정의하는 템플릿
prompt = PromptTemplate.from_template(template)  # 템플릿을 사용하여 프롬프트 객체 생성
gpu_chain = prompt | gpu_llm  # prompt와 gpu_llm을 연결하여 gpu_chain을 생성합니다.

# 프롬프트와 언어 모델을 연결하여 체인 생성
gpu_chain = prompt | gpu_llm | StrOutputParser()

question = input("질문을 입력하세요") # 질문 정의

# 체인을 호출하여 질문에 대한 답변 생성 및 출력
print(gpu_chain.invoke({"question": question}))



from datasets import load_dataset
# Convert dataset to OAI messages
system_message = """You are an text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA.
SCHEMA:
{schema}"""
 
def create_conversation(sample):
  return {
    "messages": [
      {"role": "system", "content": system_message.format(schema=sample["context"])},
      {"role": "user", "content": sample["question"]},
      {"role": "assistant", "content": sample["answer"]}
    ]
  }
 
# Load dataset from the hub
dataset = load_dataset('rdpahalavan/network-packet-flow-header-payload', split="train")
dataset = dataset.shuffle().select(range(12500))
 
# Convert dataset to OAI messages
dataset = dataset.map(create_conversation, remove_columns=dataset.features,batched=False)
# split dataset into 10,000 training samples and 2,500 test samples
dataset = dataset.train_test_split(test_size=2500/12500)
 
print(dataset["train"][345]["messages"])
 
# save datasets to disk
dataset["train"].to_json("train_dataset.json", orient="records")
dataset["test"].to_json("test_dataset.json", orient="records")