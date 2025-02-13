# config.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings



# Paths
DB_FAISS_PATH = "vectorstores/db_faiss"
CHATBOT_DATA_PATH = "chatbot_data.csv"
APPOINTMENTS_CSV_PATH = "appointments.csv"

# Token and model settings
MAX_TOKENS_PER_RESPONSE = 100
MAX_SESSION_TOKENS = 2000
SEARCH_DOCS=5

# Ollama API settings
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Common keywords for intent recognition
INSURANCE_KEYWORDS = ["insurance", "policy", "claim", "premium", "coverage", "deductible", "beneficiary", "health", "life", "vehicle"]
BOOKING_KEYWORDS = ["appointment", "book", "schedule", "meeting"]
GREETINGS = ["hi", "hello", "hey", "good morning", "good evening", "good afternoon"]

# Custom prompt template
CUSTOM_PROMPT_TEMPLATE = """
You are ADA, an assistant helping people in the insurance sector. You must strictly follow these instructions:
1. Only use the provided context to answer the user's questions.
2. If the answer to the question is not in the context provided, reply: "I don't know the answer."
3. Never provide answers based on information outside of the context.
4. Greet user responses.
5. Hold conversation as if you are an insurance agent.
6. Keep responses direct and avoid extra phrases.

Context: {context}
Question: {question}
Strictly relevant answer:
"""


# Statement constants

USER_NAME_STR="Please enter your full name: "
CONTACT_INFO_STR="Please provide your contact information (phone/email): "
APPOINTMENT_DATE_STR="Preferred date for the appointment (YYYY-MM-DD): "
PREFERRED_TIME_STR="Preferred time for the appointment (HH:MM): "

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local(DB_FAISS_PATH, embeddings)