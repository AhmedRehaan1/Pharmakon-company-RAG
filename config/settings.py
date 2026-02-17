"""
Configuration and constants for the Pharmakon Product Recommender system.
All configurable values are centralized here to avoid scattered configuration.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Application settings and configuration constants."""
    
    # Project paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    CHROMA_DB_DIR = BASE_DIR / "chroma_db"
    
    # Data files
    PRODUCTS_JSON_PATH = DATA_DIR / "pharmakon_products.json"
    LOGO_PATH = BASE_DIR / "logo.png"
    
    # OpenAI configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = "text-embedding-3-large"
    LLM_MODEL = "gpt-4o-mini"
    LLM_TEMPERATURE = 0
    
    # Vector database configuration
    PERSIST_DIRECTORY = str(CHROMA_DB_DIR)
    
    # Search configuration
    DEFAULT_TOP_K = 2
    SIMILARITY_THRESHOLD = 0.6
    DESCRIPTION_PREVIEW_LENGTH = 300
    
    # UI configuration
    APP_TITLE = "Pharmakon Product Recommender"
    LOGO_WIDTH = 100
    
    # Company information
    COMPANY_INFO = {
        "address": "Giza – 6th of october city-4th District-neighboring first-Building 168",
        "mobile": "002 01028227758",
        "email": "pharmakon.info@pharmakonegypt.org"
    }
    
    @classmethod
    def validate(cls):
        """Validate that required settings are configured."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please set it in your .env file."
            )
        
        # Ensure data directory exists
        cls.DATA_DIR.mkdir(exist_ok=True)
        
        return True
