import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from data_cleaning import clean_text

chain = Chain()
portfolio = Portfolio()
st.set_page_config( page_title="Cold Email Generator", page_icon="📧")


st.title("📧 ColdComposeAI")
url_input = st.text_input("Enter a URL:")
submit_button = st.button("Submit")

if submit_button:
    try:
        loader = WebBaseLoader([url_input])
        data = clean_text(loader.load().pop().page_content)
        portfolio.load_portfolio()
        jobs = chain.extract_jobs(data)
        for job in jobs:
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            email = chain.write_mail(job, links)
            st.code(email, language='markdown')
    except Exception as e:
        st.error(f"An Error Occurred: {e}")
