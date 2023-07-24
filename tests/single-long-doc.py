import os
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# load the document as before
loader = DirectoryLoader('../docs/',
			  glob='QuantumChemistry_Doan.pdf',
			  loader_cls=PyPDFLoader)
documents = loader.load()

# we split the data into chunks of 1,000 characters, with an overlap
# of 200 characters between the chunks, which helps to give better results
# and contain the context of the information between chunks

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(documents)

# we create our vectorDB, using the OpenAIEmbeddings tranformer to create
# embeddings from our text chunks. We set all the db information to be stored
# inside the ./data directory, so it doesn't clutter up our source files
vectordb = Chroma.from_documents(
  documents,
  embedding=OpenAIEmbeddings(),
  persist_directory='../vectorstore/db_test'
)
vectordb.persist()
