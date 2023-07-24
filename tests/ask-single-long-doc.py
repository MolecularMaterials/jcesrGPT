from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectordb = Chroma(
  embedding_function=OpenAIEmbeddings(),
  persist_directory='../vectorstore/db_test'
)

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo'),
    #llm=OpenAI(temperature=0,model_name='text-davinci-003'),
    retriever=vectordb.as_retriever(search_kwargs={'k': 1}),
    return_source_documents=True
)

# we can now execute queries against our Q&A chain
result = qa_chain({'query': 'what is the title of the paper?'})
print(result['result'])

