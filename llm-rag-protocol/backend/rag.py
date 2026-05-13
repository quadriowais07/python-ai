# PdfReader is the prefined class
# used to read data from PDF file
import os

from pypdf import PdfReader

# SentenceTransformer is used to implement the embeddings / vectors
from sentence_transformers import SentenceTransformer

# chormadb used to connect to Vector DB
import chromadb

# OpenAI used to generate the LLM output
from openai import OpenAI

# load the modal
# open source modal
# maps sentences and paragraphs to a 384-dimensional dense vector space
model = SentenceTransformer("all-MiniLM-L6-v2")

# create the table/collection
client = chromadb.Client()
collection = client.create_collection("pdf_data")

# read pdf file
def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text
    
    return text

# chunking
def chunk_text(text):
    chunk_size = 500 # LLM only able to process 500 characters 
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    
    return chunks


# embeddings
def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings # type is numpy list

# store in Vector DB
def store_in_chromadb(chunks, embeddings):
    collection.add(documents = chunks, embeddings = embeddings.tolist(), ids = [str(i) for i in range(len(chunks))])
    return "Data Stored Successfully.!"

# search / query the DB
def search_query(question):
    query_embeddings = model.encode([question])
    results = collection.query(query_embeddings = query_embeddings.tolist(), n_results = 2)
    return results

# generate output
# platform.openai.com/api-keys
def generate_answer(question, context):
    # to connect to Open AI  to generate the answer, provide key
    # to generate key, go platform.openai.com/api-keys    
    api_key = os.getenv("OPENAI_API_KEY") # read the API key from environment variable
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found in environment variables")
    
    openai_client = OpenAI(api_key = api_key) # initialize the OpenAI client with the API key

    prompt = f"""
    Answer the question using below context only

    Context:
    {context}

    Question:
    {question}
    """

    response = openai_client.chat.completions.create(model = "gpt-4.1-mini", messages = [{"role": "user", "content": prompt}])
    final_answer = response.choices[0].message.content

    return final_answer


