import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


def Embeddings(Query, Data):
    Text_Split = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '.', ','], chunk_size=1000)
    Model_Embed = SentenceTransformer('all-MiniLM-L6-v2')
    Docs = Text_Split.split_documents(Data)

    for doc in Docs:
        doc.metadata['source'] = doc.metadata.get('source', 'Unknown')

 
    Embed = Model_Embed.encode([doc.page_content for doc in Docs])
    Embed_Array = np.array(Embed)
    Embed_Query = Model_Embed.encode(Query)
    Similarities = cosine_similarity([Embed_Query], Embed_Array)[0]
    Index_Doc = np.argmax(Similarities)
    Relevant_Doc = Docs[Index_Doc]

    QA_Model = pipeline("question-answering", model="deepset/roberta-base-squad2")
    Result = QA_Model(question=Query, context=Relevant_Doc.page_content)

    Result_Source = {
        "answer": Result["answer"],
        "source": Relevant_Doc.metadata.get('source', 'Unknown')}

    return Result_Source
