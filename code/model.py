from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def get_model():
    load_dotenv("./keys.env")
    groq_key=os.getenv("GROQ_API_KEY")
    llm=ChatGroq(
        model_name="llama-3.1-70b-versatile",
        groq_api_key=groq_key,
        temperature=0,
        max_tokens=1000,
        timeout=None,
        max_retries=2
    )
    
    return llm

def extract_prompt(cleaned_text,llm):
    prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):
        """
    )
    chain_extract = prompt_extract | llm
    res = chain_extract.invoke(input={"page_data": cleaned_text})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(res.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res if isinstance(res, list) else [res]