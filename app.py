"""
Streamlit app for AI-powered financial analysis.
"""
import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from src.extraction import extract_text_from_pdf
from src.agent import create_financial_agent

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="AI Financial Analyst",
    page_icon="💼",
    layout="wide"
)

def check_api_key():
    """Check if GROQ API key is available and prompt if not."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter your GROQ API Key:", type="password")
        if api_key:
            os.environ["GROQ_API_KEY"] = api_key
            return True
        return False
    return True

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = None
    if "agent" not in st.session_state:
        st.session_state.agent = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "pdf_name" not in st.session_state:
        st.session_state.pdf_name = None

def main():
    """Main function to run the Streamlit app."""
    # Initialize session state
    initialize_session_state()
    
    # Title and description
    st.title("💼 AI Financial Analyst")
    st.markdown("Upload a financial PDF report and ask questions about it.")
    
    # Check for API key
    if not check_api_key():
        st.warning("Please enter your GROQ API key to continue.")
        return
    
    # Sidebar for PDF upload
    with st.sidebar:
        st.header("Upload Financial Report")
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
        
        if uploaded_file is not None and (st.session_state.pdf_name != uploaded_file.name):
            st.session_state.pdf_name = uploaded_file.name
            
            # Reset chat history when a new PDF is uploaded
            st.session_state.chat_history = []
            
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                pdf_path = tmp_file.name
            
            # Extract text from PDF
            with st.spinner("Extracting text from PDF..."):
                pdf_text = extract_text_from_pdf(pdf_path)
                
                # Check if extraction was successful
                if pdf_text.startswith("Failed to extract") or pdf_text.startswith("Extraction failed"):
                    st.error(f"⚠️ {pdf_text}")
                    st.warning("Please upload a text-based PDF file. If your PDF is scanned or image-based, it may not work properly.")
                    st.session_state.pdf_text = None
                    st.session_state.agent = None
                else:
                    st.success("Successfully extracted text from PDF.")
                    st.session_state.pdf_text = pdf_text
                    
                    # Create financial analysis agent
                    with st.spinner("Initializing AI financial analyst..."):
                        st.session_state.agent = create_financial_agent(pdf_text)
                    
                    st.success("AI Financial Analyst is ready!")
            
            # Clean up the temporary file
            os.unlink(pdf_path)
    
    # Main area for chat interface
    if st.session_state.pdf_text is None:
        st.info("Please upload a PDF file to start analyzing.")
    else:
        # Display chat history
        for i, (query, response) in enumerate(st.session_state.chat_history):
            with st.chat_message("user"):
                st.write(query)
            with st.chat_message("assistant"):
                st.write(response)
        
        # Chat input
        user_query = st.chat_input("What would you like to know about the report?")
        
        if user_query:
            # Add user query to chat
            with st.chat_message("user"):
                st.write(user_query)
            
            # Get response from agent
            with st.chat_message("assistant"):
                with st.spinner("Analyzing..."):
                    response = st.session_state.agent.run(user_query)
                st.write(response)
            
            # Add to chat history
            st.session_state.chat_history.append((user_query, response))

if __name__ == "__main__":
    main()
