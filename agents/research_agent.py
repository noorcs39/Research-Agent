from crewai import Agent
from langchain.llms import Ollama
from tools.web_search_tool import WebSearchTool

# Use local LLaMA 3 model running in Ollama
llm = Ollama(model="llama3")

def create_research_agent():
    return Agent(
        role="Research Expert",
        goal="Research the given topic in detail using reliable sources",
        backstory="A seasoned AI researcher equipped with local LLMs and research tools.",
        tools=[WebSearchTool()],
        llm=llm,
        verbose=True
    )
