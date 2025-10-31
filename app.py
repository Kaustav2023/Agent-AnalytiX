"""
Streamlit Dashboard for Multi-Agent Research Analyst
"""
import streamlit as st
import os
from crew import run_research_analysis
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title="AI Research Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Full Black Theme CSS
st.markdown("""
    <style>
    /* Root app container - PURE BLACK */
    .stApp {
        background-color: #000000 !important;
    }
    
    /* Main content area - PURE BLACK */
    .main {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Block container - PURE BLACK (removes white box) */
    .block-container {
        background-color: #000000 !important;
        padding: 2rem 3rem !important;
        max-width: 100% !important;
    }
    
    /* All paragraphs and divs - WHITE text */
    .main p, .main div, .main span, .main label {
        color: #ffffff !important;
    }
    
    /* Title - PURE WHITE */
    h1 {
        color: #fc1135 !important;
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Subtitle - Light Gray */
    h2 {
        color: #e2e8f0 !important;
        font-size: 1.5rem !important;
        font-weight: 400 !important;
    }
    
    h3 {
        color: #ffffff !important;
        font-size: 1.3rem !important;
    }
    
    /* Sidebar - Dark theme (already perfect) */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        width: 350px !important;
        min-width: 350px !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #c4b5fd !important;
        font-weight: 600 !important;
    }
    
    /* Text input - Dark with white text */
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #333333 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        padding: 0.75rem 1rem !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #666666 !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
    }
    
    /* Input label - WHITE */
    .stTextInput > label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Buttons - Purple gradient */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 0.85rem 2rem !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s !important;
        font-size: 1rem !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Success/Warning/Error boxes */
    .stSuccess {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border-left: 4px solid #10b981 !important;
        border-radius: 8px !important;
    }
    
    .stWarning {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border-left: 4px solid #f59e0b !important;
        border-radius: 8px !important;
    }
    
    .stError {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border-left: 4px solid #ef4444 !important;
        border-radius: 8px !important;
    }
    
    /* Metric cards - Dark with glowing effect */
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%) !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        text-align: center !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5) !important;
    }
    
    .metric-card h3 {
        color: #a78bfa !important;
        font-size: 2.2rem !important;
        margin: 0 !important;
    }
    
    .metric-card p {
        color: #cccccc !important;
        font-size: 0.95rem !important;
        margin: 0.5rem 0 0 0 !important;
    }
    
    /* Output box - Dark with purple glow */
    .output-box {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%) !important;
        padding: 2.5rem !important;
        border-radius: 12px !important;
        border-left: 4px solid #8b5cf6 !important;
        margin: 1.5rem 0 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2) !important;
    }
    
    .output-box * {
        color: #ffffff !important;
    }
    
    .output-box h1, .output-box h2, .output-box h3 {
        color: #c4b5fd !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    .output-box strong {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Progress bar - Purple */
    .stProgress > div > div > div {
        background-color: #8b5cf6 !important;
    }
    
    /* Progress text */
    .stMarkdown p {
        color: #ffffff !important;
    }
    
    /* Divider - Subtle gray */
    hr {
        border-color: #333333 !important;
        margin: 2rem 0 !important;
        opacity: 0.3 !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background-color: #1a1a1a !important;
        color: #a78bfa !important;
        border: 2px solid #8b5cf6 !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #8b5cf6 !important;
        color: #ffffff !important;
        border-color: #a78bfa !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #333333 !important;
    }
    
    /* Code blocks */
    .stCode, code {
        background-color: #1a1a1a !important;
        color: #a78bfa !important;
        border: 1px solid #333333 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #8b5cf6 !important;
    }
    
    /* Footer link */
    a {
        color: #a78bfa !important;
        text-decoration: none !important;
    }
    
    a:hover {
        color: #c4b5fd !important;
        text-decoration: underline !important;
    }
    
    /* Remove any default Streamlit padding/margin */
    .main .block-container {
        padding-top: 3rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🤖 Multi-Agent Research Analyst")
st.markdown("### AI-Powered Market Intelligence & Strategic Analysis")

# Sidebar
with st.sidebar:
    st.markdown("### 🔧 Configuration")
    
    # Check API keys
    groq_key = os.getenv("GROQ_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")
    
    st.markdown("#### API Status")
    col1, col2 = st.columns(2)
    with col1:
        if groq_key:
            st.success("✅ Groq")
        else:
            st.error("❌ Groq")
    with col2:
        if serper_key:
            st.success("✅ Serper")
        else:
            st.error("❌ Serper")
    
    st.markdown("---")
    st.markdown("### 🤖 Agent Team")
    st.markdown("""
    **1. 🔍 Researcher**  
    Gathers real-time web data
    
    **2. 📝 Summarizer**  
    Distills key insights
    
    **3. 💡 Strategist**  
    Provides strategic analysis
    
    **4. 📊 Presenter**  
    Creates executive report
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Example Topics")
    examples = [
        "AI Agents Market 2025",
        "Electric Vehicle Trends",
        "Cloud Computing Growth",
        "Quantum Computing Investment",
        "Sustainable Energy Market"
    ]
    
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state.topic_input = ex

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input(
        "🔍 Enter Research Topic",
        placeholder="e.g., AI Agents Market Trends 2025",
        value=st.session_state.get('topic_input', ''),
        help="Enter any business, technology, or market topic"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_button = st.button("🚀 Start Analysis", use_container_width=True)

# Analysis execution
if analyze_button and topic:
    if not (groq_key and serper_key):
        st.error("⚠️ Missing API keys! Please add them to your .env file.")
    else:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        statuses = [
            "🔍 Researcher gathering web data...",
            "📝 Summarizer processing insights...",
            "💡 Strategist analyzing strategy...",
            "📊 Presenter creating report..."
        ]
        
        for i, status in enumerate(statuses):
            status_text.markdown(f"**{status}**")
            progress_bar.progress((i + 1) * 20)
            time.sleep(0.5)
        
        status_text.markdown("**🤖 Running multi-agent analysis...**")
        
        # Run actual analysis
        result = run_research_analysis(topic)
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        if result['status'] == 'success':
            st.success("🎉 Research Analysis Complete!")
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown('<div class="metric-card"><h3>4</h3><p>AI Agents</p></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="metric-card"><h3>✅</h3><p>Completed</p></div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="metric-card"><h3>🌐</h3><p>Web Data</p></div>', unsafe_allow_html=True)
            with col4:
                st.markdown(f'<div class="metric-card"><h3>{datetime.now().strftime("%H:%M")}</h3><p>Finished</p></div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Display results
            st.markdown("## 📊 Executive Report")
            
            try:
                # Try to read from file first
                if os.path.exists('research_output.md'):
                    with open('research_output.md', 'r', encoding='utf-8') as f:
                        report_content = f.read()
                else:
                    # Fallback to result content
                    report_content = result.get('result', 'No report generated')
                
                # Display in dark-themed box
                st.markdown(f'<div class="output-box">{report_content}</div>', unsafe_allow_html=True)
                
                # Download button
                st.download_button(
                    label="📥 Download Full Report",
                    data=report_content,
                    file_name=f"research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"Error displaying report: {str(e)}")
                st.code(result.get('result', 'No output available'))
        
        else:
            st.error(f"❌ Analysis failed: {result.get('error', 'Unknown error')}")
            with st.expander("🔍 Error Details"):
                st.code(result.get('error', 'No error details available'))

elif analyze_button:
    st.warning("⚠️ Please enter a research topic first!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888888; padding: 1rem;'>
        Built with CrewAI, LangChain, Groq & Streamlit | 
        <a href='https://github.com'>View on GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
