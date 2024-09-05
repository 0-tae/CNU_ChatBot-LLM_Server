from datetime import datetime
import torch, transformers
# from rag.vector_db_object import vector_db_object
from rag.vector_db_object import vector_db_object

class LLMObject():
    def __init__(self):
        self.pipeline = transformers.pipeline(
            "text-generation",
            model='MLP-KTLim/llama-3-Korean-Bllossom-8B',
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )
        self.terminators = [
                self.pipeline.tokenizer.eos_token_id,
                self.pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

    def pre_rag(self,  user_input, user_args):
        retrieved_documents = []
        ids,query_result = vector_db_object.query_to_vector_db(user_input=user_input)

        for idx,result in enumerate(query_result):
            id = ids[idx]
            retrieved_documents.append((id,result))

        PROMPT = \
        f'''Based on the retrieved documents, select 3 post IDs that best answer the user's question. If no relevant posts documents, output "-1", PLEASE FORMAT THE OUTPUT EXACTLY AS SHOWN IN THE EXAMPLE.
        1. Example:
            1) input: "컴퓨터융합학부 관련 게시물 가져와줘", your_output: "10001,10003,10008"
            2) input: "영어 인정을 받고싶어", your_output: "10003,10007,10002"
            3) input: "사업단 특별 마일리지 장학금이 뭐야?", your_output: "10007,10003,10008"
            4) input: "학교 교가가 뭐야?", your_output: "-1"

        2. Retrieved document list: {retrieved_documents}
        '''

        instruction = f'{user_input}'
        messages = [
                {"role": "system", "content": f"{PROMPT}"},
                {"role": "user", "content": f"{instruction}"}
        ]

        prompt = self.pipeline.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
        )

        outputs = self.pipeline(
                prompt,
                max_new_tokens=100,
                eos_token_id=self.terminators,
                do_sample=True,
                temperature=0.1,
                top_p=0.9
        )

        answer = outputs[0]["generated_text"][len(prompt):]
        print(answer)

        return answer

    def rag(self, user_input, user_args =["컴퓨터융합학부"]):
        pre_result = self.__pre_rag(user_input,user_args)
        
        PROMPT = \
        f'''You are an AI chatbot designed to assist university students. Summarize the given post and provide a friendly and logical response to the user's question based on the post's content. Follow the conditions below to generate your answer:
            1. The user's major is {user_args[0]}.
            2. The current time is {datetime.now()}.
            3. 
            4. If the post content is "해당 사항 없음" output "질문에 대한 정보를 찾을 수 없습니다. 데이터 추가의 경우 모델 제공자에게 문의 바랍니다."
        '''


        instruction = f'{user_input}'
        messages = [
                {"role": "system", "content": f"{PROMPT}"},
                {"role": "user", "content": f"{instruction}"}
        ]

        prompt = self.pipeline.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
        )

        outputs = self.pipeline(
                prompt,
                max_new_tokens=100,
                eos_token_id=self.terminators,
                do_sample=True,
                temperature=0.1,
                top_p=0.9
        )

        # Answer
        answer = outputs[0]["generated_text"][len(prompt):]

        return answer
    
    def old_rag(self, user_input):
        ids,query_result = vector_db_object.query_to_vector_db(user_input=user_input)
        PROMPT = \
            f'''You are a helpful AI assistant. You must respond to user queries logicaly, kindly and accurately in korean.
            Refer to the searched documents to answer the user query. 
            please select 3 documents in retireved document list, 
            1. retrieved document list: {query_result}
            If the information from the retrieved documents is insufficient, respond with "Insufficient information available." and
            When a document have a time information, you must mention it correctly, Today is {datetime.now()}
            '''
        
        instruction = f'{user_input}'
        messages = [
                {"role": "system", "content": f"{PROMPT}"},
                {"role": "user", "content": f"{instruction}"}
        ]

        prompt = self.pipeline.tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
        )

        outputs = self.pipeline(
                prompt,
                max_new_tokens=2048,
                eos_token_id=self.terminators,
                do_sample=True,
                temperature=0.6,
                top_p=0.9
        )

        # Answer
        answer = outputs[0]["generated_text"][len(prompt):]

        return answer

llm_obejct = LLMObject()