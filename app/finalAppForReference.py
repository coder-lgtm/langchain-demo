# Basic
import os

# For RAG
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever


# The LLM
from langchain_openai import OpenAI

# Building LangChain for Q and A app
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.sequential import SequentialChain
from langchain.chains.llm import LLMChain
from langchain.globals import set_verbose, set_debug

# UI
import streamlit as st

# Initial setup
# You need to setup OpenAI creds here.
llm = OpenAI(temperature = 0.9) #Temperature . 0.9 means the model will respond randomly.
chain_type = 'single'

#set_debug(True)
set_verbose(True)


#
# Load PDF Documents and split them into chunks 
#
def load_documents():
    docs = []
    loaders = [PyPDFLoader("../docs/meals-more-recipes.pdf"), PyPDFLoader("../docs/comms-veg-eating-plant-based-cookbook-2021.pdf")]
    for loader in loaders:
        docs.extend(loader.load())

    r_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,
                                            chunk_overlap=100,
                                            separators=["\n\n", "\n"])

    docs_splitted = r_splitter.split_documents(docs)
    #print(docs_splitted)
    return docs_splitted  

#
# Create vector embeddings from the chunks and load those into the Vector Store. 
# We will use OpenSource Chroma DB as our vector store.
#
def create_vector_store(docs_splitted):
    vector_store = Chroma.from_documents(documents=docs_splitted,
                                     embedding = OpenAIEmbeddings(),
                                     persist_directory='vector_store/chroma/')
    
    return vector_store

# RAG based Single Chain for Q and A
def generate_ragbased_answers(vector_store, question):
    # Create Prompt
    template = '''Use shortened version of your answers for the question in the end. Keep it about a paragraph long.
    If you don't know the answer from your context, just say that you don't know. 
    Don't try to make up an answer. Use a lot of variety in your answers.
    Context: {context}

    Question: {question}
    Answer: 
    '''
    prompt = PromptTemplate(template=template, input_variables=[
        'context', 
        'question'
    ])

    retriever = VectorStoreRetriever(vectorstore=vector_store)

    chain = RetrievalQA.from_chain_type(
                llm=llm, 
                retriever=retriever,
                chain_type_kwargs={"prompt": prompt},
                output_key="recipe"
            )
    response = chain.invoke(input = {"query": question})
    return response

# Sequential Chain - RAG based Q and A followed by LLM based Youtube Script generator
def generate_ragbased_chained_answers(vector_store, question):
    # First Chain
    recipe_template = '''Use shortened version of your answers for the question in the end. Keep it about a paragraph long.
    If you don't know the answer, just say that you don't know.
    Don't try to make up an answer. Use a lot of variety in your answers {context}

    Question: {question}
    Answer: 
    '''
    prompt = PromptTemplate(template=recipe_template, input_variables=[
        'context', 
        'question'
    ])

    retriever = VectorStoreRetriever(vectorstore=vector_store, )
    etrievalQA = RetrievalQA.from_llm(llm=OpenAI(), retriever=retriever)

    recipe_chain = RetrievalQA.from_chain_type(
                llm=llm, 
                retriever=retriever,
                chain_type_kwargs={"prompt": prompt},
                output_key="recipe"
            )

    # Second Chain
    script_generator_template = """
    You are a YouTube video script creator. You are tasked
    to generate a entertaining YouTube video script given Food Recipe.
    Respond with 7 or less bullet points.

    Here is the recipe submitted to you:
    {recipe}"""

    script_prompt = PromptTemplate(
        input_variables=["recipe"],
        template = script_generator_template
    )

    script_chain = LLMChain(llm=llm, prompt=script_prompt, output_key="script_response")

    sequential_chain = SequentialChain(chains=[recipe_chain, script_chain], 
                                   input_variables=["query"],
                                   output_variables=["recipe", "script_response"]
                        )
    response = sequential_chain.invoke(question)
    return response

docs_splitted = load_documents()
vector_store = create_vector_store(docs_splitted)

# UI
st.title ("Q and A with Recipe Books")
st.caption ("This is a RAG based OpenAI Q and A aapplication that leverages the power of Generative AI. Lets ask questions! ")
recipe_text = st.empty()
script_text = st.empty()

# Option to choose Single Chain or Multiple Chains 
with st.sidebar:
    st.title('Q and A with LangChain')
    selected_model = st.sidebar.selectbox('Choose Task', ['Simple Q and A', 'Q and A with Youtube video script Generation'], key='selected_model')
    if selected_model == 'Simple Q and A':
        chain_type = 'single'
        recipe_text = st.empty()
        script_text = st.empty()
    elif selected_model == 'Q and A with Youtube video script Generation':
        chain_type = 'multi'
        recipe_text = st.empty()
        script_text = st.empty()

print(chain_type)

# Main UI area to accept the question and note the response
with st.container():
    print('init')
    if question := st.text_input(label ="Ask a question",  value = ""):
        with st.spinner("Thinking..."):
            if chain_type == 'single':
                response = generate_ragbased_answers(vector_store, question)
                recipe_text = st.text_area(label ="Recipe",  value = response.get('recipe'), height =200)
                script_text = st.empty()
            else:
                response = generate_ragbased_chained_answers(vector_store, question)
                print (response)
                recipe_text = st.text_area(label ="Recipe",  value = response.get('recipe'), height =200)
                script_text = st.text_area(label ="Script",  value = response.get('script_response'), height =200)
            