"""
Research tools for multi-agent system
"""
from crewai_tools import SerperDevTool

# Web search tool for real-time data
search_tool = SerperDevTool(
    n_results=10,  # Number of search results to fetch
)
