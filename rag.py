import random
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_store(pdf_file):

    loader = PyPDFLoader(pdf_file)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectordb


def generate_question(vectordb):

    docs = vectordb.similarity_search(
        "technical interview questions",
        k=10
    )

    questions = []

    for doc in docs:

        text = doc.page_content

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            line = re.sub(r'^\d+[\).\-\s]*', '', line)

            if len(line) < 10:
                continue

            if line.lower().startswith("page"):
                continue

            questions.append(line)

    questions = list(dict.fromkeys(questions))

    if questions:

        return random.choice(questions)

    return "No Question Found"


if __name__ == "__main__":

    pdf_file = "Interview Questions.pdf"

    vectordb = create_vector_store(
        pdf_file
    )

    print("\nGenerated Questions:\n")

    for i in range(5):

        print(
            f"{i+1}. {generate_question(vectordb)}"
        )