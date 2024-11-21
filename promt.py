from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks , embedding = embeddings)
    vector_store.save_local("Faiss_context")
    
def get_conversation_chain():
    promt_temp = '''
    Context Information:
    ====================
    {context}

    Based on the context information provided, please respond to the following question:

    Question:
    =========
    {question}

    Guidelines:
        1. Use only the information contained within the context to answer the question.
        2. If the answer is not present in the context, clearly state:
        "I’m sorry, I cannot provide the answer as it is not available within the context provided."

    '''
    model = ChatGoogleGenerativeAI(model= "gemini-pro" , temperature= 0.5)
    
    prompt = PromptTemplate(template= promt_temp , input_variables=['context','question'])
    chain = load_qa_chain(model , chain_type="stuff" , prompt = prompt )
    
    return chain

def user_input(User_questions):
    embedding = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("Faiss_context" , embedding , allow_dangerous_deserialization= True)
    docs = new_db.similarity_search(User_questions)
    
    chain = get_conversation_chain()
    
    responce = chain(
       {"input_document" :docs , "question":User_questions},
       return_only_outputs=True 
    )
    
    print(responce)
    return responce['output_text']
    
    
    
    
    
    
    