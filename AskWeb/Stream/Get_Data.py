import streamlit as Stream
from langchain_community.document_loaders import UnstructuredURLLoader

def GetData(Urls):

    Loader = UnstructuredURLLoader(urls=Urls)
    Data = Loader.load()
    return Data