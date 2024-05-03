import os
from apikey import apiKey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apiKey

st.title ("Q and A with a Vegan Cooking Blog")
prompt = st.text_input("Ask anything")

# Load Open AI

# Scrape the Blog

# Load it in Vector Database

# Retrieval and Generation
 
# Build the LangChain to respond to user's question based on the blog data

# Tune it more