qa_template1 = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""
qa_template2 = """You are a helpful assistant. 
When the user asks a quest, you will only return the helpful answer and nothing else.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Question: {question}
Helpful answer:
"""
