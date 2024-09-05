# models directory

models 디렉토리에서는 HuggingFace에서 다운로드 받은 tokenizer, config 파일 등을 저장하는 경로로 사용됩니다. (물론 수정을 자유롭게 할 수 있습니다.)

HuggingFace에서 모델을 가져오고 사용하는 방법을 정의하며, 현재 프로젝트에서는 llama-3-KoreanBllossom-8B 모델을 사용한다고 가정합니다.

### 1. git LFS(Large File System)

git LFS를 통해 HuggingFace Repository에 존재하는 모델 파일을 가져옵니다.

```bash
git lfs install

git clone https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B-gguf-Q4_K_M
```

### 2. transformers

transformers 라이브러리를 이용해서 HuggingFace Repository를 불러올 수 있습니다.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("MLP-KTLim/llama-3-Korean-Bllossom-8B")
model = AutoModelForCausalLM.from_pretrained("MLP-KTLim/llama-3-Korean-Bllossom-8B")
```
