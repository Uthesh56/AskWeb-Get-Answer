import streamlit as Stream
from Stream.Fetch_Url import FetUrl
from Stream.Get_Data import GetData
from Models.Result import Embeddings
import time


def Main():
    Stream.set_page_config(page_title="AskWeb", page_icon="🔍", layout="centered")
    Stream.title("🔍 AskWeb: Get Instant Answers")
    Place = Stream.empty()
    Fetch = FetUrl()
    Process_Urls = Stream.sidebar.button("Process URLs")
    Query = Stream.text_input("Enter Question:")

    if Process_Urls:
        Place.text("Fetching URL'S✅")
        time.sleep(2)
        Place.text("Data Loaded Sucessfully✅")
        time.sleep(2)
        Place.text("Fetching Models✅")
        time.sleep(2)
        Place.text("Split Started✅")
        time.sleep(2)
        Place.text("Embeddings Started✅")
        time.sleep(2)
        Place.text("Fetching Relevant Documents✅")
        time.sleep(2)

        FetchData = GetData(Fetch)
        Resulted_Query = Embeddings(Query, FetchData)


        Stream.subheader("Answer:")
        Stream.write(Resulted_Query["answer"])
        
        Stream.subheader("Sources:")
        Stream.write(Resulted_Query["source"])
    
if __name__ == "__main__":
    Main()