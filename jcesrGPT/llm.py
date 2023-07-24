from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.llms import CTransformers

# Local CTransformers wrapper for Llama-2-7B-Chat
#llm = CTransformers(model='/Users/hadoan/apps/meta_llama/llama.cpp/models/7B-chat/ggml-model-7bchat-q4_0.bin', # Location of downloaded GGML model
#                    model_type='llama', # Model type Llama
#                    config={'max_new_tokens': 256,
#                            'temperature': 0.01})

# OpenAI API wrapper for GPT-3
#llm = OpenAI(temperature=0, model_name='text-davinci-003')
llm = ChatOpenAI(temperature=0., model_name='gpt-3.5-turbo-16k-0613')
