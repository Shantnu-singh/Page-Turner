import streamlit as st
import parse
import generate
import promt


st.title("Chat with Pdf")
st.markdown("you can see magic of chatting with your text here...")

user_question = st.text_input("Enter your question regarding pdfs")

if user_question:
    reply = promt.user_input(user_question)
    st.write(f"Reply: " , reply)

with st.sidebar:
    
    files = st.file_uploader("Enter you pdf(s) here" , type = ['pdf'] , accept_multiple_files=True)
    starButton = st.button("Start your chat..")
    if starButton:
        if files:
            text = parse.get_pdf_text(files)
            text_chunks = parse.get_chunks(text)
            promt.get_vector_store(text_chunks)
            # st.markdown("<h2>This is the text</h2>" , unsafe_allow_html= True)
            # st.markdown(text)
            st.success("Documents uploaded sucessfully.....")
            
        else:
            st.error("Plzzz upload your files here..")
        