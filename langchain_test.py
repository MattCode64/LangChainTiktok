from langchain_community.llms import Ollama

llm = Ollama(model="llama2") # doc : https://github.com/ollama/ollama

user_prompt = "Hello, give me 3 nicknames for my pet"

response = llm.invoke(user_prompt)

# llm.invoke("Hello, give me 3 nicknames for my pet")
#%%
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ('system', "Tu es un expert en Machine Learning."),
    ('user', "{input}")
])

#%%
chain = prompt | llm

#%%
chain.invoke({'input': "Donne moi les 3 noms des métiers de la data science"})

#%%
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
#%%
chain = prompt | llm | output_parser
#%%
chain.invoke({'input': "Liste 3 bibliothèques python pour le machine learning"})

