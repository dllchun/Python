import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory

load_dotenv()
openapi_key = os.environ.get("openai_key")


def main():
    # Load PDF
    loader = PyPDFLoader("https://arxiv.org/pdf/2103.15348.pdf")
    data = loader.load()

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunk = text_splitter.split_documents(data)

    # Embedding
    embedding = OpenAIEmbeddings(openai_api_key=openapi_key)

    vectorstore = Chroma.from_documents(text_chunk, embedding).as_retriever()
    # vector_db = Chroma(
    #     persist_directory="./chromadb",
    #     embedding_function=embedding,
    # )

    # Make A chain
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", openai_api_key=openapi_key, max_tokens=2048
    )
    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore, memory=memory
    )
    print(qa_chain)


if __name__ == "__main__":
    main()
