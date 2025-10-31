"""
Multi-agent research team configuration
"""
from crewai import Agent
from tools import search_tool
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Configure via environment variables (most reliable)
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Agent 1: Researcher (no explicit llm - uses GROQ_API_KEY from env)
researcher = Agent(
    role='Senior Market Researcher',
    goal='Gather comprehensive and current data about {topic} from the web',
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned market researcher with 15 years of experience in "
        "gathering and validating business intelligence. You excel at finding "
        "credible sources, identifying trends, and collecting comprehensive data "
        "from across the web."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Agent 2: Summarizer
summarizer = Agent(
    role='Data Analyst & Summarizer',
    goal='Distill complex research data into clear, actionable insights about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a data analyst with expertise in information synthesis. "
        "You excel at identifying key patterns and presenting information clearly."
    ),
    allow_delegation=False
)

# Agent 3: Strategist
strategist = Agent(
    role='Business Strategist',
    goal='Provide strategic analysis, pros/cons, and actionable recommendations for {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a strategic business consultant with 20 years of experience "
        "advising Fortune 500 companies. You excel at SWOT analysis and "
        "providing clear, actionable recommendations."
    ),
    allow_delegation=False
)

# Agent 4: Presenter
presenter = Agent(
    role='Executive Presenter',
    goal='Create compelling, executive-ready presentations about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a presentation specialist who creates executive briefings. "
        "You structure information for maximum impact and communicate "
        "complex ideas clearly."
    ),
    allow_delegation=False
)
