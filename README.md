# Pharmakon Product Recommender 💊

A production-ready pharmaceutical product recommendation system built with **clean architecture** principles. This application leverages OpenAI embeddings, Chroma vector database, and LLM-based reasoning to provide intelligent product recommendations based on customer symptoms and needs.

## 🎥 Demo

https://github.com/user-attachments/assets/ab12b65b-92ab-43b6-adef-4960be3d7bd4

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Development Guide](#-development-guide)
- [API Reference](#-api-reference)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contact](#-contact)

---

## ✨ Features

- **Clean Architecture**: Proper separation of concerns with dedicated layers
- **Semantic Search**: Vector similarity search using OpenAI embeddings
- **AI-Powered Recommendations**: GPT-4o-mini generates contextual product recommendations
- **Interactive UI**: User-friendly Streamlit web application
- **Persistent Vector Store**: Chroma database for efficient product embedding storage
- **Centralized Configuration**: Single source of truth for all settings
- **Production-Ready**: Comprehensive error handling, validation, and logging support
- **Scalable Design**: Easy to extend with new features
- **Type-Safe**: Type hints throughout the codebase

---

## 🏗️ Architecture

This project follows **clean architecture** principles with clear separation of concerns:

```
pharmacon-recommender/
├── config/                  # ⚙️ Configuration Layer
│   ├── __init__.py
│   ├── settings.py         # All settings and constants
│   └── prompts.py          # LLM prompt templates
├── models/                  # 📦 Data Models Layer
│   ├── __init__.py
│   └── product.py          # Product data structures
├── services/                # 🔧 Business Logic Layer
│   ├── __init__.py
│   ├── data_loader.py      # JSON data loading
│   ├── vector_store.py     # Vector database management
│   └── recommendation.py   # Recommendation engine
├── utils/                   # 🛠️ Utilities Layer
│   ├── __init__.py
│   └── formatters.py       # Result formatting
├── ui/                      # 🎨 Presentation Layer
│   ├── __init__.py
│   └── streamlit_app.py    # Streamlit interface
├── data/                    # 📄 Data Files
│   └── pharmakon_products.json
├── chroma_db/              # 💾 Vector Database
├── .env                    # 🔐 Environment Variables
├── requirements.txt        # 📦 Dependencies
├── main.py                 # 🚀 Entry Point
└── README.md
```

### 🔄 Dependency Flow

```
main.py → Config → Services → Models → Utils → UI
   ↓         ↓          ↓         ↓       ↓      ↓
Initialize → Load → Vector DB → Products → Format → Display
```

**Key Principles:**
- ✅ Single Responsibility: Each module does one thing
- ✅ Dependency Injection: Services receive dependencies
- ✅ No Circular Imports: Clean one-way dependency flow
- ✅ Configuration Centralization: All settings in one place

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Git (optional)

### Setup Steps

1. **Clone or download the repository:**

   ```bash
   git clone <repository_url>
   cd pharmacon-recommender
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

---

## 🎯 Usage

### Running the Application

```bash
streamlit run main.py
```

The application will automatically:
1. ✅ Validate configuration
2. ✅ Load product data from `data/pharmakon_products.json`
3. ✅ Initialize or load the Chroma vector database
4. ✅ Launch the web interface at `http://localhost:8501`

### Using the Application

1. Open your browser to `http://localhost:8501`
2. Enter symptoms or product needs in the search box
3. View AI-powered recommendations with:
   - Product name and description
   - Price information
   - Product link
   - Relevance explanation

---

## ⚙️ Configuration

All settings are centralized in `config/settings.py`:

```python
from config.settings import Settings

# API Configuration
Settings.OPENAI_API_KEY          # From .env file
Settings.EMBEDDING_MODEL         # "text-embedding-3-large"
Settings.LLM_MODEL               # "gpt-4o-mini"
Settings.LLM_TEMPERATURE         # 0

# Search Configuration
Settings.SIMILARITY_THRESHOLD    # 0.6 (min similarity score)
Settings.DEFAULT_TOP_K           # 2 (number of results)

# Paths
Settings.PRODUCTS_JSON_PATH      # data/pharmakon_products.json
Settings.CHROMA_DB_DIR           # chroma_db/
```

### Customization Examples

**Change the AI model:**
```python
# In config/settings.py
LLM_MODEL = "gpt-4"  # Use GPT-4 instead
```

**Adjust search sensitivity:**
```python
# In config/settings.py
SIMILARITY_THRESHOLD = 0.7  # More strict matching
DEFAULT_TOP_K = 5           # Return more results
```

**Modify prompts:**
```python
# In config/prompts.py
RECOMMENDATION_PROMPT = """Your custom prompt here..."""
```

---

## 👨‍💻 Development Guide

### Project Structure Explained

```
┌─────────────────────────────────────────────┐
│              main.py (Entry Point)          │
│  • Initializes all services                 │
│  • Orchestrates application flow            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│           config/ (Configuration)           │
│  • settings.py: All constants               │
│  • prompts.py: LLM templates                │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│          services/ (Business Logic)         │
│  • data_loader.py: Load JSON data           │
│  • vector_store.py: Manage vector DB        │
│  • recommendation.py: AI recommendations    │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│           models/ (Data Structures)         │
│  • product.py: Product schema               │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│         utils/ (Helper Functions)           │
│  • formatters.py: Format results            │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│           ui/ (Presentation)                │
│  • streamlit_app.py: Web interface          │
└─────────────────────────────────────────────┘
```

### Adding New Features

#### Add a New Product Field

1. Update `models/product.py`:
```python
@dataclass
class Product:
    product_name: str
    product_price: str
    product_description: str
    product_link: str
    product_category: str  # New field
```

2. Update `to_document()` method if needed for search

#### Add a New Search Method

1. Add method to `services/vector_store.py`:
```python
def custom_search(self, query, filters):
    # Your custom search logic
    pass
```

2. Expose through `services/recommendation.py` if needed

#### Customize the UI

Edit `ui/streamlit_app.py`:
```python
def render_search_interface(recommendation_service):
    # Add your custom UI components
    st.sidebar.checkbox("Advanced options")
```

### Code Style Guidelines

- **Type hints**: Use type annotations for all functions
- **Docstrings**: Document all public methods
- **Naming**: `snake_case` for functions, `PascalCase` for classes
- **Imports**: Group by standard lib, third-party, local
- **Line length**: Max 88 characters (Black formatter)

---

## 📚 API Reference

### DataLoader

```python
from services.data_loader import DataLoader

# Load products from JSON
products = DataLoader.load_products_from_json(path)

# Validate products
DataLoader.validate_products(products)
```

### VectorStoreManager

```python
from services.vector_store import VectorStoreManager

# Initialize
vector_store = VectorStoreManager()
vector_store.initialize(documents)

# Search
results = vector_store.similarity_search(
    query="headache medicine",
    k=2,
    score_threshold=0.6
)
```

### RecommendationService

```python
from services.recommendation import RecommendationService

# Create service
service = RecommendationService(vector_store)

# Get recommendations
recommendation = service.get_recommendations(
    query="I have a headache",
    k=2
)
```

### ResultFormatter

```python
from utils.formatters import ResultFormatter

# Format for LLM
context = ResultFormatter.format_search_results(results)

# Format for display
display = ResultFormatter.format_for_display(results)
```

---

## 🧪 Testing

### Manual Testing

```bash
# Test data loading
python -c "from services.data_loader import DataLoader; from config.settings import Settings; print(len(DataLoader.load_products_from_json(Settings.PRODUCTS_JSON_PATH)))"

# Test vector store
python -c "from services.vector_store import VectorStoreManager; vm = VectorStoreManager(); print('Vector store initialized')"
```

### Unit Test Examples

```python
# test_product.py
def test_product_to_document():
    product = Product("Name", "Price", "Description", "Link")
    doc = product.to_document()
    assert doc.page_content == "Description"
    assert doc.metadata["name"] == "Name"

# test_formatter.py
def test_format_results():
    results = [(mock_doc, 0.8)]
    formatted = ResultFormatter.format_search_results(results)
    assert "Confidence: 0.80" in formatted
```

---

## 🐛 Troubleshooting

### Common Issues

#### "No module named 'config'"

**Cause:** Running from wrong directory

**Solution:**
```bash
cd "path/to/project/root"
streamlit run main.py
```

#### "OpenAI API key not found"

**Cause:** Missing or incorrect `.env` file

**Solution:**
```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

#### "Product data file not found"

**Cause:** JSON file not in `data/` folder

**Solution:** Ensure `data/pharmakon_products.json` exists

#### Vector database initialization fails

**Cause:** Permissions or corrupted database

**Solution:**
```bash
# Delete and recreate
rm -rf chroma_db/
streamlit run main.py  # Will recreate automatically
```

#### Slow search performance

**Cause:** Large database or too many results

**Solution:** Adjust in `config/settings.py`:
```python
DEFAULT_TOP_K = 2  # Reduce number of results
```

### Debug Mode

Add to `main.py` for debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📦 Dependencies

Key packages and their purposes:

| Package | Purpose |
|---------|---------|
| `streamlit` | Web UI framework |
| `langchain` | LLM orchestration |
| `langchain-openai` | OpenAI integration |
| `langchain-community` | Community integrations |
| `openai` | OpenAI API client |
| `chromadb` | Vector database |
| `python-dotenv` | Environment variables |

See `requirements.txt` for complete list.

---

## 🚀 Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add `OPENAI_API_KEY` in Secrets
5. Deploy

### Docker (Optional)

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

---

## 📈 Performance Tips

1. **Reuse vector store**: Database persists across runs
2. **Batch operations**: Load all products at once
3. **Adjust top-k**: Lower = faster searches
4. **Cache results**: Add caching to recommendation service
5. **Optimize embeddings**: Use smaller model if speed matters

---

## 🔒 Security Best Practices

- ✅ API keys in `.env`, not in code
- ✅ `.env` in `.gitignore`
- ✅ Input validation in DataLoader
- ✅ Path handling with `pathlib.Path`
- ✅ No secrets in version control
- ✅ Use environment-specific configs for production

---

## 📞 Contact & Support

**Pharmakon Egypt**

- 📍 **Address**: Giza – 6th of October City, 4th District, Building 168
- 📱 **Mobile**: +20 102 822 7758
- 📧 **Email**: pharmakon.info@pharmakonegypt.org

---

## 📄 License

[Add your license information here]

---

## 🙏 Acknowledgments

- OpenAI for embeddings and LLM capabilities
- LangChain for orchestration framework
- Streamlit for the UI framework
- ChromaDB for vector storage

---

## 📝 Changelog

### Version 2.0 (Current)
- ✅ Complete refactoring to clean architecture
- ✅ Separated concerns into layers
- ✅ Centralized configuration
- ✅ Added comprehensive documentation
- ✅ Production-ready error handling

### Version 1.0
- Initial monolithic implementation

---

**Made with ❤️ by the Pharmakon team**

## 📄 License

[Add your license information here]

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


