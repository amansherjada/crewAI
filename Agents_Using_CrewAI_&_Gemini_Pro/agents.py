from langchain_google_genai import ChatGoogleGenerativeAI
import os
from crewai import Agent
from dotenv import load_dotenv
from tools import tool
load_dotenv()

# Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv('GOOGLE_API_KEY')
                             )

# Creating a Senior Researcher Agent with memory and verbose mode
# - 'role' defines the agent's function.
# - 'goal' describes the agent's objective.
# - 'verbose' enables detailed logging.
# - 'memory' allows the agent to retain information across interactions.
# - 'backstory' provides context about the agent's background and expertise.
# - 'tools' lists the tools the agent can use (e.g., custom tool).
# - 'llm' specifies the language model to use for generating responses.
# - 'allow_delegation' enables the agent to delegate tasks if necessary.

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "As a distinguished Senior Researcher with a passion for exploring the frontiers of technology, this agent is driven by a relentless curiosity and an insatiable quest for innovation."
        "With a wealth of experience in uncovering groundbreaking technologies, they have built a reputation for pushing boundaries and challenging conventional wisdom"
        "Their journey began in a cutting-edge lab, where they pioneered advancements in various fields"
        "Now, they are dedicated to exploring new horizons and unlocking the next big breakthroughs in {topic}. Armed with a sharp intellect, a deep understanding of emerging trends, and a memory that retains valuable insights, they are committed to driving the future of technology forward"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a Writer Agent with with custom tools responsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling Tech Stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "Engaging narratives that captivate and educate, bringing new"
        "Discoveries to light an accessiable manner"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
