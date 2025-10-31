"""
Task definitions for research workflow
"""
from crewai import Task
from tools import search_tool
from agent import researcher, summarizer, strategist, presenter

# Task 1: Research
research_task = Task(
    description=(
        "Conduct comprehensive research on: {topic}\n\n"
        "Research Requirements:\n"
        "1. Current market trends and statistics (2024-2025)\n"
        "2. Key players and competitors\n"
        "3. Recent news and developments\n"
        "4. Industry challenges and opportunities\n"
        "5. Expert opinions and analysis\n"
        "6. Market size and growth projections\n\n"
        "Focus on credible sources and recent data."
    ),
    expected_output=(
        "Detailed research report with:\n"
        "- 10+ key findings with sources\n"
        "- Current statistics and trends\n"
        "- Major market players\n"
        "- Recent developments (last 6 months)"
    ),
    tools=[search_tool],
    agent=researcher
)

# Task 2: Summarize
summarize_task = Task(
    description=(
        "Analyze the research data and create a concise executive summary.\n\n"
        "Requirements:\n"
        "1. Extract the 5 most important insights\n"
        "2. Identify key trends and patterns\n"
        "3. Highlight critical statistics\n"
        "4. Remove redundant information\n"
        "5. Present data in clear, scannable format"
    ),
    expected_output=(
        "Executive summary with:\n"
        "- Top 5 key insights (bullet points)\n"
        "- 3 major trends\n"
        "- Critical statistics\n"
        "- Clear, concise language suitable for executives"
    ),
    agent=summarizer,
    context=[research_task]
)

# Task 3: Strategic Analysis
strategy_task = Task(
    description=(
        "Provide strategic analysis and recommendations for {topic}.\n\n"
        "Analysis Framework:\n"
        "1. SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)\n"
        "2. Competitive Landscape\n"
        "3. Risk Assessment\n"
        "4. Growth Opportunities\n"
        "5. Actionable Recommendations (3-5 specific actions)\n\n"
        "Consider both short-term (0-6 months) and long-term (1-3 years) perspectives."
    ),
    expected_output=(
        "Strategic analysis document with:\n"
        "- Complete SWOT analysis\n"
        "- Top 3 opportunities\n"
        "- Top 3 risks/challenges\n"
        "- 5 specific, actionable recommendations\n"
        "- Timeline for implementation"
    ),
    agent=strategist,
    context=[summarize_task]
)

# Task 4: Create Presentation
presentation_task = Task(
    description=(
        "Create an executive-ready presentation about {topic}.\n\n"
        "Presentation Structure:\n"
        "1. Executive Summary (1 slide equivalent)\n"
        "2. Key Findings (3-5 main points)\n"
        "3. Market Analysis (trends, statistics)\n"
        "4. Strategic Recommendations\n"
        "5. Action Items\n\n"
        "Format as structured Markdown suitable for Streamlit display.\n"
        "Use headers, bullet points, and clear sections."
    ),
    expected_output=(
        "Professional presentation in Markdown format with:\n"
        "- Clear section headers\n"
        "- Bullet-pointed insights\n"
        "- Key statistics highlighted\n"
        "- Actionable next steps\n"
        "- Executive-friendly language"
    ),
    agent=presenter,
    context=[strategy_task],
    output_file='research_output.md'
)
