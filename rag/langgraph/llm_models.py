
import transformers, torch
from datetime import datetime

class Llama38BKorModel():
        
    def __init__(self):
        self.model_id = 'MLP-KTLim/llama-3-Korean-Bllossom-8B'
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id ,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )

        self.pipeline.model.eval()

    def set_prompt(self):
        PROMPT = \
        f'''You are a helpful AI assistant. You must respond to user queries kindly and accurately in korean. Refer to the searched documents to answer the user's query.
        retrieved documents: {content_query_result["documents"][0]}
        If the information from the retrieved documents is insufficient, respond with "Insufficient information available."
        Today is {datetime.now()}
        '''

        return PROMPT

    def query(self, input:str):
        pipeline = self.pipeline

        context = self.prompt()
        instruction = f'User query: {input}'

        messages = [
            {"role": "system", "content": f"{context}"},
            {"role": "user", "content": f"{instruction}"}
        ]

        prompt = pipeline.tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
        )

        terminators = [
            pipeline.tokenizer.eos_token_id,
            pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = pipeline(
            prompt,
            max_new_tokens=2048,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9
        )

        return outputs[0]["generated_text"][len(prompt):]
