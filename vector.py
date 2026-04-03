"""
THEORY & CONCEPTS:
This script builds a Vector Database. 
Language models don't "read" words like humans; they understand numbers. 
"Embeddings" convert our text (reviews) into massive lists of numbers (vectors) 
that capture the core meaning of the sentence. We then save these vectors into a database (Chroma). 
Later, when a user asks a question, we convert their question into a vector, and find the reviews with the closest matching numbers!
"""
import warnings

# Suppress the Pydantic V1 compatibility warning from LangChain Core for Python 3.14+
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_core")

from langchain_ollama import OllamaEmbeddings  #  used to take text and convert it into a vector representation
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os

df=pd.read_csv("realistic_restaurant_reviews.csv")

# 1. INITIALIZE THE EMBEDDING MODEL
# mxbai-embed-large is a model highly optimized for turning text into dense vector representations.
embeddings=OllamaEmbeddings(model="mxbai-embed-large")  # we use this for creating vector representations of the data(here reviews) model we r using is mxbai-embed-large
 #which is running in cmd with the command "ollama pull mxbai-embed-large"

db_location="./chroma_db"  # location where the vector database will be stored

# 2. CHECK IF DATABASE ALREADY EXISTS
# Creating embeddings is computationally expensive. If the folder exists, we skip creating it again!
add_documents=not os.path.exists(db_location)

if add_documents:
    documents=[]  #list of documents that we will add to our vector database
    ids=[]       #list of ids for each document, which can be used to retrieve the document later

    for i,row in df.iterrows():
        # We use .append() to add each Document to our list
        # page_content is the actual text string that the AI will read, convert to vectors, and search against later.
        #metadata is additional information that we can store with each document, which can be useful for filtering or providing context during retrieval. In this case, we are storing the rating of the review as metadata.
        document=Document(page_content=row["Title"] + " " + row["Review"], metadata={"rating": row["Rating"], "date": row["Date"]}) # We also add metadata for each document, which in this case is the rating of the review
        documents.append(document)
        ids.append(str(i))

# 3. INITIALIZE CHROMA VECTOR DATABASE
# This creates the connection to the physical database folder on your hard drive.
vector_store=Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,  #store permanently in that location
    embedding_function=embeddings,
    )   

# 4. SAVE DATA (If it didn't already exist)
if add_documents:  #if not exist we shld add orelse we no need to add again
    # Adding documents is the heaviest process because the embedding model has to run on every single row.
    vector_store.add_documents(documents=documents, ids=ids)


retriever =vector_store.as_retriever(
    search_kwargs={"k": 5}          #when we search for something this will search for the 5 most similar reviews in the vector database and return those to us (kwarg means keyword args  )
    
)


    



                                                        
