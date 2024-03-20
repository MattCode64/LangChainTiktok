import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

st.title("🦜️🔗 Tiktok LangChain")

# Streamlit code for choosing the model between the two available models
model = st.selectbox("Choose a model", ["llama2", "mistral"])

print(f"Selected model: {model}")

llm = Ollama(model=model)  # doc : https://github.com/ollama/ollama

prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are an expert on creating tiktoker content.'),
    ('user', "{input}")
])

# St str input
user_prompt = st.text_input("Enter your prompt here", )
print(f"User prompt: {user_prompt}")

chain = prompt | llm

if st.button("Run"):
    response = chain.invoke({'input': user_prompt})
    st.write(response)



