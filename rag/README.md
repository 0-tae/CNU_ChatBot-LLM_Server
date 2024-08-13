---
language:
- en
- ko
license: llama3
library_name: transformers
tags:
- llama-cpp
- gguf-my-repo
base_model:
- meta-llama/Meta-Llama-3-8B
- jeiku/Average_Test_v1
- MLP-KTLim/llama-3-Korean-Bllossom-8B
---


<a href="https://github.com/MLP-Lab/Bllossom">
  <img src="https://github.com/teddysum/bllossom/blob/main//bllossom_icon.png?raw=true" width="40%" height="50%">
</a>



# Update!
* [2024.06.18] 사전학습량을 **250GB**까지 늘린 Bllossom ELO모델로 업데이트 되었습니다. 다만 단어확장은 하지 않았습니다. 기존 단어확장된 long-context 모델을 활용하고 싶으신분은 개인연락주세요!
* [2024.06.18] Bllossom ELO 모델은 자체 개발한 ELO사전학습 기반으로 새로운 학습된 모델입니다. [LogicKor](https://github.com/StableFluffy/LogicKor) 벤치마크 결과 현존하는 한국어 10B이하 모델중 SOTA점수를 받았습니다. 

LogicKor 성능표 :
| Model | Math | Reasoning | Writing | Coding | Understanding | Grammar | Single ALL | Multi ALL | Overall |
|:---------:|:-----:|:------:|:-----:|:-----:|:----:|:-----:|:-----:|:-----:|:----:|
| gpt-3.5-turbo-0125 | 7.14 | 7.71 | 8.28 | 5.85 | 9.71 | 6.28 | 7.50 | 7.95 | 7.72 |
| gemini-1.5-pro-preview-0215 | 8.00 | 7.85 | 8.14 | 7.71 | 8.42 | 7.28 | 7.90 | 6.26 | 7.08 |
| llama-3-Korean-Bllossom-8B | 5.43 | 8.29 | 9.0 | 4.43 | 7.57 | 6.86 | 6.93 | 6.93 | 6.93 |


# Bllossom | [Demo]() | [Homepage](https://www.bllossom.ai/) | [Github](https://github.com/MLP-Lab/Bllossom)

- 본 모델은 CPU에서 구동가능하며 빠른 속도를 위해서는 8GB GPU에서 구동 가능한 양자화 모델입니다! [Colab 예제](https://colab.research.google.com/drive/129ZNVg5R2NPghUEFHKF0BRdxsZxinQcJ?usp=drive_link) |

```bash
저희 Bllossom팀 에서 한국어-영어 이중 언어모델인 Bllossom을 공개했습니다!
서울과기대 슈퍼컴퓨팅 센터의 지원으로 100GB가넘는 한국어로 모델전체를 풀튜닝한 한국어 강화 이중언어 모델입니다!
한국어 잘하는 모델 찾고 있지 않으셨나요?
 - 한국어 최초! 무려 3만개가 넘는 한국어 어휘확장
 - Llama3대비 대략 25% 더 긴 길이의 한국어 Context 처리가능
 - 한국어-영어 Pararell Corpus를 활용한 한국어-영어 지식연결 (사전학습)
 - 한국어 문화, 언어를 고려해 언어학자가 제작한 데이터를 활용한 미세조정
 - 강화학습
이 모든게 한꺼번에 적용되고 상업적 이용이 가능한 Bllossom을 이용해 여러분 만의 모델을 만들어보세욥!
본 모델은 CPU에서 구동가능하며 빠른 속도를 위해서는 6GB GPU에서 구동 가능한 양자화 모델입니다!

1. Bllossom-8B는 서울과기대, 테디썸, 연세대 언어자원 연구실의 언어학자와 협업해 만든 실용주의기반 언어모델입니다! 앞으로 지속적인 업데이트를 통해 관리하겠습니다 많이 활용해주세요 🙂
2. 초 강력한 Advanced-Bllossom 8B, 70B모델, 시각-언어모델을 보유하고 있습니다! (궁금하신분은 개별 연락주세요!!)
3. Bllossom은 NAACL2024, LREC-COLING2024 (구두) 발표로 채택되었습니다.
4. 좋은 언어모델 계속 업데이트 하겠습니다!! 한국어 강화를위해 공동 연구하실분(특히논문) 언제든 환영합니다!! 
   특히 소량의 GPU라도 대여 가능한팀은 언제든 연락주세요! 만들고 싶은거 도와드려요.
```

The Bllossom language model is a Korean-English bilingual language model based on the open-source LLama3. It enhances the connection of knowledge between Korean and English. It has the following features:

* **Knowledge Linking**: Linking Korean and English knowledge through additional training
* **Vocabulary Expansion**: Expansion of Korean vocabulary to enhance Korean expressiveness.
* **Instruction Tuning**: Tuning using custom-made instruction following data specialized for Korean language and Korean culture
* **Human Feedback**: DPO has been applied
* **Vision-Language Alignment**: Aligning the vision transformer with this language model 

**This model developed by [MLPLab at Seoultech](http://mlp.seoultech.ac.kr), [Teddysum](http://teddysum.ai/) and [Yonsei Univ](https://sites.google.com/view/hansaemkim/hansaem-kim).** 
**This model was converted to GGUF format from [`MLP-KTLim/llama-3-Korean-Bllossom-8B`](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B) for more details on the model.**


## Demo Video

<div style="display: flex; justify-content: space-between;">
  <!-- 첫 번째 컬럼 -->
  <div style="width: 49%;">
    <a>
      <img src="https://github.com/lhsstn/lhsstn/blob/main/x-llava_dem.gif?raw=true" style="width: 100%; height: auto;">
    </a>
    <p style="text-align: center;">Bllossom-V Demo</p>
  </div>

  <!-- 두 번째 컬럼 (필요하다면) -->
  <div style="width: 49%;">
    <a>
      <img src="https://github.com/lhsstn/lhsstn/blob/main/bllossom_demo_kakao.gif?raw=true" style="width: 70%; height: auto;">
    </a>
    <p style="text-align: center;">Bllossom Demo(Kakao)ㅤㅤㅤㅤㅤㅤㅤㅤ</p>
  </div>
</div>



## NEWS
* [2024.05.08] Vocab Expansion Model Update
* [2024.04.25] We released Bllossom v2.0, based on llama-3
* [2023/12] We released Bllossom-Vision v1.0, based on Bllossom
* [2023/08] We released Bllossom v1.0, based on llama-2. 
* [2023/07] We released Bllossom v0.7, based on polyglot-ko.


## Example code
```python
!CMAKE_ARGS="-DLLAMA_CUDA=on" pip install llama-cpp-python
!huggingface-cli download MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M --local-dir='YOUR-LOCAL-FOLDER-PATH'

from llama_cpp import Llama
from transformers import AutoTokenizer

model_id = 'MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = Llama(
    model_path='YOUR-LOCAL-FOLDER-PATH/llama-3-Korean-Bllossom-8B-Q4_K_M.gguf',
    n_ctx=512,
    n_gpu_layers=-1        # Number of model layers to offload to GPU
)

PROMPT = \
'''당신은 유용한 AI 어시스턴트입니다. 사용자의 질의에 대해 친절하고 정확하게 답변해야 합니다.
You are a helpful AI assistant, you'll need to answer users' queries in a friendly and accurate manner.'''

instruction = 'Your Instruction'

messages = [
    {"role": "system", "content": f"{PROMPT}"},
    {"role": "user", "content": f"{instruction}"}
    ]

prompt = tokenizer.apply_chat_template(
    messages, 
    tokenize = False,
    add_generation_prompt=True
)

generation_kwargs = {
    "max_tokens":512,
    "stop":["<|eot_id|>"],
    "top_p":0.9,
    "temperature":0.6,
    "echo":True, # Echo the prompt in the output
}

resonse_msg = model(prompt, **generation_kwargs)
print(resonse_msg['choices'][0]['text'][len(prompt):])
```



## Citation
**Language Model**
```text
@misc{bllossom,
  author = {ChangSu Choi, Yongbin Jeong, Seoyoon Park, InHo Won, HyeonSeok Lim, SangMin Kim, Yejee Kang, Chanhyuk Yoon, Jaewan Park, Yiseul Lee, HyeJin Lee, Younggyun Hahm, Hansaem Kim, KyungTae Lim},
  title = {Optimizing Language Augmentation for Multilingual Large Language Models: A Case Study on Korean},
  year = {2024},
  journal = {LREC-COLING 2024},
  paperLink = {\url{https://arxiv.org/pdf/2403.10882}},
 },
}
```

**Vision-Language Model**
```text
@misc{bllossom-V,
  author = {Dongjae Shin, Hyunseok Lim, Inho Won, Changsu Choi, Minjun Kim, Seungwoo Song, Hangyeol Yoo, Sangmin Kim, Kyungtae Lim},
  title = {X-LLaVA: Optimizing Bilingual Large Vision-Language Alignment},
  year = {2024},
  publisher = {GitHub},
  journal = {NAACL 2024 findings},
  paperLink = {\url{https://arxiv.org/pdf/2403.11399}},
 },
}
```

## Contact
 - 임경태(KyungTae Lim), Professor at Seoultech. `ktlim@seoultech.ac.kr`
 - 함영균(Younggyun Hahm), CEO of Teddysum. `hahmyg@teddysum.ai`
 - 김한샘(Hansaem Kim), Professor at Yonsei. `khss@yonsei.ac.kr`

## Contributor
 - 최창수(Chansu Choi), choics2623@seoultech.ac.kr
 - 김상민(Sangmin Kim), sangmin9708@naver.com
 - 원인호(Inho Won), wih1226@seoultech.ac.kr
 - 김민준(Minjun Kim), mjkmain@seoultech.ac.kr 
 - 송승우(Seungwoo Song), sswoo@seoultech.ac.kr
 - 신동재(Dongjae Shin), dylan1998@seoultech.ac.kr
 - 임현석(Hyeonseok Lim), gustjrantk@seoultech.ac.kr
 - 육정훈(Jeonghun Yuk), usually670@gmail.com
 - 유한결(Hangyeol Yoo), 21102372@seoultech.ac.kr
 - 송서현(Seohyun Song), alexalex225225@gmail.com