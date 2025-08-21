# Pharmakon Product Recommender

This project implements a product recommender system for Pharmakon, leveraging OpenAI embeddings and Streamlit for a user-friendly interface.
https://github.com/user-attachments/assets/4f6b7553-9eae-41b2-9a36-82f3c6f63adc
- **Product Data Loading**: Loads product information from a JSON file.
- **Vector Database Creation**: Utilizes OpenAI embeddings to create a searchable vector database of product descriptions.
- **Similarity Search**: Allows users to query the product database using natural language.
- **Streamlit Interface**: Provides an interactive web application for product recommendations.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```
   OPENAI_API_KEY='your_openai_api_key_here'
   ```

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run main.py
```

Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Project Structure

- `main.py`: The main application script containing the Streamlit interface and vector database logic.
- `pharamkon.ipynb`: Jupyter Notebook for development and testing of the vector database and embedding logic.
- `pharmakon_products.json`: JSON file containing the product data.
- `logo.png`: (Assumed) Logo image used in the Streamlit application.
- `.env`: (Not committed) File to store environment variables like the OpenAI API key.
- `chroma_db/`: (Generated) Directory where the Chroma vector database is persisted.

## Dependencies

The project relies on the following Python libraries:

- `python-dotenv`
- `langchain`
- `openai`
- `streamlit`

## Contact

Developed by Ahmed Rehaan

Email: pharmakon.info@pharmakonegypt.org


