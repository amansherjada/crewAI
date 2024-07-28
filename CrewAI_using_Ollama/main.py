from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
import os

os.environ['OPENAI_API_KEY'] = "sk-proj-12121"

llm = Ollama(
    model = "llama3",
    base_url = "http://localhost:11434")

info_agent = Agent(
    role = "Information Agent",
    goal = "Give compelling information about certain topic",
    backstory = """
    You love to know information. People love and hate you for it.
    You are a winner
    """,
    llm = llm
)

task1 = Task(
    description="Tell me all about the UFC.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose = 2
)

result = crew.kickoff()

print("########################################")
print(result)