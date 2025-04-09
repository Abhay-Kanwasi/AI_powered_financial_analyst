"""
Main script for AI-powered financial analysis.
"""
import os
from dotenv import load_dotenv
from src.extraction import extract_text_from_pdf
from src.agent import create_financial_agent
from src.utils import get_pdf_path

# Load environment variables
load_dotenv()

def main():
    """
    Main function to run the financial analysis pipeline.
    """
    # Check for API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        api_key = input("Enter your GROQ API Key: ")
        os.environ["GROQ_API_KEY"] = api_key

    # Get PDF path from user if not specified
    pdf_path = get_pdf_path()

    # Extract text from PDF
    print(f"Extracting text from {pdf_path}...")
    pdf_text = extract_text_from_pdf(pdf_path)

    # Check if extraction was successful
    if pdf_text.startswith("Failed to extract") or pdf_text.startswith("Extraction failed"):
        print(f"\n⚠️ WARNING: {pdf_text}")
        proceed = input("\nProceed with analysis anyway? (y/n): ")
        if proceed.lower() != 'y':
            print("Exiting.")
            return
    else:
        print(f"Successfully extracted text from PDF.")

    # Create financial analysis agent
    print("Initializing AI financial analyst...")
    agent = create_financial_agent(pdf_text)

    # Interactive mode
    print("\n========== AI Financial Analyst ==========")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nWhat would you like to know about the report? ")
        if query.lower() in ["exit", "quit"]:
            break

        response = agent.run(query)
        print("\nAnalysis:")
        print(response)

if __name__ == "__main__":
    main()