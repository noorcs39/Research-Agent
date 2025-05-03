from crewai import Task, Crew
from agents.research_agent import create_research_agent

def build_crew(topic: str):
    agent = create_research_agent()

    task = Task(
        description=f"Summarize key trends in: {topic}",
        agent=agent,
        expected_output="A short summary of key findings.",
        async_execution=False
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    return crew
