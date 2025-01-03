# Page Turner : AI-Powered Document Conversation 📚💬

## Overview
PDF Chat Assistant is an intelligent document interaction tool that leverages Google's Gemini AI to enable natural conversations with your PDF documents. The application allows users to upload multiple PDFs and engage in meaningful dialogue about their content through an intuitive chat interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-green)
![Gemini](https://img.shields.io/badge/Gemini-AI-red)

## Features

- 📤 Multiple PDF Upload Support
- 💬 Interactive Chat Interface
- 🤖 AI-Powered Responses
- 📝 Conversation History
- 🎨 Professional UI/UX
- ⚡ Real-time Processing
- 🔄 Chat History Management
- 🎯 Context-Aware Responses

## Prerequisites

- Python 3.8+
- Google Gemini API Access
- Streamlit

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Shantnu-singh/page-turner
cd pdf-chat-assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirement.txt
```

## Environment Configuration

Create a `.env` file in the project root with your Google Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key for Gemini
3. Copy the API key to your `.env` file

## Running the Application

```bash
streamlit run app.py
```


## Application Structure

```
pdf-chat-assistant/
├── app.py                 # Main application file
├── .env                   # Environment variables
├── requirements.txt       # Project dependencies
└── README.md             # Documentation
```

## Core Components

### PDF Processing
- Supports multiple PDF uploads
- Extracts text content
- Maintains document context

### Chat Interface
- Real-time response generation
- Conversation history tracking
- Context-aware interactions

### AI Integration
- Powered by Google's Gemini AI
- Natural language understanding
- Contextual response generation

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Document summarization
- [x] Multiple language support
- [ ] Advanced PDF parsing options
- [ ] Custom chat themes
- [ ] Export conversation history
- [x] Document search functionality
