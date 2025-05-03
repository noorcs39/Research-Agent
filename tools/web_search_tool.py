from langchain.tools import Tool

def WebSearchTool():
    return Tool.from_function(
        func=lambda query: f"Mocked web search result for: {query}",
        name="Web Search Tool",
        description="Searches the web and returns relevant text"
    )
