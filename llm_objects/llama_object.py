from langchain_community.llms import Ollama
from typing import Dict
import utils.util as util
class LLMObject():
    def __init__(self):
        # Model Initialize
        util.debug_message("Waiting for Llama-2 instance..")
        instance = Ollama(model="llama2")
        instance("hi")

    def get_result(self,user_input):
        # LLM으로 질의 후 응답받기
        bot_response = self.instance(user_input)
        ok: bool
        body: Dict[str, str]
        status_code: int
        message: str
        return bot_response



llm_obejct = LLMObject()

