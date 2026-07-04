from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding_model= GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",
                                               output_dimensionality=256)

text = "Generative AI is changing the world."

vector=embedding_model.embed_query(text)
print(vector)