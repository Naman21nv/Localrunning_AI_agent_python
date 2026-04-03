from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

model=OllamaLLM(model="llama3.2")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

Prompt=PromptTemplate.from_template(template)
chain =Prompt | model