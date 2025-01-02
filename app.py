import streamlit as st
from streamlit_extras.colored_header import colored_header
import parse
import generate
from parse import get_pdf_text
from generate import get_gemini_response


# Set page configuration
st.set_page_config(
    page_title="Page Turner",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
            background-color: #FF4B4B;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #f0f2f6;
        }
        .success-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #D4EDDA;
            color: #155724;
        }
        .error-message {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #F8D7DA;
            color: #721C24;
        }
    </style>
""", unsafe_allow_html=True)

# Main content area
colored_header(
    label="Page Turner",
    description="Upload your PDFs and start a conversation with your documents",
    color_name="red-70"
)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat interface
with st.container():
    user_question = st.text_input(
        "Ask a question about your documents",
        placeholder="What would you like to know about your PDFs?",
        disabled=not st.session_state.get('files_processed', False)
    )

    if user_question:
        with st.spinner('Processing your question...'):
            reply = get_gemini_response(user_question)
            st.session_state.chat_history.append(("You", user_question))
            st.session_state.chat_history.append(("Assistant", reply))

    # Display chat history
    st.markdown("### Conversation History")
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Assistant:** {message}")

# Sidebar for file upload and processing
with st.sidebar:
    st.markdown("### Upload Documents")
    
    uploaded_files = st.file_uploader(
        "Upload your PDF files",
        type=['pdf'],
        accept_multiple_files=False,
        help="You can upload multiple PDF files"
    )

    col1, col2 = st.columns(2)
    with col1:
        start_button = st.button("Process Files", use_container_width=True)
    with col2:
        clear_button = st.button("Clear Chat", use_container_width=True)

    if start_button and uploaded_files:
        with st.spinner('Processing your documents...'):
            try:
                st.session_state.pdf_text = get_pdf_text(uploaded_files)
                # st.session_state.files_processed = True
                st.session_state.files_processed = True
                st.markdown(
                    '<div class="success-message">✅ Documents processed successfully!</div>',
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.markdown(
                    f'<div class="error-message">❌ Error processing documents: {str(e)}</div>',
                    unsafe_allow_html=True
                )
    
    elif start_button and not uploaded_files:
        st.markdown(
            '<div class="error-message">⚠️ Please upload PDF files first</div>',
            unsafe_allow_html=True
        )

    if clear_button:
        st.session_state.chat_history = []
        st.session_state.files_processed = False
        st.rerun()

    # Display file information
    if uploaded_files:
        st.markdown("### Uploaded Files")
        # for file in uploaded_files:
        #     st.markdown(f"📄 {file.name}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with Streamlit • PDF Chat Assistant"
    "</div>",
    unsafe_allow_html=True
)