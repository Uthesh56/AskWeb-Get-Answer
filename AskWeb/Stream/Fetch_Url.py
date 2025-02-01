import streamlit as Stream

def FetUrl():
    Urls = []
    Stream.sidebar.header("Enter URLs")
    for i in range(2):
        Link = Stream.sidebar.text_input(f"URL {i + 1}")
        Urls.append(Link)
    return Urls