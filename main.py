"""
THEORY & CONCEPTS:
This file is the main execution script for our AI Agent.
It uses a concept called RAG (Retrieval-Augmented Generation).

Large Language Models (LLMs) are frozen in time and only know what they were trained on. 
Instead of relying purely on the AI's pre-trained knowledge, RAG allows us to "Retrieve" 
external data (like our pizza reviews) and "Augment" the AI's prompt with that data 
before asking it to "Generate" an answer.
"""
from langchain_ollama import OllamaLLM # Used to connect to local LLMs via Ollama
from langchain_core.prompts import PromptTemplate # Used to structure instructions for the AI

# 1. INITIALIZE THE MODEL
# We use a local model (llama3.2) so data stays on our machine and runs for free.
model=OllamaLLM(model="llama3.2")

# 2. CREATE THE PROMPT TEMPLATE
# Prompt Engineering: We give the AI a persona ("expert") and strict placeholders 
# {reviews} and {question} to structure the data we send it.
template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

Prompt=PromptTemplate.from_template(template)

# 3. BUILD THE CHAIN (LCEL - LangChain Expression Language)
# The '|' operator pipes the formatted Prompt directly into the LLM. 
# Flow: Data -> PromptTemplate -> LLM
chain =Prompt | model

# 4. INTERACTIVE LOOP
# This keeps the program running so we can ask multiple questions.
while True:
    print("\n\n -----------------------------\n\n")
    question=input("Ask a question about the pizza restaurant: (x to exit) ")
    if question.lower() == "x":
        break
    
    # .invoke() triggers the chain. Right now, "reviews" is an empty list.
    # In the next step of our project, we will fetch real reviews from our Vector Database!
    result=chain.invoke({"reviews":[],"question":question})
    print(result)