from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.vectorstores import Chroma, FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings

# Load PDF file from data path
loader = DirectoryLoader('../docs/',
                         glob="*.pdf",
                         loader_cls=PyPDFLoader)
documents = loader.load()

# Split text from PDF into chunks
text_splitter = CharacterTextSplitter(chunk_size=500,
                                      chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Load embeddings from HuggingFace
#embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
#                                 model_kwargs={'device': 'cpu'})
# Build and persist vector storage using FAISS
#vectorstore = FAISS.from_documents(texts, embeddings)
#vectorstore.save_local('../vectorstore/db_jcesr')

# Build and persist vector storage using Chroma
vectorstore = Chroma.from_documents(texts,
                                    embedding=OpenAIEmbeddings(),
                                    persist_directory='../vectorstore/db_jcesr')
vectorstore.persist()