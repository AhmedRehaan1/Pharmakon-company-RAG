# %%
import os
from dotenv import load_dotenv
load_dotenv()  #load all the environment variables

# %%
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# %%
import json
from langchain.schema import Document

# Load JSON file
with open("pharmakon_products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

#  Convert each product description into a single Document
# the embedding model will be for description, not for the whole product details , but we have metadata for each product
docs = []
for product in products:
    docs.append(Document(
        page_content=product["product_description"],  # full description in one chunk
        metadata={
            "name": product["product_name"],
            "link": product["product_link"],
            "price": product["product_price"]
        }
    ))

#  Check first document
print(docs[3])


# %%
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

#  Initialize the embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

#  Create a Chroma vector store from the docs
if not os.path.exists("./chroma_db"):
    vectordb = Chroma.from_documents(
        documents=docs,       # your list of Document objects
        embedding=embedding_model,
        persist_directory="./chroma_db"  # folder to save vector database
    )

    #  Persist the database to disk
    vectordb.persist()
else:
    if os.path.exists("./chroma_db"):
    # Load existing database
        vectordb = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embedding_model
        )
        print("Loaded existing vector database.")


print("Vector database created and persisted successfully!")


# %%
# def print_results(results):
#     for i, doc in enumerate(results, 1):
#         print(f"Result {i}:")
#         print("Product Name:", doc.metadata["name"])
#         print("Link:", doc.metadata["link"])
#         print("Price:", doc.metadata["price"])
#         print("Description:", doc.page_content[:300])  # preview first 300 chars
#         print("----------------------------")
def print_results(results):
    """
    Format the similarity search results into a string, one result per block.
    """
    if not results:
        return "No results found above the threshold."

    output = ""
    for i, (doc, score) in enumerate(results, 1):  # unpack tuple
        output += f"""Result {i} (Confidence: {score:.2f})\n
Product Name: {doc.metadata["name"]}\n
Link: {doc.metadata["link"]}\n
Price: {doc.metadata["price"]}\n
Description: {doc.page_content[:300]} 
\n\n"""  # extra newline for separation

    return output


        

# %%
def query_vector_db(query, k=1):
    """
    Query the vector database and return top k results.
    
    Args:
        query (str): The search query.
        k (int): Number of top results to return.
    
    Returns:
        list: List of Document objects with metadata.
    """
    results_with_score = vectordb.similarity_search_with_score(query, k=k)
    threshold = 0.6
    filtered_results = [(doc, score) for doc, score in results_with_score if score >= threshold]
    if not filtered_results:
        print("No results found above the threshold.")
        filtered_results = []  # Return empty list if no results meet the threshold
        return 

    return filtered_results

# %%
# #  Load the persisted Chroma database
# embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
# vectordb = Chroma(
#     persist_directory="./chroma_db",
#     embedding_function=embedding_model
# )

# %%
query = "headach"  # Define your query
results = query_vector_db(query,k=2) 

#
print_results(results)

# %%
import streamlit as st
# Create a row with 2 columns: image on the left, title on the right
col1, col2 = st.columns([1, 5])  # Adjust ratio as needed
with col1:
    st.image("logo.png", width=100)  # Replace with your image file path
with col2:
    st.title("Pharmakon Product Recommender")
query = st.text_input("Enter your search query:")
if query:
    results = query_vector_db(query)
    if results:
        mystr1= print_results(results)
        st.write(mystr1)
    else:
        st.write("we have no products for your query.")
with st.sidebar:
    st.header("About")
    st.write("Address: Giza – 6th of october city-4th District-neighboring first-Building 168")
    st.write("Mob : 002 01028227758")
    st.write("Email:pharmakon.info@pharmakonegypt.org")
    st.write("Developed by Ahmed Rehaan")  # Replace with your name or organization


