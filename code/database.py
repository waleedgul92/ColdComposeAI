import chromadb
from langchain_community.document_loaders import WebBaseLoader
import pandas as pd
import uuid


def get_data_from_url(url):
    loader=WebBaseLoader(url)
    page_data=loader.load().pop().page_content
    return page_data


class Portfolio:
    def __init__(self, file_path="Data/portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

# text=get_data_from_pdf("Data/Waleed_Data_Scientist_Resume.pdf")
# print(text)