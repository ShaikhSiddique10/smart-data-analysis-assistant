from llama_cpp import Llama
import os

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=4096,           
    n_threads=16,         
    n_gpu_layers=0,       
    use_mlock=True,       
    verbose=False         
)

def ask_local_llm(messages):
    try:
        response = llm.create_chat_completion(
            messages=messages,
            temperature=0.7,
            top_p=0.95
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ LLM Error: {e}"
