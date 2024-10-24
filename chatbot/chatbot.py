from time import sleep
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from config import get_llm

def chat_with_csv(question:str, retriever)->str:
    
    chat_prompt_template="""
        You are a helpful assistant that can analyze and answer questions based on CSV data. I will provide you with a CSV file's contents, and you need to interpret the data, extract relevant information, and answer any questions I may have.

            Here's the CSV data:
                {CONTEXT}

            Please respond to the following questions based on this data:
                {QUESTION}

        If you need any clarification on the questions, feel free to ask!
        If you don't know the answer, say that you don't know.
    """

    chat_prompt = ChatPromptTemplate.from_template(chat_prompt_template)
    
    chat_chain = (
        {"CONTEXT": retriever, "QUESTION":RunnablePassthrough()} |
        chat_prompt |
        get_llm() |
        StrOutputParser()
    )
    
    answer=chat_chain.invoke({"QUESTION" : question})
    
    return answer

    
def stream_text(text:str, delay=0.05):
    for word in text.split(" "):
        yield word + " "
        sleep(delay)
        
        

