"""
Functions for creating and managing the financial analyst agent.
"""
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from .models import get_chat_model
from config import MAX_CHARS

def create_financial_agent(pdf_text):
    """
    Creates a LangChain agent for financial analysis.

    Args:
        pdf_text (str): The extracted text from the financial report

    Returns:
        Agent: A LangChain agent configured for financial analysis
    """
    # Initialize chat model
    chat_model = get_chat_model()

    # Set up memory for context retention
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create financial report analysis tool
    def analyze_financial_report(_):
        """Analyzes financial data from a report."""
        prompt = f"""
        You are a financial analyst. Analyze the following financial report text and provide insights:

        {pdf_text[:MAX_CHARS]}  # Limit input to fit model constraints
        """
        response = chat_model.invoke(prompt)
        return response.content

    pdf_tool = Tool(
        name="Financial Report Analysis",
        func=analyze_financial_report,
        description="Extracts and analyzes key financial data from reports."
    )

    # Initialize agent
    agent = initialize_agent(
        agent="chat-conversational-react-description",
        tools=[pdf_tool],
        llm=chat_model,
        memory=memory,
        verbose=False
    )

    return agent
