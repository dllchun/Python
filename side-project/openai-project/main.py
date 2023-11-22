import streamlit as st
import os
from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def generate_pdf_list(pdfs):
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


def get_directory(pdf_list):
    directory = os.path.dirname(pdf_list[0])
    return directory


def load(directory):
    loader = PyPDFDirectoryLoader(directory)
    data = loader.load_and_split()
    return data


def delete_temp_file(temp_path):
    for i in temp_path:
        os.remove(i)


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
            # accept_multiple_files=True,
        )
        process_btn = st.button("Process")

        if process_btn:
            with st.spinner("Processing"):
                # get the pdf
                pdf_list = generate_pdf_list(pdfs)
                directory = get_directory(pdf_list)
                # print(directory)
                data = load(directory)
                delete_temp_file(pdf_list)
                st.write(data)
                # split text chunks

                # text_splitter = RecursiveCharacterTextSplitter(
                #     chunk_size=1000, chunk_overlap=200
                # )
                # text_chunk = text_splitter.create_documents(data)
                # st.write(text_chunk)

            # save to vectordb


if __name__ == "__main__":
    main()
