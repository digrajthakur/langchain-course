from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Search the internet for current information.
    """

    print(f"\nSearching: {query}\n")

    result = tavily.search(
        query=query,
        max_results=3
    )

    return str(result)

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

agent = create_agent(
    model=llm,
    tools=[search]
)

def main():
    print("Hello from langchain-course!")

    result = agent.invoke({
        "messages": [
            HumanMessage(
                content="Use the search tool and tell me today's weather in Tokyo"
            )
        ]
    })

    print("\nFinal Response:\n")
    print(result)

if __name__ == "__main__":
    main()




# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# import os

# load_dotenv()

# def main():

#     print("Hello from langchain-course!")

   
#     if not os.getenv("OPENAI_API_KEY"):
#       raise ValueError("OPENAI_API_KEY are not found")

#     print("OPENAI API KEY LOADED SUCCESSFULLY")

#     information = """
#     LangChain is a software framework that helps facilitate the integration of large language models (LLMs) into applications. 
#     As a language model integration framework, LangChain's use-cases largely overlap with those of language models in general, 
#     including document analysis and summarization, chatbots, and code analysis.
#     """


#     summary_template = """
#     give me the information {information} about the model I want you to create:
#     1. A short summary
#     2. Two interesting facts about the model
#     """

#     summary_prompt_template = PromptTemplate(
#         input_variables=["information"],
#         template=summary_template,
#     )

#     llm = ChatOpenAI(temperature=0, model="gpt-5")


#     chain = summary_prompt_template | llm

#     response = chain.invoke(input={"information": information})


#     print(response.content)


# if __name__ == "__main__":
#     main()




    