# AI-Powered Financial Analyst

![Financial Analyst](https://img.shields.io/badge/AI-Financial%20Analyst-blue)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![Groq](https://img.shields.io/badge/Groq-LLama--3-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Interface-red)

A powerful AI-driven tool that analyzes financial reports from PDF files using LangChain with Groq's LLM. This application extracts text from financial PDFs and provides intelligent analysis through a conversational interface, making complex financial data more accessible and understandable.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

The AI-Powered Financial Analyst is designed to help users quickly extract insights from financial reports. By leveraging the power of Large Language Models (specifically Groq's LLama-3), the application can understand complex financial documents and answer questions about them in natural language.

## ✨ Features

- **Efficient PDF Text Extraction**: Quickly extracts text from PDF financial reports
- **Advanced Financial Analysis**: Powered by Groq's LLama-3 model (70B parameters)
- **Conversational AI Agent**: Interact with your financial data through natural language
- **Memory Capabilities**: The AI remembers context from your conversation
- **User-Friendly Interface**: Streamlit web interface for easy interaction
- **PDF Upload**: Easily upload PDF files through the web interface
- **Chat History**: View and track your conversation with the AI analyst
- **Error Handling**: Clear messages for non-text PDFs and extraction issues

## 💻 System Requirements

- Python 3.8 or higher
- Internet connection (for API calls to Groq)
- 100MB+ of free disk space
- Modern web browser (for Streamlit interface)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI_powered_financial_analyst.git
   cd AI_powered_financial_analyst
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   Create a `.env` file in the root directory with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   You can obtain a Groq API key by signing up at [https://console.groq.com/](https://console.groq.com/)

## 🚀 Usage

1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Your default web browser will open automatically with the application
3. Use the sidebar to upload a financial PDF report
4. Once the PDF is processed, you can ask questions in the chat interface
5. Your conversation history will be displayed in the main area

## 📁 Project Structure

```
.
├── app.py                 # Streamlit web interface
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
└── src/                   # Source code
    ├── agent.py           # LangChain agent implementation
    ├── extraction.py      # PDF text extraction functions
    └── models.py          # LLM model configuration
```

## ⚙️ How It Works

1. **PDF Processing**: The application extracts text from the uploaded PDF using PyMuPDF (fitz)
2. **LLM Integration**: The extracted text is processed by Groq's LLama-3 model via LangChain
3. **Agent Creation**: A conversational agent is created with the financial report context
4. **User Interaction**: Users can ask questions about the report in natural language
5. **Response Generation**: The AI analyzes the report and generates informative responses

## ❓ Troubleshooting

- **API Key Issues**: Ensure your Groq API key is correctly set in the `.env` file
- **PDF Extraction Errors**: Make sure your PDF is text-based and not scanned/image-based
- **Model Responses**: If responses are incomplete, the PDF might be too large; try with a smaller document
- **Memory Issues**: For very large reports, the system might need more memory; consider splitting the PDF

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
