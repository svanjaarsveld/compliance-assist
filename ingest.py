from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma 
import os 
from constants import CHROMA_SETTINGS

persist_directory = "db"

def loadDocs():
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                loader = PDFMinerLoader(os.path.join(root, file))
                
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, 
                                                   chunk_overlap=50)
    
    texts = text_splitter.split_documents(documents)
    
    # Create embeddings here
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create vector store here
    db = Chroma.from_documents(texts, 
                               embeddings, 
                               persist_directory=persist_directory, 
                               client_settings=CHROMA_SETTINGS
                               )
    
    db.persist()
    db=None
    
    return True
