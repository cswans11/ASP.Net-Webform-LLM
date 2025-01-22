import socket
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.prompts import PromptTemplate


# Set up the model and pipeline
token = 'hhf_jtRyuMHzDRCKkxunAWAXxeJstyiZodJCYx'
model_name = "meta-llama/Llama-3.2-3B"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=token)
hf_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=50, truncation=True)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer this: {question}"
)

chain = LLMChain(llm=llm, prompt=prompt)

# Create a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 65432))
server.listen(1)
print("Server is listening...")

# listen to the open port
while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode("utf-8")
    print(data)
    response = chain.run(data)
    conn.sendall(response.encode("utf-8"))
    conn.close()
