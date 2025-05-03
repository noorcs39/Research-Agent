from crew import build_crew

if __name__ == "__main__":
    topic = "Latest breakthroughs in AI safety research"
    crew = build_crew(topic)
    result = crew.kickoff()
    print("\nFinal Result:\n", result)
