from langchain_community.llms import OpenAI

from langchain import  VectorDBQA

from langchain_community.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
class RAGModel:
    def __init__(self, documents):
        self.embeddings = OpenAIEmbeddings()
        self.db = Chroma.from_documents(documents, self.embeddings)
        self.qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=self.db)

    def query(self, question):
        return self.qa.run(question)
