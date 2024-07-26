from crewai import Process, Crew
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Forming the Tech focused Crew
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,

)

# Staring the Execution
result = crew.kickoff(inputs={'topic': 'AI in Healthcare'})
print(result)
