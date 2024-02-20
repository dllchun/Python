import streamlit as st
import os
from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile
import dotenv

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationSummaryMemory
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv()
openai_key = os.environ.get("OPENAI_API_KEY")


def generate_pdf_list(pdfs) -> list:
    pdf_list = []
    for i in pdfs:
        bytes_data = i.read()
        with NamedTemporaryFile(
            delete=False,
            dir="/Users/vincentcheung/Desktop/Coding/Python-1/side-project/openai-project",
            suffix=".pdf",
        ) as tmp:
            tmp.write(bytes_data)
            pdf_list.append(tmp.name)

    return pdf_list


def get_directory(pdf_list: list) -> str:
    directory = os.path.dirname(pdf_list[0])
    return directory


def load(directory: str) -> list[str]:
    loader = PyPDFDirectoryLoader(directory)
    data = loader.load()
    return data


def delete_temp_file(temp_path) -> None:
    for i in temp_path:
        os.remove(i)


def split_text(data: list) -> list:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunk = text_splitter.split_documents(data)
    return text_chunk


def text_embedding() -> object:
    embedding = OpenAIEmbeddings(
        openai_api_key=openai_key,
        model="text-embedding-ada-002",
    )
    return embedding


def load_vectordb(data: list, embedding: object, persist_directory: str) -> object:
    vectordb = Chroma.from_documents(
        documents=data, embedding=embedding, persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb


def initiate_openai_chat_model(temperature: int, model_name: str) -> object:
    llm = ChatOpenAI(
        temperature=temperature,
        model_name=model_name,
        openai_api_key=openai_key,
    )
    return llm


def main():
    st.set_page_config(
        page_title="Chat with multiple PDFs",
        page_icon=":books:",
    )

    st.header("Chat with multiple PDFs")
    prompt = st.text_input("Ask a question about your documents:")

    # Sidebar
    with st.sidebar:
        st.subheader("Your documents")
        st.write("Upload your PDFs here and click on 'Process' ")
        pdfs = st.file_uploader(
            "Drag and drop files here",
            accept_multiple_files=True,
            type=["pdf"],
        )
        process_btn = st.button("Process")
        if process_btn:
            with st.spinner("Processing"):
                # get the pdf
                pdf_list = generate_pdf_list(pdfs)
                directory = get_directory(pdf_list)
                data = load(directory)
                delete_temp_file(pdf_list)

                # split text chunks
                text_chunk = split_text(data)

                # Initaite Embedding Model
                embedding = text_embedding()

                # save to vectordb
                vectordb = load_vectordb(data, embedding, "db")
                retriever = vectordb.as_retriever()

                # Make a chain to connect the retriver and llm
                turbo_llm = ChatOpenAI(
                    temperature=0,
                    model_name="gpt-3.5-turbo",
                    openai_api_key="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",
                )
                # memory = ConversationSummaryMemory(
                #     llm=llm, memory_key="chat_history", return_messages=True
                # )

                template = (
                    "Combine the chat history and follow up question into "
                    "a standalone question. Chat History: {chat_history}"
                    "Follow up question: {question}"
                )
                prompt = PromptTemplate.from_template(template)

                qa = RetrievalQA.from_chain_type(
                    llm=turbo_llm,
                    retriever=retriever,
                    return_source_documents=True,
                    chain_type="stuff",
                )
                print(qa)


if __name__ == "__main__":
    main()
