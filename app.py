from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import re

load_dotenv()

app = Flask(__name__)

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

embeddings = download_hugging_face_embeddings()
index_name = "aichatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever =  docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatGroq(model="qwen-qwq-32b")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["messageText"]
    input = msg
    print(input)
    
    response = rag_chain.invoke({"input": msg})
    full_answer = response["answer"]
   
    cleaned_answer = re.sub(r"<think>.*?</think>", "", full_answer, flags=re.DOTALL).strip()
    
    print("Cleaned Response:", cleaned_answer)
    return {"answer": cleaned_answer}

    # print("Response : ", response["answer"])
    # return jsonify({"answer": response["answer"]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)