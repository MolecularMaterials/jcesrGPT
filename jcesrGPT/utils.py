from langchain import PromptTemplate
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.vectorstores import Chroma, FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from prompts import qa_template1, qa_template2
from llm import llm

# Wrap prompt template in a PromptTemplate object
def set_qa_prompt(qa_template=qa_template1):
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context', 'question'])
                            #input_variables=['question'])
    return prompt


# Build RetrievalQA object
def build_retrieval_qa(llm, prompt, vectordb):
#    dbqa = RetrievalQA.from_chain_type(llm=llm,
#                                       chain_type='stuff',
#                                       retriever=vectordb.as_retriever(search_kwargs={'k': 3}),
#                                       return_source_documents=True,
#                                       chain_type_kwargs={'prompt': prompt})
    
    dbqa = ConversationalRetrievalChain.from_llm(llm=llm,
                                       chain_type='stuff',
                                       retriever=vectordb.as_retriever(search_type='similarity', search_kwargs={'k': 3}),
                                       return_source_documents=True)                                       
    return dbqa

# Instantiate QA object
def setup_dbqa(qa_template=qa_template1):
    #embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
    #                                   model_kwargs={'device': 'cpu'})
    #vectorstore = FAISS.load_local('../vectorstore/db_jcesr', embeddings)
    vectorstore = Chroma(embedding_function=OpenAIEmbeddings(),
    		             persist_directory='../vectorstore/db_jcesr')
    qa_prompt = set_qa_prompt(qa_template)
    dbqa = build_retrieval_qa(llm, qa_prompt, vectorstore)

    return dbqa
