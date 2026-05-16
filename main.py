from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

load_dotenv()


def main():

    print("Hello from langchain-course!")

    # Check API Key
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found")

    print("OpenAI API Key Loaded Successfully")

    information = """
    LangChain is a framework for building applications powered by LLMs.
    """

    # Prompt Template
    summary_template = """
    Give me the information below:

    {information}

    Create:
    1. A short summary
    2. Two interesting facts
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # OpenAI Model
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # Chain
    chain = summary_prompt_template | llm

    # Response
    response = chain.invoke({
        "information": information
    })

    print("\nAI RESPONSE:\n")
    print(response.content)


if __name__ == "__main__":
    main()
    