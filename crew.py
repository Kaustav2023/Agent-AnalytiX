"""
Multi-agent research crew orchestration
"""
from crewai import Crew, Process
from agent import researcher, summarizer, strategist, presenter
from tasks import research_task, summarize_task, strategy_task, presentation_task
import os
from dotenv import load_dotenv

load_dotenv()

def run_research_analysis(topic: str) -> dict:
    """
    Execute multi-agent research analysis
    
    Args:
        topic (str): Research topic to analyze
        
    Returns:
        dict: Results from all agents including final presentation
    """
    
    # Create research crew
    crew = Crew(
        agents=[researcher, summarizer, strategist, presenter],
        tasks=[research_task, summarize_task, strategy_task, presentation_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        verbose=True
    )
    
    print(f"\n{'='*80}")
    print(f"🚀 Starting Multi-Agent Research Analysis")
    print(f"📊 Topic: {topic}")
    print(f"{'='*80}\n")
    print("🤖 Agents Working:")
    print("  1. 🔍 Researcher - Gathering web data...")
    print("  2. 📝 Summarizer - Distilling insights...")
    print("  3. 💡 Strategist - Analyzing strategy...")
    print("  4. 📊 Presenter - Creating presentation...")
    print(f"{'='*80}\n")
    
    try:
        # Execute crew
        result = crew.kickoff(inputs={'topic': topic})
        
        print(f"\n{'='*80}")
        print("✅ ANALYSIS COMPLETE!")
        print(f"{'='*80}\n")
        print(f"📄 Full report saved to: research_output.md\n")
        
        return {
            'status': 'success',
            'result': str(result),  # Convert to string
            'output_file': 'research_output.md'
        }
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            'status': 'error',
            'error': str(e),
            'result': None
        }

if __name__ == "__main__":
    # Example usage for testing
    topic = "AI Agents Market Trends 2025"
    result_dict = run_research_analysis(topic)
    
    if result_dict['status'] == 'success':
        print("\n✅ SUCCESS!")
        print(result_dict['result'])
    else:
        print(f"\n❌ ERROR: {result_dict['error']}")
