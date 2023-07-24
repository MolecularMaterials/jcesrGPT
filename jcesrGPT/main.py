import argparse
import timeit
from utils import setup_dbqa
from prompts import qa_template1, qa_template2
import sys

if __name__ == "__main__":
    query = None
    chat_history = []
    while True:    
        if not query:
            query = input("Enter a question: ")
        if query in ['quit', 'q', 'exit']:
            sys.exit()
        #parser = argparse.ArgumentParser()
        #parser.add_argument('input', type=str)
        #args = parser.parse_args()
        start = timeit.default_timer() # Start timer

        # Setup QA object
        dbqa = setup_dbqa(qa_template=qa_template1)
        
        # Parse input from argparse into QA object
        #response = dbqa({'query': args.input})
        #response = dbqa({'query': query})
        response = dbqa({'question': query, 'chat_history': chat_history})
        chat_history.append((query,response['answer']))
        print(chat_history)
        end = timeit.default_timer() # End timer

        # Print document QA response
        print(f'\nAnswer: {response["answer"]}') #result
        print('='*50) # Formatting separator

        # Process source documents for better display
        source_docs = response['source_documents']
        for i, doc in enumerate(source_docs):
            #print(f'\nSource Document {i+1}\n')
            #print(f'Source Text: {doc.page_content}')
            print(f'Document Name: {doc.metadata["source"]}')
            #print(f'Page Number: {doc.metadata["page"]}\n')
            #print('='* 50) # Formatting separator
            
        # Display time taken for CPU inference
        print(f"Time to retrieve response: {end - start}")
        query = None